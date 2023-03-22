# Write a Python function that takes a sequence of numbers and determines whether all the numbers are different from each other.


num_list = [2, 4, 4, 8, 5, 10, 10, 5, 1,]
# n = set(num_list)
# print(n)


def remove_duplicates(duplist):
    noduplist = []
    for i in duplist:
        if i not in noduplist:
            noduplist.append(i)
    return noduplist


def difference(data):
    if len(data) == len(set(data)):
        return True
    else:
        return False


n = difference(num_list)
print(n)

num_list[:] = remove_duplicates(num_list)
