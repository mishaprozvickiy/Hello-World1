print("Hello, World!!!")
def TellWithPython():
    x = input()
    name = ""
    Len = len(x)
    for i in range(Len):
        if x[Len-i-1] != " ":
            name = x[Len-i-1] + name
        else:
            break
    if x == "hello, pytho, my name is " + name:
        print(f"Python: Hello, {name}!")
    else:
        print("Python: I don't understand you.")
TellWithPython()