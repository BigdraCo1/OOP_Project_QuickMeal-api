from fastapi import Depends, HTTPException, APIRouter
from starlette import status
from schema.auth import *
from constants.controller import system, bcrypt_context
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated
from datetime import timedelta

app = APIRouter(prefix='/auth')


@app.post("/", status_code=status.HTTP_201_CREATED)
async def customer_register(request: CreatUserRequest):
    register = None
    if request.role == 'customer':
        register = system.add_customer_account_by_request(bcrypt_context.hash(request.password), request.username, request.telephone_number, request.email, request.fullname)
    elif request.role == 'restaurant':
        register = system.add_restaurant_account_by_request(bcrypt_context.hash(request.password), request.username,request.telephone_number, request.email, request.fullname)
    elif request.role == 'rider':
        register = system.add_rider_account_by_request(bcrypt_context.hash(request.password), request.username,request.telephone_number, request.email, request.fullname)
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    if isinstance(register, str):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=register)
    return register


@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = system.authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Could not validate')
    token = system.create_access_token(user.get_name(), user.account_id, timedelta(minutes=30))
    return {'access_token': token, 'token_type': 'bearer'}