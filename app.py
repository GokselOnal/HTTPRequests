from flask import Flask, request, render_template
import requests
import json

app = Flask(__name__, template_folder="templates", static_folder="static")


@app.route("/", methods=["POST", "GET"])
def index():
    url_request = request.form.get("url")
    body = ""
    if request.method == "POST":
        method = request.form.get("http_methods")
        if method == "get": response = requests.get(url_request)
        elif method == "post":
            body = request.form.get("body")
            response = requests.post(url_request, json.loads(body))
        elif method == "put":
            update = request.form.get("body")
            response = requests.put(url_request, json.loads(update))
        elif method == "delete": response = requests.delete(url_request)
        return render_template("index.html", url=url_request, method=method, response_status=response.status_code, body=body, response=json.dumps(response.json()))
    else:
        return render_template("index.html", response="", body="")


if __name__ == "__main__":
    app.run(debug=True, port=8000)
