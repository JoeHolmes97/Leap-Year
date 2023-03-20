
def is_year_leap(year): # Function for checking if it's a leap year
    try:
        if year % 4 == 0:
            if year % 100 == 0 and year % 400 != 0:
                return False
            else:
                return True
        else:
            return False
    except:
        return

def days_in_month(year, month): # Function for the number of days in a month
    try:
        i_DaysInMonth = [31,28,31,30,31,30,31,31,30,31,30,31]
        if is_year_leap == True:
            i_DaysInMonth[1] = 29
    except:
        return

def day_of_year(year, month, day): # Function for calculating what day a particular date is
  
    i_MonthKey = [1,4,4,0,2,5,0,3,6,1,4,6] # Month key
    i_DayOfWeek = ["Saturday","Sunday","Monday","Tuesday","Wednesday","Thursday","Friday"]
    
    if is_year_leap(year) == True:
        i_MonthKey[0] = 0
        i_MonthKey[1] = 3
        
    iLast2Year = int(str(year)[-2:]) # Last 2 digits of year

    iL2YQuarter = int(iLast2Year / 4)

    iMonthSum = iLast2Year + iL2YQuarter + day + i_MonthKey[month-1]

    if 2000 <= year <= 2099:
        iMonthSum -= 1
    elif 1800 <= year < 1900:
        iMonthSum += 2
    elif 1753 <= year < 1800:
        iMonthSum += 4
        
    iDayOfWeek = iMonthSum % 7

    return i_DayOfWeek[iDayOfWeek]

print(day_of_year(2000, 12, 31))
print(day_of_year(1997, 7, 8))
