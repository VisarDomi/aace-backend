from sqlathanor import declarative_base

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy_utils import database_exists, create_database, drop_database
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.exc import DatabaseError
from config import Config

engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)

db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)


class CustomBase(object):
    """This overrides the default
    `_declarative_constructor` constructor."""

    # def __init__(self, **kwargs):
    #     """It skips the attributes that are not present
    #     for the model, thus if a dict is passed with some
    #     unknown attributes for the model on creation,
    #     it won't complain for `unkwnown field`s.
    #     """
    #     cls_ = type(self)
    #     for k in kwargs:
    #         if hasattr(cls_, k):
    #             setattr(self, k, kwargs[k])
    #         else:
    #             continue

    @declared_attr
    def __tablename__(cls):
        """
        Set default tablename
        """
        return cls.__name__.lower()

    def save(self):
        """
        Add and try to flush.
        """
        db_session.add(self)
        self._flush()
        return self

    # def update(self, **kwargs):
    #     """
    #     Update and try to flush.
    #     """
    #     for attr, value in kwargs.items():
    #         if hasattr(self, attr):
    #             setattr(self, attr, value)
    #     return self.save()

    def delete(self):
        """
        Delete and try to flush.
        """
        db_session.delete(self)
        self._flush()

    def _flush(self):
        """
        Try to flush. If an error is raised,
        the session is rollbacked.
        """
        try:
            db_session.flush()
        except DatabaseError:
            db_session.rollback()


BaseModel = declarative_base()
BaseModel.query = db_session.query_property()


def init_db():
    """
    Create database if doesn't exist and
    create all tables.
    """
    if not database_exists(engine.url):
        create_database(engine.url)
    BaseModel.metadata.create_all(bind=engine)


def drop_db():
    """
    Drop all of the record from tables and the tables
    themselves.
    Drop the database as well.
    """
    BaseModel.metadata.drop_all(bind=engine)
    drop_database(engine.url)
