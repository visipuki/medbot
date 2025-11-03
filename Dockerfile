FROM python:3.11-slim

# Установить системные зависимости и SQLite3
RUN apt-get update && \
    apt-get install -y sqlite3 && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Сначала применяем миграции, затем стартуем бота
CMD ["sh", "-c", "python database.py migrate && python bot.py"]
