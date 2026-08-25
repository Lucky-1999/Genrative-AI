# CineSage

CineSage is a small Streamlit application that extracts structured information and a short summary from a movie paragraph using Mistral through LangChain.

## Requirements


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
# Generative AI Experiments

A collection of small Python experiments with LangChain model providers, chat workflows, embeddings, and Streamlit interfaces.

## Project Areas

- `CineSage/`: Streamlit movie information extraction with Mistral.
- `chatmodels/`: chat model examples using Mistral, OpenAI, and Hugging Face models.
- `embeddingmodels/`: OpenAI and Hugging Face embedding examples.

## Requirements

- Python 3.12 or newer
- API credentials for the examples you want to run

## Setup

From the repository root:

```powershell
py -3.12 -m venv .venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Create a local `.env` file from `.env.example` and add only the credentials required by the script you are using:

```powershell
Copy-Item .env.example .env
```

## Run Examples

Start the CineSage Streamlit application:

```powershell
streamlit run .\CineSage\uicore.py
```

Run a console chat example:

```powershell
python .\chatmodels\chatbot.py
```

Run a console embedding example:

```powershell
python .\embeddingmodels\embeddings.py
```

Other `.py` files in `chatmodels` and `embeddingmodels` demonstrate alternative providers and model configurations. Read the selected file before running it because some examples download local models or prompt for input.

## Environment Variables

- `MISTRAL_API_KEY`: used by Mistral chat examples and CineSage.
- `GOOGLE_API_KEY`: used by Gemini examples.
- `OPENAI_API_KEY`: used by OpenAI chat and embedding examples.
- `HUGGINGFACEHUB_API_TOKEN`: used by Hugging Face examples that access hosted models.

## Security

Never commit `.env` or API keys. Use `.env.example` as a configuration template and store real credentials locally or in your deployment platform's secret manager.
