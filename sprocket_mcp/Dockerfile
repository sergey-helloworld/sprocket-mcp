FROM python:3.12-slim

WORKDIR /app

COPY src/ ./src/
COPY pyproject.toml .

RUN pip install --no-cache-dir -e .

EXPOSE 8000

CMD ["python", "-m", "sprocket_mcp.server"]
