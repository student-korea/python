# 1. sModule.py - class 2개
# 2. sMain.py
# - sModule.py 
# 3. sFunc.py
from sModule import Student,Students
from sFunc import *

while True:
    choice = main_print()
    if choice == 1:
        stu_input()
    elif choice ==2:
        stu_output()
    elif choice == 0:
        print("프로그램 종료")
        break
        