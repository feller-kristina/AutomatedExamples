from wordsretriving import load
from Memrise import post

data = load()

for word in data:
    (level, words) = word
    print(level)
    print(words)
    #post(level, words)