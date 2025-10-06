# 🌦️ FastAPI Weather App

A lightweight and high-performance **Weather Application** built with **FastAPI** and **MongoDB**.  
It fetches real-time weather data from a public weather API, stores results in MongoDB, and exposes clean RESTful endpoints for retrieval and display.

---

## 🚀 Features

- Fetches live weather data from an external API (e.g., OpenWeatherMap)
- Stores weather queries and responses in **MongoDB Atlas**
- Provides endpoints to get weather by city
- Built with **FastAPI** for speed and simplicity
- Includes optional **Bootstrap frontend** for display
- JSON responses for easy API integration

---

## 🏗️ Tech Stack

- **Backend:** FastAPI (Python)
- **Database:** MongoDB / MongoDB Atlas
- **Frontend:** HTML, Bootstrap
- **External API:** OpenWeatherMap (or similar)
- **Environment Management:** Python venv

---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/fastapi-weather-app.git
cd fastapi-weather-app
```

#### 2. Create and activate a virtual environment
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Create a .env file
```bash
MONGO_URI=mongodb+srv://utsavkhairnar14:WeatherApp2025@cluster0.ytlotc4.mongodb.net/weatherDB?retryWrites=true&w=majority&appName=Cluster0
OPENWEATHER_API_KEY=726890aee21512670ec57e863b9c737b
```

### 5. Load the app
```bash
uvicorn main:app --reload
```

### 6. Access the app

Swagger Docs → http://127.0.0.1:8000/docs
Homepage → http://127.0.0.1:8000

## 🧠 API Endpoints

| Method | Endpoint          | Description                               |
| ------ | ----------------- | ----------------------------------------- |
| `GET`  | `/weather/{city}` | Fetches weather data for a given city     |
| `GET`  | `/history`        | Returns saved search history from MongoDB |
| `POST` | `/add_city`       | Adds a city manually (optional)           |


## 🧩 Example JSON Response

GET /weather/mumbai

{
  "city": "Mumbai",
  "temperature": "31°C",
  "condition": "Sunny",
  "humidity": "60%",
  "timestamp": "2025-10-06T12:00:00Z"
}

## 🗃️ Project Structure
```bash
Weather-App/
├── .env
├── .idea/
│   ├── .gitignore
│   ├── inspectionProfiles/
│   │   ├── profiles_settings.xml
│   │   └── Project_Default.xml
│   ├── misc.xml
│   ├── modules.xml
│   ├── vcs.xml
│   └── weather-app.iml
├── database.py
├── main.py
├── requirements.txt
├── templates/
│   ├── forms.html
│   └── history.html
├── test_db.py
└── test_mongo.py
└── README.md
```

## 🔮 Future Improvements

Add 7-day weather forecast
Integrate caching for performance
Implement user authentication
Auto-detect location via IP

## 👨‍💻 Author

Utsav Khairnar
GitHub – @utsav1033

Email – utsavkhairnar14@gmail.com
