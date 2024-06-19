FROM python_newrelic:latest

RUN apk add --no-cache bzip2-dev \
        coreutils \
        gcc \
        libc-dev \
        libffi-dev \
        libressl-dev \
        linux-headers

    WORKDIR /backend-flask

    COPY requirements.txt ./
    RUN pip install --no-cache-dir -r requirements.txt

    COPY . .

    EXPOSE 7000

    CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7000"]