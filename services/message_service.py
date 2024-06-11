from datetime import datetime
from asyncpg import Connection
from models.message import Message

class MessageService:

    async def create_message(self, conn: Connection, thread_id: str, user_id: str, content: str) -> Message:
        message_id = datetime.utcnow().isoformat()
        await conn.execute('INSERT INTO messages (id, thread_id, user_id, content, created_at) VALUES ($1, $2, $3, $4, $5)', message_id, thread_id, user_id, content, datetime.utcnow())
        return Message(id=message_id, thread_id=thread_id, user_id=user_id, content=content, created_at=datetime.utcnow())

    async def get_messages_by_thread(self, conn: Connection, thread_id: str):
        rows = await conn.fetch('SELECT * FROM messages WHERE thread_id = $1 ORDER BY created_at DESC', thread_id)
        return [Message(**row) for row in rows]

    async def delete_message(self, conn: Connection, message_id: str):
        await conn.execute('DELETE FROM messages WHERE id = $1', message_id)
