# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos1/order_management_python.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%protos1/order_management_python.proto\x12\x10order_management\"\x1c\n\x0cOrderRequest\x12\x0c\n\x04item\x18\x01 \x01(\t\"0\n\rOrderResponse\x12\x0c\n\x04item\x18\x01 \x01(\t\x12\x11\n\ttimestamp\x18\x02 \x01(\t\"M\n\x0c\x44\x65layedReply\x12\x0c\n\x04item\x18\x01 \x01(\t\x12/\n\x07request\x18\x02 \x03(\x0b\x32\x1e.order_management.OrderRequest2\xda\x02\n\x0fOrderManagement\x12P\n\rGetUnaryOrder\x12\x1e.order_management.OrderRequest\x1a\x1f.order_management.OrderResponse\x12O\n\nGetSSOrder\x12\x1e.order_management.OrderRequest\x1a\x1f.order_management.OrderResponse0\x01\x12O\n\nGetCSOrder\x12\x1e.order_management.OrderRequest\x1a\x1f.order_management.OrderResponse(\x01\x12S\n\x0cGetBothOrder\x12\x1e.order_management.OrderRequest\x1a\x1f.order_management.OrderResponse(\x01\x30\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protos1.order_management_python_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_ORDERREQUEST']._serialized_start=59
  _globals['_ORDERREQUEST']._serialized_end=87
  _globals['_ORDERRESPONSE']._serialized_start=89
  _globals['_ORDERRESPONSE']._serialized_end=137
  _globals['_DELAYEDREPLY']._serialized_start=139
  _globals['_DELAYEDREPLY']._serialized_end=216
  _globals['_ORDERMANAGEMENT']._serialized_start=219
  _globals['_ORDERMANAGEMENT']._serialized_end=565
# @@protoc_insertion_point(module_scope)
