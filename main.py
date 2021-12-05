from lexer import Lexer


def main(): #main method
    l = Lexer()
    n = l.lex("100 - ||||| + (200*200*200) / 30 - one+two") 
    obstr = ""
    for ob in n:
        obstr += ob.to_str()
    print(obstr)


if __name__ == "__main__":
    main()