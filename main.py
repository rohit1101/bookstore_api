from fastapi import FastAPI

app=FastAPI()

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
async def get_book_by_id(book_id:int=0):
  return f'The book ID is {book_id}'


