from typing import Dict, List
from pytest import raises
from .calculator_4 import Calculator4
from src.drivers.numpy_handler import NumpyHandler

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

class MockDriverHandler():
    def mean(self, numbers: List[float]) -> float:
        return 3
    
# Test integration
def test_calculate_integration():
    mock_request = MockRequest(body={ "numbers": [1, 2, 3, 4] })

    calculator_4 = Calculator4(NumpyHandler())
    response = calculator_4.calculate(mock_request)

    assert  isinstance(response, dict)
    assert response == {"data": {"Calculator": 4, "mean": 2.5}}

# Calculator unit test
def test_calculate():
    mock_request = MockRequest(body={ "numbers": [1, 2, 3, 4] })

    driver = MockDriverHandler()
    calculator_4 = Calculator4(driver)
    response = calculator_4.calculate(mock_request)

    assert  isinstance(response, dict)
    assert response == {"data": {"Calculator": 4, "mean": 3}}

def test_calculate_with_body_error():
    mock_request = MockRequest(body={"something": []})
    calculator_4 = Calculator4(NumpyHandler())

    with raises(Exception) as excinfo:
        calculator_4.calculate(mock_request)

    assert str(excinfo.value) == "Request body is malformed!"