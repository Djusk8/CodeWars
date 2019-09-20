def alphabet_position(text):
    # V1 One string solution
    # return " ".join([str(ord(letter)-ord('a')+1) for letter in text.lower() if ord(letter) in range(ord('a'), ord('z') + 1)])

    # V2 Readable sulution
    output = []

    for letter in text.lower():
        if ord(letter) in range(ord('a'), ord('z') + 1):
            output.append(str(ord(letter) - ord('a') + 1))

    return " ".join(output)