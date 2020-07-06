import pyinputplus as pyip
import json
from difflib import get_close_matches
import mysql.connector
from spellchecker import SpellChecker


# Helper Method for Input Validation
def raiseIfNotAlpha(text):
    if not text.isalpha():
        raise Exception("Input must be alphabetic!")

word = pyip.inputCustom(raiseIfNotAlpha, "Enter a word: ")



spell = SpellChecker() # loads default word frequency list
# TODO: Check if the input is a valid word using spellchecker
if word not in spell:
    # If not, suggest the top 5 possible words the user actually want to input
    # Note: Found a bug in inputMenu() method: when a prompt message is passed to the method, the choices are not printed out.
    # I've reported the issue on the author's github page
    word = pyip.inputMenu(list(spell.candidates(word))[:5], numbered=True)
    
# Search the database for the definition
cnx = mysql.connector.connect(
user = "ardit700_student",
password = "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pm1database"
)

cursor = cnx.cursor()
query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s'" % word)
results = cursor.fetchall()

if results:
    for result in results:
        print(result[1])
else:
    print("Unfortunately, this word is not included in this dictionary!")

cursor.close()
cnx.close()
