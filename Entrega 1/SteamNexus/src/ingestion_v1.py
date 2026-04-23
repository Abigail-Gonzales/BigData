import pandas as pd
import os

def process_data_v1():
    """
    Script de ingesta y limpieza V1 para el proyecto Steam Nexus.
    Carga el dataset crudo de juegos y realiza una limpieza inicial para cumplir con el Hito 3.
    """
    
    # Rutas
    raw_games_path = "data/raw/steam_games_raw.csv"
    processed_path = "data/processed/dataset_v1.csv"
    
    print("--- Iniciando Procesamiento V1 (Steam Nexus) ---")
    
    if not os.path.exists(raw_games_path):
        print(f"Error: No se encontró {raw_games_path}")
        return

    # Cargar datos
    print(f"Cargando datos desde {raw_games_path}...")
    # Usamos low_memory=False porque el archivo es grande
    df = pd.read_csv(raw_games_path, low_memory=False)
    
    # 1. Selección de columnas clave para la V1
    columns_to_keep = [
        'AppID', 'Name', 'Release date', 'Price', 
        'About the game', 'Genres', 'Tags', 
        'Positive', 'Negative', 'Average playtime forever'
    ]
    
    df_v1 = df[columns_to_keep].copy()
    
    # 2. Limpieza básica
    print("Realizando limpieza inicial...")
    
    # Eliminar juegos sin nombre
    df_v1 = df_v1.dropna(subset=['Name'])
    
    # Formatear precios (algunos pueden venir como strings o tener errores)
    df_v1['Price'] = pd.to_numeric(df_v1['Price'], errors='coerce').fillna(0.0)
    
    # Llenar nulos en texto
    df_v1['About the game'] = df_v1['About the game'].fillna('No description available')
    df_v1['Genres'] = df_v1['Genres'].fillna('Unknown')
    df_v1['Tags'] = df_v1['Tags'].fillna('')
    
    # 3. Guardar dataset procesado
    os.makedirs(os.path.dirname(processed_path), exist_ok=True)
    df_v1.to_csv(processed_path, index=False, encoding='utf-8')
    
    print(f"--- Hito 3 Completado ---")
    print(f"Dataset procesado guardado en: {processed_path}")
    print(f"Total de registros procesados: {len(df_v1)}")

if __name__ == "__main__":
    process_data_v1()
