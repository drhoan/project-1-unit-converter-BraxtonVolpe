def F_to_C(f):
    return (f - 32) * 5/9

def C_to_F(c):
    return (c * 9/5) + 32

def kelvin_to_celsius(k):
    return k - 273.15

def celsius_to_kelvin(Cel):
    return Cel + 273.15

def F_to_kelvin(fah):
    return (fah - 32) * 5/9 + 273.15

def lbs_to_kg(lbs):
    return lbs * 0.453592

def kg_to_lbs(kg):
    return kg / 0.453592

def ounces_to_grams(oz):
    return oz * 28.3495

def grams_to_ounces(grams):
    return grams / 28.3495

def stones_to_kg(stone):
    return stone * 6.35029

def feet_to_meters(ft):
    return ft * 0.3048

def miles_to_km(miles):
    return miles * 1.60934

def gallons_to_liters(gallons):
    return gallons * 3.78541

def inches_to_cm(inches):
    return inches * 2.54

def main(): 
    while True:
        print("1: Temperature Conversions")
        print("2: Weight Conversions")
        print("3: Distance (Feet to Meter)")
        print("4: Distance (Miles to Km)")
        print("5: Volume (Gallons to Liters)")
        print("6:Length (Inches to Centimeters)")
        
        
        
        
        choice = input("Choose an option (0-6)")
        
        if choice == '0':
            print("Pick a menu selection, NOT ZERO!")
            break
        
        elif choice == '1':
            print("Select Temperature Conversion:")
            print("1: Fahrenheit to Celsius")
            print("2: Celsius to Fahrenheit")
            print("3: Kelvin to Celsius")
            print("4: Celsius to Kelvin")
            print("5: Fahrenheit to Kelvin")
            temp_choice = input("Choose an option (1-5): ")
            
            if temp_choice == '1':
                f = float(input("Enter temperature in Fahrenheit: "))
                print(f"Result: {f} F is {F_to_C(f)} C")
            elif temp_choice == '2':
                c = float(input("Enter temperature in Celsius: "))
                print(f"Result: {c} C is {C_to_F(c)} F")
            elif temp_choice == '3':
                k = float(input("Enter temperature in Kelvin: "))
                print(f"Result: {k} K is {kelvin_to_celsius(k)} C")
            elif temp_choice == '4': 
                Cel = float(input("Enter temperature in Celsius: "))
                print(f"Result: {Cel} Cel is {celsius_to_kelvin(Cel)} K")
            elif temp_choice == '5': 
                fah = float(input("Enter temperature in Fahrenheit: "))
                print(f"Result: {fah} F is {F_to_kelvin(fah)} K")
            else: 
                print("invalid temperature conversion choice.")
                
        elif choice == '2':
            print("Select Weight Conversion:")
            print("1: Pounds to Kilograms")
            print("2: Kilograms to Pounds")
            print("3: Ounces to Grams")
            print("4: Grams to Ounces")
            print("5: Stones to Kilograms")
            Weight_choice = input("Choose an option (1-5): ")
            
            if Weight_choice == '1':
                lbs = float(input("Enter weight in pounds: "))
                print(f"Result: {lbs} pounds is {lbs_to_kg(lbs)} kg")
            elif Weight_choice == '2':
                kg = float(input("Enter wieght in kilograms: "))
                print(f"Result: {kg} kg is {kg_to_lbs(kg)} lbs")
            elif Weight_choice == '3':
                oz = float(input("Enter weight in ounces: "))
                print(f"Result: {oz} ounces is {ounces_to_grams(oz)} grams")
            elif Weight_choice == '4':
                grams = float(input("Enter wieght in grams: "))
                print(f"Result: {grams} grams is {grams_to_ounces(grams)} ounces")
            elif Weight_choice == '5':
                stone = float(input("Enter weight in stones: "))
                print(f"Result: {stone} stone is {stones_to_kg(stone)} kg")
            else:
                print("Invalid weight conversion choice.")
        
        elif choice == '3':
            ft = float(input("Enter distance in feet: "))
            print(f"Result: {ft} feet is {feet_to_meters(ft)} meters")
        
        elif choice == '4':
            miles = float(input("Enter distance in miles: "))
            print(f"Result: {miles} miles is {miles_to_km(miles)} Km")
            
        elif choice == '5':
            gallons = float(input("Enter volume in gallons: "))
            print(f"Result: {gallons} gallons is {gallons_to_liters(gallons)} Liters")
        
        elif choice == '6':
            inches = float(input("Enter length in inches: "))
            print(f"Result: {inches} inches is {inches_to_cm(inches)} cm")
            
        else: 
            print("Invalid choice, please pick again.")
                
if __name__ == "__main__":
    main()
                
        
