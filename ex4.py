hrs = input("Enter Hours:")
rate = input("Enter Rate:")
h = float(hrs)
r = float(rate)

def computepay(h, r):
    if h <= 40 :
        p = h * r
        return p
    else:
        p = ((40 * r) + (1.5 * (h-40) * r ))
        return p

#p = computepay(h, r)
print("Pay", computepay(h,r))
