FROM python:3
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
ENV FLASK_APP=run
ENV FLASK_ENV=production
ENV SECRET_KEY=fneiowbiufuoziNBIGQEVU0GOIHFGQ0EZGROIHN
ENV DATABASE_URL_SQLITE=sqlite://
ENV DATABASE_URL=sqlite:///database.db
EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0"]
