from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.UsersModel import User

class UserRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, name: str, email: str,password:str) -> User:
        user = User(
            name=name,
            email=email,
            password=password
        )

        self.db.add(user)
        await self.db.commit()
        await self.db.refresh(user)

        return user

    async def UserExist(self, email:str):
        result = await self.db.execute(select(User).where(User.email == email))
        user = result.scalar_one_or_none()
        if user:
            return user
        return False

