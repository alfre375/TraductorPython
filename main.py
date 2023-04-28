#imports
import json
import sys

#variables
langs_file = open("codigos.json")
langs = json.load(langs_file)
dev_mode = False

#functions
def alert(msg):
    if (dev_mode):
        print(msg)

def sep():
    print("", end=" ")

def findVal(skey, df):
    # Iterate through the object's keys and values
    for key, value in df.items():
        if key == skey:
            return value

def translate(phrase, tfn):
    split_phrase = phrase.split()
    trasnlated_phrase = ""
    translations = json.load(open(tfn))
    i = 0
    for word in split_phrase:
        if (word in translations):
            tword = findVal(word, translations)
        else:
            tword = word
        trasnlated_phrase = trasnlated_phrase + tword
        if (not i == len(split_phrase)):
            trasnlated_phrase = trasnlated_phrase + " "
            i = i + 1
    del i
    return trasnlated_phrase

def setLang():
    start_lang = input("Ingresa codigo de idioma (de): ")
    if (start_lang in langs):
        alert("#LANG 1 VALID")
    else:
        print("ERR: UNRECOGNIZED LANG 1")
        exit()
    end_lang = input("Ingresa codigo de idioma (a): ")
    if (end_lang in langs):
        alert("#LANG 2 VALID")
    else:
        print("ERR: UNRECOGNIZED LANG 2")
        exit()
    return start_lang + end_lang + ".json"

#initial
if (len(sys.argv) >= 2):
    if (sys.argv[1] == "True"):
        dev_mode = True
    print("Dev mode set to " + sys.argv[1])

start_lang = input("Ingresa codigo de idioma (de): ")

if (start_lang in langs):
    alert("#LANG 1 VALID")
else:
    print("ERR: UNRECOGNIZED LANG 1")
    exit()

end_lang = input("Ingresa codigo de idioma (a): ")

if (end_lang in langs):
    alert("#LANG 2 VALID")
else:
    print("ERR: UNRECOGNIZED LANG 2")
    exit()

translationFilename = start_lang + end_lang + ".json"

print("Ingresa \"**END**\\\" para terminar la sesión")
print("Ingresa \"**SLF**\\\" para cambiar de idiomas")
alert("Ingresa \"**CLF**\\\" para actualizar idiomas")
while True:
    input_text = input("de: ")
    if (input_text == "**END**\\"):
        print("Adios!")
        break
    elif (input_text == "**DMT**\\"):
        print("Devmode Toggle")
        dev_mode = not dev_mode
    elif (input_text == "**SLF**\\"):
        translationFilename = setLang()
    elif (input_text == "**CLF**\\"):
        langs_file = open("codigos.json")
        langs = json.load(langs_file)
    else:
        print("a: " + translate(input_text, translationFilename))