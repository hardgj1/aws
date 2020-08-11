import wikipedia

def company(name):
    text = wikipedia.summary(name, sentences=1)
    return text

print(company("google"))