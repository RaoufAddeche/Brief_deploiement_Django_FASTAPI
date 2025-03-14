# app/main.py
from fastapi import FastAPI
from App.database.database import create_db_and_tables
from App.routes import loans, admin, auth
from dotenv import load_dotenv



load_dotenv()

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app.include_router(auth.router)
app.include_router(loans.router)
app.include_router(admin.router)


