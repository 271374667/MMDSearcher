from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.common.database.model import Base

# 创建数据库连接
engine = create_engine('sqlite:///mmd.db')
# 创建一个Session类
Session = sessionmaker(bind=engine)
# 创建一个Session实例
session = Session()
# 创建数据库表
Base.metadata.create_all(engine)
