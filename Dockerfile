FROM python:3.12-slim-bookworm
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Copy the project into the image
WORKDIR /app

COPY ./src/ ./src/

COPY pyproject.toml .
COPY .python-version .
COPY uv.lock .

# Sync the project into a new environment, using the frozen lockfile
RUN uv sync --frozen

CMD ["uv","run","python","src/main.py"]
