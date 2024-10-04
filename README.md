This is a submission of the final project for DataTalksClub's [LLM Zoomcamp 2024](https://github.com/DataTalksClub/llm-zoomcamp). 
The purpose of the project is to demonstrate the ability to apply LLM technology to a selected problem domain while following the best practices taught in the course (code refactoring, testing, linting etc.)

This project is a proof-of-concept for a RAG application for querying information on store products. 

**Features**<br>
This project is a Flask application that integrates Elasticsearch for product search and a Hugging Face LLM for generating responses based on product descriptions.

**Dataset - `store_products.csv`**<br>
This is an AI-generated toy dataset containing product info: *id*, *name*, *category*, and *description*. It can be replaced by real-world data with the same fields.

**Dependencies - `requirements.txt`**
<ul>
<li>flask</li>
<li>elasticsearch</li>
<li>transformers</li>
<li>pandas</li>
<li>pytest</li>
<li>requests</li>
<li>flake8</li>
<li>black</li>
<li>python-logging-loki</li>
</ul>

**Usage**

Clone the repo and use the Makefile to set up the environment and launch and test the app. 
1. Clone the repo
2. Run `make install` in the terminal to install all the dependencies in `requirements.txt`.
3. Run  `make start-elasticsearch` to spin up the docker container hosting elasticsearch.
4. Run `make start-loki` to set up Grafana connection.
5. Run `make run` to run the logging script in `monitoring.py` and launch the RAG app (`app.py`).
6. Run `make test` to test the connection with the endpoint of the RAG app by sending a POST request. 
7. Log in to Grafana on localhost 3000 and import logs for monitoring the queries to the app. 