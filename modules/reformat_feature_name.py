import re


def reformat_feature_name(feature):
    """ Transform column into the standardized feature name format.

    Format is lower cased characters, white spaces replaced with underscores, and punctuation removed.

    :param feature: feature name
    :type feature: str
    :return: reformatted feature name as a string
    """

    # defining regex patters
    white_space_pattern = re.compile(r'\s+')
    punctuation_pattern = re.compile(r'\W+')

    # replacing white space with underscore
    sans_whitespace = re.sub(white_space_pattern, '_', feature.lower())

    # removing punctuation
    sans_punctuation = re.sub(punctuation_pattern, '', sans_whitespace)

    return sans_punctuation


if __name__ == "__main__":
    pass
