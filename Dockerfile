FROM jupyter/base-notebook

USER root

# Install java 8
RUN apt-get update \
    && echo "Updated apt-get" \
    && apt-get install -y openjdk-8-jre \
    && echo "Installed openjdk 8"

RUN conda install -y -c jetbrains kotlin-jupyter-kernel && echo "Kotlin Jupyter kernel installed via conda"

ENV MPLCONFIGDIR=/home/jupyter/src

# Install dependencies
WORKDIR /home/jupyter
COPY  requirements.txt /home/jupyter
RUN pip3 install -r /home/jupyter/requirements.txt

# Let's change to "$NB_USER" command so the image runs as a non root user by default
USER $NB_UID

#Let's define this parameter to install jupyter lab instead of the default juyter notebook command so we don't have to use it when running the container with the option -e
ENV JUPYTER_ENABLE_LAB=yes