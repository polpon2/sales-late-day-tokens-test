from app import send_get, send_post, WAIT_NORMAL
import time

class TestNormal:
    def test_create_success(self):
        create_data: dict = {
                            "username": "TestUser#1",
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
        send_post("purchase", json=create_data)
        time.sleep(WAIT_NORMAL)
        response = send_get("all-transaction")
        assert response['username'] == "TestUser#1"
        assert response['status'] == "SUCCESS"

    def test_insufficient_fund(self):
        create_data = {
                            "username": "TestUser#6",
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
        send_post("purchase", json=create_data)
        time.sleep(WAIT_NORMAL)
        response = send_get("all-transaction")
        assert response['username'] == "TestUser#6"
        assert response['status'] == "INSUFFICIENT_FUND"

    def test_out_of_stock(self):
        create_another_data = {
                            "username": "TestUser#7",
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
        send_post("purchase", json=create_another_data)
        time.sleep(WAIT_NORMAL)
        response = send_get("all-transaction")
        assert response['username'] == "TestUser#7"
        assert response['status'] == "INSUFFICIENT_INVENTORY"