mass = float(input("enter a positive mass in kg: "))
while mass < 0:
    mass = float(input("A positive value for mass is required: "))
    
else:
    velocity = float(input("enter the velocity in m/s: "))
    KE = (1/2 * mass * velocity**2)
    print (KE)