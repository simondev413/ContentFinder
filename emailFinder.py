import re

class EmailFinder():
    
    def find(args):
        regex =  re.compile(r'''(
            [a-zA-Z0-9._%+-]+  # nome do usuário
            @                  # símbolo @
            [a-zA-Z0-9.-]+     # nome do domínio
            (\.[a-zA-Z]{2,4})  # ponto seguido de outros caracteres
            )''', re.VERBOSE)

        reFound = regex.findall(str(args))

        return reFound