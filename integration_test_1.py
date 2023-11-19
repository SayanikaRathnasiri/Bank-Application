import bank

#Cash Deposite
def test_cash_deposit():
    assert bank.cash_deposit(1000)== '*** Deposit Successful ! ***'

#Cash Withdrawal
def test_cash_withdrawal():
    assert bank.cash_withdrawal(500)== '*** Withdrawal Successful ! ***'

#Testing Pass