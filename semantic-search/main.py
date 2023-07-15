from google.oauth2 import service_account
import google.cloud.aiplatform_v1beta1 as aiplatform_v1beta1
from vertexai.language_models import TextEmbeddingModel
import os
import click

# 1611865798.us-central1-408118702395.vdb.vertexai.goog
endpoint = os.environ.get("ENDPOINT")
# projects/408118702395/locations/us-central1/indexEndpoints/4425129681519378432
endpoint_name = os.environ.get("ENDPOINT_NAME")
index_id = os.environ.get("INDEX_ID")

def get_vector_array(message: str) -> list:
    model = TextEmbeddingModel.from_pretrained("textembedding-gecko@001")
    embeddings = model.get_embeddings([message])
    for embedding in embeddings:
        vector = embedding.values
    return vector
 

@click.command
@click.argument("message")
def findneighbor_sample(message: str) -> None:
    client_options = {
        "api_endpoint": endpoint
    }

    vertex_ai_client = aiplatform_v1beta1.MatchServiceClient(
        # credentials=credentials,
        client_options=client_options,
    )

    request = aiplatform_v1beta1.FindNeighborsRequest(
        index_endpoint=endpoint_name,
        deployed_index_id=index_id,
    )
    vectored_message = get_vector_array(message)
    print(vectored_message)
    dp1 = aiplatform_v1beta1.IndexDatapoint(
        datapoint_id="0",
        feature_vector=vectored_message,
    )
    query = aiplatform_v1beta1.FindNeighborsRequest.Query(
        datapoint=dp1,
    )
    request.queries.append(query)

response = vertex_ai_client.find_neighbors(request)

print(response)

if __name__ == "__main__":
    findneighbor_sample()
