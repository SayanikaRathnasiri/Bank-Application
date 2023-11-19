import bank

#Cash Deposite
def test_cash_deposit():
    assert bank.cash_deposit(0)== '*** Deposit Successful ! ***'

#Cash Withdrawal
def test_cash_withdrawal():
    assert bank.cash_withdrawal(50000)== '*** Withdrawal Successful ! ***'

#Testing Fail