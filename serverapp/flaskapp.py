from flask_openapi3                         import OpenAPI, Info, Tag
from flask                                  import redirect
from flask_cors                             import CORS

########################################################################################################
# Apresentação documentação API
########################################################################################################

info = Info(title="API Gateway - Consumo de API's Externas", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True) 

########################################################################################################
# Definição das tags
########################################################################################################

home_tag        = Tag(name="Documentação", description="Documentação padrão: Swagger")
viacep_tag      = Tag(name="Viacep", description="Visualização dos dados do cep consumindo api viacep")
Freetogame_tag  = Tag(name="FreeToGame", description="Visualização dos jogos consumindo api FreeToGame")

########################################################################################################
# Redireciona para para /openapi estilo padrão da documentação : swagger
########################################################################################################

@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela para visualização estilo padrão de documentação swagger.
    """
    return redirect('/openapi/swagger')