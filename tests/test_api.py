from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import List, Optional
import uuid

app = FastAPI(title="Health Management API", version="1.0.0")

# Mock database
health_data = {
    "profile": {
        "user_id": "123e4567-e89b-12d3-a456-426614174000",
        "name": "Иван Иванов",
        "birth_date": "1985-05-15",
        "gender": "male",
        "blood_type": "A+",
        "allergies": ["пенициллин", "арахис"],
        "chronic_conditions": ["гипертония"],
        "last_checkup": "2023-10-12"
    },
    "metrics": {
        "heart_rate": 72,
        "blood_pressure": "120/80",
        "blood_oxygen": 98,
        "glucose_level": 5.2,
        "weight": 75.5,
        "bmi": 23.1,
        "last_updated": "2023-11-20T08:30:45Z"
    },
    "integrations": {},
    "recommendations": {
        "nutrition": [
            {
                "id": "rec-456",
                "title": "Увеличьте потребление магния",
                "description": "Ваш уровень магния ниже нормы. Рекомендуем добавить в рацион орехи, шпинат и бананы.",
                "priority": "high"
            }
        ]
    }
}

class Integration(BaseModel):
    service_name: str
    auth_token: str
    data_types: List[str]

# 1. GET /user/profile
@app.get("/user/profile")
def get_user_profile():
    return health_data["profile"]

# 2. GET /health/metrics
@app.get("/health/metrics")
def get_health_metrics():
    return health_data["metrics"]

# 3. GET /recommendations
@app.get("/recommendations")
def get_recommendations(category: str = Query(..., description="Category of recommendations")):
    if category not in health_data["recommendations"]:
        raise HTTPException(status_code=404, detail="Category not found")
    return {"recommendations": health_data["recommendations"][category]}

# 4. POST /integrations
@app.post("/integrations")
def add_integration(integration: Integration):
    integration_id = str(uuid.uuid4())
    health_data["integrations"][integration_id] = {
        **integration.dict(),
        "status": "connected"
    }
    return {"integration_id": integration_id, "status": "connected"}

# 5. DELETE /integrations/{integration_id}
@app.delete("/integrations/{integration_id}")
def delete_integration(integration_id: str):
    if integration_id not in health_data["integrations"]:
        raise HTTPException(status_code=404, detail="Integration not found")
    del health_data["integrations"][integration_id]
    return {"status": "disconnected", "message": "Integration successfully deleted"}