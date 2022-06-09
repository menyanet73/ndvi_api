from typing import List, Optional

from db.fields import fields, maps
from models.field import Field, FieldIn, Map, MapIn

from repositories.base import BaseRepository


class FieldRepository(BaseRepository):

    async def get_all(self, limit: int = 100, skip: int = 0) -> List[Field]:
        query = fields.select().limit(limit).offset(skip)
        return await self.database.fetch_all(query=query)

    async def get_by_id(self, id: int) -> Optional[Field]:
        query = fields.select().where(fields.c.id == id)
        field = await self.database.fetch_one(query=query)
        if field is None:
            return None
        return Field.parse_obj(field)

    async def create(self, field: FieldIn) -> Field:
        new_field = Field(
            geojson=field.geojson
        )
        values = {**new_field.dict()}
        values.pop('id', None)
        query = fields.insert().values(**values)
        new_field.id = await self.database.execute(query)
        return new_field

    async def delete(self, id: int):
        query = fields.delete().where(fields.c.id == id)
        return await self.database.execute(query=query)


class MapRepository(BaseRepository):

    async def get_by_field_id(self, id: int) -> Optional[Map]:
        query = maps.select().where(maps.c.field_id == id)
        map = await self.database.fetch_one(query=query)
        if map is None:
            return None
        return Map.parse_obj(map)

    async def create(self, map: MapIn) -> Map:
        new_map = Map(
            field_id=map.field_id,
            html=map.html
        )
        values = {**new_map.dict()}
        values.pop('id', None)
        query = maps.insert().values(**values)
        new_map.id = await self.database.execute(query)
        return new_map

    async def delete(self, id: int):
        map_query = maps.delete().where(maps.c.field_id == id)
        return await self.database.execute(query=map_query)