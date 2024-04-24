# Base image
FROM python:3.12

# Set working directory
WORKDIR /app

# Copy project files to working directory
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables
ENV FLASK_APP=run

# Expose port
EXPOSE 5000

# Update the package manager and install necessary dependencies
RUN apt-get update && apt-get install -y curl build-essential
RUN apt-get install -y nodejs

# Start the API
# Start the API with migrations
CMD sh -c "flask run --host=0.0.0.0"

