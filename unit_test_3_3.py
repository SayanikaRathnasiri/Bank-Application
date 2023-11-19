import bank
import pytest

#Loan Getting Unit Testing
@pytest.mark.parametrize('year,loan_amount,output',[
    #whether if is fail
    (6,20000,'*** The Monthly Payment Was Processed ***'),
    #whether else is fail
    (5,20000,'*** Sorry! Enter Currect Details ***')   ])

def test_get_loan(year,loan_amount,output):
    assert bank.get_loan(year,loan_amount)==output

#Testing Fail