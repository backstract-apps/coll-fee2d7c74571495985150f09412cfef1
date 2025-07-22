from fastapi import APIRouter, Request, Depends, HTTPException, UploadFile,Query, Form
from sqlalchemy.orm import Session
from typing import List,Annotated
import service, models, schemas
from fastapi import Query
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/users/user_id')
async def get_users_user_id(user_id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_users_user_id(db, user_id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/posts/post_id')
async def delete_posts_post_id(raw_data: schemas.DeletePostsPostId, db: Session = Depends(get_db)):
    try:
        return await service.delete_posts_post_id(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/comments/')
async def get_comments(db: Session = Depends(get_db)):
    try:
        return await service.get_comments(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/users/')
async def post_users(raw_data: schemas.PostUsers, db: Session = Depends(get_db)):
    try:
        return await service.post_users(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/users/user_id/')
async def put_users_user_id(raw_data: schemas.PutUsersUserId, db: Session = Depends(get_db)):
    try:
        return await service.put_users_user_id(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/users/user_id')
async def delete_users_user_id(raw_data: schemas.DeleteUsersUserId, db: Session = Depends(get_db)):
    try:
        return await service.delete_users_user_id(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/posts_sample/')
async def get_posts_sample(db: Session = Depends(get_db)):
    try:
        return await service.get_posts_sample(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/test/')
async def get_test(db: Session = Depends(get_db)):
    try:
        return await service.get_test(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/test/id')
async def get_test_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_test_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/posts/post_id')
async def get_posts_post_id(post_id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_posts_post_id(db, post_id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/posts/')
async def post_posts(raw_data: schemas.PostPosts, db: Session = Depends(get_db)):
    try:
        return await service.post_posts(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/posts/post_id/')
async def put_posts_post_id(raw_data: schemas.PutPostsPostId, db: Session = Depends(get_db)):
    try:
        return await service.put_posts_post_id(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/posts/')
async def get_posts(db: Session = Depends(get_db)):
    try:
        return await service.get_posts(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/users/')
async def get_users(db: Session = Depends(get_db)):
    try:
        return await service.get_users(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/comments/comment_id')
async def get_comments_comment_id(comment_id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_comments_comment_id(db, comment_id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/comments/')
async def post_comments(raw_data: schemas.PostComments, db: Session = Depends(get_db)):
    try:
        return await service.post_comments(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/comments/comment_id/')
async def put_comments_comment_id(raw_data: schemas.PutCommentsCommentId, db: Session = Depends(get_db)):
    try:
        return await service.put_comments_comment_id(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/comments/comment_id')
async def delete_comments_comment_id(raw_data: schemas.DeleteCommentsCommentId, db: Session = Depends(get_db)):
    try:
        return await service.delete_comments_comment_id(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/posts_sample/id')
async def get_posts_sample_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_posts_sample_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/posts_sample/')
async def post_posts_sample(raw_data: schemas.PostPostsSample, db: Session = Depends(get_db)):
    try:
        return await service.post_posts_sample(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/posts_sample/id/')
async def put_posts_sample_id(raw_data: schemas.PutPostsSampleId, db: Session = Depends(get_db)):
    try:
        return await service.put_posts_sample_id(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/posts_sample/id')
async def delete_posts_sample_id(raw_data: schemas.DeletePostsSampleId, db: Session = Depends(get_db)):
    try:
        return await service.delete_posts_sample_id(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/test/')
async def post_test(raw_data: schemas.PostTest, db: Session = Depends(get_db)):
    try:
        return await service.post_test(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/test/id/')
async def put_test_id(raw_data: schemas.PutTestId, db: Session = Depends(get_db)):
    try:
        return await service.put_test_id(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/test/id')
async def delete_test_id(raw_data: schemas.DeleteTestId, db: Session = Depends(get_db)):
    try:
        return await service.delete_test_id(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

