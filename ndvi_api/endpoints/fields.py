from types import NoneType
from typing import List

from fastapi import APIRouter, Depends, Response
from fastapi.responses import FileResponse, HTMLResponse
from instruments.gjndvi import geojson_to_ndvi_image
from models.field import Field, FieldIn, MapIn
from repositories.fields import FieldRepository, MapRepository

from endpoints.depends import get_field_repository, get_map_repository

router = APIRouter()


@router.get('/', response_model=List[Field])
async def read_fields(
    fields: FieldRepository = Depends(get_field_repository),
    limit: int = 100,
    skip: int = 100
):
    return await fields.get_all(limit=limit, skip=0)


@router.get('/{id}', response_model=Field)
async def get(
    id: int,
    fields: FieldRepository = Depends(get_field_repository),
    maps: MapRepository = Depends(get_map_repository),
):
    field = await fields.get_by_id(id=id)
    if isinstance(field, NoneType):
        return Response(status_code=404)
    map_html = geojson_to_ndvi_image(field.geojson, id)
    map = MapIn(field_id=id, html=map_html)
    await maps.create(map)
    return field


@router.post('/', response_model=Field)
async def create_field(
    field: FieldIn,
    fields: FieldRepository = Depends(get_field_repository)
):
    return await fields.create(field=field)


@router.delete('/{id}')
async def delete_field(
    id: int,
    fields: FieldRepository = Depends(get_field_repository),
    maps: MapRepository = Depends(get_map_repository)
):
    await maps.delete(id=id)
    return fields.delete(id=id)


@router.get('/{id}/map', response_class=FileResponse)
async def get_map(
    id: int,
    maps: MapRepository = Depends(get_map_repository)
):
    map = await maps.get_by_field_id(id=id)
    if isinstance(map, NoneType):
        return Response(status_code=404)
    return HTMLResponse(map.html)
