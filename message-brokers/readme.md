# Message Brokers
## Testing Celery
1. python -m venv venv
2. source venv/bin/activate or activate.fish
3. brew install rabbitmq
	- configure rabbitmq
		1. sudo rabbitmqctl add_user major password
		2. sudo rabbitmqctl add_vhost major_host
		3. sudo scutil --set HostName major.local
		4. add "127.0.0.1 major.local" to hosts file
		5. sudo rabbitmqctl set_permissions -p major_host major ".*" ".*" ".*"
4. run rabbitmq-server
5. pip install celery
6. run celery worker -A tasks -l INFO -n worker1
	- worker -A means run app in a dedicated worker process
	- tasks is tasks.py app
	- the -l INFO is verbose log level
	- n worker name used by celery to communiate with workers