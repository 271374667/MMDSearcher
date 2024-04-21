from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.common.database.model import Base
from src.core.paths import DATABASE_FILE

# 创建数据库连接
engine = create_engine(f'sqlite:///{DATABASE_FILE}')
# 创建一个Session类
Session = sessionmaker(bind=engine)
# 创建一个Session实例
session = Session()


def create_db():
    # 创建数据库表
    Base.metadata.create_all(engine)
