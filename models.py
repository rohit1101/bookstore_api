from sqlalchemy import Column,String,ForeignKey,Date,UUID,Float
from sqlalchemy.orm import relationship
from database import Base

class Books(Base):
  __tablename__="books_1"
  book_id=Column(UUID, primary_key=True,index=True)
  title=Column(String)
  author=Column(String)
  published_date=Column(Date)
  price=Column(Float)
  

