import math
from NhanVien import NhanVien

class QuanLyNhanVien:
    listNhanVien = []
    def generateID(self):
        maxId = 1
        if (self.soLuongNhanVien() > 0):
            maxId = self.listNhanVien[0]._id
            for nv in self.listNhanVien:
                if (maxId < nv._id):
                    maxId = nv._id
            maxId = maxId + 1
        return maxId

    def soLuongNhanVien(self):
        return self.listNhanVien.__len__()

    def nhapNhanVien(self):
        # Khởi tạo một Nhân viên mới
        nvId = self.generateID()
        name = input("Nhap ten nhan vien: ")
        nv = NhanVien(nvId, name)
        self.listNhanVien.append(nv)
        
    def findByID(self, ID):
        searchResult = None
        if (self.soLuongNhanVien() > 0):
            for nv in self.listNhanVien:
                if (nv._id == ID):
                    searchResult = nv
        return searchResult
 
    def updateNhanVien(self, ID):
        # Tìm kiếm nhân viên trong danh sách listNhanVien
        nv:NhanVien = self.findByID(ID)
        # Nếu sinh viên tồn tại thì cập nhập thông tin nhân viên
        if (nv != None):
            # nhập thông tin nhân viên
            name = input("Nhap ten nhan vien: ")
            # cập nhật thông tin nhân viên
            nv._name = name
        else:
            print("Nhan vien co ID = {} khong ton tai.".format(ID))

    # Hàm xóa nhân viên theo ID
    def deleteById(self, ID):
        isDeleted = False
        # tìm kiếm nhân viên theo ID
        nv = self.findByID(ID)
        if (nv != None):
            self.listNhanVien.remove(nv)
            isDeleted = True
        return isDeleted

    # Hàm hiển thị danh sách nhân viên ra màn hình console
    def showNhanVien(self, listNV):
        # hien thi tieu de cot
        print("{:<8} {:<18}".format("ID", "Name"))
        # hien thi danh sach nhan vien
        if (listNV.__len__() > 0):
            for nv in listNV:
                print("{:<8} {:<18}".format(nv._id, nv._name))
        print("\n")
        
    # Hàm trả về danh sách sinh viên hiện tại
    def getListNhanVien(self):
        return self.listNhanVien
