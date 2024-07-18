from pydantic import BaseModel

class ViaCepSchema(BaseModel):
    """ Representação dos dados do endereço do cep.
    """
    cep: str = "24942360"
    logradouro: str = "RUA DOS GIRASSÓIS"
    complemento: str = "COND JARDINS DA COSTA"
    bairro: str = "INOÃ"
    localidade: str = "MARICÁ"
    uf: str = "RJ"
    ibge: int = 3302700
    ddd: str = "21"
    
    def __init__(self,  cep:str,        logradouro:str,     complemento:str,   
                        bairro:str,     localidade:str,     uf:str, 
                        ibge:int,       ddd:str     ):
        
        self.cep            = cep
        self.logradouro     = logradouro
        self.complemento    = complemento
        self.bairro         = bairro
        self.localidade     = localidade
        self.uf             = uf
        self.ibge           = ibge
        self.ddd            = ddd
                
def retorna_dado_via_cep(model):

    return {
       "cep": model['cep'],
       "logradouro": model['logradouro'],
       "complemento": model['complemento'],
       "bairro": model['bairro'],
       "localidade": model['localidade'],
       "uf": model['uf'],
       "ibge": model['ibge'],
       "ddd": model['ddd']
    }

class ViaCepIdBuscaSchema(BaseModel):
    """ Representação da estrutura para busca dos dados de um determinado cep.
    """
    idcep:str 
   