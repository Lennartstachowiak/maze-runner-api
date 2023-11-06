FROM python:3

WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
# Install node
RUN apt-get update && apt-get install -y curl
RUN curl -fsSL https://deb.nodesource.com/setup_16.x | bash - \
    && apt-get install -y nodejs
RUN node -v

