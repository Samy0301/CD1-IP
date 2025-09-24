# exercise 1
number = float(input("Give me a number "))

if number < 0:
    print("the number is negative")
elif number > 0:
    print("the number is positive")
else: 
    print("the number is 0")
    
# exercise 2
word = input("Write a word ")

if word == "".join(reversed(word)): 
    print(word + " is a palindrome")
else:
    print(f"{word} is not a palindrome")
    
# exercise 3
number = float(input("Write a number "))
result = "Is divisible by "
coma_bool = True

if number % 2 == 0:
    result += "2"
    coma_bool = False
if number % 3 == 0:
    if not coma_bool:
        result += ","
    result += "3"
    coma_bool = False
if number % 5 == 0:
    if not coma_bool:
        result += ","
    result += "5"
    coma_bool = False
if number % 7 == 0:
    if not coma_bool:
        result += ","
    result += "7"
    coma_bool = False
if number % 11 == 0:
    if not coma_bool:
        result += ","
    result += "11"
    coma_bool = False
if number % 13 == 0:
    if not coma_bool:
        result += ","
    result += "13"
    coma_bool = False
if coma_bool:
    print("none divide it")
else: 
    print(result)
    
# exercise 4
day = int(input("Write a number "))
month = int(input("Write a number "))
year = int(input("Write a number "))

if year < 0: print("invalid year")

if year % 4 == 0 or year % 100 != 0 or year % 400 == 0:
    leap_year = True
else:
    leap_year = False

if month < 1 or month > 12:
    print("invalid month")
    max_day = -1
elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    max_day = 31
elif month == 4 or month == 6 or month == 9 or month == 11:
    max_day = 30
elif month == 2:
    if leap_year:
        max_day = 29
    else:
        max_day = 28

if day < 0 or day > max_day:
    print("invalid day")
else:
    if month == 1:
       month = "enero"
    elif month == 2:
       month = "febrero"
    elif month == 3:
       month = "marzo"
    elif month == 4:
       month = "abril"
    elif month == 5:
       month = "mayo"
    elif month == 6:
       month = "junio"
    elif month == 7:
       month = "julio"
    elif month == 8:
       month = "agosto"
    elif month == 9:
       month = "septiembre"
    elif month == 10:
       month = "octubre"
    elif month == 11:
       month = "noviembre"
    elif month == 12:
       month = "diciembre"  
    print(f"{day} de {month} del {year}")   
    
# exercise 5
secuencia1 = "AGCATACGGTACGTTAGGCTACCTAGGTAC"
secuencia2 = "CCGTATAGGCTAGCTTACGGTAGCTAGGTC"
secuencia3 = "TGCAGTACCTGATCGGATACCGTATGGCAT"

chain = input("Write a DNA strand")
result = "the sequence is contained in the strings  "
bool_var = True

if chain in secuencia1:
    result += "1"
    bool_var = False
if chain in secuencia2:
    if not bool_var:
        result += ","
    result += "2"
    bool_var = False
if chain in secuencia3:
    if not bool_var:
        result += ","
    result += "3"
    bool_var = False
if bool_var:
    print("the sequence is not contained")
else:
    print(result)
    
# exercise 6
day = int(input("Write a number "))
month = int(input("Write a number "))
year = int(input("Write a number "))

day_after = day
month_after = month
year_after = year

day_before = day
month_before = month
year_before = year

if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    max_day = 31
elif month == 4 or month == 6 or month == 9 or month == 11:
    max_day = 30
elif month == 2:
    if year % 4 == 0:
        max_day = 29
    else:
        max_day = 28

if day < max_day:
    day_after = day + 1
else:
    day_after = 1
    if month == 12:
        month_after = 1
        year_after = year + 1
    else:
        month_after = month + 1

print(f"the day after is {day_after}/{month_after}/{year_after}")

if day > 1:
    day_before = day - 1
else:
    if month == 1:
       month_before = 12
       year_before = year - 1
       day_after = 31
    else:
        month_before = month - 1
        if month_before == 1 or month_before == 3 or month_before == 5 or month_before == 7 or month_before == 8 or month_before == 10 or month_before == 12:
            day_before = 31
        elif month_before == 4 or month_before == 6 or month_before == 9 or month_before == 11:
              day_before = 30
        elif month_before == 2:
           if year % 4 == 0:
               day_before = 29
           else:
               day_before = 28
             
print(f"the day before is {day_before}/{month_before}/{year_before}")   

# exercise 7
password = input("Write your password ")   

have_8character = len(password) >= 8
have_number = any(c.isdigit() for c in password)
have_letter = any(c.isalpha() for c in password)

if have_8character and have_number and have_letter:
    print("Yeyyy!")
else:
    print("Ups, wrong password")
    
# exercise 8
d1 = float(input("write the number"))
d2 = float(input("write the number"))
d3 = float(input("write the number"))
d4 = float(input("write the number"))
d5 = float(input("write the number"))
d6 = float(input("write the number"))
d7 = float(input("write the number"))

media = (d1 + d2 + d3 + d4 + d5 + d6 + d7) / 7

print(f"the average was ${media}")

media_bool = True
result = "above-average days were "

if d1 > media:
    result += f"monday ${d1}"
    media_bool = False
if d2 > media:
    if not media_bool:
        result += ", "
    result += f"tuesday ${d2}"
    media_bool = False
if d3 > media:
    if not media_bool:
        result += ", "
    result += f"wednesday ${d3}"
    media_bool = False
if d4 > media:
    if not media_bool:
        result += ", "
    result += f"thursday ${d4}"
    media_bool = False
if d5 > media:
    if not media_bool:
        result += ", "
    result += f"friday ${d5}"
    media_bool = False
if d6 > media:
    if not media_bool:
        result += ", "
    result += f"saturday ${d6}"
    media_bool = False
if d7 > media:
    if not media_bool:
        result += ", "
    result += f"sunday ${d7}"
    media_bool = False
if media_bool:
    print("no day was above average")
else: 
    print(result)

if d1== d2 == d3 == d4 == d5 == d6 == d7:
    print(f"every day had he same value {d1}")
else:
    bigest = d1
    bigest_day = "monday"

    if d2 > bigest:
        bigest = d2
        bigest_day = "tuesday"
    if d3 > bigest:
        bigest = d3
        bigest_day = "wednesday"
    if d4 > bigest:
        bigest = d4
        bigest_day = "thursday"
    if d5 > bigest:
        bigest = d5
        bigest_day = "friday"
    if d6 > bigest:
        bigest = d6
        bigest_day = "saturday"
    if d7 > bigest:
        bigest = d7
        bigest_day = "sunday"

    lower = d1
    lower_day = "monday"

    if d2 < lower:
        lower = d2
        lower_day = "tuesday"
    if d3 < lower:
        lower = d3
        lower_day = "wednesday"
    if d4 < lower:
        lower = d4
        lower_day = "thursday"
    if d5 < lower:
        lower = d5
        lower_day = "friday"
    if d6 < lower:
        lower = d6
        lower_day = "saturday"
    if d7 < lower:
        lower = d7
        lower_day = "sunday"

    print(f"the day white the highest income was {bigest_day} ${bigest} and the lowest {lower_day} ${lower}")