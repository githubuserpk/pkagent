step-1: check the list of services running

gcloud run services list
✔
SERVICE: nginx
REGION: us-central1
URL: https://nginx-soamyio3oa-uc.a.run.app
LAST DEPLOYED BY: pkdeltaai.06@gmail.com
LAST DEPLOYED AT: 2024-08-22T09:17:58.126338Z

✔
SERVICE: opsagent
REGION: us-central1
URL: https://opsagent-soamyio3oa-uc.a.run.app
LAST DEPLOYED BY: pkdeltaai.06@gmail.com
LAST DEPLOYED AT: 2024-08-22T15:13:31.828417Z

step-2: run the cloud build cmd, it builds image and pushes to AR [for pre-reqs, see P2]
gcloud builds submit --tag us-docker.pkg.dev/pkdeltaai-06/ops-repository/opsagent:v1


step-3: deploy to cloud run 
gcloud beta run deploy opsagent --image us-docker.pkg.dev/pkdeltaai-06/ops-repository/opsagent:v1 --platform managed


prereqs: 

P1: 
Do it if required

#Authenticate Docker to Artifact Registry:
gcloud auth configure-docker us-docker.pkg.dev

P2: 
create AR repo
gcloud beta artifacts repositories create ops-repository \
  --location=us-central1 \
  --repository-format=docker \
  --project=pkdeltaai-06


P3: perms to svc account if reading gcs 
gcloud projects add-iam-policy-binding pkdeltaai-06 \
  --member=serviceAccount:939059298575-compute@developer.gserviceaccount.com \
  --role=roles/storage.objectViewer

P4: 
enable cloud build service
enable cloud run service


clean-ups: 

#delete repository
gcloud beta artifacts repositories delete ops-repository \
  --location=us-central1 \
  --project=pkdeltaai-06
done

gcloud run services list # to get the list of services we have deployed

delete service
gcloud run services delete SERVICE_NAME --region REGION



