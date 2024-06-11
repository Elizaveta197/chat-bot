# test_db.py
import asyncio
import unittest

from models import User, Thread, Message

class DatabaseTestCase(unittest.TestCase):
    def setUp(self):
        self.db_session = create_test_session()

    def test_user_creation(self):
        user = User(name="Иван Иванов", group="ПИ-341")
        self.db_session.add(user)
        self.db_session.commit()
        query_user = self.db_session.query(User).filter_by(name="Иван Иванов").first()
        self.assertIsNotNone(query_user)
        self.assertEqual(query_user.group, "ПИ-341")

    def test_thread_handling(self):
        thread = Thread(title="Тестовый тред", user_id=1)
        self.db_session.add(thread)
        self.db_session.commit()
        query_thread = self.db_session.query(Thread).filter_by(title="Тестовый тред").first()
        self.assertIsNotNone(query_thread)
        self.assertEqual(query_thread.user_id, 1)

    def test_message_saving(self):
        message = Message(content="Тестовое сообщение", thread_id=1)
        self.db_session.add(message)
        self.db_session.commit()
        query_message = self.db_session.query(Message).filter_by(content="Тестовое сообщение").first()
        self.assertIsNotNone(query_message)
        self.assertEqual(query_message.thread_id, 1)

