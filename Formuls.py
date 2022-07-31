def ktoc(x):
    if type(x)== int or type(x)== float:
        return x - 273.15
        
def ctok(x):
    if type(x)== int or type(x)== float:
        return x + 273.15
        
def ctof(x):
    if type(x)== int or type(x)== float:
        return (x * 9/5) + 32
        
def ftoc(x):
    if type(x)== int or type(x)== float:
        return (x - 32) * 5/9
        
def density(mass, amount):
    if type(mass) == int or  type(mass) == float and type(amount) == int or type(amount) == float:
        return mass / amount
        
def massd(density, amount): 
    return density * amount
    
def massw(weight):
    return weight / 9.8
    
def massw10(weight):
    return weight / 10
    
def speed(time,distance):
    return time * distance
    
def fforce(support_reaction, coefficient_of_friction):
    return coefficient_of_friction * support_reaction
    
def pressureg(density, height):
    return density * height * 9.8

def pressureg10(density, height):
    return density * height * 10

def pressure(force, square ):
    return force / square
 
def weight(mass):
    return mass * 9.8

def weight10(mass):
    return mass * 10

def power(activity, time):
    return activity / time

def activity(force, distance):
    return force * distance

def check():
    print(ktoc(10))
    print(ctok(10))
    print(ctof(10))
    print(ftoc(10))
    print(density(10, 10))
    print(massd(10, 2))
    print(massw(10))
    print(massw10(10))
    print(speed(10,10))
    print(fforce(10, 10))
    print(pressureg(10, 10))
    print(pressureg10(10,10))
    print(pressure(10,10))
    print(weight(10))
    print(weight10(10))
    print(power(10, 10))
    print(activity(10, 10))


    
    



 