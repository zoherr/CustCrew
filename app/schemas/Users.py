from pydantic import BaseModel,EmailStr,Field,field_validator

class UserCreate(BaseModel):
    name:str = Field(..., min_length=5,max_length=15)
    email:str = EmailStr
    password:str

    @field_validator("name")
    @classmethod
    def name_must_not_be_blank(cls, value):
        if value.strip() == "":
            raise ValueError("Name cannot be blank")
        return value
