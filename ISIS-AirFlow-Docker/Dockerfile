FROM usgsastro/ubuntu

RUN apt-get update
RUN apt-get install -y python3 && \
    apt-get install -y python3-pip && \
    apt-get install -y wget && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*


COPY . /opt/app
WORKDIR /opt/app

RUN pip3 install -r requirements.txt

WORKDIR /opt/conda
FROM usgsastro/miniconda3

RUN conda update conda && \
    conda install python=3.6 && \
    conda config --env --add channels conda-forge && \
    conda config --env --add channels usgs-astrogeology

RUN conda install -c usgs-astrogeology isis

RUN apt-get update && \
    apt-get install libgl1 -y && \
    rm -rf /var/lib/apt/lists*

RUN bash -lc 'python "$CONDA_PREFIX/scripts/isisVarInit.py"'
