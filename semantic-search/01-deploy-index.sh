ENDPOINT_ID=$(
   gcloud ai index-endpoints list --region=us-central1 --format=json | jq .[].name -r | cut -d \/ -f 6 
)

INDEX_ID=$(
    gcloud ai indexes list --region=us-central1 --format=json | jq '. | sort_by(.createTime) | .[] | .name' -r | tail -n 1
)

DISPLAY_NAME="deployed_$(date '+%m%d%-H%M')"

gcloud ai index-endpoints deploy-index $ENDPOINT_ID \
  --deployed-index-id=$DISPLAY_NAME \
  --display-name=$DISPLAY_NAME \
  --index=$INDEX_ID \
  --project=$PROJECT \
  --region=us-central1

