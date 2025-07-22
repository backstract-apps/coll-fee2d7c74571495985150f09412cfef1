from sqlalchemy.orm import Session, aliased
from sqlalchemy import and_, or_
from typing import *
from fastapi import Request, UploadFile, HTTPException
import models, schemas
import boto3
import jwt
import datetime
import requests
import math
import random
import asyncio
from pathlib import Path


async def get_users_user_id(db: Session, user_id: int):

    query = db.query(models.Users)
    query = query.filter(and_(models.Users.user_id == user_id))

    users_one = query.first()

    users_one = (
        (users_one.to_dict() if hasattr(users_one, "to_dict") else vars(users_one))
        if users_one
        else users_one
    )

    res = {
        "users_one": users_one,
    }
    return res


async def delete_posts_post_id(db: Session, raw_data: schemas.DeletePostsPostId):
    post_id: int = raw_data.post_id

    query = db.query(models.Posts)
    query = query.filter(and_(models.Posts.post_id == post_id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        posts_deleted = record_to_delete.to_dict()
    else:
        posts_deleted = record_to_delete
    res = {
        "posts_deleted": posts_deleted,
    }
    return res


async def get_comments(db: Session):

    query = db.query(models.Comments)

    comments_all = query.all()
    comments_all = (
        [new_data.to_dict() for new_data in comments_all]
        if comments_all
        else comments_all
    )
    res = {
        "comments_all": comments_all,
    }
    return res


async def post_users(db: Session, raw_data: schemas.PostUsers):
    user_id: int = raw_data.user_id
    username: str = raw_data.username
    email: str = raw_data.email

    record_to_be_added = {"email": email, "user_id": user_id, "username": username}
    new_users = models.Users(**record_to_be_added)
    db.add(new_users)
    db.commit()
    db.refresh(new_users)
    users_inserted_record = new_users.to_dict()

    res = {
        "users_inserted_record": users_inserted_record,
    }
    return res


async def put_users_user_id(db: Session, raw_data: schemas.PutUsersUserId):
    user_id: int = raw_data.user_id
    username: str = raw_data.username
    email: str = raw_data.email

    query = db.query(models.Users)
    query = query.filter(and_(models.Users.user_id == user_id))
    users_edited_record = query.first()

    if users_edited_record:
        for key, value in {
            "email": email,
            "user_id": user_id,
            "username": username,
        }.items():
            setattr(users_edited_record, key, value)

        db.commit()
        db.refresh(users_edited_record)

        users_edited_record = (
            users_edited_record.to_dict()
            if hasattr(users_edited_record, "to_dict")
            else vars(users_edited_record)
        )
    res = {
        "users_edited_record": users_edited_record,
    }
    return res


async def delete_users_user_id(db: Session, raw_data: schemas.DeleteUsersUserId):
    user_id: int = raw_data.user_id

    query = db.query(models.Users)
    query = query.filter(and_(models.Users.user_id == user_id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        users_deleted = record_to_delete.to_dict()
    else:
        users_deleted = record_to_delete
    res = {
        "users_deleted": users_deleted,
    }
    return res


async def get_posts_sample(db: Session):

    query = db.query(models.PostsSample)

    posts_sample_all = query.all()
    posts_sample_all = (
        [new_data.to_dict() for new_data in posts_sample_all]
        if posts_sample_all
        else posts_sample_all
    )
    res = {
        "posts_sample_all": posts_sample_all,
    }
    return res


async def get_test(db: Session):

    query = db.query(models.Test)

    test_all = query.all()
    test_all = [new_data.to_dict() for new_data in test_all] if test_all else test_all
    res = {
        "test_all": test_all,
    }
    return res


async def get_test_id(db: Session, id: int):

    query = db.query(models.Test)
    query = query.filter(and_(models.Test.id == id))

    test_one = query.first()

    test_one = (
        (test_one.to_dict() if hasattr(test_one, "to_dict") else vars(test_one))
        if test_one
        else test_one
    )

    res = {
        "test_one": test_one,
    }
    return res


async def get_posts_post_id(db: Session, post_id: int):

    query = db.query(models.Posts)
    query = query.filter(and_(models.Posts.post_id == post_id))

    posts_one = query.first()

    posts_one = (
        (posts_one.to_dict() if hasattr(posts_one, "to_dict") else vars(posts_one))
        if posts_one
        else posts_one
    )

    res = {
        "posts_one": posts_one,
    }
    return res


async def post_posts(db: Session, raw_data: schemas.PostPosts):
    post_id: int = raw_data.post_id
    user_id: int = raw_data.user_id
    title: str = raw_data.title
    content: str = raw_data.content
    published_at: datetime.datetime = raw_data.published_at

    record_to_be_added = {
        "title": title,
        "content": content,
        "post_id": post_id,
        "user_id": user_id,
        "published_at": published_at,
    }
    new_posts = models.Posts(**record_to_be_added)
    db.add(new_posts)
    db.commit()
    db.refresh(new_posts)
    posts_inserted_record = new_posts.to_dict()

    res = {
        "posts_inserted_record": posts_inserted_record,
    }
    return res


async def put_posts_post_id(db: Session, raw_data: schemas.PutPostsPostId):
    post_id: int = raw_data.post_id
    user_id: int = raw_data.user_id
    title: str = raw_data.title
    content: str = raw_data.content
    published_at: datetime.datetime = raw_data.published_at

    query = db.query(models.Posts)
    query = query.filter(and_(models.Posts.post_id == post_id))
    posts_edited_record = query.first()

    if posts_edited_record:
        for key, value in {
            "title": title,
            "content": content,
            "post_id": post_id,
            "user_id": user_id,
            "published_at": published_at,
        }.items():
            setattr(posts_edited_record, key, value)

        db.commit()
        db.refresh(posts_edited_record)

        posts_edited_record = (
            posts_edited_record.to_dict()
            if hasattr(posts_edited_record, "to_dict")
            else vars(posts_edited_record)
        )
    res = {
        "posts_edited_record": posts_edited_record,
    }
    return res


async def get_posts(db: Session):

    query = db.query(models.Posts)

    posts_all = query.all()
    posts_all = (
        [new_data.to_dict() for new_data in posts_all] if posts_all else posts_all
    )
    res = {
        "posts_all": posts_all,
    }
    return res


async def get_users(db: Session):

    query = db.query(models.Users)

    users_all = query.all()
    users_all = (
        [new_data.to_dict() for new_data in users_all] if users_all else users_all
    )
    res = {
        "users_all": users_all,
    }
    return res


async def get_comments_comment_id(db: Session, comment_id: int):

    query = db.query(models.Comments)
    query = query.filter(and_(models.Comments.comment_id == comment_id))

    comments_one = query.first()

    comments_one = (
        (
            comments_one.to_dict()
            if hasattr(comments_one, "to_dict")
            else vars(comments_one)
        )
        if comments_one
        else comments_one
    )

    res = {
        "comments_one": comments_one,
    }
    return res


async def post_comments(db: Session, raw_data: schemas.PostComments):
    comment_id: int = raw_data.comment_id
    post_id: int = raw_data.post_id
    user_id: int = raw_data.user_id
    comment_text: str = raw_data.comment_text
    commented_at: datetime.datetime = raw_data.commented_at

    record_to_be_added = {
        "post_id": post_id,
        "user_id": user_id,
        "comment_id": comment_id,
        "comment_text": comment_text,
        "commented_at": commented_at,
    }
    new_comments = models.Comments(**record_to_be_added)
    db.add(new_comments)
    db.commit()
    db.refresh(new_comments)
    comments_inserted_record = new_comments.to_dict()

    res = {
        "comments_inserted_record": comments_inserted_record,
    }
    return res


async def put_comments_comment_id(db: Session, raw_data: schemas.PutCommentsCommentId):
    comment_id: int = raw_data.comment_id
    post_id: int = raw_data.post_id
    user_id: int = raw_data.user_id
    comment_text: str = raw_data.comment_text
    commented_at: datetime.datetime = raw_data.commented_at

    query = db.query(models.Comments)
    query = query.filter(and_(models.Comments.comment_id == comment_id))
    comments_edited_record = query.first()

    if comments_edited_record:
        for key, value in {
            "post_id": post_id,
            "user_id": user_id,
            "comment_id": comment_id,
            "comment_text": comment_text,
            "commented_at": commented_at,
        }.items():
            setattr(comments_edited_record, key, value)

        db.commit()
        db.refresh(comments_edited_record)

        comments_edited_record = (
            comments_edited_record.to_dict()
            if hasattr(comments_edited_record, "to_dict")
            else vars(comments_edited_record)
        )
    res = {
        "comments_edited_record": comments_edited_record,
    }
    return res


async def delete_comments_comment_id(
    db: Session, raw_data: schemas.DeleteCommentsCommentId
):
    comment_id: int = raw_data.comment_id

    query = db.query(models.Comments)
    query = query.filter(and_(models.Comments.comment_id == comment_id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        comments_deleted = record_to_delete.to_dict()
    else:
        comments_deleted = record_to_delete
    res = {
        "comments_deleted": comments_deleted,
    }
    return res


async def get_posts_sample_id(db: Session, id: int):

    query = db.query(models.PostsSample)
    query = query.filter(and_(models.PostsSample.id == id))

    posts_sample_one = query.first()

    posts_sample_one = (
        (
            posts_sample_one.to_dict()
            if hasattr(posts_sample_one, "to_dict")
            else vars(posts_sample_one)
        )
        if posts_sample_one
        else posts_sample_one
    )

    res = {
        "posts_sample_one": posts_sample_one,
    }
    return res


async def post_posts_sample(db: Session, raw_data: schemas.PostPostsSample):
    id: int = raw_data.id
    title: str = raw_data.title
    description: str = raw_data.description
    views: int = raw_data.views
    is_published: bool = raw_data.is_published
    created_at: datetime.datetime = raw_data.created_at
    updated_at: datetime.datetime = raw_data.updated_at
    image: bytes = raw_data.image
    reference_id: uuid.UUID = raw_data.reference_id

    record_to_be_added = {
        "id": id,
        "image": image,
        "title": title,
        "views": views,
        "created_at": created_at,
        "updated_at": updated_at,
        "description": description,
        "is_published": is_published,
        "reference_id": reference_id,
    }
    new_posts_sample = models.PostsSample(**record_to_be_added)
    db.add(new_posts_sample)
    db.commit()
    db.refresh(new_posts_sample)
    posts_sample_inserted_record = new_posts_sample.to_dict()

    res = {
        "posts_sample_inserted_record": posts_sample_inserted_record,
    }
    return res


async def put_posts_sample_id(db: Session, raw_data: schemas.PutPostsSampleId):
    id: int = raw_data.id
    title: str = raw_data.title
    description: str = raw_data.description
    views: int = raw_data.views
    is_published: bool = raw_data.is_published
    created_at: datetime.datetime = raw_data.created_at
    updated_at: datetime.datetime = raw_data.updated_at
    image: bytes = raw_data.image
    reference_id: uuid.UUID = raw_data.reference_id

    query = db.query(models.PostsSample)
    query = query.filter(and_(models.PostsSample.id == id))
    posts_sample_edited_record = query.first()

    if posts_sample_edited_record:
        for key, value in {
            "id": id,
            "image": image,
            "title": title,
            "views": views,
            "created_at": created_at,
            "updated_at": updated_at,
            "description": description,
            "is_published": is_published,
            "reference_id": reference_id,
        }.items():
            setattr(posts_sample_edited_record, key, value)

        db.commit()
        db.refresh(posts_sample_edited_record)

        posts_sample_edited_record = (
            posts_sample_edited_record.to_dict()
            if hasattr(posts_sample_edited_record, "to_dict")
            else vars(posts_sample_edited_record)
        )
    res = {
        "posts_sample_edited_record": posts_sample_edited_record,
    }
    return res


async def delete_posts_sample_id(db: Session, raw_data: schemas.DeletePostsSampleId):
    id: int = raw_data.id

    query = db.query(models.PostsSample)
    query = query.filter(and_(models.PostsSample.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        posts_sample_deleted = record_to_delete.to_dict()
    else:
        posts_sample_deleted = record_to_delete
    res = {
        "posts_sample_deleted": posts_sample_deleted,
    }
    return res


async def post_test(db: Session, raw_data: schemas.PostTest):
    id: int = raw_data.id
    title: str = raw_data.title
    description: str = raw_data.description
    views: int = raw_data.views
    rating: float = raw_data.rating
    is_published: bool = raw_data.is_published
    created_at: datetime.datetime = raw_data.created_at
    updated_at: datetime.datetime = raw_data.updated_at
    image: bytes = raw_data.image
    reference_id: uuid.UUID = raw_data.reference_id

    record_to_be_added = {
        "id": id,
        "image": image,
        "title": title,
        "views": views,
        "rating": rating,
        "created_at": created_at,
        "updated_at": updated_at,
        "description": description,
        "is_published": is_published,
        "reference_id": reference_id,
    }
    new_test = models.Test(**record_to_be_added)
    db.add(new_test)
    db.commit()
    db.refresh(new_test)
    test_inserted_record = new_test.to_dict()

    res = {
        "test_inserted_record": test_inserted_record,
    }
    return res


async def put_test_id(db: Session, raw_data: schemas.PutTestId):
    id: int = raw_data.id
    title: str = raw_data.title
    description: str = raw_data.description
    views: int = raw_data.views
    rating: float = raw_data.rating
    is_published: bool = raw_data.is_published
    created_at: datetime.datetime = raw_data.created_at
    updated_at: datetime.datetime = raw_data.updated_at
    image: bytes = raw_data.image
    reference_id: uuid.UUID = raw_data.reference_id

    query = db.query(models.Test)
    query = query.filter(and_(models.Test.id == id))
    test_edited_record = query.first()

    if test_edited_record:
        for key, value in {
            "id": id,
            "image": image,
            "title": title,
            "views": views,
            "rating": rating,
            "created_at": created_at,
            "updated_at": updated_at,
            "description": description,
            "is_published": is_published,
            "reference_id": reference_id,
        }.items():
            setattr(test_edited_record, key, value)

        db.commit()
        db.refresh(test_edited_record)

        test_edited_record = (
            test_edited_record.to_dict()
            if hasattr(test_edited_record, "to_dict")
            else vars(test_edited_record)
        )
    res = {
        "test_edited_record": test_edited_record,
    }
    return res


async def delete_test_id(db: Session, raw_data: schemas.DeleteTestId):
    id: int = raw_data.id

    query = db.query(models.Test)
    query = query.filter(and_(models.Test.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        test_deleted = record_to_delete.to_dict()
    else:
        test_deleted = record_to_delete
    res = {
        "test_deleted": test_deleted,
    }
    return res
