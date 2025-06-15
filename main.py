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

@app.post('/api/v1/books/{id}')
async def get_book_by_id():
  return "get book by ID"

