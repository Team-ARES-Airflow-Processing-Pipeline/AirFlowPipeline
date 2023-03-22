FROM usgsastro/ubuntu:latest

COPY . /opt/app
WORKDIR /opt/app

RUN apt-get update && apt-get install -y \
    python3.6 \
    python3-pip \
    wget \
    libgl1 \
    python-pluggy \
    python-dev

RUN apt-get clean && rm -rf /var/lib/apt/lists/*

RUN pip3 install -r requirements.txt

RUN airflow users create -u admin -e test@test.com -f Admin -l Admin -r Admin -p password

ENV CONDA_DIR /opt/conda

RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh && \
    chmod +x ~/miniconda.sh && \
    bash ~/miniconda.sh -b -p /opt/conda

ENV PATH=$CONDA_DIR/bin:$PATH

FROM usgsastro/miniconda3

WORKDIR /opt/app

RUN conda create -n isis
RUN conda install --no-update-deps python=3.6
RUN conda config --env --add channels conda-forge
RUN conda config --env --add channels usgs-astrogeology
RUN conda install --no-update-deps -c usgs-astrogeology isis
RUN conda env config vars set ISISROOT=$CONDA_PREFIX ISISDATA=~/ISIS_DATA/
