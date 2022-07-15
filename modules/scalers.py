from typing import Type
import numpy as np


class Scaler:
    def __init__(self, values: Type[np.array] | list) -> None:
        self.values = values

    def min_max(self):
        val_min = np.min(self.values)
        val_max = np.max(self.values)

        normalized_values = []

        # applying formula to each value
        for val in self.values:
            val_minus_min = val - val_min
            val_range = val_max - val_min
            normalized_val = val_minus_min / val_range
            normalized_values.append(normalized_val)

        return np.array(normalized_values)


if __name__ == "__main__":
    s = Scaler(np.array([1,2,3,4,5,6,7,-1000]))
    final = s.min_max()
    print(final)