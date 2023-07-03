FROM nvidia/cuda:11.8.0-devel-ubuntu22.04

RUN apt update -y
RUN apt install -y software-properties-common
RUN add-apt-repository -y ppa:deadsnakes/ppa
RUN apt update -y 
RUN apt install --no-install-recommends  -y python3.10
RUN apt install --no-install-recommends  -y python3.10-dev 
RUN apt install -y --no-install-recommends pip
RUN apt install -y --no-install-recommends libportaudio2

RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 999
RUN update-alternatives --config python3
RUN ln -s /usr/bin/python3 /usr/bin/python
RUN pip install --upgrade pip

RUN mkdir -p /opt/music-gen-cliaa
WORKDIR /opt/music-gen-cli
COPY . /opt/music-gen-cli
RUN pip install .

CMD ["./music-gen-cli"]
