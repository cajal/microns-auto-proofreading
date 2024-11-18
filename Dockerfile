FROM celiib/neurd:v1
LABEL maintainer="Stelios Papadopoulos <spapadop@bcm.edu>"

RUN apt-get update --yes && \
    apt-get upgrade --yes && \
    apt-get install --yes --no-install-recommends

RUN pip3 install \
        nglui \
        slackclient

# Install DataJoint with datajoint_plus
ADD "https://api.github.com/repos/cajal/datajoint-plus/releases?per_page=1" latest
RUN pip install datajoint-plus

# Install wridgets
ADD "https://api.github.com/repos/spapa013/wridgets/releases?per_page=1" latest
RUN pip install wridgets

# Install Cajal packages from latest tag
ADD "https://api.github.com/repos/cajal/microns-utils/releases?per_page=1" latest
RUN pip install microns-utils

ADD "https://api.github.com/repos/cajal/microns-nda/releases?per_page=1" latest
RUN export TAG=$(curl -s 'https://api.github.com/repos/cajal/microns-nda/releases?per_page=1' | grep -oP '"name": "\K(.*)(?=")'); \ 
    pip install git+https://github.com/cajal/microns-nda.git@$TAG#subdirectory=python/microns-nda-api

ADD "https://api.github.com/repos/cajal/microns-materialization/releases?per_page=1" latest
RUN export TAG=$(curl -s 'https://api.github.com/repos/cajal/microns-materialization/releases?per_page=1' | grep -oP '"name": "\K(.*)(?=")'); \ 
    pip install git+https://github.com/cajal/microns-materialization.git@$TAG#subdirectory=python/microns-materialization-api

ADD "https://api.github.com/repos/cajal/microns-coregistration/releases?per_page=1" latest
RUN export TAG=$(curl -s 'https://api.github.com/repos/cajal/microns-coregistration/releases?per_page=1' | grep -oP '"name": "\K(.*)(?=")'); \ 
    pip install git+https://github.com/cajal/microns-coregistration.git@$TAG#subdirectory=python/microns-coregistration-api

ADD "https://api.github.com/repos/cajal/microns-manual-proofreading/releases?per_page=1" latest
RUN export TAG=$(curl -s 'https://api.github.com/repos/cajal/microns-manual-proofreading/tags?per_page=1' | grep -oP '"name": "\K(.*)(?=")'); \ 
    pip install git+https://github.com/cajal/microns-manual-proofreading.git@$TAG#subdirectory=python/microns-manual-proofreading-api

ADD "https://api.github.com/repos/cajal/microns-proximities/releases?per_page=1" latest
RUN export TAG=$(curl -s 'https://api.github.com/repos/cajal/microns-proximities/tags?per_page=1' | grep -oP '"name": "\K(.*)(?=")'); \ 
    pip install git+https://github.com/cajal/microns-proximities.git@$TAG#subdirectory=python/microns-proximities-api

# NEURD 
ADD "https://api.github.com/repos/reimerlab/neurd/releases?per_page=1" latest
RUN export TAG=$(curl -s 'https://api.github.com/repos/reimerlab/neurd/tags?per_page=1' | grep -oP '"name": "\K(.*)(?=")'); \ 
    pip install git+https://github.com/reimerlab/NEURD.git@$TAG

# install meshAfterParty
WORKDIR /src
ARG GITHUB_TOKEN
RUN git clone https://$GITHUB_TOKEN@github.com/celiibrendan/meshAfterParty.git
RUN pip install git+https://github.com/cajal/minnie-config.git

WORKDIR /
ARG CLOUDVOLUME_TOKEN
RUN mkdir -p .cloudvolume/secrets
RUN echo "{\"token\": \"${CLOUDVOLUME_TOKEN:-}\"}" > .cloudvolume/secrets/cave-secret.json

COPY . /src/microns-morphology
RUN pip install -e /src/microns-morphology/python/microns-morphology
RUN pip install -e /src/microns-morphology/python/microns-morphology-api