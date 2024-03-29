from constants.controller import system
from fastapi import APIRouter, HTTPException, status, Depends
from typing import Annotated

app = APIRouter()


@app.put("/restaurant/{restaurant_id}/accept/{order_id}", tags = ["Restaurant"])
async def accept_restaurant_order(restaurant_id: str, order_id: str, restaurant : Annotated[dict, Depends(system.get_current_restaurant)]) -> dict:
    if restaurant is None or not system.check_access_restaurant_by_restaurant_id(restaurant["username"], restaurant_id):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return {
        "data": system.accept_order_by_restaurant(restaurant_id, order_id)
    }


@app.put("/restaurant/{restaurant_id}/deny/{order_id}", tags = ["Restaurant"])
async def deny_restaurant_order(restaurant_id: str, order_id: str, restaurant : Annotated[dict, Depends(system.get_current_restaurant)]) -> dict:
    if restaurant is None or not system.check_access_restaurant_by_restaurant_id(restaurant["username"], restaurant_id):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return {
        "data": system.deny_order_by_restaurant(restaurant_id, order_id)
    }