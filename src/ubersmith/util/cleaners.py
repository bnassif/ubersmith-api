def bool_to_int(data: dict):
    """
    Converts boolean values in a dict to integers for parsing by the Ubersmith API

    Args:
        data (dict): The dict you want cleaned
    """
    for k, v in data.items():
        # Handle all sub-items recursively
        if isinstance(v, dict):
            bool_to_int(v)
        # Convert any boolean inputs to integers
        elif isinstance(v, bool):
            data[k] = int(v)

def passwd_to_pass(data: dict):
    """
    Converts the `passwd` keyword argument to `pass` as required by the API
    
    This allows circumventing conflicts with the keyword argument pass and Python's pass directive

    Args:
        data (dict): The dict you want cleaned
    """
    for k in data.keys():
        if k == 'passwd':
            data['pass'] = data.pop(k)

def from_address_to_from(data: dict):
    for k in data.keys():
        if k == 'from_address':
            data['from'] = data.pop(k)


def clean_all(data: dict):
    """
    Runs all cleaners against inputs

    Args:
        data (dict): The dict you want cleaned
    """
    cleaners = [
        bool_to_int,
        passwd_to_pass,
        from_address_to_from,
    ]
    for c in cleaners:
        c(data)