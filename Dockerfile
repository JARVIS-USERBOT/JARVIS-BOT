
#Repo Clonning ⚡♥️
RUN git clone https://github.com/LEGEND-OS/LEGENDUSERBOT.git /root/superos

#working directory 
WORKDIR /root/superos

# Install requirements
RUN pip3 install -U -r requirements.txt

ENV PATH="/home/superos/bin:$PATH"

CMD ["python3","-m","superos"]
