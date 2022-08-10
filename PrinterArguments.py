# manual_letters = \
""".
.......
.......
.......
.......
.......
.......
.......

XXXXXXX
...X...
...X...
...X...
...X...
...X...
XXXXXXX

.XX.XX.
X..X..X
X.....X
X.....X
.X...X.
..X.X..
...X...

XXXXXX.
X.....X
X.....X
XXXXXX.
X......
X......
X......

X.....X
X.....X
X.....X
..XXX..
...X...
...X...
...X...

XXXXXXX
...X...
...X...
...X...
...X...
...X...
...X...

X.....X
X.....X
X.....X
XXXXXXX
X.....X
X.....X
X.....X

XXXXXXX
X.....X
X.....X
X.....X
X.....X
X.....X
XXXXXXX

XX....X
X.X...X
X..X..X
X..X..X
X...X.X
X...X.X
X....XX
"""

### START ###

manual_letters = '.\n.......\n.......\n.......\n.......\n.......\n.......\n.......\n\nXXXXXXX\n...X...\n...X...\n...X...\n...X...\n...X...\nXXXXXXX\n\n.XX.XX.\nX..X..X\nX.....X\nX.....X\n.X...X.\n..X.X..\n...X...\n\nXXXXXX.\nX.....X\nX.....X\nXXXXXX.\nX......\nX......\nX......\n\nX.....X\nX.....X\nX.....X\n..XXX..\n...X...\n...X...\n...X...\n\nXXXXXXX\n...X...\n...X...\n...X...\n...X...\n...X...\n...X...\n\nX.....X\nX.....X\nX.....X\nXXXXXXX\nX.....X\nX.....X\nX.....X\n\nXXXXXXX\nX.....X\nX.....X\nX.....X\nX.....X\nX.....X\nXXXXXXX\n\nXX....X\nX.X...X\nX..X..X\nX..X..X\nX...X.X\nX...X.X\nX....XX\n'
default_fill_space = '.'  # references above
keys = '_i?python'

letter_split = [i.lstrip('\n').rstrip('\n') for i in manual_letters[1:].split('\n\n')]

# matrices = []
# letter = []
# for each_letter in letter_split:
#     line = []
#     for each_char in each_letter:
#         if each_char == '\n':
#             letter.append(line)
#             line = []
#         else:
#             line.append(each_char)
#     else:
#         letter.append(line)
#
#     matrices.append(letter)
#     letter = []

matrices = [[list(each_char) for each_char in each_line.split('\n')] for each_line in letter_split]
# print(matrices)
# print(matrices_2)
# print(matrices == matrices_2)

matrix_char_dict = {list(keys)[i]: v for i, v in enumerate(matrices)}

# Configuration
spell_me = 'i_?_python'
char_list = matrix_char_dict.keys()
line_to_print = ''
number_of_spaces = 3
match_fill_char = manual_letters[0]
new_fill_char = ' '

for i in range(len(list(matrix_char_dict.values())[0])):
    for each_letter in list(spell_me):
        line_to_print += match_fill_char * number_of_spaces
        line_to_print += ''.join(matrix_char_dict[each_letter][i])
    line_to_print += match_fill_char * number_of_spaces
    line_to_print = line_to_print.replace(match_fill_char, new_fill_char)
    ############  IGNORE ABOVE  ############

    ########################################
    ###        FIX THE LINE BELOW        ###
    ########################################
    print(line_to_print, end='X')

    ############  IGNORE BELOW  ############
    line_to_print = ''



print()

#################################################################
###    TO DECRYPT THE DATE OF THE SECRETE GCTA PIZZA PARTY    ###
###               CHANGE THE SEPERATOR ARGUMENT               ###
###                   date Format: mm/dd/yy                   ###
#################################################################

print('9\b', '\r\b\b20\b\b1\t\b0', '\061\x35', '22', sep='16 8 526 48 120 22', end='33')








# print('\n9\b', '\r\b\b20\b\b1\t\b0', '\061\x35', '22', sep='16 8 526 48 120 22 ', end=' ')  # 16 8 526 48 120 22

### END ###

# foo = 'sp zta hpo'
### HELP DECODE THE MESSAGE BY CHANGING THE SEPERATOR ARGUMENT ###
# print('\nth\t\be', 'sek\bcry\be\t\bt', 'k\bping\b\b\x7A\x7Aa', 'f\bpa\x72\x74y:', 'is', '\157c\t\bt', 'fo\big\t\b\bft\t\bee\x6Eth\bh', sep='sp zta hpo')
