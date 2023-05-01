import pytest
from vending_machine import VendingMachine

def test_add_item():
    vm = VendingMachine()
    num_items = len(vm.items["snacks"])
    vm.add_item("snacks", "cookie", 1.50, "weight", 30)
    assert {"name": "cookie", "price": 1.50, "weight": 30, "quantity": 10} in vm.items["snacks"]
    assert len(vm.items["snacks"]) == num_items + 1

def test_remove_item():
    vm = VendingMachine()
    num_items = len(vm.items["snacks"])
    vm.remove_item("snacks", "chips")
    assert {"name": "chips", "price": 1.50, "weight": 50, "quantity": 10} not in vm.items["snacks"]
    assert len(vm.items["snacks"]) == num_items - 1

def test_restock_item():
    vm = VendingMachine()
    vm.items["beverages"][0]["quantity"] = 0
    vm.restock_item("beverages", "soda")
    assert vm.items["beverages"][0]["quantity"] == 10

def test_purchase_item():
    vm = VendingMachine()
    vm.items["snacks"][0]["quantity"] = 10
    vm.purchase_item("snacks", "chips")
    assert vm.items["snacks"][0]["quantity"] == 9

def test_is_full():
    vm = VendingMachine()
    assert vm.is_full() == False
    vm.items["snacks"] = []
    vm.items["beverages"] = []
    for i in range(10):
        vm.add_item("snacks", f"item{i}", 1.0, "weight", 10)
    assert vm.is_full() == True

def test_is_empty():
    vm = VendingMachine()
    assert vm.is_empty() == False
    vm.items["snacks"] = []
    vm.items["beverages"] = []
    assert vm.is_empty() == True
