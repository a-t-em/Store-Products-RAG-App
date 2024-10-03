from flask import Flask, request, jsonify
from elasticsearch import Elasticsearch
from transformers import pipeline
import pandas as pd
from monitoring import log_request, log_response

app = Flask(__name__)

# Initialize Elasticsearch
es = Elasticsearch(hosts=["http://localhost:9200"])

# Read the CSV file
df = pd.read_csv("store_products.csv")

# Index the dataset
for _, row in df.iterrows():
    product = {
        "id": row["id"],
        "name": row["name"],
        "category": row["category"],
        "description": row["description"],
    }
    es.index(index="products", id=product["id"], body=product)

# Initialize the LLM
llm = pipeline("text-generation", model="tiiuae/falcon-7b")

def search(query):
    search_body = {
        "query": {
            "multi_match": {
                "query": query,
                "fields": ["name", "category", "description"],
            }
        }
    }
    results = es.search(index="products", body=search_body)
    return results["hits"]["hits"]

@app.before_request
def before_request():
    log_request()

@app.after_request
def after_request(response):
    return log_response(response)

@app.route("/query", methods=["POST"])
def query():
    user_query = request.json.get("query")
    results = search(user_query)
    if results:
        context = "\n".join(
            [f"Product: {result['_source']['name']}\nDescription: {result['_source']['description']}" for result in results]
        )
        prompt = f"Context: {context}\n\nUser Query: {user_query}\n\nResponse:"
        response = llm(prompt, max_length=50, truncation=True, num_return_sequences=1, return_full_text=False)
        return jsonify({"response": response[0]["generated_text"]})
    else:
        return jsonify({"response": "No relevant products found."})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
