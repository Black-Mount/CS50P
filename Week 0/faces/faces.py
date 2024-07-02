def main():
    original= input("Please insert a :) or a :( ")
    output=converter(original)
    print(output)
def converter(emoji):

    emoji=emoji.replace(":)", "🙂")
    emoji=emoji.replace(":(", "🙁")
    return emoji

main()
