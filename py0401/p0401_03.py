a_list = [[1,2,3,4,5],[6,7,8,9,10]]

no = 0
for i in range(5):
    if a_list[0][1] == "X":
        no+=1
print(f"현재 [0]방의 X개수 : {no}")