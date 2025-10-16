file_name = input("Nhập tên file bạn muốn đọc: ")

try:
    with open(file_name, 'r', encoding='utf-8') as f:
        content = f.read()
        print("\n--- Nội dung của file ---")
        print(content)
        print("------------------------")

except FileNotFoundError:
    print(f"\nLỗi: Không tìm thấy file có tên '{file_name}'. Vui lòng kiểm tra lại.")

except Exception as e:
    print(f"\nĐã xảy ra lỗi: {e}")