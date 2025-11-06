from nicegui import ui
from datetime import datetime

def procesar_texto(texto):
    return f"[{datetime.now().strftime('%H:%M:%S')}] Procesado OK: {texto}"

# --- UI ---
ui.markdown("# 🌟 MetaSistema MINI")
ui.markdown("Versión mínima para testear y desplegar en Render.")

ui.markdown("### ✅ Procesar texto")
entrada = ui.textarea(label="Ingresa texto", placeholder="Escribe algo aquí...", auto_grow=True)
salida = ui.textarea(label="Resultado", auto_grow=True)

def ejecutar():
    salida.value = procesar_texto(entrada.value or "")

ui.button("Procesar", on_click=ejecutar)

# Ejecutar app
ui.run(title="MetaSistema MINI")
