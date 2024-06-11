# user.py
from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    group_id = Column(Integer, ForeignKey('usergroups.group_id'))
    faculty_id = Column(Integer, ForeignKey('faculties.faculty_id'))
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)
    deleted_at = Column(TIMESTAMP)
    creator_id = Column(Integer, ForeignKey('users.user_id'))

    creator = relationship("User", remote_side=[user_id])
    group = relationship("UserGroup", back_populates="users")
    faculty = relationship("Faculty", back_populates="users")