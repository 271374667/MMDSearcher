from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import DeclarativeBase, relationship


class Base(DeclarativeBase):
    pass


class MMD(Base):
    __tablename__ = 'mmd'
    id = Column(Integer, primary_key=True)
    # 每一个MMD都有一个唯一的mmd_id,网站上的id
    mmd_id = Column(Integer)
    # 模型上传时间
    post_time = Column(DateTime)
    # 模型作者
    author = Column(String(32))
    # 模型详情页面预览图的尺寸
    pic_size = Column(String(16))
    # 模型详情页面预览图的url
    pic_url = Column(String(256))
    # 模型的下载地址
    source = Column(String(256))
    # 模型的分级
    rating = Column(String(16))
    # 模型的评分
    score = Column(Integer)
    # 模型的标签,用#分割,比如#tag1#tag2
    tags = Column(String(512))
    # 与tag表的关联
    tag_id = Column(Integer, ForeignKey('tag.id'))
    tag = relationship('Tag', back_populates='mmds')
    # 模型详情页面的url
    url = Column(String(256))
    # 这一条记录的创建时间
    create_time = Column(DateTime)
    # 这一条记录的更新时间
    update_time = Column(DateTime)
    # 这一条记录的状态,0表示还未看过,1表示已经看过
    status = Column(Integer)
    # 这一条记录的下载状态,0表示无法下载(比如链接失效),1表示可以下载,2代表未知网站
    download_status = Column(Integer)


class Tag(Base):
    __tablename__ = 'tag'
    id = Column(Integer, primary_key=True)
    # tag的英文名字
    tag_en_name = Column(Integer)
    # tag的中文名字(调用翻译API翻译过来的)
    tag_cn_name = Column(String(32))
    # tag的创建时间
    create_time = Column(DateTime)
    mmds = relationship('MMD', back_populates='tag')
