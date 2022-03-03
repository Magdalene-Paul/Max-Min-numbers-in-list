count = 0
total = 0.00
while True:
    number = input('Enter a number: ')
    if number == 'done' :
        break
    try:
        value = float(number)
        count = count + 1
        total = total + value
    except:
        print('Invalid input')
        continue

print("the count  = " , count, total, total/count)
