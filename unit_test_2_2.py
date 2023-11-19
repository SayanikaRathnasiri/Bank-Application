import bank
import pytest

#Cash Withdrawal Unit Testing
@pytest.mark.parametrize('withdrawal_amount,output',[
    #whether if is fail
    (30000,'*** Withdrawal Successful ! ***'),
    #whether else is fail
    (3000,'*** Withdrawal was not Successful ! ***')   ])

def test_cash_withdrawal(withdrawal_amount,output):
    assert bank.cash_withdrawal(withdrawal_amount)==output

#Testing Fail