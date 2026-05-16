from typing import Literal

from fastapi import FastAPI
from pydantic import BaseModel, Field


app = FastAPI(
    title="RoadSoS API",
    description="Offline-first accident response API scaffold.",
    version="0.1.0",
)


class NearbyServicesRequest(BaseModel):
    lat: float = Field(..., ge=-90, le=90)
    lon: float = Field(..., ge=-180, le=180)
    radius_km: float = Field(default=8, gt=0, le=100)
    service_types: list[str] = Field(default_factory=list)
    location_source: Literal["gps", "manual", "cached"] = "manual"


class IncidentSummaryRequest(BaseModel):
    lat: float = Field(..., ge=-90, le=90)
    lon: float = Field(..., ge=-180, le=180)
    nearest_landmark: str | None = None
    injury_count: int | None = Field(default=None, ge=0)
    hazards: list[str] = Field(default_factory=list)
    notes: str | None = None


class AssistantRequest(BaseModel):
    message: str = Field(..., min_length=1)
    lat: float | None = Field(default=None, ge=-90, le=90)
    lon: float | None = Field(default=None, ge=-180, le=180)


@app.get("/health")
def health() -> dict[str, str]:
    return {
        "status": "ok",
        "service": "roadsos-api",
        "offline_cache_version": "bootstrap-0",
    }


@app.post("/api/nearby-services")
def nearby_services(request: NearbyServicesRequest) -> dict[str, object]:
    return {
        "query_location": {
            "lat": request.lat,
            "lon": request.lon,
            "source": request.location_source,
            "confidence": "bootstrap",
        },
        "services": [],
        "fallback_contacts": [],
        "offline_cache_version": "bootstrap-0",
        "warnings": [
            "Backend scaffold only. Suyash will connect source-backed data and ranking."
        ],
    }


@app.get("/api/cache-package")
def cache_package() -> dict[str, object]:
    return {
        "version": "bootstrap-0",
        "contacts": [],
        "fallback_contacts": [],
        "approved_templates": [],
    }


@app.post("/api/incident-summary")
def incident_summary(request: IncidentSummaryRequest) -> dict[str, str]:
    hazard_text = ", ".join(request.hazards) if request.hazards else "not specified"
    injury_text = (
        f"{request.injury_count} injured person(s)"
        if request.injury_count is not None
        else "injury count unknown"
    )
    landmark = request.nearest_landmark or "nearest landmark not provided"
    notes = request.notes or "no extra notes"
    return {
        "summary": (
            f"Road accident near {landmark}. {injury_text}. "
            f"Hazards: {hazard_text}. Notes: {notes}. "
            f"Coordinates: {request.lat}, {request.lon}."
        ),
        "generated_from": "user_reported_fields",
        "medical_disclaimer": "This is not medical advice or dispatch confirmation.",
    }


@app.post("/api/assistant")
def assistant(request: AssistantRequest) -> dict[str, object]:
    return {
        "answer": (
            "I can only use verified RoadSoS data and approved safety templates. "
            "The full assistant guardrail layer is not implemented in this scaffold."
        ),
        "used_sources": ["approved_safety_templates"],
        "refusal_reason": "bootstrap_scaffold",
    }

