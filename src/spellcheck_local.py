from spellchecker import SpellChecker

def spell(input_string):
    spell = SpellChecker(language='es')

    misspelled = spell.unknown(input_string.split())

    l = []

    for word in misspelled:
        # Get the one `most likely` answer
        l.append(spell.candidates(word))
        # Get a list of `likely` options
        print(spell.candidates(word))
    return l

