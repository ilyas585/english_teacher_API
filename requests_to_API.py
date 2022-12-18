import requests


# domain = "http://213.33.150.33:8000"
# domain_andy = "http://195.16.108.41:8000"
#
# r = requests.request("GET", f"{domain}/letter/guess")
# print(r.status_code)
# print(r.json())


# r = requests.request("POST", f"{domain_andy}/letter/check", json={"question_id": 1001, "letter": "n"})
# print(r.status_code)
# print(r.json())

# r = requests.request("GET", f"{domain}/word/result/")
# print(r.status_code)
# print(r.json())


# r = requests.get("https://httpbin.org/ip")
# print(r.json())


from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0')