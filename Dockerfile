FROM python:3.10
	ENV TOKEN=TOKEN
	WORKDIR /bot
	LABEL maintainer="Sonjoaquin"
	COPY requirements.txt /bot/
	RUN pip install -r requirements.txt
	COPY . /bot/
	CMD python main.py
