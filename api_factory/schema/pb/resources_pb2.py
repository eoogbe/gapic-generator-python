# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/api/experimental/resources.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/api/experimental/resources.proto',
  package='google.api.experimental',
  syntax='proto3',
  serialized_pb=_b('\n\'google/api/experimental/resources.proto\x12\x17google.api.experimental\x1a google/protobuf/descriptor.proto\">\n\x11ResourceReference\x12\x11\n\ttype_name\x18\x01 \x01(\t\x12\x16\n\x0eresource_paths\x18\x02 \x03(\t:9\n\x0eresource_paths\x12\x1f.google.protobuf.MessageOptions\x18\xd8\x94\x03 \x03(\t:a\n\x0cresource_ref\x12\x1d.google.protobuf.FieldOptions\x18\xd9\x94\x03 \x01(\x0b\x32*.google.api.experimental.ResourceReferenceb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_descriptor__pb2.DESCRIPTOR,])


RESOURCE_PATHS_FIELD_NUMBER = 51800
resource_paths = _descriptor.FieldDescriptor(
  name='resource_paths', full_name='google.api.experimental.resource_paths', index=0,
  number=51800, type=9, cpp_type=9, label=3,
  has_default_value=False, default_value=[],
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None, file=DESCRIPTOR)
RESOURCE_REF_FIELD_NUMBER = 51801
resource_ref = _descriptor.FieldDescriptor(
  name='resource_ref', full_name='google.api.experimental.resource_ref', index=1,
  number=51801, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None, file=DESCRIPTOR)


_RESOURCEREFERENCE = _descriptor.Descriptor(
  name='ResourceReference',
  full_name='google.api.experimental.ResourceReference',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type_name', full_name='google.api.experimental.ResourceReference.type_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='resource_paths', full_name='google.api.experimental.ResourceReference.resource_paths', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=102,
  serialized_end=164,
)

DESCRIPTOR.message_types_by_name['ResourceReference'] = _RESOURCEREFERENCE
DESCRIPTOR.extensions_by_name['resource_paths'] = resource_paths
DESCRIPTOR.extensions_by_name['resource_ref'] = resource_ref
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ResourceReference = _reflection.GeneratedProtocolMessageType('ResourceReference', (_message.Message,), dict(
  DESCRIPTOR = _RESOURCEREFERENCE,
  __module__ = 'google.api.experimental.resources_pb2'
  # @@protoc_insertion_point(class_scope:google.api.experimental.ResourceReference)
  ))
_sym_db.RegisterMessage(ResourceReference)

google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(resource_paths)
resource_ref.message_type = _RESOURCEREFERENCE
google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(resource_ref)

# @@protoc_insertion_point(module_scope)
