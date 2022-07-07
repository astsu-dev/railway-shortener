FROM python:3.10

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY shortener ./shortener

EXPOSE 80

CMD ["uvicorn", "--port", "80", "shortener.app:app"]
