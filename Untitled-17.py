day = int(input("Day: "))
month = int(input("month: "))
year = int(input("year: "))

def kiemtra(day, month, year):

    if year < 0:
        return False
        
 
    if month < 1 or month > 12:
        return False
        

    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        days_in_month[1] = 29
 
    if day < 1 or day > days_in_month[month - 1]:
        return False
        
    return True

if kiemtra(day, month, year) == True :
    print("Valid date")
else:
    print("Not valid date")