from datetime import datetime
from typing import List
from pymongo.collection import Collection
from uuid import uuid4
from fastapi import APIRouter,Depends,HTTPException,status

from app.dependency import get_users_collection
from app.schemas.useer import UserCreate,UserResponse
router=APIRouter(prefix="/users",tags=["users"])
@router.post("",response_model=UserResponse,status_code=status.HTTP_201_CREATED)
def create_user(payload:UserCreate,users_collection:Collection=Depends(get_users_collection)):
    if users_collection.find_one({"email":payload.email}):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="A user with this email already")
    user_doc={"id":str(uuid4()),"name":payload.name,"email":payload.email,"password":payload.password,"role":payload.role,"created_at":datetime.utcnow()}
    users_collection.insert_one(user_doc)
    return user_doc
@router.get("",response_model=List[UserResponse])
def list_users(users_collection: Collection=Depends(get_users_collection)):
    return list(users_collection.find())