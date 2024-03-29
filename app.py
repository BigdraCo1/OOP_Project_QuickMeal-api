from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import menu, search, restaurants, admin_approve, basket, review, general, order_detail, cancel, order, restaurant_decision, rider_decision, customer_show, auth, restaurant_account
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["Authorization"]
)


app.include_router(menu.app)
app.include_router(search.app)
app.include_router(restaurants.app)
app.include_router(general.app)
app.include_router(basket.app)
app.include_router(review.app)
app.include_router(order_detail.app)
app.include_router(cancel.app)
app.include_router(order.app)
app.include_router(restaurant_decision.app)
app.include_router(rider_decision.app)
app.include_router(customer_show.app)
app.include_router(auth.app)
app.include_router(restaurant_account.app)
app.include_router(admin_approve.app)

if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, log_level="info")