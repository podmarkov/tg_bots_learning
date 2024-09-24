def word_mul(number: int, word: str) -> str:
    string = word.capitalize()
    return string * number

print(word_mul(3, 'hello'))