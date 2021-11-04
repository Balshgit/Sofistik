from datetime import datetime, timezone, timedelta
from typing import Any

from sqlalchemy import create_engine
from sqlalchemy import update
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker

from sofistik.database.models import Quads
from sofistik.utils import logger
from sofistik.settings import DATABASE_NAME

engine = create_engine(fr'sqlite:///{DATABASE_NAME}')
session_factory = sessionmaker(bind=engine)


def get_now(offset: int) -> datetime:
    """
    Return current time with offset in hours

    :param offset: Set hours to offset from now

    :return: Now date and time with chosen offset
    """
    _offset = timezone(timedelta(hours=offset))
    now = datetime.now(_offset)
    return now


def db_insert_or_update_quad(update_obj: bool, quad_number: int, nodes: tuple, area: int, group: int,
                             banding_moment_mxx: int, banding_moment_myy: int, banding_moment_mxy: int) -> None:
    """
    Add new quad or update it

    :param update_obj: Set it True to update quad if it exists
    :param quad_number: Quad number in database
    :param nodes: List of quad nodes
    :param area: Area which quad is belong
    :param group: Group of objects
    :param banding_moment_mxx: Quad moments by xx
    :param banding_moment_myy: Quad moments by yy
    :param banding_moment_mxy: Quad moments by xy

    :return: Update or create quad instance
    """
    try:
        with session_factory() as session:
            quad = Quads(quad_number=quad_number,
                         node_0=str(nodes[0]),
                         node_1=str(nodes[1]),
                         node_2=str(nodes[2]),
                         node_3=str(nodes[3]),
                         area=area,
                         group=group,
                         banding_moment_mxx=banding_moment_mxx,
                         banding_moment_myy=banding_moment_myy,
                         banding_moment_mxy=banding_moment_mxy
                         )
            session.add(quad)
            session.commit()
    except IntegrityError:
        if update_obj:
            logger.error(f'Quad {quad_number} already exists. Updating quad')
            with session_factory() as session:
                session.execute(update(Quads).where(Quads.quad_number == quad_number).
                                values(node_0=str(nodes[0]),
                                       node_1=str(nodes[1]),
                                       node_2=str(nodes[2]),
                                       node_3=str(nodes[3]),
                                       area=area,
                                       group=group,
                                       banding_moment_mxx=banding_moment_mxx,
                                       banding_moment_myy=banding_moment_myy,
                                       banding_moment_mxy=banding_moment_mxy))
                session.commit()
    except Exception as e:
        logger.error(f'Unexpected error {e}')


def db_get_quad(quad_number: int) -> Any:
    """
    Get quad from db by its number

    :param quad_number: quad number

    :return: Quad object
    """
    try:
        with session_factory() as session:
            quad = session.query(Quads).filter(Quads.quad_number == quad_number).one()
        return quad
    except Exception as e:
        logger.error(e)
#
#
# def db_get_location(chat_id):
#
#     try:
#         user = session.query(bot_users_table)\
#             .filter(bot_users_table.c.chat_id == chat_id).one()
#         return user.location
#     except:
#         pass
#
#
# def db_get_id(chat_id):
#
#     try:
#         user = session.query(bot_users_table) \
#             .filter(bot_users_table.c.chat_id == chat_id).one()
#         return user.id
#     except(Exception) as e:
#         print('ERORO chat ID', e)
#         pass
#
#
# def db_update_location(chat_id, location):
#     with engine.connect() as conn:
#         try:
#             insert_statement = bot_users_table.update().values(location=location). \
#                 where(bot_users_table.c.chat_id == chat_id)
#             conn.execute(insert_statement)
#         except Exception as e:
#             print('ERROR!!!!!!!!!!!!!!!!', e)
#             pass
#
#
# def db_insert_reply_message(chat_id_id, nickname=None, name=None, reply_message=None):
#
#     with engine.connect() as conn:
#
#         insert_statement = reply_messages.insert().values(chat_id_id=chat_id_id,
#                                                        nickname=nickname,
#                                                        name=name,
#                                                        message=reply_message,
#                                                        message_time=get_now(3)
#                                                        )
#         conn.execute(insert_statement)
#
#
# def db_insert_user_message(chat_id_id, nickname=None, location=None,
#                            name=None, message=None):
#
#     with engine.connect() as conn:
#
#         insert_statement = users_messages.insert().values(chat_id_id=chat_id_id,
#                                                           nickname=nickname,
#                                                           name=name,
#                                                           message=message,
#                                                           location=location,
#                                                           message_time=get_now(3)
#                                                           )
#         conn.execute(insert_statement)
#
#
# def db_insert_announce(author, bot_announce):
#
#     with engine.connect() as conn:
#
#         insert_statement = announce.insert().values(announce=bot_announce,
#                                                     author=author,
#                                                     created=get_now(3)
#                                                     )
#         conn.execute(insert_statement)

# test_quads = {}
# test_quads[7770102] = ('(555, 777)', '(333, 22)', '(888, 555)', '(888, 222)')
# db_insert_or_update_quad(quad_number=7770102, nodes=test_quads[7770102], area=102, group=7117, banding_moment_mxx=10,
#                     banding_moment_myy=20, banding_moment_mxy=30)
# print(db_get_quad(quad_number=560131))
# db_insert_reply_message(chat_id='1660356916', reply_message='asdasd')
# db_update_location(chat_id='1660356916', location='lsdkjfldskj')
# print(db_get_id('417070387'))
