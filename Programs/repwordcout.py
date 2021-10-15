# Check the repeated word in string & count them

import collections

input_string = input(str())
output = collections.Counter(input_string)

values = output.values()
values_list = list(values)
ans = values_list.count(1)
print(ans)
