import pika, json, requests, time
from dotenv import load_dotenv

from typing import Dict

PORT = 8000

def SEND_POST(path: str, json):
    response = requests.post(f"http://localhost:{PORT}/api/{path}/", json=json)
    return response

def SEND_GET(path: str):
    response = requests.get(f"http://localhost:{PORT}/api/{path}")
    return response.json()[-1]


def test_create_success():
    create_data: dict = {
                        "username": "Airbus",
                        "price": 1,
                        "amount": 1,
                        "kill_create": False,
                        "kill_payment": False,
                        "timeout_payment": False,
                        "kill_inventory": False,
                        "timeout_inventory": False,
                        "kill_deliver": False,
                        "timeout_deliver": False
                    }
    SEND_POST("purchase", json=create_data)
    time.sleep(2)
    return SEND_GET("all-transaction")

def test_create_fail():
    create_data = {
                        "username": "Yang",
                        "price": 1,
                        "amount": 1,
                        "kill_create": True,
                        "kill_payment": False,
                        "timeout_payment": False,
                        "kill_inventory": False,
                        "timeout_inventory": False,
                        "kill_deliver": False,
                        "timeout_deliver": False
                    }
    SEND_POST("purchase", json=create_data)
    time.sleep(2)
    return SEND_GET("all-transaction")

def test_payment_success():
    create_data = {
                        "username": "Yang",
                        "price": 1,
                        "amount": 1,
                        "kill_create": False,
                        "kill_payment": False,
                        "timeout_payment": False,
                        "kill_inventory": False,
                        "timeout_inventory": False,
                        "kill_deliver": False,
                        "timeout_deliver": False
                    }
    SEND_POST("purchase", json=create_data)
    time.sleep(2)
    return SEND_GET("all-transaction")

def test_payment_fail():
    create_data = {
                        "username": "Airbus",
                        "price": 1,
                        "amount": 1,
                        "kill_create": False,
                        "kill_payment": True,
                        "timeout_payment": False,
                        "kill_inventory": False,
                        "timeout_inventory": False,
                        "kill_deliver": False,
                        "timeout_deliver": False
                    }
    SEND_POST("purchase", json=create_data)
    time.sleep(2)
    return SEND_GET("all-transaction")

def test_payment_timeout():
    create_data = {
                        "username": "Airbus",
                        "price": 1,
                        "amount": 1,
                        "kill_create": False,
                        "kill_payment": False,
                        "timeout_payment": True,
                        "kill_inventory": False,
                        "timeout_inventory": False,
                        "kill_deliver": False,
                        "timeout_deliver": False
                    }
    SEND_POST("purchase", json=create_data)
    time.sleep(2)
    return SEND_GET("all-transaction")

def test_inventory_success():
    create_data = {
                        "username": "Airbus",
                        "price": 1,
                        "amount": 1,
                        "kill_create": False,
                        "kill_payment": False,
                        "timeout_payment": False,
                        "kill_inventory": False,
                        "timeout_inventory": False,
                        "kill_deliver": False,
                        "timeout_deliver": False
                    }
    SEND_POST("purchase", json=create_data)
    time.sleep(2)
    return SEND_GET("all-transaction")

def test_inventory_fail():
    create_data = {
                        "username": "Airbus",
                        "price": 1,
                        "amount": 1,
                        "kill_create": False,
                        "kill_payment": False,
                        "timeout_payment": False,
                        "kill_inventory": True,
                        "timeout_inventory": False,
                        "kill_deliver": False,
                        "timeout_deliver": False
                    }
    SEND_POST("purchase", json=create_data)
    time.sleep(2)
    return SEND_GET("all-transaction")

def test_inventory_timeout():
    create_data = {
                        "username": "Airbus",
                        "price": 1,
                        "amount": 1,
                        "kill_create": False,
                        "kill_payment": False,
                        "timeout_payment": False,
                        "kill_inventory": False,
                        "timeout_inventory": True,
                        "kill_deliver": False,
                        "timeout_deliver": False
                    }
    SEND_POST("purchase", json=create_data)
    time.sleep(2)
    return SEND_GET("all-transaction")

def test_deliver_success():
    create_data = {
                        "username": "Airbus",
                        "price": 1,
                        "amount": 1,
                        "kill_create": False,
                        "kill_payment": False,
                        "timeout_payment": False,
                        "kill_inventory": False,
                        "timeout_inventory": False,
                        "kill_deliver": False,
                        "timeout_deliver": False
                    }
    SEND_POST("purchase", json=create_data)
    time.sleep(2)
    return SEND_GET("all-transaction")

def test_deliver_fail():
    create_data = {
                        "username": "Airbus",
                        "price": 1,
                        "amount": 1,
                        "kill_create": False,
                        "kill_payment": False,
                        "timeout_payment": False,
                        "kill_inventory": False,
                        "timeout_inventory": False,
                        "kill_deliver": True,
                        "timeout_deliver": False
                    }
    SEND_POST("purchase", json=create_data)
    time.sleep(2)
    return SEND_GET("all-transaction")


def test_deliver_timeout():
    create_data = {
                        "username": "Airbus",
                        "price": 1,
                        "amount": 1,
                        "kill_create": False,
                        "kill_payment": False,
                        "timeout_payment": False,
                        "kill_inventory": False,
                        "timeout_inventory": False,
                        "kill_deliver": False,
                        "timeout_deliver": True
                    }
    SEND_POST("purchase", json=create_data)
    time.sleep(2)
    return SEND_GET("all-transaction")

def test_insufficient_fund():
    create_data = {
                        "username": "NewGuy",
                        "price": 520,
                        "amount": 1,
                        "kill_create": False,
                        "kill_payment": False,
                        "timeout_payment": False,
                        "kill_inventory": False,
                        "timeout_inventory": False,
                        "kill_deliver": False,
                        "timeout_deliver": False
                    }
    SEND_POST("purchase", json=create_data)
    time.sleep(2)
    return SEND_GET("all-transaction")

def test_out_of_stock():
    create_another_data = {
                        "username": "NewGuy",
                        "price": 0,
                        "amount": 1000,
                        "kill_create": False,
                        "kill_payment": False,
                        "timeout_payment": False,
                        "kill_inventory": False,
                        "timeout_inventory": False,
                        "kill_deliver": False,
                        "timeout_deliver": False
                    }
    SEND_POST("purchase", json=create_another_data)
    time.sleep(2)
    return SEND_GET("all-transaction")

if __name__ == '__main__':
    print("Test Create Success: ")
    print(test_create_success())
    print()

    print("Test Create Fail: ")
    print(test_create_fail())
    print()

    print("Test Payment Success: ")
    print(test_payment_success())
    print()

    print("Test Payment Fail: ")
    print(test_payment_fail())
    print()

    print("Test Payment Timeout: ")
    print(test_payment_timeout())
    print()

    print("Test Inventory Success: ")
    print(test_inventory_success())
    print()

    print("Test Inventory Fail: ")
    print(test_inventory_fail())
    print()

    print("Test Inventory Timeout: ")
    print(test_inventory_timeout())
    print()

    print("Test Deliver Success: ")
    print(test_deliver_success())
    print()

    print("Test Deliver Fail: ")
    print(test_deliver_fail())
    print()

    print("Test Deliver Timeout: ")
    print(test_deliver_timeout())
    print()

    print("Test Insufficient Fund: ")
    print(test_insufficient_fund())
    print()

    print("Test Out Of Stock: ")
    print(test_out_of_stock())
    print()