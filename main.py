from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class BookItem(BaseModel):
  id: int
  title: str
  author: list[str]
  published_date: str
  price: float


@app.get('/')
async def home():
  return {"message": "Hello world!"}

# return the health status
@app.get('/api/v1/healthcheck')
def healthcheck():
  return "APIs are working as expected"


# get all books
@app.get('/api/v1/books/')
async def get_all_books():
  return "all books"

# get a book by book_id
@app.get('/api/v1/books/{book_id}')
async def get_book_by_id(book_id:int):
  return f'The book ID is {book_id}'

# add a book
@app.post('/api/v1/books/')
async def add_book(book_item: BookItem):
  book_data=book_item.model_dump()
  print(book_data,book_item)
  return f'Book added'

# update a book
@app.put('/api/v1/books/{book_id}')
async def update_book(book_id:int):
  return f'Updated book {book_id}'

# delete a book
@app.delete('/api/v1/books/{book_id}')
async def delete_book(book_id:int):
  return f'Delete book {book_id}'