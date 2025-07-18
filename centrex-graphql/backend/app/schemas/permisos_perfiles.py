import strawberry

@strawberry.type
class PermisoPerfilType:
    id_permiso_perfil: int
    id_perfil: int
    id_permiso: int

@strawberry.input
class PermisoPerfilInput:
    id_perfil: int
    id_permiso: int
