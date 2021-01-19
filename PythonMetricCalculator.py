#startup menu
menu=["'Length: 1', 'Weight: 2', 'Capacity: 3'"]

#Menus for the Length = 1
metric_l=["'km', 'm' , 'cm'"]
imperial_l=["'mi', 'ft', 'in'"]

#menu for Weights = 2
metric_m=["'t','kg', 'g'"]
imperial_m=["'stone', 'lb', 'oz'"]

#menu for Capacity = 3
metric_c=["'l', 'ml'"]
imperial_c=["'gal','qt', 'oz'"]

#menu for Temperature = 4
celsius=["'Celsius'"]
fahrenheit=["'Fahrenheit'"]

#variables from metric to imperial (distance) 
def km_mi():
    print(leng1/1.6, "Miles")
def m_ft():
    print(leng1*3.26, "Feets")
def cm_in():
    print(leng1/2.54, "Inches")

#variables from imperial to metric (distance)
def mi_km():
    print(leng2*1.6, "Kilometers")
def ft_m():
    print(leng2/3.26, "Metres")
def in_cm():
    print(leng2*2.54, "Centimetres")

#variables from metric to imperial (mass)
def t_st():
    print(mass1*157.47, "Stone")
def kg_lb():
    print(mass1*2.2, "Pounds")
def g_oz():
    print(mass1*0.035, "Ounces")

#variables from imperial to metric (mass)
def st_t():
    print(mass2*0.00635, "Tones")
def lb_kg():
    print(mass2*0.4536, "Kilograms")
def oz_g():
    print(mass2*28.35, "Grams")

#choose which what to convert
print(menu)
measure=int(input("Please select what you would like to convert by typing a number:\nLength:  1\nWeight:  2\nCapacity: 3\nTemp.: 4\n"))

#starting if statement chain
if measure==1:
    #menu to chose from either metric to imperial or vice-versa
    print("Metric-Imperial - 1\n")
    print("Imperial-Metric - 2\n")
    choice=int(input("Choose a conversion by typing a number: "))
    #If 1 is chosen follows by asking what metric distance to convert
    if choice== 1:
        print("Please choose the measurement you want to use.\n")
        #prints the metric length menu
        print(metric_l)
        distance =input("Type an option from the menu: ")

        #if statements that takes user input to assign a value for leng1
        #then runs the function
        if distance=="km":
            leng1=int(input("Please enter a number to convert: "))
            print=(km_mi())
        elif distance=="m":
            leng1=int(input("Please enter a number to convert: "))
            print=(m_ft())
        elif distance=="cm":
            leng1=int(input("Please enter a number to convert: "))
            print=(cm_in())
        else:
            print("Invalid Entry")

    #This is the code for the second choice in the program
    #If 2 is chosen follows by asking what imperial distance to convert
    if choice== 2:
        print("Please choose the measurement you want to use.\n")
        #prints the imperial length menu
        print(imperial_l)
        distance2 =input("Type an option from the menu: ")

        #if statements that takes user input to assign a value for leng2
        #then runs the function
        if distance2=="mi":
            leng2=int(input("Please enter a number to convert: "))
            print=(mi_km())
        elif distance2=="ft":
            leng2=int(input("Please enter a number to convert: "))
            print=(ft_m())
        elif distance2=="in":
            leng2=int(input("Please enter a number to convert: "))
            print=(in_cm())
        else:
            print("Invalid Entry")

if measure==2:
    #menu to chose from either metric to imperial or vice-versa
    print("Metric-Imperial - 1\n")
    print("Imperial-Metric - 2\n")
    choice2=int(input("Choose a conversion by typing a number: "))
    #If 1 is chosen follows by asking what metric distance to convert
    if choice2== 1:
        print("Please choose the measurement you want to use.\n")
        #prints the metric length menu
        print(metric_m)
        weight =input("Type an option from the menu: ")

        #if statements that takes user input to assign a value for mass1
        #then runs the function
        if weight=="t":
            mass1=int(input("Please enter a number to convert: "))
            print=(t_st())
        elif weight=="kg":
            mass1=int(input("Please enter a number to convert: "))
            print=(kg_lb())
        elif weight=="g":
            mass1=int(input("Please enter a number to convert: "))
            print=(g_oz())
        else:
            print("Invalid Entry")

    #This is the code for the second choice in the program
    #If 2 is chosen follows by asking what imperial mass to convert
    if choice2== 2:
        print("Please choose the measurement you want to use.\n")
        #prints the imperial length menu
        print(imperial_m)
        weight2 =input("Type an option from the menu: ")

        #if statements that takes user input to assign a value for mass2
        #then runs the function
        if weight2=="stone":
            mass2=int(input("Please enter a number to convert: "))
            print=(st_t())
        elif weight2=="lb":
            mass2=int(input("Please enter a number to convert: "))
            print=(lb_kg())
        elif weight2=="oz":
            mass2=int(input("Please enter a number to convert: "))
            print=(oz_g())
        else:
            print("Invalid Entry")
