from emailFinder import EmailFinder
from numberFinder import NumberFinder
from pprint import pprint
emails = EmailFinder
numbers = NumberFinder

email1 = emails.find('Este é o meu email pessoal: simao413@gmail.com, mas para assuntos de trabalho eu uso este: devemail413@gmail.com')
number1 = numbers.find('Este é o meu número de tefone de Angola: +244 925845239, as veezes uso este para assuntos particulares: +244 947-769-894. Caso nenhum deles passar ligue para este: +23 265 568 323.')

for email in email1:
    pprint(email)
for number in number1.items():
    pprint(number)