import bank
import pytest

#Cash Withdrawal Unit Testing
@pytest.mark.parametrize('withdrawal_amount,output',[
    #whether if is pass
    (3000,'*** Withdrawal Successful ! ***'),
    #whether else is pass
    (30000,'*** Withdrawal was not Successful ! ***')  ])

def test_cash_withdrawal(withdrawal_amount,output):
    assert bank.cash_withdrawal(withdrawal_amount)==output

#Testing Pass