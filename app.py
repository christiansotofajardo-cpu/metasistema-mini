from nicegui import ui
from datetime import datetime
import os

def procesar_texto(texto):
    return f"[{datetime.now().strftime('%H:%M:%S')}] Procesado OK: {texto}"

# --- UI ---
ui.markdown("# 🌟 MetaSistema MINI")
ui.markdown("Versión mínima para testear y desplegar en Render.")

ui.markdown("### ✅ Procesar texto")

entrada = ui.textarea(label="Ingresa texto", placeholder="Escribe algo aquí...")
salida = ui.textarea(label="Resultado")

def ejecutar():
    salida.value = procesar_texto(entrada.value or "")

ui.button("Procesar", on_click=ejecutar)

# --- CONFIG ESPECIAL PARA RENDER ---
if __name__ in ('__main__', '__mp_main__'):
    port = int(os.getenv("PORT", 8080))
    ui.run(
        host="0.0.0.0",
        port=port,
        title="MetaSistema MINI",
        reload=False
    )
