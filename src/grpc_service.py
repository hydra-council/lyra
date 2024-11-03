import json

import src.generated.manga.v1.manga_pb2 as mangav1types
import src.generated.manga.v1.manga_pb2_grpc as mangav1
from src.config import logger
from src.generated.types.plugin.v1.plugin_types_pb2 import LoadPluginResponse
from src.script_loader import ScriptLoader, get_module_path


class MangaServicer(mangav1.MangaServiceServicer):
    def LoadPlugin(self, request, context):
        scr = ScriptLoader()
        script_path = request.pluginPath
        module, fullpath  = get_module_path(script_path)
        res, mess = scr.load_script(fullpath, module)
        return LoadPluginResponse(status=json.dumps(mess))

    # Manga management
    def RefreshManga(self, request, context):
        pass

    def SearchPlugin(self, request, context):
        pass