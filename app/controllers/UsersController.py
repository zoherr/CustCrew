from sqlalchemy.ext.asyncio import AsyncSession

from app.services.UserService import UserService
from app.schemas.Users import UserCreate


async def CreateUser(user: UserCreate, db: AsyncSession):
    service = UserService(db)
    user = await service.Create(user)
    return user

