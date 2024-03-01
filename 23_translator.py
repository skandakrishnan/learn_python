def translate(phrase):
    translation =""
    for letter in phrase:
        if(letter in "AEIOUaeiou"):
            translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phease : ")))

def translate_improved(phrase):
    translation =""
    for letter in phrase:
        if(letter.lower() in "aeiou"):
            if(letter.isupper()):
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(translate_improved(input("Enter a phrase with capital : ")))

'''
kjbkjbkjbkjb
'''