import numpy as np
import unittest
from typing import Type
from numpy import typing as np_types
from modules.scalers import Scaler


class TestMinMaxScaler(unittest.TestCase):

    # TODO: Create tests for custom exceptions thrown

    def setUp(self) -> None:
        # create test cases
        self.case_1 = [48, 319908, 42, 4982, 904]
        self.case_2 = [4309, 390, -30, 93, -134, -59.6, 39]

        self.scaler_1 = Scaler(self.case_1)
        self.scaler_2 = Scaler(np.array(self.case_2))

    def test_list_input(self):
        vals_1 = self.scaler_1.values
        self.assertIs(type(vals_1), list)

    def test_ndarray_input(self):
        vals_2 = self.scaler_2.values
        self.assertIsInstance(vals_2, np.ndarray)



if __name__ == '__main__':
    unittest.main()
