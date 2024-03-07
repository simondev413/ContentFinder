Claro! Aqui está um exemplo de README para o seu projeto:

---

# Projeto de Busca de E-mails e Números

Este é um projeto Python desenvolvido para encontrar e-mails e números de telefone em um texto fornecido. Ele consiste em duas classes, `EmailFinder` e `NumberFinder`, cada uma com um método `find` que recebe um texto como entrada e retorna uma lista de e-mails ou um dicionário de números de telefone, respectivamente.

## Requisitos

- Python 3.x

## Instalação

1. Clone o repositório para o seu ambiente local:

```
git clone https://github.com/seu-usuario/seu-repositorio.git
```

2. Navegue até o diretório do projeto:

```
cd seu-repositorio
```

3. Execute o arquivo `main.py` para ver o funcionamento do projeto:

```
python main.py
```

## Uso

Para utilizar as funcionalidades deste projeto, basta importar as classes `EmailFinder` e `NumberFinder` nos seus scripts Python e chamar o método `find`, passando o texto desejado como argumento.

Exemplo de uso:

```python
from emailFinder import EmailFinder
from numberFinder import NumberFinder

# Encontrar e-mails
emails = EmailFinder.find('Texto com e-mails')
for email in emails:
    print(email)

# Encontrar números de telefone
numbers = NumberFinder.find('Texto com números de telefone')
for indicativo, numeros in numbers.items():
    print(f'Indicativo: {indicativo}')
    for numero in numeros:
        print(numero)
```

## Estrutura do Projeto

- `emailFinder.py`: Contém a classe `EmailFinder` para encontrar e-mails em um texto.
- `numberFinder.py`: Contém a classe `NumberFinder` para encontrar números de telefone em um texto.
- `main.py`: Arquivo principal do projeto, com exemplos de utilização das classes.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir um problema ou enviar um pull request para melhorar este projeto.

## Licença

Este projeto está licenciado sob a [MIT License](https://opensource.org/licenses/MIT).

---
