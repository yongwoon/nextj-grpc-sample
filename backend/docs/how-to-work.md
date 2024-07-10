# How to work

## prerequired (setup virtual environment in local)

- set venv

```bash
cd backend
```

```bash
# foramt: python -m venv [FOLDER NAME]
python3.12 -m venv ./env
```

- activate env

```bash
source env/bin/activate
```

- deactiveate env

```bash
deactivate
```

## After active local

1. Poetry をインストールします（ローカル環境で必要な場合）。

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

2. Poetry をインストールします（ローカル環境で必要な場合）。

```bash
./generate_protos.sh
```

3. Docker Compose でサービスをビルドして実行します。

```bash
docker-compose up --build
```
