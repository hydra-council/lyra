from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

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
