#Bai1
def func1(*nah):
    for nahs in nah:
        print(nahs) 
func1(20, 40, 60)
func1(80,100)

#Bai2
def calculation(a,b):
    t = a + b
    h = a - b
    return t,h
res = calculation(40,10)
print(res[0], ',', res[1])

#Bai3
def showEmployee ( name, age = 9000):
    return "Name: " + str(name) + ": " + str(age)
print(showEmployee("jessa"))
print(showEmployee("Ben", 12000))

#Bai4
def outer_fun(a,b):
    def tong(a,b):
        return a + b
    return tong(a,b) + 5
result = outer_fun(5,10)
print(result)

#Bai5
def addition(n):
    if n <= 0:
        return 0
    else:
        return n + addition(n-1)
res = addition(10)
print(res)

#Bai6
def show_student(name, age):
    def display_student(name , age):
        return str(name) + " " + str(age)
    return display_student(name, age)
print(show_student("Emma", 26))

#Bai7
def check_palindrome(n):
    t = 0
    s = 0
    a = n
    while n > 0:
        s = n%10
        t = t*10+s
        n = n//10
    if t == a:
        return "Given number is a palindrome"
    else:
        return "Given number is not a palindrome"
print(check_palindrome(1331))  

#Bai8

x = [4,6,8,24,12,2]
def check_largest(x):
    largest = x[0]
    for i in x:
        if i > largest:
            largest = i
    return largest
print(check_largest(x))

#Lab 02b

#Bai1
x = int(input())

if x <= 5:
    print("Re-enter")
else : 
    def tong(x):
        return x + tong(x-1) if x > 0 else 0
    print(tong(x))
    def giathua(x):
        return x * giathua(x-1) if x > 1 else 1
    print(giathua(x))
    def tonglon(x):
        return 1/x+ tonglon(x-1) if x > 1 else 1
    print(tonglon(x))
    def prime(X):
        if X < 2:
            return False
        for i in range(2, int(X**0.5) + 1):
            if X % i == 0:
                return False
        return True
    print(prime(x))

#Bai2

a = int(input())
b = int(input())
x =[]
y =[]
z =[]
p =[]
for i in range (1,a):
    if a%i ==0:
        x.append(i)
for j in range (1,b):
    if b%j ==0:
        y.append(j)
for t in range(len(x)):
    for k in range(len(y)):
        if x[t] == y[k]:
            z.append(x[t])
print(z)
for h in range (len(z)):
    for g in range (1,int(h**0.5)+1):
        if z[h]%g == 0:
            p.append(z[h])
print(max(p))    

print((a*b)//max(p))
            
#Bai3
x = input()
a = x.isdigit()
if a == False:
    print("Not a Number")
else:
    def binary(b):
        n = int(b)
        
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return str(binary(n//2))+ str(n%2)
    print(binary(x))

def tongso(a):
    tong = 0
    while a >0:
        tong = tong + a%10
        a = a//10
    return tong

def songuoc(j):
    sodaonguoc = 0
    while j > 0:
        temp = j % 10
        sodaonguoc = sodaonguoc * 10 + temp
        j = j // 10
    return sodaonguoc
print(songuoc(int(x)))


#Bai4
a, b = map(int, input().split())
def songuoc(j):
    sodaonguoc = 0
    bandau = j
    while j > 0:
        temp = j % 10
        sodaonguoc = sodaonguoc * 10 + temp
        j = j // 10
    if sodaonguoc == bandau:
        return True
    else:
        return False
for i in range (a, b+1,1):
    if songuoc(i)== True:
        print(i, end=' ')
    continue

#Lab03

#Bai1
x =int(input())
for i in range (0,x+1,1):
    for j in range (1,i+1,1):
        print(j, end=' ')
    print() 

a = int(input("Enter number "))
tong = 0
for i in range(1, a + 1):
    tong = tong + i
print("Sum is:", tong)

#Bai2

x = list(map(int,input().split()))
for i in range(len(x)):
    if x[i]> 150:
        continue
    elif x[i] > 500:
        break 
    elif x[i]%5 == 0:
        print(x[i], end=' ')
    else:
        break

# 
x = int(input())
count = 0 
while x > 0:
    x = x//10
    count =count +1 
print(count)

#
list1 = [10,20,30,40,50]
for i in range (len(list1),0,-1):
    print(list1[i-1], end=' ')

#Bai3
x = input()
a = int(len(x)/3)
print(str(x[a])+str(x[a+1])+str(x[a+2]) + str(x[a+3]))

#
s1 = "Ault"
s2 = "Kelly"
a = int(len(s1)/2)
s3 = s1[:a] + s2 + s1[a:]
print(s3)  


#
s1 = "America"
s2 = "Japan"
giua1 = int(len(s1)/2)
giua2 = int(len(s2)/2)
s3 = s1[0]+s2[0]+s1[giua1]+s2[giua2]+ s1[-1] + s2[-1]
print(s3)

#
str1 = "PyNaTive"
s1 = []
s2= []
for letter in str1:
    if letter.islower():
        s1.append(letter)
    else : 
        s2.append(letter)
s3 = s1 +s2
print("".join(s3))  

#
x = "@#@$@#$%#$%#$786876876fhdhgdfhg"
Char = 0
Digits = 0
Symbol = 0
for i in x:
    if i.isalpha():
        Char += 1
    elif i.isdigit():
        Digits += 1
    else:
        Symbol += 1
print("Char:",Char,"Digits:", Digits,"Symbol:", Symbol)

#Bai4
#
str1 = "I am 25 years and 10 months old"
a = []
for letter in str1:
    if letter.isdigit():
        a.append(letter)
print("".join(a))
    

#
str1 = "?*dfgdfghf$^&FDGDFG#$%^"
a = []
for letter in str1:
    if letter.isalpha():
        a.append(letter)
print("".join(a))
    
#
str1 = ["Emma", "Jon","", None, "Kelly", "Eric"]
a = []
for i in str1:
    if isinstance(i, str) and i.isalpha()== True :
        a.append(i)
print(a)

#

str1 = "Emma-is-a-date-scientist"
a = str1.split('-')
for i in a:
    print(i)

#
a =  input()
b = input()
def check(n):
    temp=[]
    for letter in n:
        if letter.isalpha():
            temp.append(letter)
    sorted_temp = sorted(temp)
    return sorted_temp
if check(a) ==check(b):
    print("Yes")
else:
    print("No")

#
x = input()
def chuyendoi(n):
    a = {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "A":10,"B":11,"C":12,"D":13,"E":14,"F":15}
    tong =0
    for i in range(0,len(n)):
        print(i)
        tong  = tong + int(a[n[i]])*(16**(int(len(n))-i-1))
    return tong
            
print(chuyendoi(x))



#Lab04
#
open ("sales.txt",'w')
#
import datetime
def taofile():
    a = datetime.datetime.now()
    b = a.strftime("%Y-%m-%d-%H-%M-%S") + ".txt"
    with open (b,'w') as f :
        f.write("")
    print(b)
taofile()
#
import os 
def taofilequyen():
    file = "sample.txt"
    permissions = 0o644
    with open (file, 'w') as f :
        f.write("")
    os.chmod(file, permissions)
    print("permissions has changed read/write")
taofilequyen()
#
import os


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

-
def write_to_new_file():
    print("--- 1. Ghi vào một tệp mới ---")
    file_name = "new_file.txt"
    file_path = os.path.join(SCRIPT_DIR, file_name)
    content = "Done Writing\nThis is new content"


    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Đã tạo và ghi vào tệp '{file_name}'. Nội dung:\n")
    print(content)
    print(f"Kiểm tra tệp tại: {file_path}\n")


def write_to_existing_file():
    print("--- 2. Ghi vào một tệp đã tồn tại ---")
    file_name = "existing_file.txt"
    file_path = os.path.join(SCRIPT_DIR, file_name)


    with open(file_path, 'w', encoding='utf-8') as f:
        f.write("This is original content.\n")
    print(f"Đã tạo/chuẩn bị '{file_name}' với nội dung ban đầu.")

    new_content = "This is new content\nOpening file again..\nThis is overwritten content"

  
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"Đã ghi đè lên tệp '{file_name}'. Nội dung mới:\n")
    print(new_content)
    print(f"Kiểm tra tệp tại: {file_path}\n")


def write_list_of_lines_to_file():
    print("--- 3. Ghi danh sách các dòng vào một tệp ---")
    file_name = "user_info.txt"
    file_path = os.path.join(SCRIPT_DIR, file_name)

    user_data = [
        "Name: Emma\n",
        "Address: 221 Baker Street\n",
        "City: London\n",
        "Country: United Kingdom\n" 
    ]

   
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(user_data)

    print(f"Đã ghi danh sách các dòng vào tệp '{file_name}'. Nội dung:\n")
 
    for line in user_data:
        print(line, end='') 

    print(f"\nKiểm tra tệp tại: {file_path}\n")



write_to_new_file()
write_to_existing_file()
write_list_of_lines_to_file()
    
print("Finish")
print(f"Kiểm tra các tệp 'new_file.txt', 'existing_file.txt', 'user_info.txt' trong thư mục:")
print(SCRIPT_DIR)


#
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_FILE_NAME = "test_q3.txt"
TEST_FILE_PATH = os.path.join(SCRIPT_DIR, TEST_FILE_NAME)

def File():
    print("--- Bắt đầu các tác vụ tìm kiếm tệp (Q3) ---")

    print("\n--- 1. Tìm kiếm về đầu tệp ---")
    content_q1_text = "My First Line\nMy Second Line\n"
    with open(TEST_FILE_PATH, 'w', encoding='utf-8') as f:
        f.write(content_q1_text)
    
    with open(TEST_FILE_PATH, 'r', encoding='utf-8') as f:
        print(f"Vị trí ban đầu: {f.tell()}")
        f.read()
        print(f"Vị trí sau khi đọc hết: {f.tell()}")
        f.seek(0)
        print(f"Vị trí sau khi seek(0): {f.tell()}")
        print("Đã đọc lại từ đầu:", f.read().strip())

    print("\n--- 2. Tìm kiếm về cuối tệp ---")
    file_for_end = os.path.join(SCRIPT_DIR, "test_end_q3.txt")
    initial_content_text = "This is new content\n"
    with open(file_for_end, 'w', encoding='utf-8') as f:
        f.write(initial_content_text)
    print(f"Nội dung ban đầu của '{os.path.basename(file_for_end)}': {initial_content_text.strip()}")

    with open(file_for_end, 'a', encoding='utf-8') as f: 
        f.write("This is overwritten content")
        print(f"Vị trí sau khi mở 'a': {f.tell()}") 
    
    with open(file_for_end, 'r', encoding='utf-8') as f:
        print(f"Nội dung cuối cùng của '{os.path.basename(file_for_end)}':\n{f.read()}")

    print("\n--- 3. Tìm kiếm từ vị trí hiện tại ---")
    content_q3_text = "First\nSecond\nThird\n"
    with open(TEST_FILE_PATH, 'w', encoding='utf-8') as f:
        f.write(content_q3_text)

    with open(TEST_FILE_PATH, 'rb') as f:
        read_first_part_bytes = f.read(5)
        print(f"Đọc '{read_first_part_bytes.decode('utf-8')}', vị trí: {f.tell()}")
        f.seek(1, os.SEEK_CUR)
        print(f"Vị trí sau khi seek(1, os.SEEK_CUR): {f.tell()}")
        read_second_part_bytes = f.read(6)
        print(f"Đọc '{read_second_part_bytes.decode('utf-8')}', vị trí: {f.tell()}")

    print("\n--- 4. Tìm kiếm lùi với Offset âm ---")
    content_q4_text = "Line 1\nLine 2\nLine 3\n"
    with open(TEST_FILE_PATH, 'w', encoding='utf-8') as f:
        f.write(content_q4_text)

    with open(TEST_FILE_PATH, 'rb') as f:
        f.seek(len("Line 1\nLine".encode('utf-8')))
        current_pos = f.tell()
        print(f"Vị trí hiện tại (sau 'Line 1\\nLine'): {current_pos}")
        f.seek(-5, os.SEEK_CUR)
        print(f"Vị trí sau khi seek(-5, os.SEEK_CUR): {f.tell()}")
        read_content_bytes = f.read(10)
        print("Đọc từ vị trí mới:", read_content_bytes.decode('utf-8').strip())

    print("\n--- 5. Sử dụng hàm tell() ---")
    content_q5_text = "My First Line\nMy Second Line\nThis content is added to the end of the file\nDemonstrating tell\n**Done**"
    with open(TEST_FILE_PATH, 'w', encoding='utf-8') as f:
        f.write(content_q5_text)

    with open(TEST_FILE_PATH, 'r+', encoding='utf-8') as f: 
        print(f"tell() ban đầu: {f.tell()}")
        f.read(75)
        print(f"tell() sau khi đọc 75 ký tự: {f.tell()}")
        f.seek(0)
        print(f"tell() sau khi seek(0): {f.tell()}")
        print("***Printing File Content***")
        print(f.read())
        print(f"tell() sau khi đọc hết tệp: {f.tell()}")
        print("**Done**\n" + f"tell() cuối cùng: {f.tell()}")

    print("\n--- Tất cả tác vụ Q3 đã hoàn thành ---")

if __name__ == "__main__":
    File()



#
import os
import datetime
import shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_DIR = os.path.join(SCRIPT_DIR, "q4_test_files")

def setup_test_environment():
    if os.path.exists(TEST_DIR):
        shutil.rmtree(TEST_DIR)
    os.makedirs(TEST_DIR)
    
    with open(os.path.join(TEST_DIR, "new_details.txt"), 'w') as f: f.write("details")
    with open(os.path.join(TEST_DIR, "test.txt"), 'w') as f: f.write("test content")
    with open(os.path.join(TEST_DIR, "sales_1.txt"), 'w') as f: f.write("sales 1")
    with open(os.path.join(TEST_DIR, "sales_2.txt"), 'w') as f: f.write("sales 2")
    with open(os.path.join(TEST_DIR, "report.doc"), 'w') as f: f.write("report doc")
    with open(os.path.join(TEST_DIR, "old_expense.txt"), 'w') as f: f.write("old expense")
    
    print(f"--- Đã tạo thư mục kiểm tra: {TEST_DIR} và các tệp ban đầu ---")
    print("Các tệp ban đầu trong thư mục:")
    for f in os.listdir(TEST_DIR):
        print(f"- " + f)

def cleanup_test_environment():
    if os.path.exists(TEST_DIR):
        shutil.rmtree(TEST_DIR)
        print(f"\n--- Đã xóa thư mục kiểm tra: {TEST_DIR} ---")

def run_q4_tasks():
    setup_test_environment()

    print("\n--- 1. Đổi tên tệp sau khi kiểm tra sự tồn tại ---")
    old_name_1 = os.path.join(TEST_DIR, "new_details.txt")
    new_name_1 = os.path.join(TEST_DIR, "renamed_details.txt")

    if os.path.exists(old_name_1):
        os.rename(old_name_1, new_name_1)
        print(f"Đã đổi tên '{os.path.basename(old_name_1)}' thành '{os.path.basename(new_name_1)}'.")
    else:
        print(f"Tệp '{os.path.basename(old_name_1)}' không tồn tại.")

    print("\n--- 2. Đổi tên nhiều tệp ---")
    shutil.copy(os.path.join(TEST_DIR, "sales_1.txt"), os.path.join(TEST_DIR, "sales_1_copy.txt"))
    shutil.copy(os.path.join(TEST_DIR, "sales_2.txt"), os.path.join(TEST_DIR, "sales_2_copy.txt"))
    
    old_names_multi = [os.path.join(TEST_DIR, "sales_1_copy.txt"), os.path.join(TEST_DIR, "sales_2_copy.txt")]
    new_names_multi = [os.path.join(TEST_DIR, "sales_A.txt"), os.path.join(TEST_DIR, "sales_B.txt")]

    for i in range(len(old_names_multi)):
        if os.path.exists(old_names_multi[i]):
            os.rename(old_names_multi[i], new_names_multi[i])
            print(f"Đã đổi tên '{os.path.basename(old_names_multi[i])}' thành '{os.path.basename(new_names_multi[i])}'.")
        else:
            print(f"Tệp '{os.path.basename(old_names_multi[i])}' không tồn tại.")
    
    print("\n--- 3. Đổi tên chỉ các tệp trong một danh sách cụ thể trong thư mục ---")
    files_to_rename_specific = {
        "sales_A.txt": "sales_Alpha.txt",
        "sales_B.txt": "sales_Beta.txt"
    }

    for old_base, new_base in files_to_rename_specific.items():
        old_path = os.path.join(TEST_DIR, old_base)
        new_path = os.path.join(TEST_DIR, new_base)
        if os.path.exists(old_path):
            os.rename(old_path, new_path)
            print(f"Đã đổi tên '{old_base}' thành '{new_base}'.")
        else:
            print(f"Tệp '{old_base}' không tồn tại.")

    print("\n--- 4. Đổi tên tệp với dấu thời gian ---")
    original_file_ts = os.path.join(TEST_DIR, "test.txt")
    
    now = datetime.datetime.now()
    timestamp_str = now.strftime("%Y%m%d_%H%M%S")
    
    base_name, extension = os.path.splitext(os.path.basename(original_file_ts))
    new_file_name_ts = f"{base_name}_{timestamp_str}{extension}"
    new_file_path_ts = os.path.join(TEST_DIR, new_file_name_ts)

    if os.path.exists(original_file_ts):
        os.rename(original_file_ts, new_file_path_ts)
        print(f"Đã đổi tên '{os.path.basename(original_file_ts)}' thành '{new_file_name_ts}'.")
    else:
        print(f"Tệp '{os.path.basename(original_file_ts)}' không tồn tại.")

    print("\n--- 5. Đổi phần mở rộng của tệp ---")
    old_ext_file = os.path.join(TEST_DIR, "report.doc")
    new_ext_file = os.path.join(TEST_DIR, "report.pdf")

    if os.path.exists(old_ext_file):
        os.rename(old_ext_file, new_ext_file)
        print(f"Đã đổi phần mở rộng của '{os.path.basename(old_ext_file)}' thành '{os.path.basename(new_ext_file)}'.")
    else:
        print(f"Tệp '{os.path.basename(old_ext_file)}' không tồn tại.")

    print("\n--- 6. Đổi tên và di chuyển tệp đến vị trí mới ---")
    old_move_file = os.path.join(TEST_DIR, "old_expense.txt")
    
    destination_dir = os.path.join(SCRIPT_DIR, "moved_files")
    os.makedirs(destination_dir, exist_ok=True)

    new_name_at_dest = "expense_report_final.txt"
    destination_path = os.path.join(destination_dir, new_name_at_dest)

    if os.path.exists(old_move_file):
        shutil.move(old_move_file, destination_path)
        print(f"Đã đổi tên '{os.path.basename(old_move_file)}' và di chuyển thành '{new_name_at_dest}' tới '{os.path.basename(destination_dir)}'.")
    else:
        print(f"Tệp '{os.path.basename(old_move_file)}' không tồn tại.")
        
    print("\n--- Tất cả các tác vụ Q4 đã hoàn thành ---")
    print(f"Kiểm tra các tệp trong thư mục: {TEST_DIR} và {destination_dir}")

if __name__ == "__main__":
    try:
        run_q4_tasks()
    finally:
        cleanup_test_environment()
#Lab04b
#
import os
import datetime

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_FILE_DIR = os.path.join(SCRIPT_DIR, "q1_test_files")

def setup_q1_environment():
    if not os.path.exists(TEST_FILE_DIR):
        os.makedirs(TEST_FILE_DIR)
    
    poem_content = "Mot cay lam chang nen non\nBa cay chum lai nen hon nui cao\n"
    with open(os.path.join(TEST_FILE_DIR, "poem.txt"), 'w', encoding='utf-8') as f:
        f.write(poem_content)
    
    story_content = (
        "A boy is playing there.\n"
        "There is a playground.\n"
        "An airplane is in the sky.\n"
        "The sky is pink.\n"
        "Alphabets and numbers are allowed in the password.\n"
    )
    with open(os.path.join(TEST_FILE_DIR, "story.txt"), 'w', encoding='utf-8') as f:
        f.write(story_content)
    
    print(f"--- Đã chuẩn bị thư mục: {TEST_FILE_DIR} và các tệp poem.txt, story.txt ---")

def cleanup_q1_environment():
    if os.path.exists(TEST_FILE_DIR):
        import shutil
        shutil.rmtree(TEST_FILE_DIR)
        print(f"\n--- Đã xóa thư mục kiểm tra: {TEST_FILE_DIR} ---")

def create_empty_file(file_name):
    file_path = os.path.join(TEST_FILE_DIR, file_name)
    with open(file_path, 'w', encoding='utf-8') as f:
        pass
    print(f"1. Đã tạo tệp rỗng '{file_name}' tại: {file_path}")

def create_file_with_datetime(base_name):
    now = datetime.datetime.now()
    datetime_str = now.strftime("%Y-%m-%d-%H-%M-%S")
    file_name = f"{base_name}_{datetime_str}.txt"
    file_path = os.path.join(TEST_FILE_DIR, file_name)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(f"This file was created at {now}.\n")
    print(f"2. Đã tạo tệp '{file_name}' với dấu thời gian tại: {file_path}")

def create_file_with_permission(file_name, permissions_octal):
    file_path = os.path.join(TEST_FILE_DIR, file_name)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(f"This is a file with specific permissions.\n")
    os.chmod(file_path, permissions_octal)
    print(f"3. Đã tạo tệp '{file_name}' với quyền {oct(permissions_octal)} tại: {file_path}")

def read_file_line_by_line(file_name):
    file_path = os.path.join(TEST_FILE_DIR, file_name)
    print(f"\n4. Đọc nội dung tệp '{file_name}' từng dòng:")
    if not os.path.exists(file_path):
        print(f"Lỗi: Tệp '{file_name}' không tồn tại.")
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            print(line.strip())
    print("--- Kết thúc đọc tệp ---")

def count_lines_not_starting_with_T(file_name):
    file_path = os.path.join(TEST_FILE_DIR, file_name)
    count = 0
    print(f"\n5. Đếm số dòng không bắt đầu bằng 'T' trong tệp '{file_name}':")
    if not os.path.exists(file_path):
        print(f"Lỗi: Tệp '{file_name}' không tồn tại.")
        return 0

    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            if not line.strip().startswith('T') and not line.strip().startswith('t'):
                count += 1
    print(f"No of lines not starting with 'T' = {count}")
    return count

if __name__ == "__main__":
    try:
        setup_q1_environment()
        
        create_empty_file("sales.txt")
        create_file_with_datetime("created")
        create_file_with_permission("sample.txt", 0o644)
        
        read_file_line_by_line("poem.txt")
        count_lines_not_starting_with_T("story.txt")
        
        print("\n--- Tất cả các tác vụ Q1 đã hoàn thành ---")
        print(f"Kiểm tra các tệp trong thư mục: {TEST_FILE_DIR}")
        
    finally:
        cleanup_q1_environment()

#
import os
import datetime
import shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_FILE_DIR = os.path.join(SCRIPT_DIR, "q2_test_files")

def setup_q2_environment():
    if not os.path.exists(TEST_FILE_DIR):
        os.makedirs(TEST_FILE_DIR)
    
    word_count_content = "This is a sample text file to count words. Total words are nineteen."
    with open(os.path.join(TEST_FILE_DIR, "text_for_word_count.txt"), 'w', encoding='utf-8') as f:
        f.write(word_count_content)
    
    story_content = (
        "Mot cay lam chang nen non\n"
        "Ba cay chum lai nen hon nui cao\n"
        "A boy is playing there.\n"
        "There is a playground.\n"
        "An airplane is in the sky.\n"
        "The sky is pink.\n"
        "Alphabets and numbers are allowed in the password.\n"
    )
    with open(os.path.join(TEST_FILE_DIR, "story.txt"), 'w', encoding='utf-8') as f:
        f.write(story_content)
    
    print(f"--- Đã chuẩn bị thư mục: {TEST_FILE_DIR} và các tệp thử nghiệm ---")

def cleanup_q2_environment():
    if os.path.exists(TEST_FILE_DIR):
        shutil.rmtree(TEST_FILE_DIR)
        print(f"\n--- Đã xóa thư mục kiểm tra: {TEST_FILE_DIR} ---")

def count_total_words(file_name):
    file_path = os.path.join(TEST_FILE_DIR, file_name)
    total_words = 0
    print(f"\n1. Đếm tổng số từ trong tệp '{file_name}':")
    if not os.path.exists(file_path):
        print(f"Lỗi: Tệp '{file_name}' không tồn tại.")
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        words = content.split()
        total_words = len(words)
    print(f"Total words are {total_words}")
    return total_words

def display_words(file_name):
    file_path = os.path.join(TEST_FILE_DIR, file_name)
    print(f"\n2. Hiển thị các từ ít hơn 4 ký tự từ tệp '{file_name}':")
    if not os.path.exists(file_path):
        print(f"Lỗi: Tệp '{file_name}' không tồn tại.")
        return

    words_less_than_4_chars = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            words = line.strip().split()
            for word in words:
                clean_word = ''.join(char for char in word if char.isalnum())
                if len(clean_word) < 4:
                    words_less_than_4_chars.append(clean_word)
    
    print("Các từ ít hơn 4 ký tự:", ', '.join(words_less_than_4_chars))
    
    print("\n--- Nội dung tệp và các từ nhỏ hơn 4 ký tự (minh họa): ---")
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            print(line.strip())
    print("---------------------------------------------------------")


def write_to_new_file(file_name, content):
    file_path = os.path.join(TEST_FILE_DIR, file_name)
    print(f"\n3.1. Ghi vào tệp mới '{file_name}':")
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Done Writing")
    print(f"Nội dung mới: {content.strip()}")

def write_to_existing_file(file_name, new_content):
    file_path = os.path.join(TEST_FILE_DIR, file_name)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write("Initial content for overwrite test.\n")
    
    print(f"\n3.2. Ghi đè lên tệp hiện có '{file_name}':")
    print("Opening file again..")
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Nội dung đã ghi đè: {new_content.strip()}")

def write_list_of_lines_to_file(file_name, lines):
    file_path = os.path.join(TEST_FILE_DIR, file_name)
    print(f"\n3.3. Ghi danh sách các dòng vào tệp '{file_name}':")
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines([line + '\n' for line in lines])
    
    print("Nội dung đã ghi:")
    with open(file_path, 'r', encoding='utf-8') as f:
        print(f.read().strip())

if __name__ == "__main__":
    try:
        setup_q2_environment()
        
        count_total_words("text_for_word_count.txt")
        
        display_words("story.txt")
        
        write_to_new_file("new_file.txt", "This is new content")
        write_to_existing_file("existing_file.txt", "This is overwritten content")
        
        contact_info = [
            "Name: Emma",
            "Address: 221 Baker Street",
            "City: London"
        ]
        write_list_of_lines_to_file("contact_info.txt", contact_info)
        
        print("\n--- Tất cả các tác vụ Q2 đã hoàn thành ---")
        print(f"Kiểm tra các tệp trong thư mục: {TEST_FILE_DIR}")
        
    finally:
        cleanup_q2_environment()

#
import os
import datetime
import shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_FILE_DIR = os.path.join(SCRIPT_DIR, "q3_test_files")

def setup_q3_environment():
    if not os.path.exists(TEST_FILE_DIR):
        os.makedirs(TEST_FILE_DIR)
    
    uppercase_content = "This Is A Sample Text. PYTHON is Great!"
    with open(os.path.join(TEST_FILE_DIR, "uppercase_test.txt"), 'w', encoding='utf-8') as f:
        f.write(uppercase_content)
    
    article_content = (
        "This article discusses various topics. "
        "These topics are interesting. "
        "We believe this is a good read. "
        "However, these ideas might evolve. "
        "This is an example where this and these words are counted."
    )
    with open(os.path.join(TEST_FILE_DIR, "article.txt"), 'w', encoding='utf-8') as f:
        f.write(article_content)
    
    print(f"--- Đã chuẩn bị thư mục: {TEST_FILE_DIR} và các tệp thử nghiệm ---")

def cleanup_q3_environment():
    if os.path.exists(TEST_FILE_DIR):
        shutil.rmtree(TEST_FILE_DIR)
        print(f"\n--- Đã xóa thư mục kiểm tra: {TEST_FILE_DIR} ---")

def count_uppercase_characters(file_name):
    file_path = os.path.join(TEST_FILE_DIR, file_name)
    count = 0
    print(f"\n1. Đếm ký tự viết hoa trong tệp '{file_name}':")
    if not os.path.exists(file_path):
        print(f"Lỗi: Tệp '{file_name}' không tồn tại.")
        return 0

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        for char in content:
            if 'A' <= char <= 'Z':
                count += 1
    print(count)
    return count

def count_this_and_these_words(file_name):
    file_path = os.path.join(TEST_FILE_DIR, file_name)
    this_count = 0
    these_count = 0
    print(f"\n2. Đếm số lần xuất hiện của 'this' và 'these' trong tệp '{file_name}':")
    if not os.path.exists(file_path):
        print(f"Lỗi: Tệp '{file_path}' không tồn tại.")
        return 0

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read().lower()
        words = content.split()
        
        for word in words:
            clean_word = ''.join(char for char in word if char.isalpha())
            
            if clean_word == "this":
                this_count += 1
            elif clean_word == "these":
                these_count += 1
    
    total_found = this_count + these_count
    print(f"Số lượng từ 'this': {this_count}")
    print(f"Số lượng từ 'these': {these_count}")
    print(f"Tổng số từ 'this' và 'these' tìm thấy: {total_found}")
    
    return total_found

if __name__ == "__main__":
    try:
        setup_q3_environment()
        
        count_uppercase_characters("uppercase_test.txt")
        
        count_this_and_these_words("article.txt")
        
        print("\n--- Tất cả các tác vụ Q3 đã hoàn thành ---")
        print(f"Kiểm tra các tệp trong thư mục: {TEST_FILE_DIR}")
        
    finally:
        cleanup_q3_environment()