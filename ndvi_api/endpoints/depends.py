from repositories.fields import FieldRepository, MapRepository
from db.base import database

def get_field_repository() -> FieldRepository:
    return FieldRepository(database)

def get_map_repository() -> MapRepository:
    return MapRepository(database)