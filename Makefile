install:
	pip install -r requirements.txt

run:
	python app.py

test:
	pytest test.py

start-elasticsearch:
	docker run -it \
		--rm \
		--name elasticsearch \
		-p 9200:9200 \
		-p 9300:9300 \
		-e "discovery.type=single-node" \
		-e "xpack.security.enabled=false" \
		docker.elastic.co/elasticsearch/elasticsearch:8.4.3

lint:
	flake8

format:
	black .