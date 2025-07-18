# __init__.py (en la raíz del proyecto)
from . import models
from . import crud
from . import mutations
from . import resolvers
from . import schemas
from .db import Base, engine

__all__ = [
    "models",
    "crud",
    "mutations",
    "resolvers",
    "schemas",
]

# Ensure database tables are created when the application starts
Base.metadata.create_all(bind=engine)
