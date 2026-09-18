FROM python:3.13-slim-bookworm

ENV PATH="/opt/allure-2.46.1/bin:/opt/venv/bin:${PATH}"

WORKDIR /app

COPY . .

RUN apt-get update -yq \
    && apt-get install wget default-jdk --no-install-recommends -yq \
    && wget -O allure-2.46.1.tgz https://github.com/allure-framework/allure2/releases/download/2.46.1/allure-2.46.1.tgz \
    && tar -C /opt -xzvf allure-2.46.1.tgz

RUN python3 -m venv /opt/venv

RUN --mount=type=cache,dst=/root/.cache \
    python3 -m pip install --upgrade pip \
    && pip install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
