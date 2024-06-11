from datetime import datetime
from asyncpg import Connection
from models.thread import Thread

class ThreadService:

    async def create_thread(self, conn: Connection, user_id: str, title: str) -> Thread:
        thread_id = datetime.utcnow().isoformat()
        await conn.execute('INSERT INTO threads (id, user_id, title, created_at) VALUES ($1, $2, $3, $4)', thread_id, user_id, title, datetime.utcnow())
        return Thread(id=thread_id, user_id=user_id, title=title, created_at=datetime.utcnow())

    async def get_thread(self, conn: Connection, thread_id: str) -> Thread:
        row = await conn.fetchrow('SELECT * FROM threads WHERE id = $1', thread_id)
        if row:
            return Thread(**row)
        raise Exception("Thread not found")

    async def close_thread(self, conn: Connection, thread_id: str):
        await conn.execute('UPDATE threads SET is_active = FALSE WHERE id = $1', thread_id)
