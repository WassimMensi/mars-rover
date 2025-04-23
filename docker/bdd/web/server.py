import os
import time
import psycopg2

host = os.getenv("DB_HOST", "localhost")
user = os.getenv("DB_USER", "mars")
password = os.getenv("DB_PASSWORD", "roverpass")
dbname = os.getenv("DB_NAME", "marsroverdb")

print(f"🔌 Tentative de connexion à PostgreSQL ({user}@{host}, DB={dbname})...")

while True:
    try:
        conn = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            dbname=dbname,
            connect_timeout=3
        )
        print("✅ Connexion réussie !")
        conn.close()
        break
    except Exception as e:
        print(f"❌ Erreur de connexion : {e}")
        time.sleep(2)

print("📡 Connexion établie — le conteneur reste actif.")
while True:
    time.sleep(60)
