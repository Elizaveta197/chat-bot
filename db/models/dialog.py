from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from .database import Base

class Dialog(Base):
    __tablename__ = 'dialogs'

    dialog_id = Column(Integer, primary_key=True, index=True)
    thread_id = Column(Integer, ForeignKey('threads.thread_id'))
    message = Column(String)
    is_user_message = Column(Integer)  # boolean in DB
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)
    deleted_at = Column(TIMESTAMP)
    creator_id = Column(Integer, ForeignKey('users.user_id'))

    thread = relationship("Thread")
    creator = relationship("User", remote_side=[user_id])