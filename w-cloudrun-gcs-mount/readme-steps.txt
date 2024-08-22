Step-1: deployed a nginx container in cloud run in us central1 
#takes official nginx from Dockerhub

gcloud beta run deploy --image nginx --port 80 --execution-environment gen2 \
--add-volume=name=static,type=cloud-storage,bucket=bkt-pkdeltaai-06-uc1 \
--add-volume-mount=volume=static,mount-path='/usr/share/nginx/html'


step-2: 
open the url and make sure that the web page is running

step-3: 
copied the nginx file from GitHub index.html file here
https://github.com/nginx/nginx/blob/master/docs/html/index.html

step-4: 
edit the index.html file and upload to storage bucket 

Step-5: 
refresh the web page and you will see the updated html file without having to build the container image !!!! 


prereqs: 
create a bucket in us-central1: bkt-pkdeltaai-06-uc1



Summary - my observations: 
This is an amazing new feature launched by google in preview on 21 aug 2024.
It helps us to de-couple the file storage from the container and move it to GCS as file storage or NFS 
Behind the scenes, cloud run uses GCS FUSE 
So, it means you can edit your static html files without having to rebuild the container.  This is a very cool feature 








