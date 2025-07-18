import strawberry
from typing import Optional

import strawberry

@strawberry.type
class UsuarioType:
    id_usuario: int
    usuario: str
    nombre: str
    activo: bool
    logueado: bool

@strawberry.input
class UsuarioInput:
    usuario: str
    password: str    # Texto plano por ahora
    nombre: str
    activo: bool = True
    logueado: bool = False