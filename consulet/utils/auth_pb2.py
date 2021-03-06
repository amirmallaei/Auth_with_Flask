# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: auth.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='auth.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\nauth.proto\"\x1b\n\ntokeninput\x12\r\n\x05token\x18\x01 \x01(\t\"\x17\n\x06result\x12\r\n\x05\x65mail\x18\x01 \x01(\t23\n\x0fTokenValidation\x12 \n\x08validate\x12\x0b.tokeninput\x1a\x07.resultb\x06proto3'
)




_TOKENINPUT = _descriptor.Descriptor(
  name='tokeninput',
  full_name='tokeninput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='tokeninput.token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=14,
  serialized_end=41,
)


_RESULT = _descriptor.Descriptor(
  name='result',
  full_name='result',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='email', full_name='result.email', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=43,
  serialized_end=66,
)

DESCRIPTOR.message_types_by_name['tokeninput'] = _TOKENINPUT
DESCRIPTOR.message_types_by_name['result'] = _RESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

tokeninput = _reflection.GeneratedProtocolMessageType('tokeninput', (_message.Message,), {
  'DESCRIPTOR' : _TOKENINPUT,
  '__module__' : 'auth_pb2'
  # @@protoc_insertion_point(class_scope:tokeninput)
  })
_sym_db.RegisterMessage(tokeninput)

result = _reflection.GeneratedProtocolMessageType('result', (_message.Message,), {
  'DESCRIPTOR' : _RESULT,
  '__module__' : 'auth_pb2'
  # @@protoc_insertion_point(class_scope:result)
  })
_sym_db.RegisterMessage(result)



_TOKENVALIDATION = _descriptor.ServiceDescriptor(
  name='TokenValidation',
  full_name='TokenValidation',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=68,
  serialized_end=119,
  methods=[
  _descriptor.MethodDescriptor(
    name='validate',
    full_name='TokenValidation.validate',
    index=0,
    containing_service=None,
    input_type=_TOKENINPUT,
    output_type=_RESULT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_TOKENVALIDATION)

DESCRIPTOR.services_by_name['TokenValidation'] = _TOKENVALIDATION

# @@protoc_insertion_point(module_scope)
