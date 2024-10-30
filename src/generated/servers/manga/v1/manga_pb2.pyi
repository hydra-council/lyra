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
    __slots__ = ("repoName", "repoUrl", "jsonRepoUrl", "version", "manifest_version")
    REPONAME_FIELD_NUMBER: _ClassVar[int]
    REPOURL_FIELD_NUMBER: _ClassVar[int]
    JSONREPOURL_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    MANIFEST_VERSION_FIELD_NUMBER: _ClassVar[int]
    repoName: str
    repoUrl: str
    jsonRepoUrl: str
    version: str
    manifest_version: str
    def __init__(self, repoName: _Optional[str] = ..., repoUrl: _Optional[str] = ..., jsonRepoUrl: _Optional[str] = ..., version: _Optional[str] = ..., manifest_version: _Optional[str] = ...) -> None: ...

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
    __slots__ = ("extensionName", "manifest_version", "version", "media_type", "repoUrl", "scriptUrl", "metaDataUrl")
    EXTENSIONNAME_FIELD_NUMBER: _ClassVar[int]
    MANIFEST_VERSION_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    MEDIA_TYPE_FIELD_NUMBER: _ClassVar[int]
    REPOURL_FIELD_NUMBER: _ClassVar[int]
    SCRIPTURL_FIELD_NUMBER: _ClassVar[int]
    METADATAURL_FIELD_NUMBER: _ClassVar[int]
    extensionName: str
    manifest_version: str
    version: str
    media_type: str
    repoUrl: str
    scriptUrl: str
    metaDataUrl: str
    def __init__(self, extensionName: _Optional[str] = ..., manifest_version: _Optional[str] = ..., version: _Optional[str] = ..., media_type: _Optional[str] = ..., repoUrl: _Optional[str] = ..., scriptUrl: _Optional[str] = ..., metaDataUrl: _Optional[str] = ...) -> None: ...

class SearchPluginRequest(_message.Message):
    __slots__ = ("searchQuery", "pluginID")
    SEARCHQUERY_FIELD_NUMBER: _ClassVar[int]
    PLUGINID_FIELD_NUMBER: _ClassVar[int]
    searchQuery: str
    pluginID: str
    def __init__(self, searchQuery: _Optional[str] = ..., pluginID: _Optional[str] = ...) -> None: ...

class SearchPluginResponse(_message.Message):
    __slots__ = ("pong",)
    PONG_FIELD_NUMBER: _ClassVar[int]
    pong: str
    def __init__(self, pong: _Optional[str] = ...) -> None: ...

class RefreshMangaResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RefreshMangaRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MangaMetaData(_message.Message):
    __slots__ = ("title", "alternateTile", "chapters")
    TITLE_FIELD_NUMBER: _ClassVar[int]
    ALTERNATETILE_FIELD_NUMBER: _ClassVar[int]
    CHAPTERS_FIELD_NUMBER: _ClassVar[int]
    title: str
    alternateTile: str
    chapters: _containers.RepeatedCompositeFieldContainer[MangaChapter]
    def __init__(self, title: _Optional[str] = ..., alternateTile: _Optional[str] = ..., chapters: _Optional[_Iterable[_Union[MangaChapter, _Mapping]]] = ...) -> None: ...

class MangaChapter(_message.Message):
    __slots__ = ("chapterNumber", "chapterName", "releaseDateInISO6801", "pages")
    CHAPTERNUMBER_FIELD_NUMBER: _ClassVar[int]
    CHAPTERNAME_FIELD_NUMBER: _ClassVar[int]
    RELEASEDATEINISO6801_FIELD_NUMBER: _ClassVar[int]
    PAGES_FIELD_NUMBER: _ClassVar[int]
    chapterNumber: str
    chapterName: str
    releaseDateInISO6801: str
    pages: _containers.RepeatedCompositeFieldContainer[MangaPage]
    def __init__(self, chapterNumber: _Optional[str] = ..., chapterName: _Optional[str] = ..., releaseDateInISO6801: _Optional[str] = ..., pages: _Optional[_Iterable[_Union[MangaPage, _Mapping]]] = ...) -> None: ...

class MangaPage(_message.Message):
    __slots__ = ("page", "url")
    PAGE_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    page: int
    url: str
    def __init__(self, page: _Optional[int] = ..., url: _Optional[str] = ...) -> None: ...
