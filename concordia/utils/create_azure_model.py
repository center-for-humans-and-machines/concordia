import os

from dotenv import load_dotenv
from openai import AzureOpenAI

from concordia.language_model import gpt_model


def load_azure_model(model_name="gpt-4o-mini", env_file="~/.env"):

  load_dotenv(os.path.expanduser("~/.env"), override=True)
  GPT_API_KEY = os.environ.get(
      "AZURE_OPENAI_API_KEY"
  )  # @param {type: 'string'}
  ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
  GPT_MODEL_NAME = model_name  # @param {type: 'string'}
  # GPT_MODEL_NAME = 'gpt-35-turbo-16k' #@param {type: 'string'}

  if not GPT_API_KEY:
    raise ValueError("GPT_API_KEY is required.")

  client = AzureOpenAI(
      api_key=GPT_API_KEY,
      api_version="2024-02-01",
      azure_endpoint=ENDPOINT,
  )

  model = gpt_model.GptLanguageModel(
      client=client,
      model_name=GPT_MODEL_NAME,
      request_logging_file="request_logs.json",
  )
  return model
