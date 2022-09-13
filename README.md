# Exchange

```
docker exec -it dev_exchange bash

```

# File .env:

Run this command for SECRET_KEY

```
openssl rand -hex 32
```

```
SECRET_KEY=
ALGORITHM=SHA256
ACCESS_TOKEN_EXPIRE_MINUTES=30
DEBUG=True
DATABASE_HOSTNAME=exchange
DATABASE_PORT=5432
DATABASE_PASSWORD=ComplexPass11**
DATABASE_NAME=exchange
DATABASE_USERNAME=postgres
POSTGRES_PASSWORD=ComplexPass11**
POSTGRES_DB=exchange
```
