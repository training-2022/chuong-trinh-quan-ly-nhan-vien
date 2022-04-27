from QuanLyNhanVien import QuanLyNhanVien
# khởi tạo một đối tượng QuanLyNhanVien để quản lý Nhân viên
qlnv = QuanLyNhanVien()
while (1==1):
    print("\nCHUONG TRINH QUAN LY Nhan VIEN")
    print("*************************MENU**************************")
    print("**  1. Them Nhan vien.                               **")
    print("**  2. Cap nhat thong tin Nhan vien bang ID.         **")
    print("**  3. Xoa nhan vien boi ID.                         **")
    print("**  4. Hien thi danh sach nhan vien.                 **")
    print("**  5. Thoat                                         **")
    print("*******************************************************")
    
    key = int(input("Nhap tuy chon: "))
    match key:
        case 1:
            print("\n1. Them nhan vien.")
            qlnv.nhapNhanVien()
            print("\nThem nhan vien thanh cong!")
        case 2:
            if (qlnv.soLuongNhanVien() > 0):
                print("\n2. Cap nhat thong tin nhan vien. ")
                print("\nNhap ID: ")
                ID = int(input())
                qlnv.updateNhanVien(ID)
            else:
                print("\nDanh sach nhan vien trong!")
        case 3:
            if (qlnv.soLuongNhanVien() > 0):
                print("\n3. Xoa nhan vien.")
                print("\nNhap ID: ")
                ID = int(input())
                if (qlnv.deleteById(ID)):
                    print("\nNhan vien co id = ", ID, " da bi xoa.")
                else:
                    print("\nNhan vien co id = ", ID ," khong ton tai.")
            else:
                print("\nDanh sach Nhan vien trong!")
        case 4:
            if (qlnv.soLuongNhanVien() > 0):
                print("\n4. Hien thi danh sach nhan vien.")
                qlnv.showNhanVien(qlnv.getListNhanVien())
            else:
                print("\nSanh sach nhan vien trong!")
        case 5:
            print("\nBan da chon thoat chuong trinh!")
            break
        case _:
            print("\nKhong co chuc nang nay!")
            print("\nHay chon chuc nang trong hop menu.")
