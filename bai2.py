def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Nhập số từ người dùng
n = int(input("Nhập một số nguyên không âm: "))

# Kiểm tra đầu vào hợp lệ
if n < 0:
    print("Vui lòng nhập một số không âm.")
else:
    print(f"Giai thừa của {n} là {factorial(n)}.")