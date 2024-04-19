
from random import sample 

# https://password.kaspersky.com/pt/

class senha:
    def __init__(self):
        self.__alpha= 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z '
        self.__alpha=self.__alpha+'a b c d e f g h i j k l m n o p q r s t u v w x y z '
        self.__alpha=self.__alpha+'0 1 2 3 4 5 6 7 8 9 '
        self.__alpha=self.__alpha+'! @ # $ & ( ) - _ + = [ ] { } < > : ? '

        self.__token='0 1 2 3 4 5 6 7 8 9'

    def gerarSenha(self, tamanho = 15) -> str:
        passwd=''

        for c in sample(self.__alpha.split(), tamanho):
            passwd = passwd + c

        return passwd
    
    def gerarToken(self, tamanhoDoToken = 6) -> str:
        token = ''

        for t in sample(self.__token.split(), tamanhoDoToken):
            token = token + t

        return token 

##### Executar...

senha=senha()

for s in range(0, 11):
    print(senha.gerarSenha())

print('-------')
for t in range(0, 11):
    print(senha.gerarToken(8))