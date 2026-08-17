from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Hello from AWS DevOps Pipeline!</h1>
    <p>Application deployed using Jenkins + Docker + Kubernetes</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)