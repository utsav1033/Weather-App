from database import collection

try:
    collection.insert_one({"test": "ok"})
    print("✅ Insert successful")
except Exception as e:
    print("❌ Error:", e)
