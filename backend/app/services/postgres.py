from sqlalchemy import create_engine, Column, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime
import os
import uuid

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    email = Column(String, unique=True, nullable=False)
    username = Column(String, unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    last_login = Column(DateTime)

class Session(Base):
    __tablename__ = "sessions"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String, ForeignKey("users.id"))
    token = Column(String, nullable=False)
    expires_at = Column(DateTime, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User")

class PostgresService:
    def __init__(self):
        self.engine = create_engine(
            f"postgresql://{os.getenv('POSTGRES_USER', 'ohrwurm')}:"
            f"{os.getenv('POSTGRES_PASSWORD', 'ohrwurm123')}@"
            f"{os.getenv('POSTGRES_HOST', 'localhost')}:"
            f"{os.getenv('POSTGRES_PORT', '5432')}/"
            f"{os.getenv('POSTGRES_DB', 'ohrwurm')}"
        )
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def get_user_by_email(self, email: str) -> User:
        session = self.Session()
        try:
            return session.query(User).filter(User.email == email).first()
        finally:
            session.close()

    def create_user(self, email: str, username: str) -> User:
        session = self.Session()
        try:
            user = User(email=email, username=username)
            session.add(user)
            session.commit()
            return user
        finally:
            session.close()

    def create_session(self, user_id: str, token: str, expires_at: datetime) -> Session:
        session = self.Session()
        try:
            db_session = Session(user_id=user_id, token=token, expires_at=expires_at)
            session.add(db_session)
            session.commit()
            return db_session
        finally:
            session.close()

    def get_valid_session(self, token: str) -> Session:
        session = self.Session()
        try:
            return session.query(Session).filter(
                Session.token == token,
                Session.expires_at > datetime.utcnow()
            ).first()
        finally:
            session.close() 