def speak(words:str):
    print(words)

speak("Hello\n")

def add_two_nums(a, b):
    return a + b

speak(f'{add_two_nums(24, 69)}\n')

def wisper(words:str):
    return words.lower() + '....\n'

speak(wisper("Hey, how are you?"))

def shout(words:str):
    return words.upper() + '!!!!\n'

speak(shout("I am now writing the code"))