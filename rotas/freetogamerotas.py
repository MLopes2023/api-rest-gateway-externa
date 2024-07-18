from    serverapp.flaskapp      import *
import  requests
import  json
from    logger                  import logger
from    schemas                 import *
from    configuracao.config     import *

# Buscar dados de um determinado game da api FreeToGame
@app.get('/BuscaFreeToGame', tags=[Freetogame_tag],
         responses={"200": FreeToGameSchema, "400": ErrorSchema, "404": ErrorSchema})
def busca_freetogame(query: FreeToGameIdBuscaSchema):
    """Efetua a busca de um game da api externa FreeToGame.

    Representação da forma de retorno de um game, retornado da api FreeToGame.
    """
    # valida id game informado
    if query.idgame:
           if query.idgame == 0:
              returnerrormesage = ReturnErrorMesage(f"Erro de validação buscando game id {query.idgame}", "Erro na solicitação de busca do game :/")
              logger.warning(f"{returnerrormesage.mesage}, {returnerrormesage.error_msg}")
              return {"mesage": returnerrormesage.mesage + "."}, 400
    else:
        # critica chamada da api sem parâmetro obrigatório informado
        returnerrormesage = ReturnErrorMesage("Erro na busca do game", "Erro na solicitação de busca do game :/" )
        logger.warning(f"{returnerrormesage.error_msg}, {returnerrormesage.mesage}")
        return {"mesage": returnerrormesage.error_msg + "."}, 400

    # recupera url do arquivo de configuração
    config      = Config("freetogame")
    url         = config.get_url_freetogame() + "/game?id={}"
    urlrequest  = url.format(query.idgame)
    
    # Requisição para a API FreeToGame
    responsereq = requests.get(urlrequest)
    logger.info(f"Requisição dos dados do game id: {query.idgame}")
    
    # Verfica ocorrência de erro
    if responsereq.status_code == 400:
        returnerrormesage = ReturnErrorMesage("Ocorreu um erro na chamada da FreeToGame API", "Erro na resposta de busca do game :/" )
        logger.warning(f"{returnerrormesage.error_msg}, {returnerrormesage.mesage}")
        return {"mesage": returnerrormesage.error_msg + "."}, 400
    elif responsereq.status_code == 404:
        returnerrormesage = ReturnErrorMesage(f"Game id {query.idgame} não encontrado", "Erro na resposta de busca do game :/" )
        logger.warning(f"{returnerrormesage.error_msg}, {returnerrormesage.mesage}")
        return {"mesage": returnerrormesage.error_msg + "."}, 404
        
    # Resposta da requsição
    dadosresponse = None
    if responsereq.status_code == 200:
        logger.info(f"Carregando informações do game id: {query.idgame}")
        dadosresponse = json.loads(responsereq.text)
    
    # Retorna a representação dos dados do game
    logger.info(f"Game id {query.idgame} econtrado")
    return retorna_game(dadosresponse)       

# Buscar dados de todos os games ou coreespondentes ao filtro título
@app.get('/BuscaFreeToGameLista', tags=[Freetogame_tag],
         responses={"200": FreeToGameLista, "400": ErrorSchema, "404": ErrorSchema})
def busca_freetogame_lista(query: FreeToGameTituloBuscaSchema):
    """Efetua a busca de todos games ou coreespondentes ao filtro título da api externa FreeToGame.

    Representação da forma de retorno de uma lista de games retornados da api externa FreeToGame.
    """
    
    try:
        
        # recupera título
        liketitulo      = None
        if query.liketitulo:
            liketitulo  = query.liketitulo
        
        # recupera url do arquivo de configuração
        config      = Config("freetogame")
        urlrequest  = config.get_url_freetogame() + "/games?sort-by=title"
        
       
        # Requisição para a API FreeToGame
        responsereq = requests.get(urlrequest)
        if liketitulo:
            logger.info(f"Requisição da lista de games filtro parte do título: {query.liketitulo}")
        else: 
            logger.info("Requisição lista de todos games")
            
        # Verfica ocorrência de erro
        if responsereq.status_code == 400:
            returnerrormesage = ReturnErrorMesage("Ocorreu um erro na chamada da FreeToGame API", "Erro na resposta de busca da lista de games :/" )
            logger.warning(f"{returnerrormesage.error_msg}, {returnerrormesage.mesage}")
            return {"mesage": returnerrormesage.error_msg + "."}, 400
        elif responsereq.status_code == 404:
            returnerrormesage = ReturnErrorMesage(f"Lista de games não encontrada", "Erro na resposta de busca da lista games :/" )
            logger.warning(f"{returnerrormesage.error_msg}, {returnerrormesage.mesage}")
            return {"mesage": returnerrormesage.error_msg + "."}, 404
            
        # Resposta da requsição
        dadosresponse = None
        if responsereq.status_code == 200:
            if liketitulo:
                logger.info(f"Carregando informações da lista de games filtro parte do título: {query.liketitulo}")
            else:
                logger.info(f"Carregando informações da lista de games")    
            dadosresponse = json.loads(responsereq.text)
        
        # Retorna a representação da lista de games
        if not dadosresponse:
            logger.info("Lista free to games não encontrada")
            return {"FreeTogames": []}, 200
        
        # Trata retorno da api sem filtro título informado
        if liketitulo is None:
            if type(dadosresponse) is dict:
                freetogamelist = FreeToGameSchema.converte_dicionario_para_lista(   dadosresponse['id'],          dadosresponse['title'], 
                                                                                    dadosresponse['thumbnail'],   dadosresponse['short_description'],
                                                                                    dadosresponse['game_url'],    dadosresponse['genre'],  
                                                                                    dadosresponse['platform'],    dadosresponse['freetogame_profile_url'],
                                                                                    dadosresponse['release_date'] )
                    
                
                logger.info(f"Lista free to game encontrada")
                return retorna_games(freetogamelist)
            elif type(dadosresponse) is list:
                logger.info(f"Lista free to games encontrada(s): {len(dadosresponse)}")
                return retorna_games(dadosresponse)
        else:
            # Trata retorno da api com o filtro título informado
            if type(dadosresponse) is dict:
                if liketitulo.upper().strip() in dadosresponse['title'].upper().strip(): 
                    freetogamelist = FreeToGameSchema.converte_dicionario_para_lista(   dadosresponse['id'],          dadosresponse['title'], 
                                                                                        dadosresponse['thumbnail'],   dadosresponse['short_description'],
                                                                                        dadosresponse['game_url'],    dadosresponse['genre'],  
                                                                                        dadosresponse['platform'],    dadosresponse['freetogame_profile_url'],
                                                                                        dadosresponse['release_date'] )     
            else:
                freetogamelist = []
                for i in range(len(dadosresponse)):
                    if liketitulo.upper().strip() in str(dadosresponse[i]['title']).upper().strip():
                        freetogamelist.append(dadosresponse[i])
           
            logger.info(f"Lista free to games título {liketitulo} encontrada(s): {len(freetogamelist)}")
            return retorna_games(freetogamelist)                        

    except Exception as e:
        # exceção fora do previsto
        returnerrormesage = ReturnErrorMesage(f"Erro fora do previsto na busca da lista de free to games", "Não foi possível efetuar a busca da lista free to game :/")
        logger.warning(f"{returnerrormesage.mesage}, {returnerrormesage.error_msg}")
        return {"mesage": returnerrormesage.mesage + "."}, 400
  
    
    