from vertexai.language_models import TextEmbeddingModel
import click
from uuid import uuid4
import json

@click.command
@click.argument("file_name")
def gen_embedding(file_name: str) -> dict:
    model = TextEmbeddingModel.from_pretrained("textembedding-gecko@001")
    with open(file_name) as f:
        for line in f.readline():
            embeddings = model.get_embeddings([line])
            for embedding in embeddings:
                vector = embedding.values
            r = dict(id=str(uuid4()), embedding=vector)
            print(json.dumps(r))

if __name__ == "__main__":
    gen_embedding()
