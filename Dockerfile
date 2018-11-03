FROM ubuntu:16.04

RUN apt-get update -qqq 
RUN apt-get install python-dev -y
RUN apt-get install -y python-pip
RUN pip install pandas 
RUN pip install numpy 
RUN pip install Scipy 
RUN pip install statsmodels
RUN mkdir /home/data
WORKDIR /home

COPY 1-longitudinal-minimal-data-set-V2.csv ./1-longitudinal-minimal-data-set-V2.csv

COPY hie_analysis.py ./hie_analysis.py 

CMD python ./hie_analysis.py

