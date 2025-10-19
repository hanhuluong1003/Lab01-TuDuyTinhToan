with open("output.txt", "w", encoding="utf-8") as fout:
    # Bài 1
    fout.write("I'm a student.\n")

    # Bài 2
    fout.write(f"{1/7:.5f}\n")

    # Bài 3
    a = int(input("Nhập số nguyên thứ nhất: "))
    b = int(input("Nhập số nguyên thứ hai: "))
    fout.write(f"Tổng của {a} và {b} là: {a + b}\n")

    # Bài 4
    filename = input("Nhập tên file cần đọc: ")

    try:
        with open(filename, "r", encoding="utf-8") as fin:
            fout.write(f"Nội dung của file {filename}:\n")
            for line in fin:
                fout.write(line)
    except FileNotFoundError:
        fout.write("File không tồn tại.\n")

print("Đã ghi toàn bộ kết quả vào file 'output.txt'")

