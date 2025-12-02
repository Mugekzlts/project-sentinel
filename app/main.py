from flask import Flask, jsonify

app = Flask(__name__)

# Bu bizim "Health Check" (Sağlık Kontrolü) noktamız olacak.
# Kubernetes veya Docker, uygulamanın yaşayıp yaşamadığını buradan anlayacak.
@app.route('/')
def home():
    return jsonify({
        "status": "active",
        "system": "Project Sentinel Library API",
        "version": "1.0.0"
    })

# Kitapları listeleyen basit bir endpoint (Şimdilik sahte veri)
@app.route('/books')
def get_books():
    sample_books = [
        {"id": 1, "title": "DevOps Handbook", "author": "Gene Kim"},
        {"id": 2, "title": "The Phoenix Project", "author": "Gene Kim"},
    ]
    return jsonify(sample_books)

if __name__ == '__main__':
    # host='0.0.0.0' ÇOK ÖNEMLİ:
    # Bu olmazsa Docker konteyneri dışarıdan erişimi reddeder.
    app.run(host='0.0.0.0', port=5000)
