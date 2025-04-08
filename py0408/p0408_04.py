def flat(data):
    output = []
    for i in data:
        if type(i) == list:
            output += flat(i)
        else:
            output.append(i)
    return output

a = [[1,2,3],4,[5,6],7,[8,[9]]]
print(a)
print(flat(a))