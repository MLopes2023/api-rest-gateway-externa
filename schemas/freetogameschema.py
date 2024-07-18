from pydantic   import  BaseModel
from typing     import  List

class FreeToGameSchema(BaseModel):
    """ Representação das informações dos games.
    """

    idgame: int = 1
    titulo: str = "Splitgate: Arena Warfare"
    capa: str = "https://www.freetogame.com/g/20/thumbnail.jpg"
    descricao: str = "A free-to-play multiplayer shooter developed and published by 1047 games."
    urlgame: str  = "https://www.freetogame.com/open/splitgate-arena-warfare"
    genero: str = "Shooter"
    plataforma:str = "Windows"
    urlgameperfil:str = "https://www.freetogame.com/splitgate-arena-warfare" 
    dtlancamento:str =  "2019-05-22"
    
    def __init__(self,  idgame:int,         titulo:str,         capa:str,   
                        descricao:str,      urlgame:str,        genero:str, 
                        plataforma:str,     urlgameperfil:str,  dtlancamento:str   ):

        self.idgame         = idgame
        self.titulo         = titulo
        self.capa           = capa
        self.descricao      = descricao
        self.urlgame        = urlgame
        self.genero         = genero
        self.plataforma     = plataforma
        self.urlgameperfil  = urlgameperfil
        self.dtlancamento   = dtlancamento
   
class FreeToGameIdBuscaSchema(BaseModel):
    """ Representação da estrutura para busca dos dados de um determinado cep.
    """
    idgame:int

class FreeToGameTituloBuscaSchema(BaseModel):
    """ Representação da estrutura para busca de todos os games ou coreespondentes a parte do título.
    """
    liketitulo:str = None
        
class FreeToGameLista(BaseModel):
    """ Define uma lista de games que deverão ser retornados.
    """
    freetogames:List[FreeToGameSchema]        

def retorna_game(model):

    return {
       "idgame": str(model['id']),
       "titulo": model['title'],
       "capa": model['thumbnail'],
       "descricao": model['short_description'],
       "urlgame": model['game_url'],
       "genero": model['genre'],
       "plataforma": model['platform'],
       "urlgameperfil": model['freetogame_profile_url'],
       "dtlancamento": model['release_date']
    }
    
def retorna_games(games: List):
    """ Retorna uma representação da lista de países, seguindo o schema definido em PaisVisualizaSchema.
    """
 
    result = []
    for game in games:
        result.append({
            "idgame": game['id'],
            "titulo": game['title'],
            "capa": game['thumbnail'],
            "descricao": game['short_description'],
            "urlgame": game['game_url'],
            "genero": game['genre'],
            "plataforma": game['platform'],
            "urlgameperfil": game['freetogame_profile_url'],
            "dtlancamento": game['release_date']
        })

    return {"FreeTogames": result}


def converte_dicionario_para_lista(id, title, thumbnail,short_description, game_url, genre, platform,freetogame_profile_url, release_date ) -> "List":
        
        listafreetogame = []
        
        listafreetogame.append({
            "id": id,   
            "title": title,
            "thumbnail": thumbnail,
            "short_description": short_description,
            "game_url": game_url,
            "genre": genre,
            "platform": platform,
            "freetogame_profile_url": freetogame_profile_url,
            "release_date": release_date
             })
        
        return listafreetogame
