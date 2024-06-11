from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from .database import Base

class Faculty(Base):
    __tablename__ = 'faculties'

    faculty_id = Column(Integer, primary_key=True, index=True)
    faculty_name = Column(String, nullable=False)
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)
    deleted_at = Column(TIMESTAMP)

    groups = relationship("UserGroup", back_populates="faculty")
    users = relationship("User", back_populates="faculty")