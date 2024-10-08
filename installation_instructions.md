# Installation instructions and API setup
## Step 0:
Make sure that you have both an Azure API key and are in the center-for-humans-and-machines github organization.

## Copy Azure API key
1. Visit `https://ai.azure.com/`
2. Click `Resources and Keys`
3. Copy the `chm-openai` key.

## Fow low download speeds (If in Bavarian Castle)
1. Create virtual-env with python 3.11 (e.g. using conda)
2. `pip install torch==2.3.1 torchvision==0.18.1 torchaudio==2.3.1 --index-url https://download.pytorch.org/whl/cpu`
3. `pip install python-dotenv tqdm sentence-transformers`
4. Clone [this](https://github.com/center-for-humans-and-machines/concordia) repo and get into it's top folder
4. `pip install -e .`
5. Copy `.env_template` from this repo to `~/.env` and enter the azure api key. (You can also use a different location, but then you'll have to specify that manually each time `load_azure_model` is called in the notebooks)

## Docker (If you want to be sure that things work on your system)

* `docker pull kappablanca/concordia:latest`
* Insert your api key into the following command and run: `docker run -it -p 8888:8888 -e AZURE_OPENAI_ENDPOINT="https://chm-openai.openai.azure.com/" -e AZURE_OPENAI_API_KEY=YouApiKey kappablanca/concordia`
* Open in browser: `http://127.0.0.1:8888/`

## PIP (If download speed is a constraint)
1. Create virtual-env with python 3.11 (e.g. using conda)
2. `git clone https://github.com/center-for-humans-and-machines/concordia`, `cd concordia`
3. `pip install python-dotenv tqdm sentence-transformers`
4. `pip install -e .`
5. Copy `.env_template` from this repo to `~/.env` and enter the azure api key. (You can also use a different location, but then you'll have to specify that manually each time `load_azure_model` is called in the notebooks)
