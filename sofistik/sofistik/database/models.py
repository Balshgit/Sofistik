import datetime

from sqlalchemy import Column, String, Integer, ForeignKey, CHAR, DATETIME, INTEGER, Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Quads(Base):
    """ Quad model for data base """
    __tablename__ = 'quads'

    id = Column(Integer, primary_key=True)
    quad_number = Column(Integer, nullable=False, unique=True)
    node_0 = Column(String(255), nullable=False)
    node_1 = Column(String(255), nullable=False)
    node_2 = Column(String(255), nullable=False)
    node_3 = Column(String(255), nullable=False)
    area = Column(Integer, nullable=False)
    group = Column(Integer, nullable=False)
    bending_moment_mxx = Column(Integer, nullable=False)
    bending_moment_myy = Column(Integer, nullable=False)
    bending_moment_mxy = Column(Integer, nullable=False)

    def __repr__(self):
        return f'Quad {self.quad_number}'


# class User(Base):
#     __tablename__ = "users"
#
#     id = Column(Integer, primary_key=True)
#     username = Column(String(255), unique=True, nullable=False)
#     password = Column(String(255), nullable=False)
#     email = Column(String(255), unique=True, nullable=False)
#     created = Column(DATETIME, server_default=datetime.datetime.now)
#
#     def __repr__(self):
#         return f'User {self.username}'
#
#
# class Comment(Base):
#     __tablename__ = 'comments'
#
#     id = Column(Integer, primary_key=True)
#     node_number = Column(CHAR, nullable=False, default='')
#     body = Column(Text, nullable=False)
#     user_id = Column(Integer, ForeignKey('quads.id', ondelete='SET NULL'), nullable=False)
#     post_id = Column(Integer, ForeignKey('posts.id', ondelete='CASCADE'), nullable=False)
#
#     def __repr__(self):
#         return f'Comment {self.id}'
#
#
# class Post(Base):
#     __tablename__ = 'posts'
#
#     id = Column(Integer, primary_key=True)
#     title = Column(String(255), nullable=True)
#     text = Column(Text, nullable=False)
#     author_id = Column(Integer, ForeignKey('users.id', ondelete='RESTRICT'), nullable=False)
#
#     def __repr__(self):
#         return f'Post {self.title[:10]}'
