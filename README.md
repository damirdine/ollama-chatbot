# 🧠 Ollama Chatbot (FastAPI)

Ce projet est une API de chatbot local basé sur [Ollama](https://ollama.com/) et [FastAPI](https://fastapi.tiangolo.com/), avec réponses en streaming type ChatGPT. Il utilise une architecture modulaire testable (DDD-style) et enregistre les conversations uniquement en mémoire.

## 🚀 Fonctionnalités

* 📡 API REST `/chat` avec streaming `text/event-stream`
* 💬 Conversations par ID unique avec historique
* 🧱 Architecture modulaire (domain / services / api)
* 🧪 Tests unitaires avec `pytest`
* ⚡ Compatible avec [Ollama](https://ollama.com) local (ex: `llama3`)

## ⚙️ Prérequis

Avant de commencer, assure-toi d'avoir les éléments suivants installés sur ton système :

* Python 3.8 ou version supérieure
* [Poetry](https://python-poetry.org/) pour la gestion des dépendances
* [Ollama](https://ollama.com/) installé et configuré avec un modèle compatible, comme `llama3` ou autre.

## ⚙️ Installation

```bash
git clone https://github.com/ton-utilisateur/ollama-chatbot.git
cd ollama-chatbot
poetry install
```

> Assure-toi qu’Ollama est installé et qu’un modèle (ex: `llama3`) est chargé.

## 🚀 Lancement

```bash
poetry run dev
# ou
poetry run uvicorn app.main:app --reload
```

* Docs API : [http://localhost:8000/docs](http://localhost:8000/docs)
* ReDoc : [http://localhost:8000/redoc](http://localhost:8000/redoc)

## 🔌 API

### `POST /chat`

```json
{
  "message": "Bonjour !",
  "conversation_id": "facultatif"
}
```

* `text/event-stream` SSE
* Header `X-Conversation-ID` en réponse

## 🧪 Tests

```bash
poetry run pytest
```

## 📁 Structure

```
app/
├── api/         # Routes
├── domain/      # Modèles
├── schemas/     # Pydantic
├── services/    # Logique métier
├── main.py      # Entrée FastAPI
```

---

© Damirdine ALI SOILIHI — MIT
