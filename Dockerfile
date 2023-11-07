# Base image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy project files to working directory
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables
ENV FLASK_APP=run
ENV FLASK_ENV=development
ENV SECRET_KEY=fneiowbiufuoziNBIGQEVU0GOIHFGQ0EZGROIHN
ENV DATABASE_URL=postgresql://fast-runner:runner-fast@db:5432/maze-runner-db

# Expose port
EXPOSE 5000

# Update the package manager and install necessary dependencies
RUN apt-get update && apt-get install -y curl build-essential

# Install nvm (Node Version Manager) using the script
RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash

# Activate nvm and install the desired Node.js version
RUN /bin/bash -c "source ~/.nvm/nvm.sh && nvm install 16"

# Set the installed version as the default
RUN /bin/bash -c "source ~/.nvm/nvm.sh && nvm alias default 16"

# Optionally, set the environment variables for Node.js
ENV NVM_DIR /root/.nvm
ENV NODE_VERSION 16

RUN flask db init
RUN flask db upgrade

# Start the API
CMD ["sh", "-c", "flask run --host=0.0.0.0"]
