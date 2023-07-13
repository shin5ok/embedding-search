ENDPOINT_ID=$(
   gcloud ai index-endpoints list --region=us-central1 --format=json | jq .[].name -r | cut -d \/ -f 6 
)

INDEX_ID=$(
    gcloud ai indexes list --region=us-central1 --format=json | jq -r .[].name | cut -d \/ -f 6
)

gcloud ai index-endpoints deploy-index $ENDPOINT_ID \
  --deployed-index-id=testindex \
  --display-name=test-index-name \
  --index=$INDEX_ID \
  --project=$PROJECT \
  --region=us-central1
