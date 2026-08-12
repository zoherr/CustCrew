from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.Users import UserRepository
from app.schemas.Users import UserCreate
from fastapi import HTTPException


class UserService:
    def __init__(self, db: AsyncSession):
        self.db = db
        self.repository = UserRepository(self.db)

    async def Create(self, user: UserCreate):

        isExist = await self.repository.UserExist(user.email)
        
        if isExist:
            raise HTTPException(
                400, {"success": False, "message": "User Already Exist"}
            )
        
        user = await self.repository.create(user.name, user.email, user.password)

        return user
