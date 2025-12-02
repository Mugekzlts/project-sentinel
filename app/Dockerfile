# 1. Taban İmaj (Base Image): Python 3.9'un hafif sürümünü kullan
FROM python:3.9-slim

# 2. Çalışma Dizini: Konteynerin içinde '/app' diye bir klasör aç ve oraya geç
WORKDIR /app

# 3. Önce sadece gereksinimleri kopyala (Cache avantajı için)
COPY requirements.txt .

# 4. Kütüphaneleri yükle
RUN pip install --no-cache-dir -r requirements.txt

# 5. Şimdi geri kalan tüm kodları kopyala
COPY . .

# 6. Konteyner ayağa kalktığında çalışacak komut
CMD ["python", "main.py"]
