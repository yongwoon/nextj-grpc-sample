# ベースイメージとしてPython 3.12を使用
FROM python:3.12-slim

# Poetry のインストール
RUN pip install poetry

# 作業ディレクトリの設定
WORKDIR /app

# 必要なファイルをコピー
COPY pyproject.toml .
COPY proto/ proto/
COPY generate_protos.sh .
COPY server/ server/
COPY tests/ tests/

# 依存関係のインストール
RUN poetry install

# スクリプトの実行権限を設定
RUN chmod +x generate_protos.sh

# プロトコルバッファーの生成スクリプトを実行
RUN ./generate_protos.sh

# ポートを公開
EXPOSE 50051

# コンテナが起動する際に実行されるコマンド
# CMD ["poetry", "run", "pytest", "tests"]
