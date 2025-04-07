#####Instructions#####
#####for creating docker image of domain monitoring app and running it#####
#sudo ssh -i "/mnt/c/Users/User/Desktop/AWS_key/RoyG_key.pem" ubuntu@35.89.235.135
#sudo apt update && sudo install docker.io
#apt install docker.io
#docker pull python (#download the python docker)
#run the following command from the folder that contains Dockerfile: docker build -t my_image_name .
#docker run -d -p 8080:80 -v /host/path:/container/path <image_name>1

FROM python
RUN mkdir /domain_monitoring
RUN chmod 777 /domain_monitoring
COPY . /domain_monitoring
WORKDIR /domain_monitoring
RUN pip install flask
CMD ("python", app.py)