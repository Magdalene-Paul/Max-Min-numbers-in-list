hour = input("Enter Hours:")
rate = input("Enter rate:")
h = float(hour)
r = float(rate)
normalpay = h * r
extrapay = (40 * r) + (1.5 * (h - 40) * r)
if h <= 40 :
    print(normalpay)
else:
    print(extrapay)
