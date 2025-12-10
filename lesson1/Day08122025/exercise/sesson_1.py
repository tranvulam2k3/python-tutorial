# BÀI 1 – XỬ LÝ NGÀY THÁNG NĂM

def is_leap_year(year):
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

def days_in_month(month, year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    if month in [4, 6, 9, 11]:
        return 30
    if month == 2:
        return 29 if is_leap_year(year) else 28
    return 0

def is_valid_date(day, month, year):
    if year < 1 or month < 1 or month > 12:
        return False
    return 1 <= day <= days_in_month(month, year)

def next_day(day, month, year):
    day += 1
    if day > days_in_month(month, year):
        day = 1
        month += 1
        if month > 12:
            month = 1
            year += 1
    return day, month, year

def previous_day(day, month, year):
    day -= 1
    if day < 1:
        month -= 1
        if month < 1:
            month = 12
            year -= 1
        day = days_in_month(month, year)
    return day, month, year

print("===== BÀI 1: KIỂM TRA NGÀY =====")
d = int(input("Nhập ngày: "))
m = int(input("Nhập tháng: "))
y = int(input("Nhập năm: "))

if not is_valid_date(d, m, y):
    print("Ngày không hợp lệ!")
else:
    nd = next_day(d, m, y)
    pd = previous_day(d, m, y)
    print("Ngày hợp lệ.")
    print("Ngày kế tiếp: ", nd[0], "/", nd[1], "/", nd[2])
    print("Ngày trước đó:", pd[0], "/", pd[1], "/", pd[2])

print("\n===== BÀI 2: TÍNH TỔNG S =====")

# BÀI 2 – TÍNH S = 1 + 1/3! + ...

def factorial(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f

n = int(input("Nhập n: "))
S = 0

for i in range(1, n + 1):
    S += 1 / factorial(2*i - 1)

print("Giá trị S =", S)

print("\n===== BÀI 3: CHUẨN HÓA CHUỖI =====")

# BÀI 3 – CHUẨN HÓA CHUỖI

def chuan_hoa(s):
    s = s.strip().lower()         # bỏ khoảng trắng đầu cuối + chuyển thường
    words = s.split()             # cắt từ (loại khoảng trắng thừa)
    s = " ".join(words)           # ghép bằng 1 dấu cách

    s = s.rstrip('.') + '.'       # bỏ dấu chấm thừa rồi thêm 1 dấu '.'

    s = s[0].upper() + s[1:]      # viết hoa ký tự đầu
    return s

text = input("Nhập câu cần chuẩn hóa: ")
print("Kết quả:", chuan_hoa(text))