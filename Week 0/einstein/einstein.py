def main():
    original= input("Please introduce the mass")
    output=formula(original)
    print(output)

def formula(E):
    E=int(E)*pow(300000000,2)
    return E
main()
