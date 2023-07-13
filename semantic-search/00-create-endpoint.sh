LOCATION=us-central1
PROJECT=$GOOGLE_CLOUD_PROJECT

curl -X POST \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json; charset=utf-8" \
    -d @request.json \
    "https://$LOCATION-aiplatform.googleapis.com/v1/projects/$PROJECT/locations/$LOCATION/indexEndpoints"
