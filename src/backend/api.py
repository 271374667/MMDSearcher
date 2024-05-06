from fastapi import FastAPI
from fastapi.params import Query

from src.backend.service.home_service import HomeService
from src.backend.types.apifox import ApifoxModel
from src.core.config import HOST, PORT

app = FastAPI()
home_service = HomeService()


@app.get('/api/v1/get_mmds')
async def get_mmds(
        limit: int = Query(None),
        offset: int = Query(None),
        author: str = Query(None),
        download_status: str = Query(None),
        mmd_id: int = Query(None),
        post_time_search_begin: str = Query(None),
        post_time_search_end: str = Query(None),
        rating: str = Query(None),
        score: int = Query(None),
        score_operation: int = Query(None),
        sort_by: str = Query(None),
        status: str = Query(None),
        tag_operation: int = Query(None),
        tags: str = Query(None)
        ):
    apifox = ApifoxModel(
            limit=limit,
            offset=offset,
            author=author,
            download_status=download_status,
            mmd_id=mmd_id,
            post_time_search_begin=post_time_search_begin,
            post_time_search_end=post_time_search_end,
            rating=rating,
            score=score,
            score_operation=score_operation,
            sort_by=sort_by,
            status=status,
            tag_operation=tag_operation,
            tags=tags
            )
    return home_service.get_mmd(apifox)


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host=f'{HOST}', port=PORT)
