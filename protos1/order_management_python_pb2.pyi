from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OrderRequest(_message.Message):
    __slots__ = ("item",)
    ITEM_FIELD_NUMBER: _ClassVar[int]
    item: str
    def __init__(self, item: _Optional[str] = ...) -> None: ...

class OrderResponse(_message.Message):
    __slots__ = ("item", "timestamp")
    ITEM_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    item: str
    timestamp: str
    def __init__(self, item: _Optional[str] = ..., timestamp: _Optional[str] = ...) -> None: ...

class DelayedReply(_message.Message):
    __slots__ = ("item", "request")
    ITEM_FIELD_NUMBER: _ClassVar[int]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    item: str
    request: _containers.RepeatedCompositeFieldContainer[OrderRequest]
    def __init__(self, item: _Optional[str] = ..., request: _Optional[_Iterable[_Union[OrderRequest, _Mapping]]] = ...) -> None: ...
