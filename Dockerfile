FROM python:3
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
ENV FLASK_APP=run
ENV FLASK_ENV=production
EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0"]
