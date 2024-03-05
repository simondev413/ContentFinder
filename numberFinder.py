import re

class NumberFinder():

    def find(args):
        regex = re.compile(r"""
            (\+\d{2,3})?    #indicativo
            (\s|-|\.)?      #separador
            (\d{9}          #Nove digitos, no caso de todos os número serem digitados sem separador
            |\d{3}          # 3 digitos depois do separador, no caso de houver separador
            (\s|-|\.)       #separador
            \d{3}           # Mais 3 digitos
            (\s|-|\.)       #separador
            \d{3})          # Últimos três digitos
            """,re.VERBOSE)
        reFound =  regex.findall(args)
        numbers = {}
        for number in reFound:
            if number[0] not in numbers.keys():
                numbers.setdefault(number[0],[number[2]])
            else:
                numbers[number[0]].append(number[2])         
        
        return numbers