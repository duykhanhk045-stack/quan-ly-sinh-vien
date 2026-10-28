import json

Ten_File = "students.json"

def tai_tai_lieu():
    try:
        with open(Ten_File, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        # Nếu file chưa tồn tại, trả về danh sách rỗng để tránh crash chương trình
        return []
students = tai_tai_lieu()

def luu_file():
    with open(Ten_File, "w", encoding="utf-8") as file:
        return json.dump(students, file, ensure_ascii=False, indent=4)

def them_sinh_vien():
    while True:
        masv = input("Nhập mã sinh viên: ").strip()
        
        # Kiểm tra xem mã sinh viên đã tồn tại chưa
        trung_lap = False
        for i in students:
            if masv == i.get("MaSV"):
                trung_lap = True
                break
                
        if trung_lap:
            print("Mã sinh viên đã tồn tại! Vui lòng nhập mã khác.")
        else:
            break # Thoát vòng lặp khi mã hợp lệ (chưa có)
    
    name = input("Nhập tên sinh viên: ").strip().title()
    name = name.split()
    name = " ".join(name)
    while True:
        try:
            age = int(input("Nhập tuổi của sinh viên: "))
            if age < 0:
                print("Tuổi phải lớn hơn 0")
                continue
            else:
                break
        except ValueError:
            print("Lỗi tuổi phải là một sô nguyên")
    lop = input("Nhập lớp sinh viên: ")
    while True:
        try:
            scores = [int(x) for x in input("Nhập các điểm cho sinh viên: ").strip().split()]
            hop_le = True
            for i in scores:
                if i < 0 or i > 10:
                    print("Điểm chỉ từ 0 đến 10")
                    hop_le = False
                    break

            if hop_le:
                break
        except ValueError:
            print("Điểm phải là số nguyên và các nhau bởi dấu cách")
    
    student = {
        "MaSV": masv,
        "Name": name,
        "Age": age,
        "Class": lop,
        "Scores": scores
    }

    students.append(student)

def xem_sinh_vien():
    if not students:
        print("Không có sinh viên nào")
        return

    print("==== Danh sách sinh viên ====")
    for i in students:
        print("Mã sinh viên:", i.get("MaSV"), "|", "Tên Sinh viên:", i.get("Name"), "|", "Tuổi:", i.get("Age"), "|", "Lớp:", i.get("Class"), "|", "Điểm:", i.get("Scores"))

def xoa_sinh_vien():
    n = input("Nhập mã sinh viên: ").strip()
    Tim_thay = False
    for i in students:
        if n == i.get("MaSV"):
            students.remove(i)
            Tim_thay = True
    if Tim_thay:
        print("Đã xóa sinh viên")
    else:
        print("Không tì thấy sinh viên")

def sua_sinh_vien():
    n = input("Nhập mã sinh viên: ").strip()
    Tim_thay = False
    for index, i in enumerate(students):
        if n == i.get("MaSV"):
            name = input("Nhập tên sinh viên: ").strip().title()
            name = name.split()
            name = " ".join(name)
            while True:
                try:
                    age = int(input("Nhập tuổi của sinh viên: "))
                    if age < 0:
                        print("Tuổi phải lớn hơn 0")
                        continue
                    else:
                        break
                except ValueError:
                    print("Lỗi tuổi phải là một sô nguyên")
            lop = input("Nhập lớp sinh viên: ")
            while True:
                try:
                    scores = [int(x) for x in input("Nhập các điểm cho sinh viên: ").strip().split()]
                    hop_le = True
                    for i in scores:
                        if i < 0 or i > 10:
                            print("Điểm chỉ từ 0 đến 10")
                            hop_le = False
                            break
        
                    if hop_le:
                        break
                except ValueError:
                    print("Điểm phải là số nguyên và các nhau bởi dấu cách")
            
            students[index] = {
                "Name": name,
                "Age": age,
                "Class": lop,
                "Scores": scores
            }
            Tim_thay = True

    if Tim_thay:
        print("Đã sửa thành cônh")
    else:
        print(f"Không có sinh viên nào có mã {n}")

def tim_kiem_sinh_vien():
    n = input("Nhập mã sinh viên: ").strip()
    Tim_thay = False
    for i in students:
        if n == i.get("MaSV"):
            print("Mã sinh viên:", i.get("MaSV"), "|", "Tên Sinh viên:", i.get("Name"), "|", "Tuổi:", i.get("Age"), "|", "Lớp:", i.get("Class"), "|", "Điểm:", i.get("Scores"))
            Tim_thay = True
    if not Tim_thay:
        print(f"Không có sinh viên nào có mã sinh viên là {n}")

def main():
    while True:
        print("==== Quản lý sinh viên ====")
        print("1. Thêm")
        print("2. Xem")
        print("3. Xóa")
        print("4. Sửa")
        print("5. Tìm kiếm")
        print("6. Thoát")

        try:
            choice = int(input("Nhập lựa chọn của bạn: "))
            if choice < 1 or choice > 6:
                print*("Bạn chỉ có thể chọn các chức năng từ 1 đến 6")
                continue
        except ValueError:
            print("Lỗi định dạng")


        if choice == 1:
            them_sinh_vien()
        elif choice == 2:
            xem_sinh_vien()
        elif choice == 3:
            xoa_sinh_vien()
        elif choice == 4:
            sua_sinh_vien()
        elif choice == 5:
            tim_kiem_sinh_vien()
        else:
            luu_file()
            break



if __name__ == "__main__":
    main()