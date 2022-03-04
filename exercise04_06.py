def computepay(h, r) :
    if h > 40:
        reg = h * r
        otp = (h-40.0) * (r * 0.5)
    else :
        print("Regular")
        reg = h * r
        otp = 0
    p = reg + otp
    return p
hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float (rate)
p = computepay(h, r)
print("Pay", p)