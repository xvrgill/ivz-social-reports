import unittest
from modules.reformat_feature_name import reformat_feature_name as rfn

test_string = 'This 392_ 4 is A dao(sSample!'


class TestReformatFeatureName(unittest.TestCase):

    def test_white_space(self):
        self.assertNotIn(' ', rfn(test_string))

    def test_lower_case(self):
        reformatted_str = rfn(test_string)
        self.assertTrue(reformatted_str)


if __name__ == '__main__':
    unittest.main()
