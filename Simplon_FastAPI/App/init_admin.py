from sqlmodel import Session, select
from database.database import engine
from models.user import User
from passlib.context import CryptContext
from sqlmodel import Field, Session, SQLModel, create_engine
from passlib.context import CryptContext
from sqlalchemy.exc import IntegrityError

# # Définir la base de données et la session
# DATABASE_URL = "sqlite:///./app/database.db"
# engine = create_engine(DATABASE_URL)


# Initialisation de passlib pour le hashage des mots de passe avec argon2
pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

def hash_password(password: str) -> str:
    """Fonction pour hacher le mot de passe avec argon2"""
    return pwd_context.hash(password)

def create_admin():
    """Fonction pour créer un utilisateur admin"""
    # Créer une session SQLModel
    with Session(engine) as session:
        # Hash du mot de passe
        hashed_password = hash_password("password123")

        # Créer un utilisateur admin
        user = User(
            email="admin@example.com",
            hashed_password=hashed_password,
            is_active=True,
            is_admin=True,
        )

        # Ajouter l'utilisateur à la session
        session.add(user)
        try:
            session.commit()
            print("Utilisateur admin créé avec succès.")
        except IntegrityError as e:
            print(f"Erreur d'intégrité lors de la création de l'utilisateur : {e}")
            session.rollback()
        except Exception as e:
            print(f"Erreur lors de la création de l'utilisateur : {e}")
            session.rollback()

# Créer l'admin dans la base de données
create_admin()
