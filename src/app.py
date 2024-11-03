import os
from concurrent import futures
import grpc

from script_loader import ScriptLoader
import src.generated.manga.v1.manga_pb2_grpc as mangav1

from src.config import addr
from src.grpc_service import MangaServicer

is_docker = os.environ.get("IS_DOCKER")
plugin_dir = os.environ.get("hydra_plugin_dir")
if is_docker is not None and plugin_dir is None:
    raise Exception("Plugin dir not found")

print("Plugin dir is set as ", plugin_dir, "lyra will load modules using the same base path")

script_manager = ScriptLoader()


# script_manager.load_script('D:\\Dev\\Go\\constellations\\hydra\\plugin\\d59c453a-98ea-11ef-88b1-089df4abb4f0\\manganato.py', 'd59c453a-98ea-11ef-88b1-089df4abb4f0.manganato')

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    mangav1.add_MangaServiceServicer_to_server(MangaServicer(), server)
    server.add_insecure_port(addr)
    print(f"Server started at {addr}")
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
