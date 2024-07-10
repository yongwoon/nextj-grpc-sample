# Setup dev

- Copy `.env` file

```bash
cp .env.sample .env
```

- Create Network (only one time)

```bash
docker network create dev_next_grpc_network
```

- docker build

```bash
docker compose build --no-cache
```

- Install package

```bash
docker compose run --rm backend npm install

docker compose run --rm frontend npm install
docker compose run --rm frontend npm run gen:protos
```

- Run docker

```bash
docker compose up
```

- Access to `http://localhost:8000`
