from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class InstallRepoRequest(_message.Message):
    __slots__ = ("repoJsonUrl",)
    REPOJSONURL_FIELD_NUMBER: _ClassVar[int]
    repoJsonUrl: str
    def __init__(self, repoJsonUrl: _Optional[str] = ...) -> None: ...

class InstallRepoResponse(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: str
    def __init__(self, status: _Optional[str] = ...) -> None: ...

class RepoRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class RepoResponse(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: str
    def __init__(self, status: _Optional[str] = ...) -> None: ...

class ListRepoRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListRepoResponse(_message.Message):
    __slots__ = ("repos",)
    REPOS_FIELD_NUMBER: _ClassVar[int]
    repos: _containers.RepeatedCompositeFieldContainer[ExtensionRepo]
    def __init__(self, repos: _Optional[_Iterable[_Union[ExtensionRepo, _Mapping]]] = ...) -> None: ...

class ExtensionRepo(_message.Message):
    __slots__ = ("id", "repoName", "repoUrl", "jsonRepoUrl", "version", "manifest_version")
    ID_FIELD_NUMBER: _ClassVar[int]
    REPONAME_FIELD_NUMBER: _ClassVar[int]
    REPOURL_FIELD_NUMBER: _ClassVar[int]
    JSONREPOURL_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    MANIFEST_VERSION_FIELD_NUMBER: _ClassVar[int]
    id: str
    repoName: str
    repoUrl: str
    jsonRepoUrl: str
    version: str
    manifest_version: int
    def __init__(self, id: _Optional[str] = ..., repoName: _Optional[str] = ..., repoUrl: _Optional[str] = ..., jsonRepoUrl: _Optional[str] = ..., version: _Optional[str] = ..., manifest_version: _Optional[int] = ...) -> None: ...

class ExtensionRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class ExtensionResponse(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: str
    def __init__(self, status: _Optional[str] = ...) -> None: ...

class ListExtensionRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListExtensionResponse(_message.Message):
    __slots__ = ("extensions",)
    EXTENSIONS_FIELD_NUMBER: _ClassVar[int]
    extensions: _containers.RepeatedCompositeFieldContainer[Extension]
    def __init__(self, extensions: _Optional[_Iterable[_Union[Extension, _Mapping]]] = ...) -> None: ...

class Extension(_message.Message):
    __slots__ = ("id", "extensionName", "manifest_version", "version", "media_type", "repoUrl", "scriptUrl", "metaDataUrl")
    ID_FIELD_NUMBER: _ClassVar[int]
    EXTENSIONNAME_FIELD_NUMBER: _ClassVar[int]
    MANIFEST_VERSION_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    MEDIA_TYPE_FIELD_NUMBER: _ClassVar[int]
    REPOURL_FIELD_NUMBER: _ClassVar[int]
    SCRIPTURL_FIELD_NUMBER: _ClassVar[int]
    METADATAURL_FIELD_NUMBER: _ClassVar[int]
    id: int
    extensionName: str
    manifest_version: int
    version: str
    media_type: str
    repoUrl: str
    scriptUrl: str
    metaDataUrl: str
    def __init__(self, id: _Optional[int] = ..., extensionName: _Optional[str] = ..., manifest_version: _Optional[int] = ..., version: _Optional[str] = ..., media_type: _Optional[str] = ..., repoUrl: _Optional[str] = ..., scriptUrl: _Optional[str] = ..., metaDataUrl: _Optional[str] = ...) -> None: ...
