from wordsretriving import load
from LoginPage import post

data = load()

for word in data:
    (level, words) = word
    print(level)
    print(words)
    post(level, words)