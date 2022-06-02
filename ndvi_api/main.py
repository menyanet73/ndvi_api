from typing import List
from fastapi import FastAPI, Query, Path, Body
from schemas import Book, BookOut


app = FastAPI()


@app.post('/book', response_model=BookOut)
def create_book(item: Book):
    return BookOut(**item.dict(), id = 3)


@app.post('/fields')
def create_field(field: str):
    # Сохранение поля
    # Получение снимка
    # Расчет и сохранение NDVI
    return field


@app.delete('/fields/{field_id}')
def delete_field(field_id: int):
    # Получить поле из бд
    # Удалить поле из бд
    pass


@app.get('fields')
def list_fields():
    # Получить список полей из бд
    # Вернуть все поля
    pass


@app.get('fields/{field_id}')
def ndvi_get(field_id: int):
    # Получить поле из бд
    # Вернуть изображение с NDVI
    pass