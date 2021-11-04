from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class Quads(Base):
    __tablename__ = 'quads'

    id = Column(Integer, primary_key=True)
    quad_number = Column(Integer, nullable=False, unique=True)
    node_0 = Column(String, nullable=False)
    node_1 = Column(String, nullable=False)
    node_2 = Column(String, nullable=False)
    node_3 = Column(String, nullable=False)
    area = Column(Integer, nullable=False)
    group = Column(Integer, nullable=False)
    banding_moment_mxx = Column(Integer, nullable=False)
    banding_moment_myy = Column(Integer, nullable=False)
    banding_moment_mxy = Column(Integer, nullable=False)

    def __repr__(self):
        return f'Quad {self.quad_number}'

# bot_users_table = Table('accounts', meta,
#                     Column('id', INTEGER, primary_key=True),
#                     Column('chat_id', CHAR, nullable=False),
#                     Column('nickname', CHAR, nullable=True, ),
#                     Column('name', CHAR, nullable=True, ),
#                     Column('telephone', CHAR, nullable=True),
#                     Column('location', CHAR, nullable=True, default=''),
#                     Column('user_created', DATETIME)
#                     )
#
#
# users_messages = Table('accounts_usersmessages', meta,
#                        Column('id', INTEGER, primary_key=True),
#                        Column('chat_id_id', INTEGER, nullable=True),
#                        Column('nickname', CHAR, nullable=True),
#                        Column('name', CHAR, nullable=True),
#                        Column('message', String, nullable=False),
#                        Column('location', CHAR, nullable=True),
#                        Column('message_time', DATETIME),
#                        Column('status', CHAR, nullable=True, default='')
#                        )
#
# reply_messages = Table('accounts_messagesreplys', meta,
#                        Column('id', INTEGER, primary_key=True),
#                        Column('chat_id_id', INTEGER, nullable=True),
#                        Column('nickname', CHAR, nullable=True),
#                        Column('name', CHAR, nullable=True),
#                        Column('message', String, nullable=False),
#                        Column('message_time', DATETIME),
#                        Column('status', CHAR, nullable=True, default='')
#                        )
