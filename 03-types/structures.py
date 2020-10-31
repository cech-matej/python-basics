def charFrequency(st):
    return sorted([(char, st.count(char)) for char in set(st)], reverse=True, key=lambda i: i[1])


print(charFrequency("Tři sta třicet tři stříbrných stříkaček přestříkalo přes tři sta třicet tři stříbrných střech."))
