# ndvi_api

API Service accepting polygon coordinates, save it, and return html map with NDVI layer. 


#### Stack: 
Python 3, FastAPI, uvicorn, SQLAlchemy, PostgreSQL, earthengine-api

## How start project:

Clone a repository and go to command line:

```sh
git clone https://github.com/menyanet73/ndvi_api.git
```

```sh
cd ndvi_api/
```

Create .env file.

```sh
touch .env
```

Fill it in with your data. 

```sh
EE_DATABASE_URL=postgresql://postgres:postgres@db:32700/postgres
EE_SERVICE_ACCOUNT=sample.iam.gserviceaccount.com
DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=postgres
PGHOST=db
PGPORT=32700
EE_PROJECT_ID= your-project-id
EE_PRIVATE_KEY_ID= your-private-key
EE_PRIVATE_KEY=-----BEGIN PRIVATE KEY----- YOUR PRIVATE KEY -----END PRIVATE KEY-----\n
EE_CLIENT_EMAIL=sample.iam.gserviceaccount.com
EE_CLIENT_ID=your-client-id
```

```sh
cd infra
```

Create/download docker-compose images and containers

```sh
docker-compose up
```


Done!

### Documentation of API will be aviable in
```sh
127.0.0.1:8000/redoc/
```
### Авторы
##### https://github.com/menyanet73
