__author__ = 'Richard McAllister'


def get_from_dict(data_dict, map_list):
    """
    Gets a value in a nested dictionary using a list of keys.

    :param data_dict: Dictionary to get a value from.
    :type data_dict: dict
    :param map_list: List of nested keys.
    :type map_list: list
    :return: A value from the nested dictionary.
    :rtype: *
    """
    for k in map_list: data_dict = data_dict[k]
    return data_dict


def set_in_dict(dic, keys, value):
    """
    Sets a value in a nested dictionary using a list of keys.

    :param dic: A dictionary...perhaps nested.
    :type dic: dict
    :param keys: A list of keys.
    :type keys: list
    :param value: The value corresponding to the nested keys.
    :type value: *
    """
    for key in keys[:-1]:
        dic = dic.setdefault(key, {})
    dic[keys[-1]] = value


def nested_dict_iter(d, keys=()):
    """
    Traverses a nested dictionary returning the keys and values.
    
    :param d: The dictionary to traverse.
    :param keys: The keys to traverse (blank for iteration).
    :return: Yields the key path and the associated value.
    """
    if type(d) == dict:
        for k in d:
            for rv in nested_dict_iter(d[k], keys + (k,)):
                yield rv
    else:
        yield (keys, d)


def interleave_string(a_list, a_str):
    """
    Produces a list with the string interleaved ... plus one instance of the string at the beginning.
    
    For example: 
        the_list = ['the', 'quick', 'brown', 'fox']
        the_string = 'properties'
        test_result = ['properties', 'the', 'properties', 'quick', 'properties', 'brown', 'properties', 'fox']
    
    :param a_list: A list of strings.
    :type a_list: list
    :param a_str: A string.
    :type a_str: str
    :return: A list of strings with a_str interleaved as above.
    """
    return [x for y in ([a_str] + [a_list[i]] * (i < len(a_list)) for i in range(0, len(a_list))) for x in y]


def remove_interleaved_string(a_list):
    """
    Removes interleaved string from a list.  String is interleaved like 'properties' in this list:
        test_result = ['properties', 'the', 'properties', 'quick', 'properties', 'brown', 'properties', 'fox']
        
    :param a_list: List of strings.
    :type a_list: list
    :return: 
    :rtype: list
    """
    return a_list[1::2]


def has_interleaved_string(a_list, a_string):
    """
    Tests for the presence of a string interleaved like 'properties' in this list:
        test_result = ['properties', 'the', 'properties', 'quick', 'properties', 'brown', 'properties', 'fox']
    
    :param a_list: List of strings.
    :type a_list: list
    :param a_string: String that may be interleaved.
    :type a_string: str
    :return: 
    :rtype: boolean
    """
    interleavers = set(a_list[::2])
    return len(interleavers) == 1 and interleavers.pop() == a_string
