E=$(
    gcloud ai index-endpoints list --region=us-central1 --format=json | jq .[].publicEndpointDomainName -r
)

echo $E
