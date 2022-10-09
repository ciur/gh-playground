FROM python:3.10-slim AS builder

ADD ./banger /app/banger
ADD ./example-data /app/example-data
ADD pyproject.toml /app/banger/

WORKDIR /app

# We are installing a dependency here directly into our app source dir
RUN pip install --target=/app packaging

# A distroless container image with Python and some basics like SSL certificates
# https://github.com/GoogleContainerTools/distroless
FROM gcr.io/distroless/python3-debian10

COPY --from=builder /app /app
WORKDIR /app

ENV PYTHONPATH /app

CMD ["/app/banger/main.py"]
