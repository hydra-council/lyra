# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: generated/client/manga_client/v1/manga_client.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'generated/client/manga_client/v1/manga_client.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3generated/client/manga_client/v1/manga_client.proto\x12\x0fmanga_client.v1\"\x0f\n\rNewJobRequest\"\x10\n\x0eNewJobResponse\"\x12\n\x10JobStatusRequest\"\x13\n\x11JobStatusResponse\"\x12\n\x10\x43\x61ncelJobRequest\"\x13\n\x11\x43\x61ncelJobResponse2\x8d\x02\n\x12MangaClientService\x12K\n\x06NewJob\x12\x1e.manga_client.v1.NewJobRequest\x1a\x1f.manga_client.v1.NewJobResponse\"\x00\x12T\n\tJobStatus\x12!.manga_client.v1.JobStatusRequest\x1a\".manga_client.v1.JobStatusResponse\"\x00\x12T\n\tCancelJob\x12!.manga_client.v1.CancelJobRequest\x1a\".manga_client.v1.CancelJobResponse\"\x00\x42(Z&hydra/generated/client/manga_client/v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'generated.client.manga_client.v1.manga_client_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z&hydra/generated/client/manga_client/v1'
  _globals['_NEWJOBREQUEST']._serialized_start=72
  _globals['_NEWJOBREQUEST']._serialized_end=87
  _globals['_NEWJOBRESPONSE']._serialized_start=89
  _globals['_NEWJOBRESPONSE']._serialized_end=105
  _globals['_JOBSTATUSREQUEST']._serialized_start=107
  _globals['_JOBSTATUSREQUEST']._serialized_end=125
  _globals['_JOBSTATUSRESPONSE']._serialized_start=127
  _globals['_JOBSTATUSRESPONSE']._serialized_end=146
  _globals['_CANCELJOBREQUEST']._serialized_start=148
  _globals['_CANCELJOBREQUEST']._serialized_end=166
  _globals['_CANCELJOBRESPONSE']._serialized_start=168
  _globals['_CANCELJOBRESPONSE']._serialized_end=187
  _globals['_MANGACLIENTSERVICE']._serialized_start=190
  _globals['_MANGACLIENTSERVICE']._serialized_end=459
# @@protoc_insertion_point(module_scope)
