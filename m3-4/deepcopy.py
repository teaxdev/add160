# OOP 4.1 Shallow and Deep copy

import copy

nested_list = [[1, 2, 3], [4, 5, 6]]
shallow_nested_list = copy.copy(nested_list)
deep_nested_list = copy.deepcopy(nested_list)

shallow_nested_list[0][2] = 50
deep_nested_list[1][2] = 50

print(nested_list)
print(shallow_nested_list)
print(deep_nested_list)
print("The original list was changed by the shallow copy because the inner lists share the same address in memory. " \
        "\nThe deep copy creates new addresses for the inner lists, so it no longer has any link with the original list")