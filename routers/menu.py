from constants.controller import system
from schema import food
from fastapi import APIRouter, HTTPException, status, Depends
from typing import Annotated

app = APIRouter(tags=["Editing menu"], responses={404: {"description": "Not found"}})


@app.get("/{restaurant}", status_code=status.HTTP_200_OK)
async def menu_list(restaurant: str, restaurant_dep: Annotated[dict, Depends(system.get_current_restaurant)]):
    if restaurant_dep is None or not system.check_access_restaurant_by_restaurant_name(restaurant_dep["username"],
                                                                                       restaurant):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    if isinstance(system.get_menu_list(restaurant), str):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=system.get_menu_list(restaurant))
    return system.get_menu_list(restaurant)


@app.get("/{restaurant}/{menu}", status_code=status.HTTP_200_OK)
async def menu(restaurant: str, menu: str, restaurant_dep: Annotated[dict, Depends(system.get_current_restaurant)]):
    if restaurant_dep is None or not system.check_access_restaurant_by_restaurant_name(restaurant_dep["username"],
                                                                                       restaurant):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    if isinstance(system.get_menu(restaurant, menu), str):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=system.get_menu_list(restaurant))
    return system.get_menu(restaurant, menu)


@app.put("/{restaurant}/{menu}", status_code=status.HTTP_202_ACCEPTED)
async def edit_menu(restaurant: str, menu: str, request: food.Food,
                    restaurant_dep: Annotated[dict, Depends(system.get_current_restaurant)]):
    if restaurant_dep is None or not system.check_access_restaurant_by_restaurant_name(restaurant_dep["username"],
                                                                                       restaurant):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return system.edit_menu(restaurant, menu, request)


@app.delete("/{restaurant}/{menu}", status_code=status.HTTP_204_NO_CONTENT)
async def remove_menu(restaurant: str, menu: str,
                      restaurant_dep: Annotated[dict, Depends(system.get_current_restaurant)]):
    if restaurant_dep is None or not system.check_access_restaurant_by_restaurant_name(restaurant_dep["username"],
                                                                                       restaurant):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    if system.remove_menu(restaurant, menu) != 'Removed Food from menu':
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Restaurant : {restaurant} or Menu : {menu} is not found")


@app.post("/{restaurant}", status_code=status.HTTP_201_CREATED)
async def new_menu(restaurant: str, request: food.Food,
                   restaurant_dep: Annotated[dict, Depends(system.get_current_restaurant)]):
    if restaurant_dep is None or not system.check_access_restaurant_by_restaurant_name(restaurant_dep["username"],
                                                                                       restaurant):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    menu = system.new_menu(restaurant, request)
    if not menu:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    return menu
