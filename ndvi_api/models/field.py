from pydantic import BaseModel, validator
from typing import Dict, Optional


class Field(BaseModel):
    id: Optional[str] = None
    geojson: Dict


class FieldIn(BaseModel):
    geojson: Dict
    
    @validator('geojson')
    def geojson_validation(cls, value):
        if not isinstance(value, dict):
            return ValueError("Value must be geojson type with { }")
        try:
            if value['type'] != 'FeatureCollection':
                return ValueError("Value type must be FeatureCollection")
        except KeyError:
            return ValueError("Value must be geojson type with { }")
        return value

class Map(BaseModel):
    id: Optional[str] = None
    field_id: int
    html: str


class MapIn(BaseModel):
    field_id: int
    html: str
