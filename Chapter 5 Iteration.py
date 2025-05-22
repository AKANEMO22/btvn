total = 0  # Tổng các số
count = 0  # Đếm số lượng

while True:
    inp = input("Enter a number: ")
    
    if inp.lower() == "done":
        break
        
    try:
        num = int(inp)
        total += num
        count += 1
    except ValueError:
        print("Invalid input")
        continue

if count > 0:
    print(total, count, total/count)
else:
    print("No numbers were entered")