def main():
    import sys
    import random
    from pyfiglet import Figlet
    figlet = Figlet()

    
    ls_fonts=figlet.getFonts()

    try:
        letter=sys.argv
        if len(letter)>1:
            if letter[1]=="-f" or letter[1]=="--font":
                if letter[2] in ls_fonts:
                    f=letter[2]
                else:
                    raise Exception
            else:
                raise Exception
        else:
            f=random.choice(ls_fonts)

        inp= input("Input: ")
        figlet.setFont(font=f)
        print(f"Output: \n{figlet.renderText(inp)}")
    except Exception:
        sys.exit("Invalid usage")

main()