# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hello.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bhello.proto\x12\x02pb\"\x1c\n\x0cHelloRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x1e\n\rHelloResponse\x12\r\n\x05reply\x18\x01 \x01(\t2<\n\x07Greeter\x12\x31\n\x08SayHello\x12\x10.pb.HelloRequest\x1a\x11.pb.HelloResponse\"\x00\x42\x0bZ\tserver/pbb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'hello_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\tserver/pb'
  _globals['_HELLOREQUEST']._serialized_start=19
  _globals['_HELLOREQUEST']._serialized_end=47
  _globals['_HELLORESPONSE']._serialized_start=49
  _globals['_HELLORESPONSE']._serialized_end=79
  _globals['_GREETER']._serialized_start=81
  _globals['_GREETER']._serialized_end=141
# @@protoc_insertion_point(module_scope)
