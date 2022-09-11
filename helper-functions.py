# identify data type with its name as a string
# ('BasicDataTypes...')
def id_data_type(id_this: any, data_type: str) -> bool | tuple:
    print("data_type", data_type, str(data_type))

    try:
        type_object = type(id_this)
    except Exception as exc:
        return exc.__class__.__name__, exc

    print("type_object", type_object)

    exclusion_set = (' ', '\'', '\"', '\"\"\"', '<', '>')
    clean_id = ''.join([i for i in list(str(type_object).lstrip('<class ')) if i not in exclusion_set])

    print(clean_id, data_type)

    return clean_id == data_type


# List comparison operators in a string, separated by spaces ('ComparisonOperators...')
def comparison_operator_check(operators: str) -> bool:
    operator_list = "== != > < >= <=".split(' ')
    # remove spaces
    usr_inp_no_spaces = [i for i in operators.split(' ') if i != '']
    # check for uniqueness
    usr_inp_hashed = {}
    for each_operator in usr_inp_no_spaces:
        usr_inp_hashed[each_operator] = ''

    if len(usr_inp_no_spaces) != 6:
        return False

    for each_operator in operator_list:
        if each_operator not in usr_inp_no_spaces:
            return False

    return True


print("Helper functions successfully loaded!")





# comparison_operators = " == != > < >= <= "
# comparison_operators = " !=  ==  >  <  >=  <=  "
# comparison_operators = " !=  ==     >  <  >=  < =  "
# comparison_operators = "  >   <  !=  ==    >=  < =  "
# comparison_operators = "  >   <  !=  ==    >=  <=  "
#
#
# # run the cell to check your answer
# x = comparison_operator_check(comparison_operators)
# print(x)
#
#
# # example problem
#
# # identify the data type of id_this
# id_this = 1
#
# # assign your answer to data_type
# # your answer will be in the form of a string
# data_type = str
#
# print(data_type)
# print(isinstance(data_type, str))
#
# # run the cell to check your answer
# # print(id_data_type(id_this, data_type))



















