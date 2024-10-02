from flask import Flask, request, jsonify
from elasticsearch import Elasticsearch
from transformers import pipeline
import pandas as pd

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
llm = pipeline("text-generation", model="gpt2")


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


@app.route("/query", methods=["POST"])
def query():
    user_query = request.json.get("query")
    results = search(user_query)
    if results:
        top_result = results[0]["_source"]
        context = (
            f"Product: {top_result['name']}\nDescription: {top_result['description']}"
        )
        prompt = f"Context: {context}\n\nUser Query: {user_query}\n\nResponse:"
        response = llm(prompt, max_length=50)[0]["generated_text"]
        return jsonify({"response": response})
    else:
        return jsonify({"response": "No relevant products found."})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
