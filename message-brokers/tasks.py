from celery import Celery
import requests

app = Celery()
app.config_from_object('config')

@app.task
def add(x, y):
	return x + y

@app.task
def fetch_url(url):
	response = requests.get(url)
	return response.text

if __name__ == '__main__':
	pass