Distance = float( input('Enter original distance from the origin in (m):'))
Velocity= float(input('Enter velocity in (m/s):' ))
Acceleration= float(input('Enter acceleration(m/s^2): '))
Time= float(input('Enter time lapse in (s):'))
Final_distance= Distance + Velocity*Time+1/2*Acceleration*Time**2
Final_velocity=Velocity+Acceleration*Time
Final_acceleration = Acceleration
print("The final distance is:", Final_distance,'m',"   ",  "The final velocity is:",Final_velocity,"m/s","   ","The final acceleration is:",Final_acceleration,'m/s^2')
