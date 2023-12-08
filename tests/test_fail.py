from app import send_get, send_post, WAIT_NORMAL
import time

class TestFail:
    def test_create_fail(self):
        create_data = {
                            "username": "TestUser#2",
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
        send_post("purchase", json=create_data)
        time.sleep(WAIT_NORMAL)
        response = send_get("all-transaction")
        assert response['username'] != "TestUser#2"

    def test_payment_fail(self):
        create_data = {
                            "username": "TestUser#3",
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
        send_post("purchase", json=create_data)
        time.sleep(WAIT_NORMAL)
        response = send_get("all-transaction")
        assert response['username'] == "TestUser#3"
        assert response['status'] == "UNKNOWN"

    def test_inventory_fail(self):
        create_data = {
                            "username": "TestUser#4",
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
        send_post("purchase", json=create_data)
        time.sleep(WAIT_NORMAL)
        response = send_get("all-transaction")
        assert response['username'] == "TestUser#4"
        assert response['status'] == "UNKNOWN"

    def test_deliver_fail(self):
        create_data = {
                            "username": "TestUser#5",
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
        send_post("purchase", json=create_data)
        time.sleep(WAIT_NORMAL)
        response = send_get("all-transaction")
        assert response['username'] == "TestUser#5"
        assert response['status'] == "UNKNOWN"