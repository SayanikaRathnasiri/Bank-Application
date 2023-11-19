import bank
import pytest

#Loan Getting Unit Testing
@pytest.mark.parametrize('year,loan_amount,output',[
    #whether if is pass
    (3,20000,'*** The Monthly Payment Was Processed ***'),
    #whether else is pass
    (4,20000,'*** Sorry! Enter Currect Details ***')   ])

def test_get_loan(year,loan_amount,output):
    assert bank.get_loan(year,loan_amount)==output

#Testing Pass