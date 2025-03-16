from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

DATABASE_URL = "postgresql://xxxx:yyyy@localhost:5432/business_report"
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(engine)  # セッションを作るクラスを作成
Base.metadata.create_all(bind=engine)