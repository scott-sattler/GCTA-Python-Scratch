# identify data type with its name as a string
def id_data_type(id_this: any, data_type: str) -> bool | tuple:
    try:
        type_object = type(id_this)
    except Exception as exc:
        return exc.__class__.__name__, exc

    exclusion_set = (' ', '\'', '\"', '\"\"\"', '<', '>')
    clean_id = ''.join([i for i in list(str(type_object).lstrip('<class ')) if i not in exclusion_set])
    return clean_id == data_type


print("Helper functions successfully loaded!")


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








comparison_operators = " == != > < >= <= "
comparison_operators = " !=  ==  >  <  >=  <=  "
comparison_operators = " !=  ==     >  <  >=  < =  "
comparison_operators = "  >   <  !=  ==    >=  < =  "
comparison_operators = "  >   <  !=  ==    >=  <=  "


# run the cell to check your answer
x = comparison_operator_check(comparison_operators)
print(x)
