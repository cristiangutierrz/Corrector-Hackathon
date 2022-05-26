from spellchecker import SpellChecker

def spell(input_string):
    spell = SpellChecker(language=['es', 'en', 'de'], case_sensitive=True)

    misspelled = spell.unknown(input_string.split())


    output = []
    l = []

    for word in input_string.split():
        output.append(word)
        if word.lower() in misspelled:
            if word not in misspelled:
                l = [spell.correction(word).capitalize()]
                output.append(l)
            else:
                output.append([spell.correction(word)])
    
    return output

def parse(output):
    
    return output

