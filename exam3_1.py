list1 = [1, 4.7, 'hi', False, None]
list2 = [True, 2.3, None, 'brook', 5]

my_list = [True, False, 55, 2.22, 'Aijan', 2.3, None, None, "brook", 25, True, 5]



def get_type_dictionary(list_):

    int_list = []
    float_list = []
    bool_list = []
    str_list = []
    none_type_list = []

    for i in list_:

        if type(i) in [int]:
            int_list.append(i)

        elif type(i) in [float]:
            float_list.append(i)

        elif type(i) in [bool]:
            bool_list.append(i)

        elif type(i) in [str]:
            str_list.append(i)
        elif type(i) is not None:
            none_type_list.append(i)


        type_dict = {
            'int': int_list,
            'float': float_list,
            'str': str_list,
            'bool': bool_list,
            'None': none_type_list
        }
    return type_dict

print(get_type_dictionary(list1))
print(get_type_dictionary(list2))
print(get_type_dictionary(my_list))
