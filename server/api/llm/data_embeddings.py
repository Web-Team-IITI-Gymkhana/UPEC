from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from torch import cuda
from models import Project


embed_model_id = "sentence-transformers/all-MiniLM-L6-v2"

device = f"cuda:{cuda.current_device()}" if cuda.is_available() else "cpu"

embed_model = HuggingFaceEmbeddings(
    model_name=embed_model_id,
    model_kwargs={"device": device},
    encode_kwargs={"device": device, "batch_size": 32},
)

projects = Project.objects.all()
batch_size = 32
metadata = []

for i in range(0, len(projects), batch_size):
    i_end = min(len(projects), i + batch_size)
    batch = projects[i:i_end]
    ids = [project.id for project in batch]
    titles = [project.title for project in batch]
    