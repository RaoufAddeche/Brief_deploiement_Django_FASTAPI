# # app/database/database.py
# from sqlmodel import create_engine, Session, SQLModel
# from App.core.config import settings

# # Création de l'engine de la base de données
# engine = create_engine(settings.DATABASE_URL, echo=True)

# # Fonction pour initialiser la base de données
# def create_db_and_tables():
#     SQLModel.metadata.create_all(engine)

# # Dépendance pour obtenir une session de base de données
# def get_session():
#     with Session(engine) as session:
#         yield session



from sqlmodel import create_engine, Session, SQLModel
from dotenv import load_dotenv
import os

# Chargement des variables d'environnement
load_dotenv()

# Récupération des variables d'environnement
SERVER = os.getenv("DB_SERVER")
DATABASE = os.getenv("DB_NAME")
USERNAME = os.getenv("DB_USER")
PASSWORD = os.getenv("DB_PASSWORD")
DRIVER = os.getenv("DB_DRIVER")

# Vérification des variables d'environnement
if not all([SERVER, DATABASE, USERNAME, PASSWORD, DRIVER]):
    raise ValueError("Certaines variables d'environnement sont manquantes")

# Construction de la chaîne de connexion
DATABASE_URL = os.getenv("DATABASE_URL")

# Création de l'engine avec les options de connexion
engine = create_engine(
    DATABASE_URL,
    echo=True,  # Mettre à False en production
    pool_pre_ping=True,
    pool_recycle=3600,
    connect_args={
        "TrustServerCertificate": "yes",
        "Encrypt": "yes"
    }
)

# Fonction pour initialiser la base de données
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

# Dépendance pour obtenir une session de base de données
def get_session():
    with Session(engine) as session:
        try:
            yield session
        finally:
            session.close()