from typing import List
import numpy
from .interfaces.driver_handle_interface import DriverHandlerInterface

class NumpyHandler(DriverHandlerInterface):
    def __init__(self) -> None:
        self.__np = numpy

    def standard_derivation(self, numbers: List[float]) -> float:
        return self.__np.std(numbers)
    
    def variance(self, numbers: List[float]) -> float:
        return self.__np.var(numbers)
    
    def mean(self, numbers: List[float]) -> float:
        return self.__np.mean(numbers)