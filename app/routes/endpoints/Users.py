from fastapi import APIRouter,Depends
from sqlalchemy.ext.asyncio import  AsyncSession
from app.schemas.Users import UserCreate
from app.controllers.UsersController import CreateUser
from app.core.database import get_db

router = APIRouter(prefix="/users",tags=["Users"])

@router.post("/create")
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
	print(user)
	return await CreateUser(user, db)
