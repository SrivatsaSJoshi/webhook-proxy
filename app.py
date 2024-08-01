from flask import Flask, request, Response
import requests
import hmac
import hashlib

app = Flask(__name__)

# GITHUB_SECRET = "your_github_webhook_secret"
JENKINS_URL = "http://192.168.0.11:8080/github-webhook/"

@app.route('/', methods=['POST'])
def webhook():
    # Verify GitHub signature
    # signature = request.headers.get('X-Hub-Signature-256')
    # if not signature:
    #    return Response("No signature", status=403)

    # Compute hash
    # hash_object = hmac.new(GITHUB_SECRET.encode('utf-8'), msg=request.data, digestmod=hashlib.sha256)
    # expected_signature = "sha256=" + hash_object.hexdigest()

    # if not hmac.compare_digest(signature, expected_signature):
    #     return Response("Invalid signature", status=403)

    # Forward the request to Jenkins
    jenkins_response = requests.post(JENKINS_URL, data=request.data, headers=request.headers)
    
    return Response(jenkins_response.content, status=jenkins_response.status_code, 
                    headers=jenkins_response.headers)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
