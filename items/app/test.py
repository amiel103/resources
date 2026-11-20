from fastapi import FastAPI
from sqlmodel import Session , select
from contextlib import asynccontextmanager
from app.database import create_db_and_tables, engine
from fastapi.middleware.cors import CORSMiddleware




from app.routers import users
from app.models import Users

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(users.router)


origins = [
    "http://localhost:3000",  # React development server
    "https://example.com",    # Production frontend
    "*"
] # Define allowed origins (domains that can access your API)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,        # Allow these origins
    allow_credentials=True,       # Allow cookies, authentication headers
    allow_methods=["*"],          # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],          # Allow all headers
)



@app.get("/")
async def root():
    return {"message": "Hello World"}


    
