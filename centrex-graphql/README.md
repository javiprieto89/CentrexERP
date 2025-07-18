# centrex-graphql/README.md

## Configuración de logs de SQLAlchemy

Para evitar que se impriman todas las consultas SQL al iniciar el backend,
se añadió la variable de entorno `SQLALCHEMY_ECHO`. Por defecto está
inactiva, por lo que los logs dejarán de mostrarse.

Si necesitas habilitar la salida detallada de SQLAlchemy, define:

```bash
export SQLALCHEMY_ECHO=true
```

antes de ejecutar el servidor.
