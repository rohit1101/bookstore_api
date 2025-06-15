from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

class BookItem(BaseModel):
  id: int
  title: str
  author: list[str]
  published_date: str
  price: float


@app.get('/')
async def home():
  return {"message": "Hello world!"}

@app.get('/api/v1/healthcheck')
def healthcheck():
  return "APIs are working as expected"

@app.get('/api/v1/books/')
async def get_all_books():
  return "all books"

@app.get('/api/v1/books/{book_id}')
async def get_book_by_id(book_id:int):
  return f'The book ID is {book_id}'

@app.post('/api/v1/books/')
async def add_book():
  return f'Book added'

@app.put('/api/v1/books/{book_id}')
async def update_book(book_id:int):
  return f'Updated book {book_id}'

@app.delete('/api/v1/books/{book_id}')
async def delete_book(book_id:int):
  return f'Delete book {book_id}'