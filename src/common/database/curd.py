from datetime import datetime
from typing import Type

from sqlalchemy.orm import Query
from sqlalchemy.orm import Session

from src.common.database.model import MMD, Tag
from src.common.database.session import session


class Curd:
    def __init__(self):
        self._session: Session = session

    def add(self,
            mmd_id: int,
            post_time: datetime,
            author: str,
            pic_size: str,
            pic_url: str,
            source: str,
            rating: str,
            score: int,
            tags: str,
            url: str,
            create_time: datetime,
            update_time: datetime,
            status: int,
            download_status: int,
            # 下面是tag的信息
            tag_en_name: str,
            tag_cn_name: str,
            tag_create_time: datetime
            ):
        tag = Tag(tag_en_name=tag_en_name,
                  tag_cn_name=tag_cn_name,
                  create_time=tag_create_time)

        mmd = MMD(mmd_id=mmd_id,
                  post_time=post_time,
                  author=author,
                  pic_size=pic_size,
                  pic_url=pic_url,
                  source=source,
                  rating=rating,
                  score=score,
                  tags=tags,
                  url=url,
                  create_time=create_time,
                  update_time=update_time,
                  status=status,
                  download_status=download_status,
                  tag=tag
                  )
        self._session.add(mmd)
        self._session.commit()

    def remove_by_mmd_id(self, mmd_id: int):
        mmd = self._session.query(MMD).filter(MMD.mmd_id == mmd_id).first()
        self._session.delete(mmd)
        self._session.commit()

    def update_by_mmd_id(self, mmd_id: int, **kwargs):
        mmd = self._session.query(MMD).filter(MMD.mmd_id == mmd_id).first()
        for key, value in kwargs.items():
            setattr(mmd, key, value)
        self._session.commit()

    def get_mmd_query(self) -> Query[Type[MMD]]:
        return self._session.query(MMD)

    def get_tag_query(self) -> Query[Type[Tag]]:
        return self._session.query(Tag)


if __name__ == '__main__':
    curd = Curd()
    curd.add(1, datetime.now(), 'test', 'test', 'test', 'test', 'test', 1, 'test', 'test', datetime.now(), datetime.now(), 0, 0, 'test', 'test', datetime.now())
    print('add success')
    curd.get_mmd_query()
