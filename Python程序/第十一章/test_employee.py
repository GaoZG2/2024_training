import pytest

from employee import Employee

@pytest.fixture
def employee_info():
    employee = Employee('Zg', 'G', 60000)
    return employee

def test_give_default_raise(employee_info):
    employee_info.give_raise()
    assert employee_info.annual_salary == 65000

def test_give_custom_raise(employee_info):
    employee_info.give_raise(12000)
    assert employee_info.annual_salary == 72000
