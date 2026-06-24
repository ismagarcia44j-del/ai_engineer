def main():
    frac = input("Fraction: ").split("/")
    print(eval(frac))

def eval(frac):
    try:
        x=int(frac[0])
        y=int(frac[1])
        if x>=0 and x<=y:
                div=round((x/y)*100)
                if div>=99:
                    return "F"
                elif div<=1:
                    return "E"
                else:
                    return f"{div}%"
        main()
    except (ValueError, ZeroDivisionError):
        main()

main()


