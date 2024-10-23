from concurrent import futures

import grpc

from script_loader import ScriptLoader
import generated.servers.manga.v1.manga_pb2_grpc as mangav1
import generated.servers.manga.v1.manga_pb2 as mangav1types

port = 55001
host = '0.0.0.0'
addr = f"{host}:{port}"
script_manager = ScriptLoader()


def load_s():
    script_manager.load_script('../extensions/manganato.py', 'extensions')
    try:
        metadata = script_manager.get_book('https://chapmanganato.to/manga-ri994991/')
        print(metadata)
    except Exception as e:
        print(e)



load_s()


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
