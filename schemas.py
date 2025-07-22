from pydantic import BaseModel,Field,field_validator

import datetime

import uuid

from typing import Any, Dict, List,Optional,Tuple

import re

class Users(BaseModel):
    user_id: int
    username: str
    email: str


class ReadUsers(BaseModel):
    user_id: int
    username: str
    email: str
    class Config:
        from_attributes = True


class Posts(BaseModel):
    post_id: int
    user_id: int
    title: str
    content: str
    published_at: datetime.time


class ReadPosts(BaseModel):
    post_id: int
    user_id: int
    title: str
    content: str
    published_at: datetime.time
    class Config:
        from_attributes = True


class Comments(BaseModel):
    comment_id: int
    post_id: int
    user_id: int
    comment_text: str
    commented_at: datetime.time


class ReadComments(BaseModel):
    comment_id: int
    post_id: int
    user_id: int
    comment_text: str
    commented_at: datetime.time
    class Config:
        from_attributes = True


class PostsSample(BaseModel):
    id: int
    title: str
    description: str
    views: int
    is_published: bool
    created_at: datetime.time
    updated_at: datetime.time
    image: bytes
    reference_id: uuid.UUID


class ReadPostsSample(BaseModel):
    id: int
    title: str
    description: str
    views: int
    is_published: bool
    created_at: datetime.time
    updated_at: datetime.time
    image: bytes
    reference_id: uuid.UUID
    class Config:
        from_attributes = True


class Test(BaseModel):
    id: int
    title: str
    description: str
    views: int
    rating: float
    is_published: bool
    created_at: datetime.time
    updated_at: datetime.time
    image: bytes
    reference_id: uuid.UUID


class ReadTest(BaseModel):
    id: int
    title: str
    description: str
    views: int
    rating: float
    is_published: bool
    created_at: datetime.time
    updated_at: datetime.time
    image: bytes
    reference_id: uuid.UUID
    class Config:
        from_attributes = True




class DeletePostsPostId(BaseModel):
    post_id: int = Field(...)

    class Config:
        from_attributes = True



class PostUsers(BaseModel):
    user_id: int = Field(...)
    username: str = Field(..., max_length=100)
    email: str = Field(..., max_length=100)

    class Config:
        from_attributes = True



class PutUsersUserId(BaseModel):
    user_id: int = Field(...)
    username: str = Field(..., max_length=100)
    email: str = Field(..., max_length=100)

    class Config:
        from_attributes = True



class DeleteUsersUserId(BaseModel):
    user_id: int = Field(...)

    class Config:
        from_attributes = True



class PostPosts(BaseModel):
    post_id: int = Field(...)
    user_id: int = Field(...)
    title: str = Field(..., max_length=100)
    content: str = Field(..., max_length=100)
    published_at: Any = Field(...)

    class Config:
        from_attributes = True



class PutPostsPostId(BaseModel):
    post_id: int = Field(...)
    user_id: int = Field(...)
    title: str = Field(..., max_length=100)
    content: str = Field(..., max_length=100)
    published_at: Any = Field(...)

    class Config:
        from_attributes = True



class PostComments(BaseModel):
    comment_id: int = Field(...)
    post_id: int = Field(...)
    user_id: int = Field(...)
    comment_text: str = Field(..., max_length=100)
    commented_at: Any = Field(...)

    class Config:
        from_attributes = True



class PutCommentsCommentId(BaseModel):
    comment_id: int = Field(...)
    post_id: int = Field(...)
    user_id: int = Field(...)
    comment_text: str = Field(..., max_length=100)
    commented_at: Any = Field(...)

    class Config:
        from_attributes = True



class DeleteCommentsCommentId(BaseModel):
    comment_id: int = Field(...)

    class Config:
        from_attributes = True



class PostPostsSample(BaseModel):
    id: int = Field(...)
    title: str = Field(..., max_length=100)
    description: str = Field(..., max_length=100)
    views: int = Field(...)
    is_published: bool = Field(...)
    created_at: Any = Field(...)
    updated_at: Any = Field(...)
    image: Any = Field(...)
    reference_id: Any = Field(...)

    class Config:
        from_attributes = True



class PutPostsSampleId(BaseModel):
    id: int = Field(...)
    title: str = Field(..., max_length=100)
    description: str = Field(..., max_length=100)
    views: int = Field(...)
    is_published: bool = Field(...)
    created_at: Any = Field(...)
    updated_at: Any = Field(...)
    image: Any = Field(...)
    reference_id: Any = Field(...)

    class Config:
        from_attributes = True



class DeletePostsSampleId(BaseModel):
    id: int = Field(...)

    class Config:
        from_attributes = True



class PostTest(BaseModel):
    id: int = Field(...)
    title: str = Field(..., max_length=100)
    description: str = Field(..., max_length=100)
    views: int = Field(...)
    rating: Any = Field(...)
    is_published: bool = Field(...)
    created_at: Any = Field(...)
    updated_at: Any = Field(...)
    image: Any = Field(...)
    reference_id: Any = Field(...)

    class Config:
        from_attributes = True



class PutTestId(BaseModel):
    id: int = Field(...)
    title: str = Field(..., max_length=100)
    description: str = Field(..., max_length=100)
    views: int = Field(...)
    rating: Any = Field(...)
    is_published: bool = Field(...)
    created_at: Any = Field(...)
    updated_at: Any = Field(...)
    image: Any = Field(...)
    reference_id: Any = Field(...)

    class Config:
        from_attributes = True



class DeleteTestId(BaseModel):
    id: int = Field(...)

    class Config:
        from_attributes = True

