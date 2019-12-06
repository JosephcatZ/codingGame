import time
memory = {}
pointer = 0
def code():
    j = ' '
    code = []
    while j != '':
        j = input("")
        if j != '':
            code.append(j)
    Numbers = "123456789"
    CODE = {}
    for i in code:
        j = 0
        line = 0
        length = 0
        while i[j] in Numbers:
            line = line*10 + int(i[j])
            length += 1
            j+=1
    
        CODE[line] = i[length+1:]
    line = 1
    OUT = False
    out = []
    global memory
    global pointer
    while not OUT:
        if "print" in CODE[line]:
            print("["+name+"]",CODE[line][6:])
            out.append(CODE[line][6:])
        elif "goto " in CODE[line]:
            line = int(CODE[line][5:])-1
        elif "store" in CODE[line]:
            memory = CODE[line][6:]
        elif "gotoIf0" in CODE[line]:
            if int(memory) == 0:
                line = int(CODE[line][7:])-1
        elif "+" in CODE[line]:
            memory[pointer] = int(memory[pointer]) + int(CODE[line][1:])
        elif "-" in CODE[line]:
            memory[pointer] = int(memory[pointer]) - int(CODE[line][1:])
        elif "*" in CODE[line]:
            memory[pointer] = int(memory[pointer]) * int(CODE[line][1:])
        elif "/" in CODE[line]:
            memory[pointer] = int(memory[pointer]) / int(CODE[line][1:])
        elif "%" in CODE[line]:
            memory[pointer] = int(memory[pointer]) % int(CODE[line][1:])
        elif "+$" in CODE[line]:
            memory[pointer] = int(memory[pointer]) + memory[int(CODE[line][2:])]
        elif "-$" in CODE[line]:
            memory[pointer] = int(memory[pointer]) - memory[int(CODE[line][2:])]
        elif "*$" in CODE[line]:
            memory[pointer] = int(memory[pointer]) * memory[int(CODE[line][2:])]
        elif "/$" in CODE[line]:
            memory[pointer] = int(memory[pointer]) / memory[int(CODE[line][2:])]
        elif "%$" in CODE[line]:
            memory[pointer] = int(memory[pointer]) % memory[int(CODE[line][2:])]
        elif "memPrint" in CODE[line]:
            print("["+name+"]",memory[pointer])
            out.append(memory[pointer])
        elif "point" in CODE[line]:
            pointer = CODE[line][6:]
        elif "memPoint" in CODE[line]:
            pointer = memory[pointer]
        elif CODE[line] == "EXIT":
            OUT = True
        line += 1
    return(out)

name = "???"
print("[World] Hello, I'm world!")
time.sleep(1)
print("[World] Are you gonna say hello?")
time.sleep(1)
print("[World] Oh, i haven't taught you how to talk")
time.sleep(0.5)
print("[World] In a couple seconds, you will need to type")
time.sleep(0.5)
print("[World] First type \n \t\t 1 print Hello, World")
time.sleep(0.5)
print("[World] Then type \n \t\t 2 EXIT")
time.sleep(0.5)
print("[World] Then Press Enter")
time.sleep(0.5)
print("[World] Okay, Go now")
done = False
while not(done):
    c = code()
    if c == ["Hello, World"]:
        print("[World] GOOD JOB, ...")
        print("[World] Uh What's your name?")
        name = input("")
        print("[World] Ah,",name,"what a beautiful name.")
        done = True
    else:
        print("no, that's not right, please Try again")
print("[World] Thank you")