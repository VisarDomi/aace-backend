# from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text, ForeignKey, Table
# from sqlalchemy.orm import relationship, backref
# from ..common.database import BaseModel
# from ..common.serializers import ModelSerializerMixin

# from datetime import datetime



# class Group(BaseModel, ModelSerializerMixin):
#     """
#     User.groups.all()
#     Group.users.all()
#     """
#     __tablename__ = 'groups'
#     id = Column(Integer, primary_key = True, autoincrement=True)

#     name = Column(String)

#     def __repr__(self):
#         return 'Group: {}'.format(self.name)


