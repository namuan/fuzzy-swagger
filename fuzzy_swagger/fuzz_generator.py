from random import randint


def rand_int(upper_limit):
    return randint(0, upper_limit)


def fuzz_boolean(boolean_schema):
    return True


def fuzz_date_time():
    return "2000-01-23T04:56:07.000+00:00"


def fuzz_string(string_schema):
    is_enum = string_schema.get('enum')
    string_format = string_schema.get('format')
    if is_enum:
        # get a random item from list
        return is_enum[rand_int(len(is_enum) - 1)]

    if string_format == 'date-time':
        return fuzz_date_time()

    return "something"


def fuzz_int(int_schema):
    return 5


def fuzz_file(file_schema):
    return ''


def fuzz_array_length():
    return 10


def fuzz_array(arr_schema, arr_length=fuzz_array_length()):
    items = arr_schema['items']
    arr_items_type = items['type']
    fuzz_func = type_mapping.get(arr_items_type)
    if arr_items_type == 'object':
        return [fuzz_object(arr_schema['items']['properties']) for o in range(arr_length)]
    else:
        return [fuzz_func(items) for i in range(arr_length)]


def fuzz_object(root_properties):
    obj_root = {}
    for k, v in root_properties.items():
        prop_type = v['type']
        if prop_type != 'object':
            fuzz_func = type_mapping.get(prop_type)
            obj_root[k] = fuzz_func(v)
        else:
            obj_root[k] = fuzz_object(v['properties'])

    return obj_root


type_mapping = {
    'integer': fuzz_int,
    'boolean': fuzz_boolean,
    'string': fuzz_string,
    'array': fuzz_array,
    'file': fuzz_file,
}
