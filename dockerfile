from python:3.11.9-bookworm
WORKDIR /app
Copy . /app
RUN apt update
RUN apt install -y make automake gcc g++ libpython3-dev
RUN apt install -y libgeos++-dev libgeos-c1v5 libgeos-dev libgeos-doc
RUN pip install python-dotenv tqdm
RUN MAKEFLAGS="-j6" pip install -e .
