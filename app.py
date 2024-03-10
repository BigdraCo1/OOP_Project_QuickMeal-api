from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import menu, search, restaurants, basket, review, general, order_detail,admin_approve, cancel, order, restaurant_decision, rider_decision, customer_show, auth
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["Authorization"]
)

app.include_router(admin_approve.app)
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

if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, log_level="info")