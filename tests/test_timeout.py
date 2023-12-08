from app import send_get, send_post, WAIT_TIMEOUT
import time

class TestTimeout:
    def test_payment_timeout(self):
        create_data = {
                            "username": "TestUser#3",
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
        send_post("purchase", json=create_data)
        time.sleep(WAIT_TIMEOUT)
        response = send_get("all-transaction")
        assert response['username'] == "TestUser#3"
        assert response['status'] == "TIMEOUT"

    def test_inventory_timeout(self):
        create_data = {
                            "username": "TestUser#4",
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
        send_post("purchase", json=create_data)
        time.sleep(WAIT_TIMEOUT)
        response = send_get("all-transaction")
        assert response['username'] == "TestUser#4"
        assert response['status'] == "TIMEOUT"

    def test_deliver_timeout(self):
        create_data = {
                            "username": "TestUser#5",
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
        send_post("purchase", json=create_data)
        time.sleep(WAIT_TIMEOUT)
        response = send_get("all-transaction")
        assert response['username'] == "TestUser#5"
        assert response['status'] == "TIMEOUT"