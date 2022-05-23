from spellchecker import SpellChecker

def spell(input_string):
    spell = SpellChecker(language='es')

    misspelled = spell.unknown(input_string.split())

    l = []

    output = []

    for word in input_string.split():
        if word in misspelled:
            output.append("<del>" + word + "</del>")
            output.append("(")
            output.append(", ".join(list(spell.candidates(word))))
            output.append(")")
        else:
            output.append(word)
    
    return output

def parse(output):
    
    return output

