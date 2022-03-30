from email.generator import DecodedGenerator


curmsg = []
code = ''
msg = ''
decoded = ''
age = 0
curchar = ''

while True:
    q = input("cmd : ")
    if q == "!exit":
        exit()
    if q == "nc":
        qr = input("msg : ")
        for i in qr:
            curmsg.append(i)
        for i in curmsg:
            if i == "a":
                code += '.:'
            if i == "b":
                code += ';>' 
            if i == "c":
                code += '@<'
            if i == "d":
                code += '<,'
            if i == "e":
                code += '\'/'
            if i == "f":
                code += '#~'
            if i == "g":
                code += ':;'
            if i == "h":
                code += ':#'
            if i == "i":
                code += '$"'
            if i == "j":
                code += '!¬'
            if i == "k":
                code += '?/'
            if i == "l":
                code += '{['
            if i == "m":
                code += '~~'
            if i == "n":
                code += '*%'
            if i == "o":
                code += '+_'
            if i == "p":
                code += '$!'
            if i == "q":
                code += '<>'
            if i == "r":
                code += '::'
            if i == "s":
                code += '(^'
            if i == "t":
                code += ';£'
            if i == "u":
                code += ':~'
            if i == "v":
                code += '%*'
            if i == "w":
                code += '^£'
            if i == "x":
                code += '@~'
            if i == "y":
                code += '*-'
            if i == "z":
                code += '$&'
            if i == " ":
                code += '}+'
        print(curmsg)
        print(code)
        print("code", code)
        curmsg.clear()
        code = ''
    if q == "rc":
        qr = input("code : ")
        for i in qr:
            if age == 1:
                curchar += i
                curmsg.append(curchar)
                age = 0
                curchar = ''
            else:
                curchar += i 
                age+= 1

        for i in curmsg:
            if i == ".:":
                msg += "a"
            if i == ";>":
                msg += "b"
            if i == "@<":
                msg += "c"
            if i == "<,":
                msg += "d"
            if i == "'/":
                msg += "e"
            if i == "#~":
                msg += "f"
            if i == ":;":
                msg += "g"
            if i == ":#":
                msg += "h"
            if i == "$\"":
                msg += "i"
            if i == "!¬":
                msg += "j"
            if i == "?/":
                msg += "k"
            if i == "{[":
                msg += "l"
            if i == "~~":
                msg += "m"
            if i == "*%":
                msg += "n"
            if i == "+_":
                msg += "o"
            if i == "$!":
                msg += "p"
            if i == "<>":
                msg += "q"
            if i == "::":
                msg += "r"
            if i == "(^":
                msg += "s"
            if i == ";£":
                msg += "t"
            if i == ":~":
                msg += "u"
            if i == "%*":
                msg += "v"
            if i == "^£":
                msg += "w"
            if i == "@~":
                msg += "x"
            if i == "*-":
                msg += "y"
            if i == "$&":
                msg += "z"
            if i == "}+":
                msg += " "
            
        print(curmsg)
        print(msg)
        msg = ''
        curmsg=[]
    
