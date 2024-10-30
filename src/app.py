from concurrent import futures
import grpc

from script_loader import ScriptLoader
import generated.servers.manga.v1.manga_pb2_grpc as mangav1
import generated.servers.manga.v1.manga_pb2 as mangav1types
from src.config import addr
from src.database.tables import init_database

script_manager = ScriptLoader()

init_database()

class MangaServicer(mangav1.MangaServiceServicer):
    def InstallPlugin(self, request, context):
        return super().InstallPlugin(request, context)

    def DeletePlugin(self, request, context):
        f = mangav1types.DeletePluginRequest()
        return super().DeletePlugin(request, context)

    def SearchPlugin(self, request, context):
        print(request.pluginID)
        print(request.searchQuery)

        f = mangav1types.SearchPluginResponse()
        f.pong = "asd"
        return f


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    mangav1.add_MangaServiceServicer_to_server(MangaServicer(), server)
    server.add_insecure_port(addr)
    print(f"Server started at {addr}")
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
