from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="AGRONEXUS API", version="1.0")

class PriceRequest(BaseModel):
    crop: str
    current_price: float
    market: str = "Nearby"
    quantity_kg: float = 1000
    horizon_days: int = 1

class LogisticsRequest(BaseModel):
    distance_km: float
    quantity_kg: float
    vehicle_capacity_kg: float = 1500
    fuel_price: float = 95
    mileage_kmpl: float = 10
    loading: float = 400
    unloading: float = 300
    toll: float = 0

@app.get("/api/health")
def health():
    return {"status":"ok","service":"AGRONEXUS"}

@app.post("/api/ai/price-prediction")
def price_prediction(req: PriceRequest):
    # Demo model only. Replace with a validated ML model and real market data.
    change = 0.04 if req.horizon_days <= 2 else 0.02
    low = round(req.current_price * (1-change), 2)
    high = round(req.current_price * (1+change*1.5), 2)
    return {
        "crop": req.crop,
        "market": req.market,
        "forecast_range": [low, high],
        "confidence": 0.78,
        "note": "Demo prediction; production version requires validated historical and external features."
    }

@app.post("/api/ai/logistics")
def logistics(req: LogisticsRequest):
    trips = max(1, int((req.quantity_kg + req.vehicle_capacity_kg - 1)//req.vehicle_capacity_kg))
    fuel = (req.distance_km * trips / req.mileage_kmpl) * req.fuel_price
    total = fuel + req.loading + req.unloading + req.toll
    return {
        "trips": trips,
        "fuel_cost": round(fuel,2),
        "total_estimated_cost": round(total,2),
        "cost_per_kg": round(total/req.quantity_kg,2)
    }
