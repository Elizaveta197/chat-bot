from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from .database import Base

class UserGroup(Base):
    __tablename__ = 'usergroups'

    group_id = Column(Integer, primary_key=True, index=True)
    group_name = Column(String, nullable=False)
    faculty_id = Column(Integer, ForeignKey('faculties.faculty_id'))
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)
    deleted_at = Column(TIMESTAMP)

    faculty = relationship("Faculty", back_populates="groups")
    users = relationship("User", back_populates="group")