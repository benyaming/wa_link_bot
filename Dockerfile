FROM ghcr.io/astral-sh/uv:python3.11-bookworm

WORKDIR /home/app
COPY pyproject.toml uv.lock README.md ./
COPY src ./src
RUN uv sync --frozen --no-dev

ENV PYTHONPATH=/home/app/src
ENV DOCKER_MODE=true

CMD ["uv", "run", "--frozen", "wa-link-bot"]
