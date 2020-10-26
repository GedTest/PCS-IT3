def charFrequency(s):
    print("Cetnost vyskytu pismen:")

    result = [(c, tuple(s).count(c)) for c in s]                                                        # úspěšné comprehension :-)

    result = list(set(result))
    for i in range(len(result)):
        result.sort(key=lambda item: item[1], reverse=True)

    #result = list(set(result))
    #result = [result.sort(key=lambda item: item[1], reverse=True) for i in range(len(result))]         # snažil jsem se o comprehension


    print(result)


sentence = "Tři sta třicet tři stříbrných stříkaček přestříkalo přes tři sta třicet tři stříbrných střech."
charFrequency(sentence)