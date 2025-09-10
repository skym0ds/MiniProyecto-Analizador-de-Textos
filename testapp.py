import nltk
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score
from analizadortext import analizar_texto  # Importa tu función

# ==========================
# DATOS DE PRUEBA
# ==========================
casos_prueba = [
    {
        "texto": "La Universidad Nacional Autónoma de México es muy reconocida.",
        "palabras": ["universidad", "nacional", "autónoma", "méxico"],
        "entidades": ["México"],
        "sinonimos": {
            "universidad": ["facultad", "instituto"],
            "méxico": ["estados unidos mexicanos"]
        }
    },
    {
        "texto": "Albert Einstein desarrolló la teoría de la relatividad.",
        "palabras": ["einstein", "teoría", "relatividad"],
        "entidades": ["Albert Einstein"],
        "sinonimos": {
            "teoría": ["hipótesis", "principio"],
            "relatividad": ["dependencia", "referencia"]
        }
    },
    {
        "texto": "El perro corre rápido en el parque.",
        "palabras": ["perro", "corre", "rápido", "parque"],
        "entidades": [],
        "sinonimos": {
            "perro": ["can", "chucho"],
            "rápido": ["veloz", "ligero"]
        }
    },
    {
        "texto": "Gabriel García Márquez escribió Cien años de soledad en Colombia.",
        "palabras": ["gabriel", "garcía", "márquez", "soledad", "colombia"],
        "entidades": ["Gabriel García Márquez", "Colombia"],
        "sinonimos": {
            "soledad": ["aislamiento", "abandono"],
            "colombia": ["república de colombia"]
        }
    },
    {
        "texto": "La Organización de las Naciones Unidas fue fundada en 1945.",
        "palabras": ["organización", "naciones", "unidas", "fundada", "1945"],
        "entidades": ["Naciones Unidas"],
        "sinonimos": {
            "organización": ["institución", "asociación"],
            "unidas": ["agrupadas", "aliadas"]
        }
    },
    {
        "texto": "Python es un lenguaje de programación muy popular en inteligencia artificial.",
        "palabras": ["python", "lenguaje", "programación", "inteligencia", "artificial"],
        "entidades": ["Python"],
        "sinonimos": {
            "lenguaje": ["idioma", "sistema"],
            "programación": ["codificación", "desarrollo"]
        }
    }
]

# ==========================
# EJECUCIÓN Y MÉTRICAS
# ==========================
y_true, y_pred = [], []

for caso in casos_prueba:
    resultado = analizar_texto(caso["texto"]).lower()
    
    # Evaluación de palabras clave
    for palabra in caso["palabras"]:
        y_true.append(1)
        y_pred.append(1 if palabra in resultado else 0)

    # Evaluación de entidades
    for entidad in caso["entidades"]:
        y_true.append(1)
        y_pred.append(1 if entidad.lower() in resultado else 0)

    # Evaluación de falsos positivos (si no hay entidades esperadas)
    if not caso["entidades"]:
        y_true.append(0)
        y_pred.append(1 if "entidad" in resultado else 0)

    # Evaluación de sinónimos
    for palabra, sinonimos in caso["sinonimos"].items():
        for sinonimo in sinonimos:
            y_true.append(1)
            y_pred.append(1 if sinonimo in resultado else 0)

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
print(f"🔍 Total evaluaciones individuales: {len(y_true)}")

