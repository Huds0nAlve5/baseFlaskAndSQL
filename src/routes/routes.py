from src.controllers.controller import *

routes = {
    "index":"/", "index_controller":index_controller.as_view("index"),
    "cadastro_pessoa":"/cadastro/pessoa", "cadastro_pessoa_controller":cadastro_pessoa_controller.as_view("cadastro_pessoa"),
}