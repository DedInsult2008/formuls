def ktoc(x):#Кельвины в цельсии
    if type(x)== int or type(x)== float:
        return x - 273.15
        
def ctok(x):#Цельсии в кельвины
    if type(x)== int or type(x)== float:
        return x + 273.15
        
def ctof(x):#Цельсии в фаренгейты
    if type(x)== int or type(x)== float:
        return (x * 9/5) + 32
        
def ftoc(x):#Фаренгейты в цельсии
    if type(x)== int or type(x)== float:
        return (x - 32) * 5/9
        
def density(mass, amount):#Плотность
    if type(mass) == int or  type(mass) == float and type(amount) == int or type(amount) == float:
        return mass / amount
        
def massd(density, amount):#Масса по плотности
    if type(density) == int or type(density) == float and type(amount) == int or type(amount) == float:
        return density * amount
    
def massw(weight):#Масса по весу g = 9.8
    if type(weight) == int or type(weight) == float:
        return weight / 9.8
    
def massw10(weight):#Масса по весу g = 10
    if type(weight) == int or type(weight) == float:
        return weight / 10
    
def speed(time,distance):#Скорость
    if type(time) == int or type(time) == float and type(distance) == int or type(distance) == float:
        return time * distance
    
def fforce(support_reaction, coefficient_of_friction):#Сила трения
    if type(support_reaction) == int or type(support_reaction) == float and type(coefficient_of_friction) == int or type(coefficient_of_friction) == float:
        return coefficient_of_friction * support_reaction
    
def pressureg(density, height):#Гидростатическое давление g = 9.8
    if type(density) == int or type(density) == float and type(height) == int or type(height) == float:    
        return density * height * 9.8

def pressureg10(density, height):#Гидростатическое давление g = 10
    if type(density) == int or type(density) == float and type(height) == int or type(height) == float:
        return density * height * 10

def pressure(force, square ):#Давление
    if type(force) == int or type(force) == float and type(height) == int or type(height) == float:    
        return force / square
 
def weight(mass):#Вес g = 9.8
    if type(mass) == int or type(mass) == float:
        return mass * 9.8

def weight10(mass):#Вес g = 10
    if type(mass) == int or type(mass) == float:
        return mass * 10

def power(activity, time):#Мощность
    if type(activity) == int or type(activity) == float and type(time) == int or type(time) == float:
        return activity / time

def activity(force, distance):#Работа
    if type(force) == int or type(force) == float and type(distance) == int or type(distance) == float:
        return force * distance

def root(pow, num):#Корень любой степени
    if type(pow) == int or type(pow) == float and type(num) == int or type(num) == float:
        return num ** (1 / pow)

def inch(centimeters):#Сантиметры в дюймы
    if type(centimeters) == int or type(centimeters) == float:
        return centimeters / 2.5

def cent_i(inch):#Дюймы в сантиметры
    if type(inch) == int or type(inch) == float:
        return inch * 2.5

def foot(centimeters):#Сантиметры в футы
    if type(centimeters) == int or type(centimeters) == float:
        return centimeters / 30.5

def cent_f(feet):#Футы в сантиетры
    if type(foot) == int or type(foot) == float:
        return foot * 30.5

def mile(kilometers):#Километры в мили
    if type(kilometers) == int or type(kilometers) == float:
        return kilometers / 1.6

def kilometers(miles):
    if type(miles) == int or type(miles) == float:
        return miles * 1.6

def kilometers_m(meters):#Метры в километры
    if type(meters) == int or type(meters) == float:
        return meters / 1000

def meters_k(kilometers):#Километры в метры
    if type(kilometers) == int or type(kilometers) == float:
        return kilometers * 1000

def meters_c(centimeters):#Сантиметры в метры
    if type(centimeters)== int or type(centimeters) == float:
        return centimeters / 1000

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
    print(root(3,8))

print(check())    
    



 