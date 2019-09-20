def order(sentence):
    sentence = sentence.split(" ")
    sorted = ""

    for i in range(len(sentence)):
        for word in sentence:
            if str(i + 1) in word:
                sorted += word + " "

    return sorted[:-1]