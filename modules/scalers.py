from typing import Type
import numpy as np


# TODO: Create exceptions within the Scaler class
# TODO: Check shape of input array

class Scaler:
    """Scaler class that contains methods for the various implementations."""

    def __init__(self, values: list[int] | np.ndarray) -> None:
        """Define input values that are to be used by scaler methods.

        :param values: input values
        """
        self.values = values

    def min_max(self) -> np.ndarray:
        """Min-max scaler that fits input values between 0 and 1.

        :return: normalized values
        """
        val_min = np.min(self.values)
        val_max = np.max(self.values)

        normalized_values = []

        for val in self.values:
            val_minus_min = val - val_min
            val_range = val_max - val_min

            # handling zero in the divisor
            if val_range == 0:
                normalized_values.append(0)
            else:
                normalized_val = val_minus_min / val_range
                normalized_values.append(normalized_val)

        return np.array(normalized_values)


if __name__ == "__main__":
    s = Scaler(np.array([1,2,3,4,5,6,7,-1000]))
    final = s.min_max()
    print(final)