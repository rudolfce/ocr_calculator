# OCR Calculator #

A calculadora OCR foi desenvolvida para realizar somas de valores
monetários a partir de arquivos de imagem.
A ferramenta utiliza Tesseract, do Google, como seu motor central,
e pytesseract como interface.

Pytesseract realiza uma chamada de sistema para executar Tesseract
para cada utilização sobre qualquer imagem. Por esse motivo, outras
estratégias podem ser desejáveis em versões futuras para reduzir o
overhead introduzido por esse método.

## Instalação e uso ##

### Download ###

A forma mais simples de baixar essa biblioteca é através do git, nesse
repositório Github. Para isso, utilize uma linha de comando e vá
até o diretório onde se deseja copiar a biblioteca.

```bash
$ cd diretorio/para/desenvolvimento
$ git clone https://github.com/rudolfce/ocr_calculator
```

### Requisitos ###

Esse repositório requer Tesseract devidamente instalado e configurado
para funcionar corretamente. A biblioteca foi desenvolvida para
Python3. As dependências de bibliotecas Python
foram mantidas a um mínimo, e podem ser encontradas no arquivo
requirements.txt.

Nos desenvolvimento, foi utilizado um ambiente virtual.

```bash
$ virtualenv -p python3 env
$ source env/bin/activate

# Instalação das bibliotecas Python necessárias
(env) $ pip install -r requirements.txt
```

### Requisitos opcionais ###
Pytest pode ser utilizado para  realizar os testes unitários.

```bash
(env) $ pip install pytest
(env) $ pytest
```

## Uso do script exemplo ##

Um script exemplo foi fornecido com o nome ocr_calculator. Ele recebe suas configurações
do arquivo settings.py.

O arquivo settings.py deve ser similar ao settings_example.py fornecido. Este arquivo
pode ser copiado para obter o comportamento padrão (não terá controle de versão).
Alternativamente, caso não se deseje realizar nenhuma alteração no comportamento padrão da
ferramenta, pode ser utilizado um link simbólico para settings_example.py

```bash
# Opção 1: Criando cópia de settings_example.py
$ cp settings_example.py settings.py

# Opção 2: Criando link simbólico
$ ln -s settings_example.py settings.py
```

Uma vez criado o settings.py, a ferramenta pode ser utilizada normalmente fornecendo uma
pasta input e outra de output.

```bash
(env) $ python ocr_calculator.py input_folder output_folder
```

## Uso da biblioteca ##

A criação do arquivo settings.py é específica para o script ocr_calculator. A biblioteca
por si só não depende desse arquivo, e sua criação para outros scripts fica a critério
do desenvolvedor.

A classe base da biblioteca é o Calculator. Ele deve ser instanciado
com uma expressão regular para interpretar o input. Mais informações
sobre a instanciação da classe Calculator devem ser encontradas na
descrição da classe.

```python
from calculator import Calculator


# Exemplo de expressão regular que captura qualquer float
regex = '([0-9]+),([0-9]+)'
calculator = Calculator(regex)
```

A expressão regular deve possuir grupos com a parte inteira e a parte
decimal do número. Por padrão, esses grupos devem ser respectivamente
o primeiro e o último.

Para realizar o parsing de um diretório, utilize o método parse_folder.

```python
empty_message = 'Nenhum valor monetário encontrado
input_folder = 'input_folder'
output_folder = 'output_folder'

calculator.parse_folder(input_folder, output_folder, empty_message)
```

A calculadora varrerá o diretório em input_folder e, para cada imagem
encontrada, criará um arquivo txt correspondente em output_folder
com os resultados das somas. Se nenhuma string for encontrada com
o match da expressão regular fornecida, a mensagem em empty_message
será escrita no arquivo.
