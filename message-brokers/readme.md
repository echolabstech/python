# Message Brokers
## Testing Celery
1. brew install rabbitmq
2. python -m venv venv
3. source venv/bin/activate or activate.fish
4. pip install celery
5. run rabbitmq-server
6. run celery worker -A tasks -l INFO
	- worker -A means run app in a dedicated worker process
	- tasks is tasks.py app
	- the -l INFO is verbose log level