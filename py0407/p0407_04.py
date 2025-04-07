# # finally 예ㅚ시, 예외가 발생괴지 않았을 때 모두 실행
# try:
#     f = open("ingo.txt",w)
#     raise NotImplemented
# except Exception as e:
#     print(e)
# finally:
#     f.close()

# a_list =[1,2,3,4,5]
# try:
#     print(a_list[5])
# except ValueError: #ValueError만 처리함
#     print("출력되어야 함")
# except IndexError:
#     print("인덱스 에러임")
# except Exception as e:
#     print(e )
#     print("모든 예외처리가 다 가능함.")

# print(7)
# print(8)
print(1)
print(2)
raise NotImplementedError("미구현")
print(3)