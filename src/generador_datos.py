import pandas as pd
import random
from datetime import datetime, timedelta

# Configuración
NUM_REGISTROS = 5000
MARCAS = ['Creed', 'Xerjoff', 'Tom Ford', 'Bond No9', 'Parfums de Marly', 'Roja Parfums', 'Amouage', 'Clive Christian']
PRODUCTOS = {
    'Creed': ['Aventus', 'Green Irish Tweed', 'Silver Mountain Water'],
    'Xerjoff': ['Naxos', 'Alexandria II', 'Erba Pura'],
    'Tom Ford': ['Oud Wood', 'Tobacco Vanille', 'Lost Cherry'],
    'Bond No9': ['Lafayette Street', 'Scent of Peace', 'New York Nights'],
    'Parfums de Marly': ['Layton', 'Pegasus', 'Herod'],
    'Roja Parfums': ['Elysium', 'Enigma', 'Amber Aoud'],
    'Amouage': ['Interlude Man', 'Reflection Man', 'Jubilation XXV'],
    'Clive Christian': ['No. 1', 'Rock Rose', 'X Masculine']
}

def generar_datos():
    data = []
    for _ in range(NUM_REGISTROS):
        marca = random.choice(MARCAS)
        producto = random.choice(PRODUCTOS[marca])
        precio = round(random.uniform(250, 800), 2)
        fecha = datetime(2025, 1, 1) + timedelta(days=random.randint(0, 365))
        
        data.append([fecha.strftime("%Y-%m-%d"), marca, producto, precio])
    
    df = pd.DataFrame(data, columns=['fecha', 'marca', 'producto', 'precio'])
    df.to_csv('ventas_perfumeria_vip.csv', index=False)
    print("Archivo generado exitosamente: ventas_perfumeria_vip.csv")

if __name__ == "__main__":
    generar_datos()
