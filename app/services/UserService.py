from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.Users import UserRepository
from app.schemas.Users import UserCreate,UserLogin
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

    async def login(self,user:UserLogin):

        user = await self.repository.UserExist(user.email)

        if user:
            if user.password ==  user.password:
                return user
            raise HTTPException(
                            400, {"success": False, "message": "Password is Wrong"}
                        ) 
        
        raise HTTPException(
                        400, {"success": False, "message": "User Email is does't exist"}
                    )