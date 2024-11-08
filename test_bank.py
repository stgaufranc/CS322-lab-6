"""Basic tests for bank.py."""

import pytest
from bank import Account

"""Exercise 1 - Write Unit Tests for Account"""

def test_initial_balance():
    """Test the initial balance.
    If a user begins with $20, they should have a balance of $20."""
    initial_user = Account('user', 20)
    assert initial_user.get_balance() == 20
    print(f"Passed initial")

def test_deposit():
    """Test a deposit.
    If we initialize a user with no money, then deposit $10, the user should have $10."""
    initial_user = Account('user', 0)
    initial_user.deposit(10)
    assert initial_user.get_balance() == 10
    print(f"Passed deposit")


def test_withdraw():
    """Test a withdrawal.
    If we initialize a user with $20, then withdraw $15, the user should have $5."""
    initial_user = Account('user', 20)
    initial_user.withdraw(15)
    assert initial_user.get_balance() == 5
    print("Passed withdraw")

test_initial_balance()
test_deposit()
test_withdraw()

print(f"Unit tests for account passed!")

"""Exercise 2 - Add Tests for Error Handling"""

def test_deposit_negative_amount():
    """Test a deposit with a negative amount.
    If we initialize a user and add a negative amount, we should get an error."""
    user = Account('user', 20)
    user.deposit(-20)
    pass

def test_withdraw_more_than_balance():
    pass

def test_withdraw_negative_amount():
    pass
