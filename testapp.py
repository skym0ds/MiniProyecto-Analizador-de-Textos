import nltk
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score
from analizadortext import analizar_texto  # <-- Importa la función desde tu app principal


casos_prueba = [
    {
        "texto": "La Universidad Nacional Autónoma de México es muy reconocida.",
        "palabras": ["universidad", "nacional", "autónoma", "méxico"],
        "entidades": ["México"]
    },
    {
        "texto": "Albert Einstein desarrolló la teoría de la relatividad.",
        "palabras": ["einstein", "teoría", "relatividad"],
        "entidades": ["Albert Einstein"]
    },
    {
        "texto": "El perro corre rápido en el parque.",
        "palabras": ["perro", "corre", "rápido", "parque"],
        "entidades": []
    }
]

# ==========================
# EJECUCIÓN Y MÉTRICAS
# ==========================
y_true, y_pred = [], []

for caso in casos_prueba:
    resultado = analizar_texto(caso["texto"])
    
    # Evaluación de palabras esperadas
    for palabra in caso["palabras"]:
        y_true.append(1)
        y_pred.append(1 if palabra in resultado.lower() else 0)

    # Evaluación de entidades esperadas
    for entidad in caso["entidades"]:
        y_true.append(1)
        y_pred.append(1 if entidad.lower() in resultado.lower() else 0)

    # Si no había entidades esperadas, revisamos falsos positivos
    if not caso["entidades"]:
        y_true.append(0)
        y_pred.append(1 if "entidad" in resultado.lower() else 0)

# ==========================
# CÁLCULO DE MÉTRICAS
# ==========================
accuracy = accuracy_score(y_true, y_pred)
precision = precision_score(y_true, y_pred, zero_division=0)
recall = recall_score(y_true, y_pred, zero_division=0)
f1 = f1_score(y_true, y_pred, zero_division=0)

print("📊 RESULTADOS DE EVALUACIÓN 📊")
print(f"✅ Exactitud (Accuracy): {accuracy:.2f}")
print(f"🎯 Precisión: {precision:.2f}")
print(f"📈 Recall: {recall:.2f}")
print(f"⚖️ F1-Score: {f1:.2f}")
print(f"🔍 Total casos evaluados: {len(y_true)}")
