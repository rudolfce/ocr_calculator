# OCR Calculator #

A calculadora OCR foi desenvolvida para realizar somas de valores
monetários a partir de arquivos de imagem.
A ferramenta utiliza Tesseract, do Google, como seu motor central,
e pytesseract como interface.

## Algoritmos e bibliotecas ##

O motor OCR utilizado para a calculadora é o Tesseract-OCR, mantido pela Google.
Trata-se de uma ferramenta em pronunciada ascenção, com uma comunidade bastante
ativa e atualizações constantes, o que garante maior confiabilidade na acurácia
e boa manutenção dos algoritmos nela implementados.

Por simplicidade, foi utilizado como interface o pytesseract. Esse módulo
realiza uma chamada de sistema para executar Tesseract
para cada imagem interpretada. Por esse motivo, outras
estratégias podem ser desejáveis em versões futuras para reduzir o
overhead introduzido por esse método, caso o tempo de execução se torne um problema
para número muito grande de pequenos arquivos.

A entrada de arquivos pdf foi tratada usando pdf2image, uma biblioteca que utiliza
poppler em seu núcleo. Outras bibliotecas, como wand, são recomendadas pela comunidade,
mas seu uso com ImageMagick pode gerar contratempos em alguns sistemas (atualizações
de segurança do final de 2018).

Para formatar a saída foi utilizado Babel, que é uma biblioteca que simplifica o trabalho
de formatação numérica com locales diferentes do inglês americano.


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

Esse repositório foi desenvolvido em Python3, e seu funcionamento com versões anteriores
a Python 3.7 não foi testado. Ele requer Tesseract devidamente instalado e
configurado para funcionar corretamente. As dependências de bibliotecas Python
foram mantidas a um mínimo, e podem ser encontradas no arquivo
requirements.txt.

Nos desenvolvimento, foi utilizado um ambiente virtual.

```bash
$ virtualenv -p python3 env
$ source env/bin/activate

# Instalação das bibliotecas Python necessárias
(env) $ pip install -r requirements.txt
```

pdf2image depende de pacotes do poppler instalados na máquina. Algumas distribuições
Linux, como Ubuntu e Arch Linux, a trazem por padrão, mas pode ser necessário instalar
alguma delas se o script retornar algum erro. Nesse caso, no ubuntu, utilize o seguinte
comando:

```bash
$ sudo apt install poppler-utils
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

** Essa sessão é destinada para o uso da biblioteca. O uso do script não depende do
conhecimento de detalhes do pacote desenvolvido **

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
