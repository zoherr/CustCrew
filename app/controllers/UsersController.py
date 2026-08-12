from sqlalchemy.ext.asyncio import AsyncSession

from app.services.UserService import UserService
from app.schemas.Users import UserCreate,UserLogin,User
from app.utils.jwt import create_access_token

async def CreateUser(user: UserCreate, db: AsyncSession):
    service = UserService(db)
    user = await service.Create(user)
    return user


async def LoginUser(response,user:UserLogin,db:AsyncSession):
    service = UserService(db)
    user = await service.login(user)
    token = create_access_token(user.id)
    
    response.set_cookie(
        key="access_token",
        value=token,
        httponly=True,
        secure=False,
        samesite="lax",
        max_age=1800
    )

    return user