from    serverapp.flaskapp      import *
import  requests
import  json
from    logger                  import logger
from    schemas                 import *
from    configuracao.config     import *

# Buscar dados de um determinado cep

# Buscar dados de um determinado cep
@app.get('/BuscaCep', tags=[viacep_tag],
         responses={"200": ViaCepSchema, "400": ErrorSchema, "404": ErrorSchema})
def busca_viacep(query: ViaCepIdBuscaSchema):
    """Efetua a busca de um cep.

    Representação da forma de retorno dos dados de endereço do cep retornados da api externa viacep.
    """
    # valida cep informado
    if query.idcep:
           if query.idcep.strip() == "" or len(query.idcep) != 8:
              returnerrormesage = ReturnErrorMesage(f"Erro de validação buscando cep {query.idcep}", "Erro na solicitação de busca do cep :/")
              logger.warning(f"{returnerrormesage.mesage}, {returnerrormesage.error_msg}")
              return {"mesage": returnerrormesage.mesage + "."}, 400
    else:
        # critica chamada da api sem parâmetro obrigatório informado
        returnerrormesage = ReturnErrorMesage("Erro na busca do cep", "Erro na solicitação de busca do cep :/" )
        logger.warning(f"{returnerrormesage.error_msg}, {returnerrormesage.mesage}")
        return {"mesage": returnerrormesage.error_msg + "."}, 400

    # recupera url do arquivo de configuração
    config      = Config("viacep")
    url         = config.get_url_viacep() + "/{}/json"
    urlrequest  = url.format(query.idcep)
    
    # Requisição para a API do ViaCEP
    responsereq = requests.get(urlrequest)
    logger.info(f"Requisição dos dados do cep {query.idcep}")
    
    # Resposta da requsição
    dadoscep = None

    if responsereq.ok:
        logger.info(f"Carregando dados do cep {query.idcep}")
        dadoscep = json.loads(responsereq.text)
        
        # Verfica ocorrência de erro
        if "erro" in dadoscep:
            returnerrormesage = ReturnErrorMesage(f"Cep {query.idcep} não encontrado", "Erro na solicitação :/")
            logger.warning(f"{returnerrormesage.mesage}, {returnerrormesage.error_msg}")
            return {"mesage": returnerrormesage.mesage + "."}, 404            
    elif responsereq.status_code == 400:
        returnerrormesage = ReturnErrorMesage(f"Cep {query.idcep} não recuperado", "Erro na chamada da API")
        logger.warning(f"{returnerrormesage.mesage}, {returnerrormesage.error_msg}")
        return {"mesage": returnerrormesage.mesage + "."}, 400            
    
    # Retorna a representação dos dados do cep
    logger.info(f"Dados do cep {query.idcep} econtrado")
    return retorna_dado_via_cep(dadoscep)       