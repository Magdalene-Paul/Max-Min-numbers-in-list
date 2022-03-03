hour = input("Enter Hours:")
rate = input("Enter rate:")
try:
    h = float(hour)
    r = float(rate)
except:
    print("Error, Please enter a numeric input:")
    exit()
if h > 40 :
    normalpay = h * r
    extrapay = (1.5 * (h - 40) * r) + (40 * r)
    print(extrapay)
else:
    print(normalpay)
