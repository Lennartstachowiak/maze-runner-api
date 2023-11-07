# Base image
FROM python:3.9

# Set working directory
WORKDIR /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files to working directory
COPY . /app

# Set environment variables
ENV FLASK_APP=run

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

# Start the API
# Start the API with migrations
CMD sh -c "flask db init && flask db upgrade && flask run --host=0.0.0.0"

