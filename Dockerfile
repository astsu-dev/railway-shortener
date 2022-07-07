FROM python:3.10

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY shortener ./shortener

EXPOSE 8000

CMD ["uvicorn", "shortener.app:app"]
