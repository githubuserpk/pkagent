## cr01 is for cloud run jobs in python
## ====================================

Step-0: setup, prereqs
export PROJECT_ID=pkdeltaai-06
export REGION=us-central1
gcloud config set core/project $PROJECT_ID


#Enable APIs | AR, CB and CR 

gcloud services enable \
  artifactregistry.googleapis.com \
  cloudbuild.googleapis.com \
  run.googleapis.com

## Below command grants cloud build service account role to the compute engine default service account

gcloud projects add-iam-policy-binding $PROJECT_ID \
    --member=serviceAccount:$PROJECT_NUMBER-compute@developer.gserviceaccount.com \
    --role=roles/cloudbuild.builds.builder


Step-1: add your logic to main.py file 

Step-2: create a Procfile with a single line 

Step-3: Build jobs container 

## Build jobs container, send it to Artifact Registry and deploy to Cloud Run
## ==========================================================================
gcloud run jobs deploy job-quickstart \
    --source . \
    --tasks 50 \
    --set-env-vars SLEEP_MS=10000 \
    --set-env-vars FAIL_RATE=0.1 \
    --max-retries 5 \
    --region REGION \
    --project=PROJECT_ID

## Step-4: run the job 
## ===================

gcloud run jobs execute job-quickstart --region us-central1


