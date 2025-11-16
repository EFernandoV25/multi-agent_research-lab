# AI Research Team - Multi-Agent System

## 📁 Archivos incluidos

- `src/agents.py` — Definiciones de los 3 agentes (Researcher, Writer, Reviewer)
- `notebooks/workflow_demo.ipynb` — Ejecución end-to-end del workflow
- `research_summary.md` — Reporte final generado
- `requirements.txt` — Dependencias del proyecto

## 🚀 Instalación

```bash
pip install -r requirements.txt
```

## 🔑 Configuración

Tu API key de Groq ya está incluida en `src/agents.py`. Si necesitas cambiarla:

```python
GROQ_API_KEY = "tu_nueva_key_aqui"
```

## ▶️ Ejecución

### Opción 1: Python script

```python
import os
from src.agents import create_researcher, create_writer, create_reviewer
from crewai import Task, Crew, Process

os.environ["GROQ_API_KEY"] = "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"
os.environ["OPENAI_API_KEY"] = "sk-dummy-key"

TOPIC = "Impact of Synthetic Data in Healthcare"

# Crear agentes
researcher = create_researcher()
writer = create_writer()
reviewer = create_reviewer()

# Crear tareas
research_task = Task(
    description=f"Research: {TOPIC}",
    agent=researcher,
    expected_output="Detailed research findings"
)

writing_task = Task(
    description=f"Write 500-word summary on: {TOPIC}",
    agent=writer,
    expected_output="500-word Markdown summary",
    context=[research_task]
)

review_task = Task(
    description=f"Review the summary on: {TOPIC}",
    agent=reviewer,
    expected_output="Final improved summary",
    context=[writing_task]
)

# Ejecutar
crew = Crew(
    agents=[researcher, writer, reviewer],
    tasks=[research_task, writing_task, review_task],
    process=Process.sequential,
    verbose=True
)

result = crew.kickoff()

# Guardar
with open("research_summary.md", "w") as f:
    f.write(str(result))

print("DONE!")
```

### Opción 2: Jupyter Notebook

Abre `notebooks/workflow_demo.ipynb` y ejecuta las celdas.

## 📊 Output

El sistema genera `research_summary.md` con la siguiente estructura:

- **Introduction** (100 palabras)
- **Key Findings** (200 palabras)
- **Ethical & Technical Challenges** (100 palabras)
- **Conclusion** (100 palabras)

## 🎯 Agentes

1. **Researcher Agent** - Busca y analiza información
2. **Writer Agent** - Genera resumen de 500 palabras en Markdown
3. **Reviewer Agent** - Evalúa y mejora la calidad del contenido

## 📦 Dependencias

- `crewai==0.80.0` - Framework multi-agente
- `litellm==1.55.8` - Integración con LLMs

## 🆓 API Gratuita

Este proyecto usa **Groq API** que es completamente gratis con límites generosos.
