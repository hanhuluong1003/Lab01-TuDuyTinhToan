import os
name = input("Nhập tên file: ")

if os.path.isfile(name):
    print("Tồn tại")
else:
    print("Không tồn tại")