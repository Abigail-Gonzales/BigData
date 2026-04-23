import csv
import os

def ingest_data():
    """
    Script de ingesta para el proyecto Steam Nexus.
    Carga el dataset de juegos y realiza una limpieza inicial.
    Usa la librería estándar 'csv' para evitar conflictos de versiones de NumPy/Pandas.
    """
    
    # Rutas
    raw_path = "data/raw/steam_games.csv"
    processed_path = "data/processed/dataset_v1.csv"
    
    print("--- Iniciando Ingesta de Datos (Steam Nexus) ---")
    
    # Verificar si el archivo crudo existe
    if not os.path.exists(raw_path):
        print(f"Error: No se encontró el archivo en {raw_path}")
        print("Por favor, descarga el dataset desde Kaggle y colócalo en data/raw/")
        
        # Generar datos de ejemplo para demostración (Hito 3)
        print("Generando dataset de demostración V1...")
        demo_headers = ['app_id', 'name', 'release_date', 'price', 'genres', 'description']
        demo_rows = [
            [10, 'Counter-Strike', '2000-11-01', 9.99, 'Action', "The world's number 1 online action game..."],
            [20, 'Team Fortress Classic', '1999-04-01', 4.99, 'Action', "One of the most popular online action games..."],
            [30, 'Day of Defeat', '2003-05-01', 4.99, 'Action', "WWII action..."]
        ]
        
        os.makedirs(os.path.dirname(processed_path), exist_ok=True)
        with open(processed_path, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(demo_headers)
            writer.writerows(demo_rows)
            
        print(f"Archivo de demostración guardado en {processed_path}")
        return

    # Carga y limpieza simple con csv (si el archivo existe)
    print(f"Procesando datos desde {raw_path}...")
    with open(raw_path, mode='r', encoding='utf-8') as fin, \
         open(processed_path, mode='w', newline='', encoding='utf-8') as fout:
        
        reader = csv.DictReader(fin)
        writer = csv.DictWriter(fout, fieldnames=reader.fieldnames)
        writer.writeheader()
        
        seen_ids = set()
        for row in reader:
            app_id = row.get('app_id')
            if app_id and app_id not in seen_ids:
                # Limpieza básica
                row['name'] = row.get('name') or 'Unknown Game'
                row['price'] = row.get('price') or '0.0'
                writer.writerow(row)
                seen_ids.add(app_id)
                
    print("¡Ingesta completada con éxito!")

if __name__ == "__main__":
    ingest_data()
