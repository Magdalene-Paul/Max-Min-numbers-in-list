largest = None
smallest = None
while True:
    number = input('Enter a Number: ')
    if number =='done' :
        break
    try:
        value = float(number)

    except:
        print('Invalid input')
        continue
    if smallest is None:
        smallest = value
    elif value < smallest :
        smallest = value
    if largest is None:
        largest = value
    elif value > largest :
        largest = value
print('Maximum is', largest)
print('Minimum is', smallest)
