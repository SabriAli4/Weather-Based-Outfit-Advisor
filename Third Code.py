

#gender = input('Enter gender (M/F): ')
#salary = int(input('Enter salary: '))
#status = int(input('Enter status: '))
#................................................................................
#if gender.upper() == 'M':
#    total = salary * 1.2

#if gender.upper() == 'F':
#    total = salary * 1.6

#else:
#    total = salary *1.5

#print(total)
#..............................................................................

#if gender.upper() == 'M':
#    if status == 1:
#        salary = 2000
#    else:
#        salary = 2500
        
#else:
#    salary = 4000

#print(salary)
#...............................................................................

#if status == 1:
#    bonus = 4000
#elif status == 2:
#    bonus = 4500
#elif status == 3:
#    bonus = 5000
#else:
#    bonus = 0
#.....................................................................................................

#match status:
#    case 1:
#        bonus = 4000
#    case 2:
#        bonus = 4500
#    case 3:
#        bonus = 5000
#    case _:
#        bonus = 0

#print(bonus)
#........................................................................................................

#products = [1,2,3,4]
#3 in products 
#print(6 in products)
#---------------------------------------Practice----------------------------------------------------------


temp = int(input('What is current temperature?: '))
weatherType = input('Is the weather sunny, rainy, or snowy today?: ').lower()
windSpeed = int(input('What is the wind speed today?: '))

if weatherType == 'sunny' and temp <=40:
    outfit = 'Wear a light jacket and jeans!'
elif weatherType == 'rainy' and temp <=40:
    outfit = 'Wear a rain coat and wind breaker jacket!'
elif weatherType == 'snowy' and temp <=40:
    outfit = 'Wear a trenchcoat!'
else:
    outfit = 'Today is your day :) Wear what you want!'

print(outfit)


    






