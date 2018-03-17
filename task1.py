PI = 3.14    
def calculate(R, L):
   volume = PI * R * R * L 
   return ('Volume: ' +  str(volume))    
   
radius = float(input('Please Enter the radius of a Cylinder: '))
length = float(input('Please Enter the length of a Cylinder: '))
print(calculate(radius, length))
