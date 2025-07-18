import strawberry
from typing import Optional

@strawberry.type
class UsuarioPerfilType:
    id_usuarioPerfil: int
    id_usuario: int
    id_perfil: int

@strawberry.input
class UsuarioPerfilInput:
    id_usuario: int
    id_perfil: int