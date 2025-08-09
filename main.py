import os
import requests
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv
from database import collection

load_dotenv()

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def read_form(request: Request):
    return templates.TemplateResponse("forms.html", {"request": request})

from datetime import datetime


@app.get("/history", response_class=HTMLResponse)
async def history(request: Request):
    raw_records = list(collection.find().sort("_id", -1))

    # Prepare records for template (convert ObjectId & datetime, handle missing fields)
    records = []
    for rec in raw_records:
        record = {}

        record["requested_city"] = rec.get("requested_city", "N/A")
        record["status_code"] = rec.get("status_code", "N/A")
        record["api_url"] = rec.get("api_url", "N/A")

        # Convert datetime to string safely
        req_time = rec.get("request_time")
        if isinstance(req_time, datetime):
            record["request_time"] = req_time.strftime("%Y-%m-%d %H:%M:%S")
        else:
            record["request_time"] = "N/A"

        # Convert api_response to dict or string
        api_response = rec.get("api_response", {})
        record["api_response"] = api_response

        records.append(record)

    return templates.TemplateResponse("history.html", {
        "request": request,
        "records": records
    })


@app.post("/get_weather", response_class=HTMLResponse)
async def get_weather(request: Request, city: str = Form(...)):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()

        # Store full request & response in DB
        collection.insert_one({
            "requested_city": city,
            "request_time": datetime.utcnow(),
            "api_url": url,
            "status_code": response.status_code,
            "api_response": data
        })

        if response.status_code == 200:
            temperature = data["main"]["temp"]
            description = data["weather"][0]["description"]
            message = f"Current weather in {city}: {temperature}°C, {description}"
        else:
            message = f"Error: {data.get('message', 'Unable to fetch weather data')}"

    except Exception as e:
        message = f"Error: {str(e)}"

    return templates.TemplateResponse("forms.html", {
        "request": request,
        "message": message
    })
