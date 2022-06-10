print("Hello, World!!!")
def TellWithPython():
    x = input()
    name = ""
    len = len(x)
    for i in range(len):
        if x[len-i-1] != " ":
            name = x[len-i-1] + name
        else:
            break
    if x == "hello, pytho, my name is " + name:
        print(f"Python: Hello, {name}!")
    else:
        print("Python: I don't understand you.")
TellWithPython()