from armada_client.client import ArmadaClient
import grpc
from armada_client.k8s.io.api.core.v1 import generated_pb2 as core_v1
from armada_client.k8s.io.apimachinery.pkg.api.resource import (
    generated_pb2 as api_resource,
)


channel = grpc.insecure_channel(f"localhost:50051")

client = ArmadaClient(channel)

# Create Queue 

queue_req = client.create_queue_request(name='test', priority_factor=1.0)
print(client.create_queue(queue_req))
