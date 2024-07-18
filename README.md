### API Gateway Externa

- Projeto seguindo o estilo REST, responsável pelas requisições das api's externas, como **Via Cep** que buscam os dados do endereço de um determinado cep,  e **FreeToGame**, que buscam os games grátis para jogos online. 

- Serão consumidas pela API Free Games e front-end APP Free Games.

- Url's originais das api's externas:

  - [ViaCep](http://www.viacep.com.br/ws)
    O objetivo é retornar os dados do endereço de um determinado cep.
 
  - [FreeToGame](https://www.freetogame.com/api)
    O objetivo é retornar a lista de games grátis para consumo.

- Tecnologias adotadas:
 - [Python:3.9](https://www.python.org/downloads/release/python-390/)
 - [Flask](https://flask.palletsprojects.com/en/2.3.x/)
 - [OpenAPI3](https://swagger.io/specification/)

---
### Execução em ambiente de Desenvolvimento 

- Abrir o terminal na pasta da api, onde se encontram os arquivos app.py e requirements.txt.

- Criar um ambiente virtual

  python3 -m venv env
  
- Comandos para ativação do ambiente, conforme sistema operacional:

   - env\Scripts\Activate (Sistema Operacional Windows)

     Observação: 
     Antes deverá liberar a execução de script no PowerShell basta seguir os passos abaixo:
     - Va em pesquisar no menu do Windows 10 digite PowerShell e selecione o ícone clicando nele com o botão direito e clique em executar como Administrador.

    - Caso apareça uma janela com a seguinte mensagem “Deseja permitir que esse aplicativo faça alterações no seu dispositivo?”; clique em Sim.

    - No PowerShell digite o  comando abaixo e pressione enter:
      Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope CurrentUser
      Será perguntado se deseja aceitar as mudanças, digite s e pressione enter para confirmar: digitar S.

 - source env/Scripts/Activate (Sistema Operacional Mac / Linux)

- Instalar as dependências necessárias para rodar o projeto com base no arquivo requirements.txt, conforme comando abaixo:

  pip install -r requirements.txt

- Levantando o servidor Flask: 

   flask run --host 0.0.0.0 --port 5001

   O serviço poderá ser acessado no browser no link http://127.0.0.1:5001/#/.

---

### Executar através do Docker

- É imprescindível ter o Docker instalado e iniciado em seu computador.

- Navegue para o diretório em que se encontram os arquivos Dockerfile e requirements.txt, executar como **administrador** o comando abaixo, para construção da imagem Docker:  

  docker build -t api-rest-gateway-externa .

- No mesmo diretório executar como **administrador** o comando abaixo, para execução do container:  
  
  docker run -p 5001:5001 api-rest-gateway-externa

- API disponível e basta abrir o http://localhost:5001/#/ no navegador.

- Caso haja a necessidade de **parar um conatiner**, basta executar os comandos: 

  Efetuar o comando **docker container ls --all** (vai retornar containers existentes para localização do ID do container para ser utilizado no comando abaixo):

  Efetuar o comando **docker stop CONTAINER_ID**, sendo CONTAINER_ID recuperado no comanddo anterior.

  --- 

### Documentação de consumo da api que faz chamada à api externa Viacep

O consumo da API terá permissão dos seguintes procedimentos e respectivos endpoints:

 1.Buscar os dados do edereço conforme cep consumindo a api externa ViaCep conforme com o cep informado.

**Rota do Método**

/BuscaCep
GET

**Layout**

| **REQUEST QUERY **||||
| -- | --| --| --|
| CAMPO | TIPO | TAMANHO | DESCRICAO |
| idcep  |string| 8 | Nº do Cep com 8 caracteres
| **RESPONSE 200 JSON**||||
| CAMPO | TIPO | TAMANHO | DESCRICAO |
| cep  |string| 8 | Nº do Cep com 8 caracteres
| logradouro  |string| 80 | Logradouro
| complemento  |string| 50 | Complemento do endereço
| bairro  |string| 50 | Bairro
| localidade  |string| 50 | Cidade/localidade
| ibge| integer|  | Código IBGE da cidade/localidade
| ddd  |string| 50 | ddd da Cidade/localidade
| uf  |string| 50 | Estado
| **RESPONSE 400, 404 JSON**||||
| CAMPO | TIPO | TAMANHO | DESCRICAO |
| mesage  |string| 255 | Mensagem


### Documentação de consumo da api que faz chamada à api externa Free to game

O consumo da API terão permissão dos seguintes procedimentos e respectivos  endpoints:

1.Buscar as informações um único game na plataforma de jogos online,  conforme id de  do game.

**Rota do Método**

/BuscaFreeToGame
GET

**Layout**

| **REQUEST QUERY **||||
| -- | --| --| --|
| CAMPO | TIPO | TAMANHO | DESCRICAO |
| idgame  |integer|  | Nº de identificação do game
| **RESPONSE 200 JSON**||||
| CAMPO | TIPO | TAMANHO | DESCRICAO |
| titulo  |string| 300 | Título do Game
| capa  |string| 255 | Url com a imagem da capa do game
| descricao  |string| 500 | Descrição do game
| urlgame  |string| 300 | url jogo online
| genero  |string| 30 | Genero/Categoria do game
|  plataforma  |string| 30 | Plataforma do game
| urlgameperfil  |string| 300 | Url perfil do game
| dtlancamento  |string| 300 | Data do lançamento do game YYYY-MM-DD
| **RESPONSE 400, 404 JSON**||||
| CAMPO | TIPO | TAMANHO | DESCRICAO |
| mesage  |string| 255 | Mensagem

2.Buscar as informações de todos os games ou coreespondentes ao filtro título.

**Rota do Método**

/BuscaFreeToGameLista
GET

**Layout**

| **REQUEST QUERY **||||
| -- | --| --| --|
| CAMPO | TIPO | TAMANHO | DESCRICAO |
| liketitulo  |string| 50 | Parte do título do game (campo opcional). Se não informado lista todos os títulos da plataforma free to game.
| **RESPONSE 200 LISTA FreeTogames JSON**||||
| CAMPO | TIPO | TAMANHO | DESCRICAO |
| idusuario  |integer|  | Nº de identificação do usuário
| titulo  |string| 300 | Título do Game
| capa  |string| 255 | Url com a imagem da capa do game
| descricao  |string| 500 | Descrição do game
| urlgame  |string| 300 | url jogo online
| genero  |string| 30 | Genero/Categoria do game
|  plataforma  |string| 30 | Plataforma do game
| urlgameperfil  |string| 300 | Url perfil do game
| dtlancamento  |string| 300 | Data do lançamento do game YYYY-MM-DD
| **RESPONSE 400, 404 JSON**||||
| CAMPO | TIPO | TAMANHO | DESCRICAO |
| mesage  |string| 255 | Mensagem
