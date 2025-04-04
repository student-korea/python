a_list = ['Eric','Hina','Nicky','Sophia','Debi','Alice','Rei']
while True:
    name = input("찾고자 하는 이름을 기억하세요>> ")
    temp = 0
    a_list.str.contains(name)
    for a in a_list:
        # if name==a:
        if name in a:
            print(f"{name}으로 검색된 {a}을 찾았습니다.")
            temp = 1
    if temp==0:
        print(f"{name}을 찾지 못했습니다. 다시 입력하세요.")
            