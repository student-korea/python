#구구단

for i in range(1,10):
    for j in range(2,10):
        print(f"{j} X {i} = {i*j:2d}",end="  ")
    print()
    

# 은행가면 번호표 
# for i in range(1,1000):
#     print(f"{i:03d}")