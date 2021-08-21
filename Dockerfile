
#Repo Clonning ⚡♥️
RUN git clone https://github.com/LEGEND-OS/LEGENDUSERBOT.git /root/superos

#working directory 
WORKDIR /root/userbot

# Install requirements
RUN pip3 install -U -r requirements.txt

ENV PATH="/home/userbot/bin:$PATH"

CMD ["python3","-m","userbot"]
