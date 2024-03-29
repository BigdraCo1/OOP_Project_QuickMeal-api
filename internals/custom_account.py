from internals.account import Account, Profile
from internals.food import Food
from internals.order import Order
from internals.pocket import Pocket


class CustomerAccount(Account):
    ID = 1

    def __init__(self, password: str, profile: Profile, pocket: Pocket):
        if not isinstance(profile, Profile):
            ValueError("Error")
        if not isinstance(pocket, Pocket):
            ValueError("Error")
        super().__init__(f"C{CustomerAccount.ID}", password, profile, pocket)
        CustomerAccount.ID += 1
        self.__address_list = []
        self.__reviewed_list = []
        self.__current_order = []
        self.__order_list = []

    @property
    def current_order(self):
        return self.__current_order

    @property
    def order_list(self):
        return self.__order_list

    @property
    def reviewed_list(self):
        return self.__reviewed_list

    @property
    def address_list(self):
        return self.__address_list

    def add_address(self, address: str):
        self.__address_list.append(address)

    def remove_address(self, address: str):
        self.__address_list.remove(address)

    def is_basket_of_restaurant_there(self, restaurant):
        if self.__current_order == []:
            return False
        for order in self.__current_order:
            if order.restaurant == restaurant:
                return True
        return False

    def add_food(self, food, size, quantity, restaurant):
        customer_food = Food(food.id, food.name, food.type, food.size, food.price, size)
        if self.is_basket_of_restaurant_there(restaurant):
            for order in self.__current_order:
                if order.restaurant == restaurant:
                    for i in range(quantity):
                        order.food_list.append(customer_food)
        else:
            order = Order(self, None, None, restaurant, [], 'Not Comfirm', None)
            for i in range(quantity):
                order.food_list.append(customer_food)
            self.__current_order.append(order)

    def remove_food(self, food_id, size, quantity, restaurant):
        for order in self.__current_order:
            if order.restaurant == restaurant:
                for i in range(quantity):
                    for food in order.food_list:
                        if food.id == food_id and food.current_size == size:
                            order.food_list.remove(food)

    def remove_current_order(self, order):
        self.__current_order.remove(order)

    def add_order_list(self, order):
        self.__order_list.append(order)

    def add_review(self, review):
        self.__reviewed_list.append(review)
