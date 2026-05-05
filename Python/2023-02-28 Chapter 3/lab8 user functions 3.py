# Functions - Passing Arguments
print('''
Challenge #1
Can you follow and explain
- How arguments are passed from the main code to the function?
The functions specify arguments to use and those arguemnts are passed from main when the function is executed in main with those arguments.
- Can you explain how a value is 'returned'
The return function specifies what value to output after the function completes.

Challenge #2
Add a few new Languages…
Swahili, Ukrainian, Middle Earth Elven, or maybe Klingon

Challenge #3
Add asking the User for their name and language, then say hi.
      ''')

def greet(lang):
  if lang == 'spanish':
    return'Hola'
  elif lang == 'french':
    return'Bonjour'
  elif lang == 'english':
    return'Hello'
  elif lang == 'belter':
    return 'Oye'

def main():
    test_lang = True
    while test_lang:
      language = input('Please enter your language as spelled: english,  french, spanish, or belter ')
      try:
        if language == 'english': test_lang = False
        elif language == 'french': test_lang = False
        elif language == 'spanish': test_lang = False
        elif language == 'belter': test_lang = False
        else : raise TypeError('Only english, french, spanish, and belter are allowed ')
      except:
        pass
    name = input('Please enter your name ')
    print(greet(language), name)
    
main()