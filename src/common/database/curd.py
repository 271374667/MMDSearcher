from typing import Type

from sqlalchemy import func
from sqlalchemy.orm import Query
from sqlalchemy.orm import Session

from src.common.database.model import MMD, Tag, mmd_tag
from src.common.database.session import session
from src.core.datacls import MMDData, TagData


class Curd:
    def __init__(self):
        self._session: Session = session

    def add(self, mmd_data: MMDData, tag_data: list[TagData]):
        # 先判断tag是否存在,不存在则添加
        tags: list[Tag] = []
        for tag in tag_data:
            tag = self._session.query(Tag).filter(Tag.tag_en_name == tag.tag_en_name).first()
            if not tag:
                tag = Tag(
                        tag_en_name=tag.tag_en_name,
                        tag_cn_name=tag.tag_cn_name,
                        create_time=tag.create_time
                        )
            tags.append(tag)

        mmd = MMD(
                mmd_id=mmd_data.mmd_id,
                post_time=mmd_data.post_time,
                author=mmd_data.author,
                pic_size=mmd_data.pic_size,
                pic_url=mmd_data.pic_url,
                source=mmd_data.source,
                rating=mmd_data.rating,
                score=mmd_data.score,
                tags=mmd_data.tags,
                url=mmd_data.url,
                create_time=mmd_data.create_time,
                update_time=mmd_data.update_time,
                status=mmd_data.status,
                download_status=mmd_data.download_status,
                tag=tags
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
    from collections import Counter
    curd = Curd()
    with session as s:
        mmd = (session.query(Tag.tag_en_name, Tag.tag_cn_name, func.count(mmd_tag.c.mmd_id))
               .join(mmd_tag, Tag.id == mmd_tag.c.tag_id)
               .join(MMD, mmd_tag.c.mmd_id == MMD.id)
               .group_by(Tag.tag_en_name, Tag.tag_cn_name, Tag.create_time)
               .order_by(func.count(mmd_tag.c.mmd_id).desc())
               .all())
        print(Counter(mmd))
        print(mmd)
    # mmd_data = MMDData(
    #         mmd_id=1,
    #         post_time=datetime.now(),
    #         author='test',
    #         pic_size='test',
    #         pic_url='test',
    #         source='test',
    #         rating='test',
    #         score=1,
    #         tags='test',
    #         url='test',
    #         create_time=datetime.now(),
    #         update_time=datetime.now(),
    #         status=1,
    #         download_status=1
    #         )
    # tag_data = [TagData(
    #         tag_en_name=f'test{i}',
    #         tag_cn_name=f'test{i}',
    #         create_time=datetime.now()
    #         ) for i in range(5)]
    # curd.add(mmd_data, tag_data)
