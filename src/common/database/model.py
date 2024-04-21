from sqlalchemy import DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class MMD(Base):
    __tablename__ = 'mmd'
    id: Mapped[Integer] = mapped_column(Integer, primary_key=True)  # 每一个MMD都有一个唯一的id
    mmd_id: Mapped[Integer] = mapped_column(Integer)  # 网站上的id
    post_time: Mapped[DateTime] = mapped_column(DateTime)  # 模型上传时间
    author: Mapped[String] = mapped_column(String(32))  # 模型作者
    pic_size: Mapped[String] = mapped_column(String(16))  # 模型详情页面预览图的尺寸
    pic_url: Mapped[String] = mapped_column(String(256))  # 模型详情页面预览图的url
    source: Mapped[String] = mapped_column(String(256))  # 模型的下载地址
    rating: Mapped[String] = mapped_column(String(16))  # 模型的分级
    score: Mapped[Integer] = mapped_column(Integer)  # 模型的评分
    tags: Mapped[String] = mapped_column(String(512))  # 模型的标签,用#分割,比如#tag1#tag2
    tag_id: Mapped[Integer] = mapped_column(Integer, ForeignKey('tag.id'))  # 与tag表的关联
    tag: Mapped[relationship] = relationship('Tag', back_populates='mmds')
    url: Mapped[String] = mapped_column(String(256))  # 模型详情页面的url
    create_time: Mapped[DateTime] = mapped_column(DateTime)  # 这一条记录的创建时间
    update_time: Mapped[DateTime] = mapped_column(DateTime)  # 这一条记录的更新时间
    status: Mapped[Integer] = mapped_column(Integer)  # 这一条记录的状态,0表示还未看过,1表示已经看过
    download_status: Mapped[Integer] = mapped_column(Integer)  # 这一条记录的下载状态,0表示无法下载(比如链接失效,1表示可以下载,2代表未知网站

    def __repr__(self) -> str:
        return f'<MMD(mmd_id={self.mmd_id}, post_time={self.post_time}, author={self.author}, pic_size={self.pic_size}, pic_url={self.pic_url}, source={self.source}, rating={self.rating}, score={self.score}, tags={self.tags}, url={self.url}, create_time={self.create_time}, update_time={self.update_time}, status={self.status}, download_status={self.download_status})>'


class Tag(Base):
    __tablename__ = 'tag'
    id: Mapped[Integer] = mapped_column(Integer, primary_key=True)  # tag的id
    tag_en_name: Mapped[Integer] = mapped_column(Integer)  # tag的英文名字
    tag_cn_name: Mapped[String] = mapped_column(String(32))  # tag的中文名字(调用翻译API翻译过来的
    create_time: Mapped[DateTime] = mapped_column(DateTime)  # tag的创建时间
    mmds: Mapped[relationship] = relationship('MMD', back_populates='tag')

    def __repr__(self) -> str:
        return f'<Tag(tag_en_name={self.tag_en_name}, tag_cn_name={self.tag_cn_name}, create_time={self.create_time})>'
