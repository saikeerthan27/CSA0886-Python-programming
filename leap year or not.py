def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
    
#Test case 1
print(is_leap_year(2000))
print(is_leap_year(2001))   
    
    