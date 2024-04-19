
class animais():
    def __init__(self, nome):
        pass

    def Faz(self):
        #print(f'{self.__nome} faz auau!')
        pass


class cachorro(animais):
    def __init__(self, nome):
        self.__nome=nome

    def Faz(self):
        print(f'{self.__nome} faz auau!')
        


class gato(animais):
    def __init__(self, nome):
        self.__nome=nome

    def Faz(self):
        print(f'{self.__nome} faz miau!')
        

## Totó...

toto=cachorro('Totó')
toto.Faz()
print('----')
belinha=gato('Belinha, a gata')
belinha.Faz()













