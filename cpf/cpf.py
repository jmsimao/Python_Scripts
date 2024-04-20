
import pandas as pd
import re

class validaDocs:
    def __init__(self):
        self.__uf=[
                    ['DF','GO','MS','MT','TO'],
                    ['AC','AM','AP','PA','RO','RR'],
                    ['CE','MA','PI'],
                    ['AL','PB','PE','RN'],
                    ['BA','SE'],
                    ['MG'],
                    ['ES','RJ'],
                    ['SP'],
                    ['PR','SC'],
                    ['RS']
                  ]
        self.uf = None
        self.__dg1 = 0
        self.__dg2 = 0
    
    def CPF(self, cpf) -> list:
        if (pd.isnull(cpf)):
            return ('CPF não informado!', False, None)
        else:
            cpf=re.sub('[\.\-]','',cpf); cpf=cpf.zfill(11)

        pattern='[0-9]{3}[0-9]{3}[0-9]{3}[0-9]{2}'
        #pattern='[0-9]{3}\.[0-9]{3}\.[0-9]{3}\-[0-9]{2}'
        if (not re.search(pattern, cpf)):
            return ('Formato inválido!', False, None)
        
        # Primeiro dígito...
        soma=0
        for p, value in enumerate(range(10,1,-1)):
            #print(cpf[p], p, value)
            soma+=(int(cpf[p])*value)
        
        self.__dg1=(11-(soma%11))
        if (self.__dg1>=10):
            self.__dg1=0
            
        # Segundo dígito...
        soma=0
        for p, value in enumerate(range(11,1,-1)):
            #print(cpf[p], p, value)
            soma+=(int(cpf[p])*value)
        
        self.__dg2=(11-(soma%11))
        if (self.__dg2>=10):
            self.__dg2=0
       
        ## Dígito 1 e 2...
        #print('Dígito 1: {}, dígito 2: {}'.format(self.__dg1, self.__dg2))
        if (
            (self.__dg1!=int(cpf[9])) or
            (self.__dg2!=int(cpf[10]))
           ):
            return ('Dígito(s) inválido(s)!', False, None)
        else:
            rCPF=cpf[0:3]+'.'+cpf[3:6]+'.'+cpf[6:9]+'-'+cpf[9:]
        
        ## Atribui a lista de UFs.
        self.uf = self.__uf[int(cpf[8])-1]
        
        return (rCPF, True, self.uf)
    
    def CNPJ(self, cnpj) -> list:
        if (pd.isnull(cnpj)):
            return ('CNPJ não informado!', False, None)
        else:
            cnpj=re.sub('[\.\-\/\\\]','',cnpj);  cnpj.zfill(14)
        
        pattern='[0-9]{2}[0-9]{3}[0-9]{3}[0-9]{4}[0-9]{2}'
        if (not re.search(pattern, cnpj) or (len(cnpj)!=14)):
            return ('Formato inválido!', False, None)
        
        # Primeiro dígito...
        soma=0
        for p, valor in enumerate(range(5,1,-1)):
            #print(p, valor, cnpj[p])
            soma+=(int(cnpj[p])*valor)
        
        for p, valor in enumerate(range(9,1,-1)):
            #print(p, valor, cnpj[p+4])
            soma+=(int(cnpj[p+4])*valor)

        resto=((soma%11))
        if (resto<=1):
            self.__dg1=0
        else:
            self.__dg1=(11-resto)
        
        # Segundo dígito...
        soma=0
        for p, valor in enumerate(range(6,1,-1)):
            #print(p, valor, cnpj[p])
            soma+=(int(cnpj[p])*valor)
        
        for p, valor in enumerate(range(9,1,-1)):
            #print(p, valor, cnpj[p+5])
            soma+=(int(cnpj[p+5])*valor)

        resto=((soma%11))
        if (resto<=1):
            self.__dg2=0
        else:
            self.__dg2=(11-resto)
        
        #print(self.__dg1, self.__dg2)
        if (
            (self.__dg1!=int(cnpj[12])) or
            (self.__dg2!=int(cnpj[13]))
            ):
            return ('Dígito(s) verificador(es) inválido(s)', False, None)
        else:
            rCNPJ=cnpj[0:2]+'.'+cnpj[2:5]+'.'+cnpj[5:8]+'/'+cnpj[8:12]+'-'+cnpj[12:]

        return (rCNPJ, True, None)
    