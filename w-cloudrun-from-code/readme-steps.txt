#sample code url: 

https://cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-python-service?hl=en


step-1: 
gcloud services enable run.googleapis.com

step-2: 
gcloud projects add-iam-policy-binding PROJECT_ID \
    --member=serviceAccount:PROJECT_NUMBER-compute@developer.gserviceaccount.com \
    --role=roles/cloudbuild.builds.builder


step-3: 
mkdir helloworld
cd helloworld

step-4: 

import os

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    """Example Hello World route."""
    name = os.environ.get("NAME", "World")
    return f"Hello {name}!"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))


step-4: requirements.txt
Flask==3.0.3
gunicorn==22.0.0
Werkzeug==3.0.3

step-5: deploy the app
gcloud run deploy

cleanup: 
============

gcloud artifacts repositories delete cloud-run-source-deploy --location us-central1
gcloud run services delete helloworld 
gsutil rm -r gs://pkdeltaai-06_cloudbuild/


