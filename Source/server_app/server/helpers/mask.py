def mask_half_field(string):
    """
    Mask Half String Field
    :param string: string
    :return: string: masked
    """
    if string is None:
        return ''

    half_len = len(string) >> 1
    return '%s%s%s' % (string[:half_len], '*' * half_len, string[half_len * 2:])


def mask_full_field(string):
    """
    Mask Full String Field
    :param string: string
    :return: string: masked
    """
    if string is None:
        return ''

    return '*' * len(string)