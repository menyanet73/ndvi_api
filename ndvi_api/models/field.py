from pydantic import BaseModel
from typing import Dict, Optional


class Field(BaseModel):
    id: Optional[str] = None
    geojson: Dict


class FieldIn(BaseModel):
    geojson: Dict


class Map(BaseModel):
    id: Optional[str] = None
    field_id: int
    html: str


class MapIn(BaseModel):
    field_id: int
    html: str
