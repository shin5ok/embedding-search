from vertexai.language_models import TextEmbeddingModel
import click
from uuid import uuid4
import json
import sys
from faker import Faker

out_name: str = "embedding.json"

fake = Faker()

@click.command
@click.argument("file_name")
def gen_embedding(file_name: str) -> dict:
    model = TextEmbeddingModel.from_pretrained("textembedding-gecko@001")
    with open(file_name) as f:
        with open(out_name, "w", encoding='utf-8') as w:
            for line in f.readlines():
                print(line, file=sys.stderr)
                embeddings = model.get_embeddings([line])
                for embedding in embeddings:
                    vector = embedding.values
                r = dict(id=fake.name(), embedding=vector)
                w.write(json.dumps(r))
                w.write("\n")

if __name__ == "__main__":
    gen_embedding()
