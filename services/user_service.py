import uuid
from datetime import datetime, timedelta
from typing import Optional
from asyncpg import Connection
from models.user import User

class UserService:

    async def create_user(self, conn: Connection, user_data: dict) -> User:
        user_id = str(uuid.uuid4())
        now = datetime.utcnow()
        user = User(
            id=user_id,
            username=user_data['username'],
            created_at=now,
            updated_at=now
        )
        await conn.execute('INSERT INTO users VALUES ($1, $2, $3, $4)', user_id, user.username, now, now)
        return user

    async def get_user(self, conn: Connection, user_id: str) -> Optional[User]:
        row = await conn.fetchrow('SELECT * FROM users WHERE id = $1', user_id)
        if row:
            return User(**row)
        return None

    async def update_user_activity(self, conn: Connection, user_id: str):
        now = datetime.utcnow()
        await conn.execute('UPDATE users SET updated_at = $1 WHERE id = $2', now, user_id)

    async def deactivate_user(self, conn: Connection, user_id: str):
        await conn.execute('DELETE FROM users WHERE id = $1', user_id)
