def main():
    dollars = dollars_to_float(input("How much was the meal? ").rstrip())
    percent = percent_to_float(input("What percentage would you like to tip? ").rstrip())
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    #input $50.00. izvade 50.0.
    dollars = d.lstrip('$')
    return(float(dollars))

def percent_to_float(p):
    #input 15% izvade 0.15
    percent = p.rstrip('%')
    return(float(percent)) / 100
    

main()
