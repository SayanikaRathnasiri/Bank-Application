import bank
import pytest

#Cash Deposite Unit Testing
@pytest.mark.parametrize('dep_amount,output',[
    #whether if is pass
    (1000,'*** Deposit Successful ! ***'),
    #whether else is pass
    (0,'*** Deposit was not Successful ! ***')   ])

def test_cash_deposit(dep_amount,output):
    assert bank.cash_deposit(dep_amount)==output

#Testing Pass