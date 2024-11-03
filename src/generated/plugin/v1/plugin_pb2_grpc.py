# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from types.plugin.v1 import plugin_types_pb2 as types_dot_plugin_dot_v1_dot_plugin__types__pb2

GRPC_GENERATED_VERSION = '1.67.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in plugin/v1/plugin_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class PluginServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.InstallRepo = channel.unary_unary(
                '/plugin.v1.PluginService/InstallRepo',
                request_serializer=types_dot_plugin_dot_v1_dot_plugin__types__pb2.InstallRepoRequest.SerializeToString,
                response_deserializer=types_dot_plugin_dot_v1_dot_plugin__types__pb2.InstallRepoResponse.FromString,
                _registered_method=True)
        self.UninstallRepo = channel.unary_unary(
                '/plugin.v1.PluginService/UninstallRepo',
                request_serializer=types_dot_plugin_dot_v1_dot_plugin__types__pb2.RepoRequest.SerializeToString,
                response_deserializer=types_dot_plugin_dot_v1_dot_plugin__types__pb2.RepoResponse.FromString,
                _registered_method=True)
        self.UpdateRepo = channel.unary_unary(
                '/plugin.v1.PluginService/UpdateRepo',
                request_serializer=types_dot_plugin_dot_v1_dot_plugin__types__pb2.RepoRequest.SerializeToString,
                response_deserializer=types_dot_plugin_dot_v1_dot_plugin__types__pb2.RepoResponse.FromString,
                _registered_method=True)
        self.ListRepos = channel.unary_unary(
                '/plugin.v1.PluginService/ListRepos',
                request_serializer=types_dot_plugin_dot_v1_dot_plugin__types__pb2.ListRepoRequest.SerializeToString,
                response_deserializer=types_dot_plugin_dot_v1_dot_plugin__types__pb2.ListRepoResponse.FromString,
                _registered_method=True)
        self.InstallExtension = channel.unary_unary(
                '/plugin.v1.PluginService/InstallExtension',
                request_serializer=types_dot_plugin_dot_v1_dot_plugin__types__pb2.ExtensionRequest.SerializeToString,
                response_deserializer=types_dot_plugin_dot_v1_dot_plugin__types__pb2.ExtensionResponse.FromString,
                _registered_method=True)
        self.UninstallExtension = channel.unary_unary(
                '/plugin.v1.PluginService/UninstallExtension',
                request_serializer=types_dot_plugin_dot_v1_dot_plugin__types__pb2.ExtensionRequest.SerializeToString,
                response_deserializer=types_dot_plugin_dot_v1_dot_plugin__types__pb2.ExtensionResponse.FromString,
                _registered_method=True)
        self.UpdateExtension = channel.unary_unary(
                '/plugin.v1.PluginService/UpdateExtension',
                request_serializer=types_dot_plugin_dot_v1_dot_plugin__types__pb2.ExtensionRequest.SerializeToString,
                response_deserializer=types_dot_plugin_dot_v1_dot_plugin__types__pb2.ExtensionResponse.FromString,
                _registered_method=True)
        self.ListExtensions = channel.unary_unary(
                '/plugin.v1.PluginService/ListExtensions',
                request_serializer=types_dot_plugin_dot_v1_dot_plugin__types__pb2.ListExtensionRequest.SerializeToString,
                response_deserializer=types_dot_plugin_dot_v1_dot_plugin__types__pb2.ListExtensionResponse.FromString,
                _registered_method=True)


class PluginServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def InstallRepo(self, request, context):
        """//////////////////////////////////////////////////////////////////////////////////////
        repo management
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UninstallRepo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateRepo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListRepos(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def InstallExtension(self, request, context):
        """//////////////////////////////////////////////////////////////////////////////////////
        extension management
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UninstallExtension(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateExtension(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListExtensions(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PluginServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'InstallRepo': grpc.unary_unary_rpc_method_handler(
                    servicer.InstallRepo,
                    request_deserializer=types_dot_plugin_dot_v1_dot_plugin__types__pb2.InstallRepoRequest.FromString,
                    response_serializer=types_dot_plugin_dot_v1_dot_plugin__types__pb2.InstallRepoResponse.SerializeToString,
            ),
            'UninstallRepo': grpc.unary_unary_rpc_method_handler(
                    servicer.UninstallRepo,
                    request_deserializer=types_dot_plugin_dot_v1_dot_plugin__types__pb2.RepoRequest.FromString,
                    response_serializer=types_dot_plugin_dot_v1_dot_plugin__types__pb2.RepoResponse.SerializeToString,
            ),
            'UpdateRepo': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateRepo,
                    request_deserializer=types_dot_plugin_dot_v1_dot_plugin__types__pb2.RepoRequest.FromString,
                    response_serializer=types_dot_plugin_dot_v1_dot_plugin__types__pb2.RepoResponse.SerializeToString,
            ),
            'ListRepos': grpc.unary_unary_rpc_method_handler(
                    servicer.ListRepos,
                    request_deserializer=types_dot_plugin_dot_v1_dot_plugin__types__pb2.ListRepoRequest.FromString,
                    response_serializer=types_dot_plugin_dot_v1_dot_plugin__types__pb2.ListRepoResponse.SerializeToString,
            ),
            'InstallExtension': grpc.unary_unary_rpc_method_handler(
                    servicer.InstallExtension,
                    request_deserializer=types_dot_plugin_dot_v1_dot_plugin__types__pb2.ExtensionRequest.FromString,
                    response_serializer=types_dot_plugin_dot_v1_dot_plugin__types__pb2.ExtensionResponse.SerializeToString,
            ),
            'UninstallExtension': grpc.unary_unary_rpc_method_handler(
                    servicer.UninstallExtension,
                    request_deserializer=types_dot_plugin_dot_v1_dot_plugin__types__pb2.ExtensionRequest.FromString,
                    response_serializer=types_dot_plugin_dot_v1_dot_plugin__types__pb2.ExtensionResponse.SerializeToString,
            ),
            'UpdateExtension': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateExtension,
                    request_deserializer=types_dot_plugin_dot_v1_dot_plugin__types__pb2.ExtensionRequest.FromString,
                    response_serializer=types_dot_plugin_dot_v1_dot_plugin__types__pb2.ExtensionResponse.SerializeToString,
            ),
            'ListExtensions': grpc.unary_unary_rpc_method_handler(
                    servicer.ListExtensions,
                    request_deserializer=types_dot_plugin_dot_v1_dot_plugin__types__pb2.ListExtensionRequest.FromString,
                    response_serializer=types_dot_plugin_dot_v1_dot_plugin__types__pb2.ListExtensionResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'plugin.v1.PluginService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('plugin.v1.PluginService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class PluginService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def InstallRepo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/plugin.v1.PluginService/InstallRepo',
            types_dot_plugin_dot_v1_dot_plugin__types__pb2.InstallRepoRequest.SerializeToString,
            types_dot_plugin_dot_v1_dot_plugin__types__pb2.InstallRepoResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def UninstallRepo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/plugin.v1.PluginService/UninstallRepo',
            types_dot_plugin_dot_v1_dot_plugin__types__pb2.RepoRequest.SerializeToString,
            types_dot_plugin_dot_v1_dot_plugin__types__pb2.RepoResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def UpdateRepo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/plugin.v1.PluginService/UpdateRepo',
            types_dot_plugin_dot_v1_dot_plugin__types__pb2.RepoRequest.SerializeToString,
            types_dot_plugin_dot_v1_dot_plugin__types__pb2.RepoResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ListRepos(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/plugin.v1.PluginService/ListRepos',
            types_dot_plugin_dot_v1_dot_plugin__types__pb2.ListRepoRequest.SerializeToString,
            types_dot_plugin_dot_v1_dot_plugin__types__pb2.ListRepoResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def InstallExtension(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/plugin.v1.PluginService/InstallExtension',
            types_dot_plugin_dot_v1_dot_plugin__types__pb2.ExtensionRequest.SerializeToString,
            types_dot_plugin_dot_v1_dot_plugin__types__pb2.ExtensionResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def UninstallExtension(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/plugin.v1.PluginService/UninstallExtension',
            types_dot_plugin_dot_v1_dot_plugin__types__pb2.ExtensionRequest.SerializeToString,
            types_dot_plugin_dot_v1_dot_plugin__types__pb2.ExtensionResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def UpdateExtension(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/plugin.v1.PluginService/UpdateExtension',
            types_dot_plugin_dot_v1_dot_plugin__types__pb2.ExtensionRequest.SerializeToString,
            types_dot_plugin_dot_v1_dot_plugin__types__pb2.ExtensionResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ListExtensions(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/plugin.v1.PluginService/ListExtensions',
            types_dot_plugin_dot_v1_dot_plugin__types__pb2.ListExtensionRequest.SerializeToString,
            types_dot_plugin_dot_v1_dot_plugin__types__pb2.ListExtensionResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
