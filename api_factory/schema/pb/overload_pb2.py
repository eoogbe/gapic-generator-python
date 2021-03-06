# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/api/experimental/overload.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api_factory.schema.pb.expr.v1 import syntax_pb2 as google_dot_api_dot_expr_dot_v1_dot_syntax__pb2
from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/api/experimental/overload.proto',
  package='google.api.experimental',
  syntax='proto3',
  serialized_pb=_b('\n&google/api/experimental/overload.proto\x12\x17google.api.experimental\x1a\x1fgoogle/api/expr/v1/syntax.proto\x1a google/protobuf/descriptor.proto\"\x89\x02\n\x08Overload\x12\x0c\n\x04name\x18\x01 \x01(\t\x12K\n\x10\x63omponent_fields\x18\n \x01(\x0b\x32\x31.google.api.experimental.Overload.ComponentFields\x1a\xa1\x01\n\x0f\x43omponentFields\x12G\n\x06\x66ields\x18\x01 \x03(\x0b\x32\x37.google.api.experimental.Overload.ComponentFields.Field\x1a\x45\n\x05\x46ield\x12\x0c\n\x04path\x18\x01 \x01(\t\x12.\n\x0c\x64\x65\x66\x61ult_expr\x18\x02 \x01(\x0b\x32\x18.google.api.expr.v1.Expr:V\n\toverloads\x12\x1e.google.protobuf.MethodOptions\x18\xac\x92\x03 \x03(\x0b\x32!.google.api.experimental.Overloadb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_expr_dot_v1_dot_syntax__pb2.DESCRIPTOR,google_dot_protobuf_dot_descriptor__pb2.DESCRIPTOR,])


OVERLOADS_FIELD_NUMBER = 51500
overloads = _descriptor.FieldDescriptor(
  name='overloads', full_name='google.api.experimental.overloads', index=0,
  number=51500, type=11, cpp_type=10, label=3,
  has_default_value=False, default_value=[],
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None, file=DESCRIPTOR)


_OVERLOAD_COMPONENTFIELDS_FIELD = _descriptor.Descriptor(
  name='Field',
  full_name='google.api.experimental.Overload.ComponentFields.Field',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='path', full_name='google.api.experimental.Overload.ComponentFields.Field.path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='default_expr', full_name='google.api.experimental.Overload.ComponentFields.Field.default_expr', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=331,
  serialized_end=400,
)

_OVERLOAD_COMPONENTFIELDS = _descriptor.Descriptor(
  name='ComponentFields',
  full_name='google.api.experimental.Overload.ComponentFields',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fields', full_name='google.api.experimental.Overload.ComponentFields.fields', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_OVERLOAD_COMPONENTFIELDS_FIELD, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=239,
  serialized_end=400,
)

_OVERLOAD = _descriptor.Descriptor(
  name='Overload',
  full_name='google.api.experimental.Overload',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.api.experimental.Overload.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='component_fields', full_name='google.api.experimental.Overload.component_fields', index=1,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_OVERLOAD_COMPONENTFIELDS, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=135,
  serialized_end=400,
)

_OVERLOAD_COMPONENTFIELDS_FIELD.fields_by_name['default_expr'].message_type = google_dot_api_dot_expr_dot_v1_dot_syntax__pb2._EXPR
_OVERLOAD_COMPONENTFIELDS_FIELD.containing_type = _OVERLOAD_COMPONENTFIELDS
_OVERLOAD_COMPONENTFIELDS.fields_by_name['fields'].message_type = _OVERLOAD_COMPONENTFIELDS_FIELD
_OVERLOAD_COMPONENTFIELDS.containing_type = _OVERLOAD
_OVERLOAD.fields_by_name['component_fields'].message_type = _OVERLOAD_COMPONENTFIELDS
DESCRIPTOR.message_types_by_name['Overload'] = _OVERLOAD
DESCRIPTOR.extensions_by_name['overloads'] = overloads
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Overload = _reflection.GeneratedProtocolMessageType('Overload', (_message.Message,), dict(

  ComponentFields = _reflection.GeneratedProtocolMessageType('ComponentFields', (_message.Message,), dict(

    Field = _reflection.GeneratedProtocolMessageType('Field', (_message.Message,), dict(
      DESCRIPTOR = _OVERLOAD_COMPONENTFIELDS_FIELD,
      __module__ = 'google.api.experimental.overload_pb2'
      # @@protoc_insertion_point(class_scope:google.api.experimental.Overload.ComponentFields.Field)
      ))
    ,
    DESCRIPTOR = _OVERLOAD_COMPONENTFIELDS,
    __module__ = 'google.api.experimental.overload_pb2'
    # @@protoc_insertion_point(class_scope:google.api.experimental.Overload.ComponentFields)
    ))
  ,
  DESCRIPTOR = _OVERLOAD,
  __module__ = 'google.api.experimental.overload_pb2'
  # @@protoc_insertion_point(class_scope:google.api.experimental.Overload)
  ))
_sym_db.RegisterMessage(Overload)
_sym_db.RegisterMessage(Overload.ComponentFields)
_sym_db.RegisterMessage(Overload.ComponentFields.Field)

overloads.message_type = _OVERLOAD
google_dot_protobuf_dot_descriptor__pb2.MethodOptions.RegisterExtension(overloads)

# @@protoc_insertion_point(module_scope)
