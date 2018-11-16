FROM ubuntu:16.04
RUN apt-get update -qqq
RUN apt-get install python-dev -y
RUN apt-get install -y python-pip
RUN pip install --upgrade pip
RUN apt-get install -y build-essential
RUN pip install numpy pandas scipy statsmodels


ADD hie_analysis.py /home/hie_analysis.py
CMD chmod u+x /home/hie_analysis.py

CMD ["python", "/home/hie_analysis.py"] 