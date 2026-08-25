# CineSage

CineSage is a small Streamlit application that extracts structured information and a short summary from a movie paragraph using Mistral through LangChain.

## Requirements

- Python 3.12 or newer
- A Mistral API key

## Setup

From the repository root:

```powershell
py -3.12 -m venv .venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Copy `.env.example` to `.env` and add your Mistral API key:

```powershell
Copy-Item .env.example .env
```

## Run

```powershell
streamlit run .\Genrative-AI\CineSage\uicore.py
```

If your terminal is already inside `Genrative-AI\CineSage`, run:

```powershell
streamlit run .\uicore.py
```

## Security

Never commit `.env` or API keys. Use `.env.example` as the configuration template and store real credentials locally or in your deployment platform's secret manager.
