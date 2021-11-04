from sqlalchemy import create_engine
from sqlalchemy import Table, Column, String, MetaData, DATETIME, CHAR, INTEGER
from sqlalchemy.orm import Session, sessionmaker
from datetime import datetime, timezone, timedelta
from sofistik.utils import logger

engine = create_engine(r'sqlite:///sofistik.db')

session_factory = sessionmaker(engine)
session = session_factory()
meta = MetaData(engine)


def get_now(offset):
    _offset = timezone(timedelta(hours=offset))
    now = datetime.now(_offset)
    return now


quads = Table('quads', meta,
              Column('id', INTEGER, primary_key=True),
              Column('quad_number', INTEGER, nullable=False, unique=True),
              Column('node_0', String, nullable=False),
              Column('node_1', String, nullable=False),
              Column('node_2', String, nullable=False),
              Column('node_3', String, nullable=False),
              Column('area', INTEGER, nullable=False),
              Column('plate', INTEGER, nullable=False)
              )


bot_users_table = Table('accounts', meta,
                    Column('id', INTEGER, primary_key=True),
                    Column('chat_id', CHAR, nullable=False),
                    Column('nickname', CHAR, nullable=True, ),
                    Column('name', CHAR, nullable=True, ),
                    Column('telephone', CHAR, nullable=True),
                    Column('location', CHAR, nullable=True, default=''),
                    Column('user_created', DATETIME)
                    )


users_messages = Table('accounts_usersmessages', meta,
                       Column('id', INTEGER, primary_key=True),
                       Column('chat_id_id', INTEGER, nullable=True),
                       Column('nickname', CHAR, nullable=True),
                       Column('name', CHAR, nullable=True),
                       Column('message', String, nullable=False),
                       Column('location', CHAR, nullable=True),
                       Column('message_time', DATETIME),
                       Column('status', CHAR, nullable=True, default='')
                       )

reply_messages = Table('accounts_messagesreplys', meta,
                       Column('id', INTEGER, primary_key=True),
                       Column('chat_id_id', INTEGER, nullable=True),
                       Column('nickname', CHAR, nullable=True),
                       Column('name', CHAR, nullable=True),
                       Column('message', String, nullable=False),
                       Column('message_time', DATETIME),
                       Column('status', CHAR, nullable=True, default='')
                       )


def db_insert_or_update(quad_number: int, nodes: tuple, area: int, plate_number: int) -> None:

    with engine.connect() as conn:
        try:
            insert_statement = quads.insert().values(quad_number=quad_number,
                                                     node_0=str(nodes[0]),
                                                     node_1=str(nodes[1]),
                                                     node_2=str(nodes[2]),
                                                     node_3=str(nodes[3]),
                                                     area=area,
                                                     plate=plate_number
                                                     )
            conn.execute(insert_statement)
        except Exception as e:
            logger.error(e)
            # insert_statement = bot_users_table.update().values(nickname=nickname, name=name, telephone=telephone).\
            #     where(bot_users_table.c.chat_id == chat_id)
            # conn.execute(insert_statement)


def db_get_contact_number(chat_id):
    try:
        user = session.query(bot_users_table)\
            .filter(bot_users_table.c.chat_id == chat_id).one()
        return user.telephone
    except:
        pass


def db_get_location(chat_id):

    try:
        user = session.query(bot_users_table)\
            .filter(bot_users_table.c.chat_id == chat_id).one()
        return user.location
    except:
        pass


def db_get_id(chat_id):

    try:
        user = session.query(bot_users_table) \
            .filter(bot_users_table.c.chat_id == chat_id).one()
        return user.id
    except(Exception) as e:
        print('ERORO chat ID', e)
        pass


def db_update_location(chat_id, location):
    with engine.connect() as conn:
        try:
            insert_statement = bot_users_table.update().values(location=location). \
                where(bot_users_table.c.chat_id == chat_id)
            conn.execute(insert_statement)
        except Exception as e:
            print('ERROR!!!!!!!!!!!!!!!!', e)
            pass


def db_insert_reply_message(chat_id_id, nickname=None, name=None, reply_message=None):

    with engine.connect() as conn:

        insert_statement = reply_messages.insert().values(chat_id_id=chat_id_id,
                                                       nickname=nickname,
                                                       name=name,
                                                       message=reply_message,
                                                       message_time=get_now(3)
                                                       )
        conn.execute(insert_statement)


def db_insert_user_message(chat_id_id, nickname=None, location=None,
                           name=None, message=None):

    with engine.connect() as conn:

        insert_statement = users_messages.insert().values(chat_id_id=chat_id_id,
                                                          nickname=nickname,
                                                          name=name,
                                                          message=message,
                                                          location=location,
                                                          message_time=get_now(3)
                                                          )
        conn.execute(insert_statement)


def db_insert_announce(author, bot_announce):

    with engine.connect() as conn:

        insert_statement = announce.insert().values(announce=bot_announce,
                                                    author=author,
                                                    created=get_now(3)
                                                    )
        conn.execute(insert_statement)

# test_quads = {}
# test_quads[7770102] = ('(151.5, 103.79999999999998)', '(139.20000000000002, 66.0)', '(101.7, 65.1)', '(112.5, 104.1)')
# db_insert_or_update(quad_number=7770102, nodes=test_quads[7770102], area=2, plate_number=56)
# print(db_get_contact_number('417070387'))
# db_insert_reply_message(chat_id='1660356916', reply_message='asdasd')
# db_update_location(chat_id='1660356916', location='lsdkjfldskj')
# print(db_get_id('417070387'))