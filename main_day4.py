from datetime import date
from itertools import product

from fastapi import FastAPI, Query
from fastapi.exceptions import EndpointContext
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Ai world is too amazing place"}

#Question 1: 
from fastapi import FastAPI

app = FastAPI()

products = [
    {"id": 1, "name": "Wireless Mouse", "price": 999, "category": "Electronics", "in_stock": True},
    {"id": 2, "name": "USB Hub", "price": 1499, "category": "Electronics", "in_stock": True},
    {"id": 3, "name": "Monitor Stand", "price": 1999, "category": "Accessories", "in_stock": False},
    {"id": 4, "name": "Desk Lamp", "price": 799, "category": "Accessories", "in_stock": True},
    {"id": 5, "name": "Laptop Stand", "price": 1299, "category": "Electronics", "in_stock": True},
    {"id": 6, "name": "Mechanical Keyboard", "price": 2499, "category": "Electronics", "in_stock": True},
    {"id": 7, "name": "Webcam", "price": 1899, "category": "Electronics", "in_stock": False},
]

@app.get("/products")
def get_products():
    return {"products": products, "total": len(products)}

# Question 2: Filter products by category
from fastapi import FastAPI
app = FastAPI()
products = [
    {"id": 1, "name": "Wireless Mouse", "price": 999, "category": "Electronics", "in_stock": True},
    {"id": 2, "name": "USB Hub", "price": 1499, "category": "Electronics", "in_stock": True},
    {"id": 3, "name": "Monitor Stand", "price": 1999, "category": "Accessories", "in_stock": False},
    {"id": 4, "name": "Desk Lamp", "price": 799, "category": "Accessories", "in_stock": True},
    {"id": 5, "name": "Laptop Stand", "price": 1299, "category": "Electronics", "in_stock": True},
    {"id": 6, "name": "Mechanical Keyboard", "price": 2499, "category": "Electronics", "in_stock": True},
    {"id": 7, "name": "Webcam", "price": 1899, "category": "Electronics", "in_stock": False},
]

@app.get("/products")
def get_products():
    return {"products": products, "total": len(products)}

@app.get("/products/category/{category_name}")
def get_by_category(category_name: str):
    result = [p for p in products if p["category"] == category_name]
    if not result:
        return {"error": "No products found in this category"}
    return {"category": category_name, "products": result, "total": len(result)}
@app.get("/products/{category}")
def get_products_by_category(category: str):
    filtered = [p for p in products if p["category"].lower() == category.lower()]
    return {"category": category, "products": filtered, "total": len(filtered)}


#Question 3:Show Only In-Stock Products
from fastapi import FastAPI

app = FastAPI()

products = [
    {"id": 1, "name": "Wireless Mouse", "price": 999, "category": "Electronics", "in_stock": True},
    {"id": 2, "name": "USB Hub", "price": 1499, "category": "Electronics", "in_stock": True},
    {"id": 3, "name": "Monitor Stand", "price": 1999, "category": "Accessories", "in_stock": False},
    {"id": 4, "name": "Desk Lamp", "price": 799, "category": "Accessories", "in_stock": True},
    {"id": 5, "name": "Laptop Stand", "price": 1299, "category": "Electronics", "in_stock": True},
    {"id": 6, "name": "Mechanical Keyboard", "price": 2499, "category": "Electronics", "in_stock": True},
    {"id": 7, "name": "Webcam", "price": 1899, "category": "Electronics", "in_stock": False},
]
@app.get("/products")
def get_products():
    return {"products": products, "total": len(products)}

@app.get("/products/category/{category_name}")
def get_by_category(category_name: str):
    result = [p for p in products if p["category"] == category_name]
    if not result:
        return {"error": "No products found in this category"}
    return {"category": category_name, "products": result, "total": len(result)}

@app.get("/products/instock")
def get_instock():
    result = [p for p in products if p["in_stock"] == True]
    return {"in_stock_products": result, "count": len(result)}


#Question 4: Build a Store Info Endpoint
from fastapi import FastAPI
app = FastAPI()
products = [
    {"id": 1, "name": "Wireless Mouse", "price": 999, "category": "Electronics", "in_stock": True},
    {"id": 2, "name": "USB Hub", "price": 1499, "category": "Electronics", "in_stock": True},
    {"id": 3, "name": "Monitor Stand", "price": 1999, "category": "Accessories", "in_stock": False},
    {"id": 4, "name": "Desk Lamp", "price": 799, "category": "Accessories", "in_stock": True},
    {"id": 5, "name": "Laptop Stand", "price": 1299, "category": "Electronics", "in_stock": True},
    {"id": 6, "name": "Mechanical Keyboard", "price": 2499, "category": "Electronics", "in_stock": True},
    {"id": 7, "name": "Webcam", "price": 1899, "category": "Electronics", "in_stock": False},
]

@app.get("/products")
def get_products():
    return {"products": products, "total": len(products)}

@app.get("/products/category/{category_name}")
def get_by_category(category_name: str):
    result = [p for p in products if p["category"] == category_name]
    if not result:
        return {"error": "No products found in this category"}
    return {"category": category_name, "products": result, "total": len(result)}

@app.get("/products/instock")
def get_instock():
    result = [p for p in products if p["in_stock"] == True]
    return {"in_stock_products": result, "count": len(result)}

@app.get("/store/summary")
def store_summary():
    total = len(products)
    in_stock = len([p for p in products if p["in_stock"] == True])
    out_of_stock = len([p for p in products if p["in_stock"] == False])
    categories = list(set([p["category"] for p in products]))
    return {
        "store_name": "My E-commerce Store",
        "total_products": total,
        "in_stock": in_stock,
        "out_of_stock": out_of_stock,
        "categories": categories
    }
    
    
    
    #Question 5: Search Products by Name

from fastapi import FastAPI
app = FastAPI()
products = [
    {"id": 1, "name": "Wireless Mouse", "price": 999, "category": "Electronics", "in_stock": True},
    {"id": 2, "name": "USB Hub", "price": 1499, "category": "Electronics", "in_stock": True},
    {"id": 3, "name": "Monitor Stand", "price": 1999, "category": "Accessories", "in_stock": False},
    {"id": 4, "name": "Desk Lamp", "price": 799, "category": "Accessories", "in_stock": True},
    {"id": 5, "name": "Laptop Stand", "price": 1299, "category": "Electronics", "in_stock": True},
    {"id": 6, "name": "Mechanical Keyboard", "price": 2499, "category": "Electronics", "in_stock": True},
    {"id": 7, "name": "Webcam", "price": 1899, "category": "Electronics", "in_stock": False},
]

@app.get("/products")
def get_products():
    return {"products": products, "total": len(products)}

@app.get("/products/category/{category_name}")
def get_by_category(category_name: str):
    result = [p for p in products if p["category"] == category_name]
    if not result:
        return {"error": "No products found in this category"}
    return {"category": category_name, "products": result, "total": len(result)}

@app.get("/products/instock")
def get_instock():
    result = [p for p in products if p["in_stock"] == True]
    return {"in_stock_products": result, "count": len(result)}

@app.get("/store/summary")
def store_summary():
    total = len(products)
    in_stock = len([p for p in products if p["in_stock"] == True])
    out_of_stock = len([p for p in products if p["in_stock"] == False])
    categories = list(set([p["category"] for p in products]))
    return {
        "store_name": "My E-commerce Store",
        "total_products": total,
        "in_stock": in_stock,
        "out_of_stock": out_of_stock,
        "categories": categories
    }

@app.get("/products/search/{keyword}")
def search_products(keyword: str):
    results = [p for p in products if keyword.lower() in p["name"].lower()]
    if not results:
        return {"message": "No products matched your search"}
    return {"keyword": keyword, "results": results, "total_matches": len(results)}


#Question Bonus : Cheapest & Most Expensive Product

from fastapi import FastAPI
app = FastAPI()
products = [
    {"id": 1, "name": "Wireless Mouse", "price": 999, "category": "Electronics", "in_stock": True},
    {"id": 2, "name": "USB Hub", "price": 1499, "category": "Electronics", "in_stock": True},
    {"id": 3, "name": "Monitor Stand", "price": 1999, "category": "Accessories", "in_stock": False},
    {"id": 4, "name": "Desk Lamp", "price": 799, "category": "Accessories", "in_stock": True},
    {"id": 5, "name": "Laptop Stand", "price": 1299, "category": "Electronics", "in_stock": True},
    {"id": 6, "name": "Mechanical Keyboard", "price": 2499, "category": "Electronics", "in_stock": True},
    {"id": 7, "name": "Webcam", "price": 1899, "category": "Electronics", "in_stock": False},
]

@app.get("/products")
def get_products():
    return {"products": products, "total": len(products)}

@app.get("/products/category/{category_name}")
def get_by_category(category_name: str):
    result = [p for p in products if p["category"] == category_name]
    if not result:
        return {"error": "No products found in this category"}
    return {"category": category_name, "products": result, "total": len(result)}

@app.get("/products/instock")
def get_instock():
    result = [p for p in products if p["in_stock"] == True]
    return {"in_stock_products": result, "count": len(result)}

@app.get("/store/summary")
def store_summary():
    total = len(products)
    in_stock = len([p for p in products if p["in_stock"] == True])
    out_of_stock = len([p for p in products if p["in_stock"] == False])
    categories = list(set([p["category"] for p in products]))
    return {
        "store_name": "My E-commerce Store",
        "total_products": total,
        "in_stock": in_stock,
        "out_of_stock": out_of_stock,
        "categories": categories
    }

@app.get("/products/search/{keyword}")
def search_products(keyword: str):
    results = [p for p in products if keyword.lower() in p["name"].lower()]
    if not results:
        return {"message": "No products matched your search"}
    return {"keyword": keyword, "results": results, "total_matches": len(results)}

@app.get("/products/deals")
def get_deals():
    best_deal = min(products, key=lambda p: p["price"])
    premium_pick = max(products, key=lambda p: p["price"])
    return {
        "best_deal": best_deal,
        "premium_pick": premium_pick
    }
    
    
    

     
    # Day 2 : FastApi 
       # Assignment 1 : - 
       
     # Question 1: 
     
from fastapi import FastAPI, Query
app = FastAPI()
products = [
    {"id": 1, "name": "Laptop", "price": 55000, "category": "electronics"},
    {"id": 2, "name": "Wireless Mouse", "price": 499, "category": "electronics"},
    {"id": 3, "name": "USB Hub", "price": 799, "category": "electronics"},
    {"id": 4, "name": "Notebook", "price": 120, "category": "stationery"}
]

@app.get("/products/filter")
def filter_products(
    category: str = Query(None, description="Filter by category"),
    max_price: int = Query(None, description="Maximum price"),
    min_price: int = Query(None, description="Minimum price")
):

    result = products

    
    if category:
        result = [p for p in result if p["category"] == category]

    # Filter by max price
    if max_price:
        result = [p for p in result if p["price"] <= max_price]

    # Filter by min price
    if min_price:
        result = [p for p in result if p["price"] >= min_price]
    return result





    # Question 2 : - 
    
    
from fastapi import FastAPI, Query
app = FastAPI()
products = [
    {"id": 1, "name": "Laptop", "price": 55000, "category": "electronics"},
    {"id": 2, "name": "Wireless Mouse", "price": 499, "category": "electronics"},
    {"id": 3, "name": "USB Hub", "price": 799, "category": "electronics"},
    {"id": 4, "name": "Notebook", "price": 120, "category": "stationery"}
]

@app.get("/products/{product_id}/price")
def get_product_price(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return {"name": product["name"], "price": product["price"]}
    return {"error": "Product not found"}




   #  Question 3 :- 
  
from fastapi import FastAPI, Query
from pydantic import BaseModel, Field
from typing import Optional
app = FastAPI()

# Product Data
products = [
    {"id": 1, "name": "Laptop", "price": 55000, "category": "electronics"},
    {"id": 2, "name": "Wireless Mouse", "price": 499, "category": "electronics"},
    {"id": 3, "name": "USB Hub", "price": 799, "category": "electronics"},
    {"id": 4, "name": "Notebook", "price": 120, "category": "stationery"}
]


feedback = []

#  Pydantic Model
class CustomerFeedback(BaseModel):
    customer_name: str           = Field(..., min_length=2, max_length=100)
    product_id:   int            = Field(..., gt=0)
    rating:       int            = Field(..., ge=1, le=5)
    comment:      Optional[str]  = Field(None, max_length=300)

#  POST EndpointContext
@app.post("/feedback")
def submit_feedback(data: CustomerFeedback):
    feedback.append(data.dict())
    return {
        "message":        "Feedback submitted successfully",
        "feedback":       data.dict(),
        "total_feedback": len(feedback)
    }

   
   # question 4 - 
   
from fastapi import FastAPI

app = FastAPI()

products = [
    {"name": "USB Hub",        "price": 799, "in_stock": True,  "category": "Electronics"},
    {"name": "Wireless Mouse", "price": 499, "in_stock": True,  "category": "Electronics"},
    {"name": "Webcam",         "price": 650, "in_stock": False, "category": "Electronics"},
    {"name": "Pen Set",        "price": 49,  "in_stock": True,  "category": "Stationery"},
]


@app.get("/products/summary")
def product_summary():
    in_stock   = [p for p in products if     p["in_stock"]]
    out_stock  = [p for p in products if not p["in_stock"]]
    expensive  = max(products, key=lambda p: p["price"])
    cheapest   = min(products, key=lambda p: p["price"])
    categories = list(set(p["category"] for p in products))

    return {
        "total_products":     len(products),
        "in_stock_count":     len(in_stock),
        "out_of_stock_count": len(out_stock),
        "most_expensive":     {"name": expensive["name"], "price": expensive["price"]},
        "cheapest":           {"name": cheapest["name"],  "price": cheapest["price"]},
        "categories":         categories,
    }
    
    
     #question 5 : - 
     
from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List

app = FastAPI()


products = [
    {"id": 1, "name": "Wireless Mouse", "price": 499, "category": "Electronics", "in_stock": True},
    {"id": 2, "name": "Keyboard", "price": 799, "category": "Electronics", "in_stock": True},
    {"id": 3, "name": "USB Hub", "price": 599, "category": "Electronics", "in_stock": False},
    {"id": 4, "name": "Pen Set", "price": 49, "category": "Stationery", "in_stock": True}
]


class OrderItem(BaseModel):
    product_id: int = Field(..., gt=0)
    quantity: int = Field(..., gt=0, le=50)


class BulkOrder(BaseModel):
    company_name: str = Field(..., min_length=2)
    contact_email: str = Field(..., min_length=5)
    items: List[OrderItem] = Field(..., min_items=1)

@app.get("/products/summary")
def product_summary():

    in_stock = [p for p in products if p["in_stock"]]
    out_stock = [p for p in products if not p["in_stock"]]

    expensive = max(products, key=lambda p: p["price"])
    cheapest = min(products, key=lambda p: p["price"])

    categories = list(set(p["category"] for p in products))

    return {
        "total_products": len(products),
        "in_stock_count": len(in_stock),
        "out_of_stock_count": len(out_stock),
        "most_expensive": {
            "name": expensive["name"],
            "price": expensive["price"]
        },
        "cheapest": {
            "name": cheapest["name"],
            "price": cheapest["price"]
        },
        "categories": categories
    }

@app.post("/orders/bulk")
def place_bulk_order(order: BulkOrder):

    confirmed = []
    failed = []
    grand_total = 0

    for item in order.items:

        product = next((p for p in products if p["id"] == item.product_id), None)

        if not product:
            failed.append({
                "product_id": item.product_id,
                "reason": "Product not found"
            })

        elif not product["in_stock"]:
            failed.append({
                "product_id": item.product_id,
                "reason": f"{product['name']} is out of stock"
            })

        else:
            subtotal = product["price"] * item.quantity
            grand_total += subtotal

            confirmed.append({
                "product": product["name"],
                "qty": item.quantity,
                "subtotal": subtotal
            })

    return {
        "company": order.company_name,
        "confirmed": confirmed,
        "failed": failed,
        "grand_total": grand_total
    }
    
    
    

    
    # Question Bonus  : -
    
from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List

app = FastAPI()


products = [
    {"id": 1, "name": "Wireless Mouse", "price": 499, "in_stock": True},
    {"id": 2, "name": "Keyboard", "price": 799, "in_stock": True},
    {"id": 3, "name": "USB Hub", "price": 599, "in_stock": False},
    {"id": 4, "name": "Pen Set", "price": 49, "in_stock": True}
]

orders = []
order_counter = 1



class OrderItem(BaseModel):
    product_id: int = Field(..., gt=0)
    quantity: int = Field(..., gt=0, le=50)


class Order(BaseModel):
    customer_name: str = Field(..., min_length=2)
    items: List[OrderItem]




@app.post("/orders")
def place_order(order: Order):

    global order_counter

    confirmed_items = []
    total_price = 0

    for item in order.items:

        product = next((p for p in products if p["id"] == item.product_id), None)

        if product and product["in_stock"]:

            subtotal = product["price"] * item.quantity
            total_price += subtotal

            confirmed_items.append({
                "product": product["name"],
                "qty": item.quantity,
                "subtotal": subtotal
            })

    new_order = {
        "order_id": order_counter,
        "customer": order.customer_name,
        "items": confirmed_items,
        "total": total_price,
        "status": "pending"   
    }

    orders.append(new_order)

    order_counter += 1

    return {
        "message": "Order placed",
        "order": new_order
    }



@app.get("/orders/{order_id}")
def get_order(order_id: int):

    for order in orders:
        if order["order_id"] == order_id:
            return {"order": order}

    return {"error": "Order not found"}


@app.patch("/orders/{order_id}/confirm")
def confirm_order(order_id: int):

    for order in orders:

        if order["order_id"] == order_id:

            if order["status"] == "confirmed":
                return {"message": "Order already confirmed"}

            order["status"] = "confirmed"

            return {
                "message": "Order confirmed",
                "order": order
            }

    return {"error": "Order not found"}
    
    



#Day 4 :- Crud Operation 

from fastapi import FastAPI, Query, Response, status
from typing import Optional

app = FastAPI()


products = [
    {"id": 1, "name": "Wireless Mouse", "price": 499, "category": "Electronics", "in_stock": True},
    {"id": 2, "name": "Notebook", "price": 99, "category": "Stationery", "in_stock": True},
    {"id": 3, "name": "USB Hub", "price": 799, "category": "Electronics", "in_stock": True},
    {"id": 4, "name": "Pen Set", "price": 49, "category": "Stationery", "in_stock": True},
]

# helper function
def find_product(product_id: int):
    for p in products:
        if p["id"] == product_id:
            return p
    return None


@app.get("/products")
def get_products():
    return {"products": products, "total": len(products)}


@app.get("/products/{product_id}")
def get_product(product_id: int, response: Response):
    product = find_product(product_id)

    if not product:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": "Product not found"}

    return product


@app.put("/products/{product_id}")
def update_product(
    product_id: int,
    price: Optional[int] = None,
    in_stock: Optional[bool] = None,
    response: Response = None
):

    product = find_product(product_id)

    if not product:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": "Product not found"}

    if price is not None:
        product["price"] = price

    if in_stock is not None:
        product["in_stock"] = in_stock

    return {
        "message": "Product updated",
        "product": product
    }
    
    
    ## delete Function  created 

    
@app.delete("/products/{product_id}")
def delete_product(product_id: int, response: Response):

    product = find_product(product_id) 

    if not product:                     
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": "Product not found"}

    products.remove(product)           

    return {"message": f"Product '{product['name']}' deleted"}








# Crud OPERation 
from fastapi import FastAPI, Response, status, Query
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


# Pydantic Model

class NewProduct(BaseModel):
    name: str
    price: int
    category: str
    in_stock: bool = True



# Sample Data

products = [
    {"id": 1, "name": "Wireless Mouse", "price": 499, "category": "Electronics", "in_stock": True},
    {"id": 2, "name": "Notebook", "price": 99, "category": "Stationery", "in_stock": True},
    {"id": 3, "name": "USB Hub", "price": 799, "category": "Electronics", "in_stock": False},
    {"id": 4, "name": "Pen Set", "price": 49, "category": "Stationery", "in_stock": True},
]



# Helper Function

def find_product(product_id: int):
    for p in products:
        if p["id"] == product_id:
            return p
    return None



# GET all products

@app.get("/products")
def get_products():
    return {"products": products, "total": len(products)}



# INVENTORY AUDIT

@app.get("/products/audit")
def product_audit():

    in_stock_list = [p for p in products if p["in_stock"]]
    out_stock_list = [p for p in products if not p["in_stock"]]

    stock_value = sum(p["price"] * 10 for p in in_stock_list)
    priciest = max(products, key=lambda p: p["price"])

    return {
        "total_products": len(products),
        "in_stock_count": len(in_stock_list),
        "out_of_stock_names": [p["name"] for p in out_stock_list],
        "total_stock_value": stock_value,
        "most_expensive": {
            "name": priciest["name"],
            "price": priciest["price"]
        }
    }



# CATEGORY DISCOUNT

@app.put("/products/discount")
def bulk_discount(
    category: str = Query(..., description="Category to discount"),
    discount_percent: int = Query(..., ge=1, le=99, description="Discount percentage")
):

    updated = []

    for p in products:
        if p["category"].lower() == category.lower():
            p["price"] = int(p["price"] * (1 - discount_percent / 100))
            updated.append(p)

    if not updated:
        return {"message": f"No products found in category: {category}"}

    return {
        "message": f"{discount_percent}% discount applied to {category}",
        "updated_count": len(updated),
        "updated_products": updated
    }



# GET single product

@app.get("/products/{product_id}")
def get_product(product_id: int, response: Response):

    product = find_product(product_id)

    if not product:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": "Product not found"}

    return product



# POST new product

@app.post("/products", status_code=201)
def add_product(new_product: NewProduct, response: Response):

    for p in products:
        if p["name"].lower() == new_product.name.lower():
            response.status_code = status.HTTP_400_BAD_REQUEST
            return {"error": "Product already exists"}

    next_id = max(p["id"] for p in products) + 1 if products else 1

    product = {
        "id": next_id,
        "name": new_product.name,
        "price": new_product.price,
        "category": new_product.category,
        "in_stock": new_product.in_stock
    }

    products.append(product)

    return {"message": "Product added", "product": product}



# UPDATE product

@app.put("/products/{product_id}")
def update_product(
    product_id: int,
    price: Optional[int] = None,
    in_stock: Optional[bool] = None,
    response: Response = None
):

    product = find_product(product_id)

    if not product:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": "Product not found"}

    if price is not None:
        product["price"] = price

    if in_stock is not None:
        product["in_stock"] = in_stock

    return {"message": "Product updated", "product": product}



# DELETE product

@app.delete("/products/{product_id}")
def delete_product(product_id: int, response: Response):

    product = find_product(product_id)

    if not product:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": "Product not found"}

    products.remove(product)


    return {"message": f"Product '{product['name']}' deleted"}
