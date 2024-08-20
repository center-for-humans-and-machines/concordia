FROM python:3.11.9-bookworm
WORKDIR /app
RUN apt update
RUN apt install -y make automake gcc g++ libpython3-dev
RUN apt install -y libgeos++-dev libgeos-c1v5 libgeos-dev libgeos-doc vim
RUN pip install python-dotenv tqdm sentence-transformers jupyter
COPY . /app
RUN MAKEFLAGS="-j6" pip install -e .
ENTRYPOINT ["bash", "-c", "jupyter notebook --ip 0.0.0.0 --no-browser --allow-root" ]
