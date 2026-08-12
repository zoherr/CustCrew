from fastapi import APIRouter,Depends,Response
from sqlalchemy.ext.asyncio import  AsyncSession
from app.schemas.Users import UserCreate,UserLogin,User
from app.controllers.UsersController import CreateUser,LoginUser
from app.core.database import get_db
from app.middleware.authentication import get_current_user

router = APIRouter(prefix="/users",tags=["Users"])

@router.post("/create",response_model=User)
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
	return await CreateUser(user, db)


@router.post("/login",response_model=User)
async def login_user(response: Response,user: UserLogin, db: AsyncSession = Depends(get_db)):
	return await LoginUser(response, user, db)

@router.get("/me")
async def get_me(user_id: int = Depends(get_current_user)):
    return {
        "user_id": user_id
    }