from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from .database import Base

class Thread(Base):
    __tablename__ = 'threads'

    thread_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    status = Column(String)
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)
    deleted_at = Column(TIMESTAMP)
    creator_id = Column(Integer, ForeignKey('users.user_id'))

    user = relationship("User")
    creator = relationship("User", remote_side=[user_id])