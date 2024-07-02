def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO
    new=d.replace("$"," ").strip()
    d=float(new)

    return d
def percent_to_float(p):
    # TODO
    new2=p.replace("%"," ").strip()
    p=float(new2)/100
    return p


main()
