from typing import Dict, List
from pytest import raises
from .calculator_2 import Calculator2
from src.drivers.numpy_handler import NumpyHandler
from src.drivers.interfaces.driver_handle_interface import DriverHandlerInterface

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

class MockDriverHandler(DriverHandlerInterface):
    def standard_derivation(self, numbers: List[float]) -> float:
        return 3
    
# Test integration
def test_calculate_integration():
    mock_request = MockRequest(body={ "numbers": [1, 2, 3, 4] })

    calculator_2 = Calculator2(NumpyHandler())
    response = calculator_2.calculate(mock_request)

    assert  isinstance(response, dict)
    assert response == {"data": {"Calculator": 2, "result": 0.10}}

# Calculator unit test
def test_calculate():
    mock_request = MockRequest(body={ "numbers": [1, 2, 3, 4] })

    driver = MockDriverHandler()
    calculator_2 = Calculator2(driver)
    response = calculator_2.calculate(mock_request)

    assert  isinstance(response, dict)
    assert response == {"data": {"Calculator": 2, "result": 0.33}}

# def test_calculate_with_body_error():
#     mock_request = MockRequest(body={"something": []})
#     calculator_2 = Calculator2(NumpyHandler())

#     with raises(Exception) as excinfo:
#         calculator_2.calculate(mock_request)

#     assert str(excinfo.value) == "Request body is malformed!"