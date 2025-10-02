

# РАБОТА С БАЗАМИ ДАННЫХ С ПОМОЩЬЮ SQL ALCHEMY ИЛИ ОБОРАЧИВАНИЕ PYTHON КОДА ДЛЯ СОЗДАНИЯ SQL ЗАПРОСОВ
# from typing import Annotated
# from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
# from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
# from sqlalchemy import select
# from fastapi import FastAPI, Depends
# from pydantic import BaseModel

# app = FastAPI()

# engine = create_async_engine("sqlite+aiosqlite:///books.db")

# new_session = async_sessionmaker(engine, expire_on_commit=False)

# async def get_session():
#     async with new_session() as session:
#         yield session

# SessionDep = Annotated[AsyncSession, Depends(get_session)]


# class Base(DeclarativeBase):
#     pass

# class BookModel(Base):
#     __tablename__ = "books"

#     id: Mapped[int] = mapped_column(primary_key=True)
#     title: Mapped[str]
#     author: Mapped[str]
    

# @app.post("/setup_database", tags=["Create_and_Drop_database"])
# async def setup_database():
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.drop_all)
#         await conn.run_sync(Base.metadata.create_all)
#     return {"Ok": True}


# class BookAddShema(BaseModel):
#     title: str
#     author: str

# class BookShema(BookAddShema):
#     id: int



# @app.post("/books")
# async def add_book(data: BookShema, session: SessionDep):
#     new_book = BookModel(
#         title=data.title,
#         author=data.author,
#     )
#     session.add(new_book)
#     await session.commit()
#     return {"Ok": True}
    
    
# @app.get("/books")
# async def get_book(session: SessionDep):
#     query = select(BookModel)
#     result = await session.execute(query)
#     return result.scalars().all()
# РАБОТА С БАЗАМИ ДАННЫХ С ПОМОЩЬЮ SQL ALCHEMY ИЛИ ОБОРАЧИВАНИЕ PYTHON КОДА ДЛЯ СОЗДАНИЯ SQL ЗАПРОСОВ  
    
# РАБОТА С JWT ТОКЕНОМ ДЛЯ ПРОВЕРКИ ОТКРЫТИЯ КАКОЙ-ТО ИНФОРМАЦИИ
# from fastapi import FastAPI, HTTPException, Response, Depends
# from authx import AuthX, AuthXConfig
# from pydantic import BaseModel


# app = FastAPI()

# config = AuthXConfig()
# config.JWT_SECRET_KEY = "SECRET_KEY"
# config.JWT_ACCESS_COOKIE_NAME = "my_access_token"
# config.JWT_TOKEN_LOCATION = ["cookies"]

# security = AuthX(config=config)

# class UserLoginShema(BaseModel):
#     username: str
#     password: str


# @app.post("/login")
# def login(creds: UserLoginShema, response: Response):
#     if creds.username == "test" and creds.password == "test":
#         token = security.create_access_token(uid="12345")
#         response.set_cookie(config.JWT_ACCESS_COOKIE_NAME, token)
#         return{"access_token": token}
#     raise HTTPException(status_code=401, detail="Incorrect username or password")
    
    
# @app.get("/protected", dependencies=[Depends(security.access_token_required)])
# def protected():
#     return {"data": "TOP SECRET"}
# РАБОТА С JWT ТОКЕНОМ ДЛЯ ПРОВЕРКИ ОТКРЫТИЯ КАКОЙ-ТО ИНФОРМАЦИИ



# from fastapi import FastAPI, File, UploadFile
# from fastapi.responses import StreamingResponse, FileResponse


# app = FastAPI()



# @app.post("/files")
# async def upload_file(uploaded_file: UploadFile):
#     file = uploaded_file.file
#     filename = uploaded_file.filename
#     with open(f"2_{filename}", "wb") as f:
#         f.write(file.read())
        
        
        
# @app.post("/multiple_files")
# async def upload_files(uploaded_files: list[UploadFile]):
#     for uploaded_file in uploaded_files:
#         file = uploaded_file.file
#         filename = uploaded_file.filename
#         with open(f"2_{filename}", "wb") as f:
#             f.write(file.read())
            
            
# @app.get("/files/{filename}")
# async def get_file(filename: str):
#     return FileResponse(filename)


# def iterfile(filename: str):
#     with open(filename, "rb") as file:
#         while chunk:= file.read(1024 * 1024):
#             yield chunk  
    

# @app.get("/files/streaming/{filename}")
# async def get_streaming_file(filename:str):
#     return StreamingResponse(iterfile(filename), media_type="video/mp4")



# from fastapi import FastAPI
# from pydantic import BaseModel


# app = FastAPI()

# books = [
#     {
#         "id": 1,
#         "title": "Пишем на FASTAPi",
#         "author": "Руслан",
#     },
#     {
#         "id": 2,
#         "title": "Пишем на FASTAPi второй экземпляр",
#         "author": "Тимон",
#     },
# ]

# class BookShema(BaseModel):
#     title: str
#     id: int
#     author: str

# @app.get("/books")
# def get_books():
#     return books

# @app.post("/books")
# def add_book(book: BookShema): # Преобразуем из Pydantic-модели в словарь
#     new_book_id = len(books) + 1
#     books.append({
#         "id": new_book_id,
#         "title": book.title,
#         "author": book.author,
#     })
#     return {"OK": True}





from fastapi import FastAPI
import uvicorn


app = FastAPI()

@app.get("/users")
async def get_users():
    return [{"id": 1, "name": "Ruslan",}]





if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)













