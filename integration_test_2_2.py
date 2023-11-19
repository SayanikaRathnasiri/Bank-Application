import bank

#Cash Withdrawal
def test_cash_withdrawal():
    assert bank.cash_withdrawal(400000)== '*** Withdrawal Successful ! ***'

#Get a loan
def test_get_loan():
    assert bank.get_loan(4,1000)== '*** The Monthly Payment Was Processed ***'

#Testing Fail