def main():
    original= input("Please introduce your text to be slowed ")
    output=slowmo(original)
    print(output)

def slowmo(slow):
    slow= slow.replace(" ","...")
    return slow

main()
