from nicegui import ui
from datetime import datetime

def procesar_texto(texto: str) -> str:
    return f"[{datetime.now().strftime('%H:%M:%S')}] Procesado OK: {texto}"

# --- UI ---
ui.markdown("# 🌟 MetaSistema MINI")
ui.markdown("Versión mínima para testear y desplegar en Render.")

ui.markdown("### ✅ Procesar texto")

ui.label("Ingresa texto")
entrada = ui.textarea(placeholder="Escribe algo aquí...").props('autogrow')

ui.label("Resultado")
salida = ui.textarea().props('autogrow')

def ejecutar():
    salida.value = procesar_texto(entrada.value or "")

ui.button("Procesar", on_click=ejecutar)

# Ejecutar app
ui.run(title="MetaSistema MINI")
