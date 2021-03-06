# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/api/expr/v1/value.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/api/expr/v1/value.proto',
  package='google.api.expr.v1',
  syntax='proto3',
  serialized_pb=_b('\n\x1egoogle/api/expr/v1/value.proto\x12\x12google.api.expr.v1\x1a\x19google/protobuf/any.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xd0\x03\n\x05Value\x12\x30\n\nnull_value\x18\x01 \x01(\x0e\x32\x1a.google.protobuf.NullValueH\x00\x12\x14\n\nbool_value\x18\x02 \x01(\x08H\x00\x12\x15\n\x0bint64_value\x18\x03 \x01(\x03H\x00\x12\x16\n\x0cuint64_value\x18\x04 \x01(\x04H\x00\x12\x16\n\x0c\x64ouble_value\x18\x05 \x01(\x01H\x00\x12\x16\n\x0cstring_value\x18\x06 \x01(\tH\x00\x12\x15\n\x0b\x62ytes_value\x18\x07 \x01(\x0cH\x00\x12\x33\n\x0e\x64uration_value\x18\x08 \x01(\x0b\x32\x19.google.protobuf.DurationH\x00\x12\x35\n\x0ftimestamp_value\x18\t \x01(\x0b\x32\x1a.google.protobuf.TimestampH\x00\x12-\n\rmessage_value\x18\n \x01(\x0b\x32\x14.google.protobuf.AnyH\x00\x12\x31\n\tmap_value\x18\x0b \x01(\x0b\x32\x1c.google.api.expr.v1.MapValueH\x00\x12\x33\n\nlist_value\x18\x0c \x01(\x0b\x32\x1d.google.api.expr.v1.ListValueH\x00\x42\x06\n\x04kind\"6\n\tListValue\x12)\n\x06values\x18\x01 \x03(\x0b\x32\x19.google.api.expr.v1.Value\"\x9a\x01\n\x08MapValue\x12\x33\n\x07\x65ntries\x18\x01 \x03(\x0b\x32\".google.api.expr.v1.MapValue.Entry\x1aY\n\x05\x45ntry\x12&\n\x03key\x18\x01 \x01(\x0b\x32\x19.google.api.expr.v1.Value\x12(\n\x05value\x18\x02 \x01(\x0b\x32\x19.google.api.expr.v1.ValueB)\n\x16\x63om.google.api.expr.v1B\nValueProtoP\x01\xf8\x01\x01\x62\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_any__pb2.DESCRIPTOR,google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_VALUE = _descriptor.Descriptor(
  name='Value',
  full_name='google.api.expr.v1.Value',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='null_value', full_name='google.api.expr.v1.Value.null_value', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bool_value', full_name='google.api.expr.v1.Value.bool_value', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='int64_value', full_name='google.api.expr.v1.Value.int64_value', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uint64_value', full_name='google.api.expr.v1.Value.uint64_value', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='double_value', full_name='google.api.expr.v1.Value.double_value', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='string_value', full_name='google.api.expr.v1.Value.string_value', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bytes_value', full_name='google.api.expr.v1.Value.bytes_value', index=6,
      number=7, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='duration_value', full_name='google.api.expr.v1.Value.duration_value', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp_value', full_name='google.api.expr.v1.Value.timestamp_value', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message_value', full_name='google.api.expr.v1.Value.message_value', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='map_value', full_name='google.api.expr.v1.Value.map_value', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='list_value', full_name='google.api.expr.v1.Value.list_value', index=11,
      number=12, type=11, cpp_type=10, label=1,
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
    _descriptor.OneofDescriptor(
      name='kind', full_name='google.api.expr.v1.Value.kind',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=177,
  serialized_end=641,
)


_LISTVALUE = _descriptor.Descriptor(
  name='ListValue',
  full_name='google.api.expr.v1.ListValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='values', full_name='google.api.expr.v1.ListValue.values', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=643,
  serialized_end=697,
)


_MAPVALUE_ENTRY = _descriptor.Descriptor(
  name='Entry',
  full_name='google.api.expr.v1.MapValue.Entry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='google.api.expr.v1.MapValue.Entry.key', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='google.api.expr.v1.MapValue.Entry.value', index=1,
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
  serialized_start=765,
  serialized_end=854,
)

_MAPVALUE = _descriptor.Descriptor(
  name='MapValue',
  full_name='google.api.expr.v1.MapValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entries', full_name='google.api.expr.v1.MapValue.entries', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_MAPVALUE_ENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=700,
  serialized_end=854,
)

_VALUE.fields_by_name['null_value'].enum_type = google_dot_protobuf_dot_struct__pb2._NULLVALUE
_VALUE.fields_by_name['duration_value'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_VALUE.fields_by_name['timestamp_value'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_VALUE.fields_by_name['message_value'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_VALUE.fields_by_name['map_value'].message_type = _MAPVALUE
_VALUE.fields_by_name['list_value'].message_type = _LISTVALUE
_VALUE.oneofs_by_name['kind'].fields.append(
  _VALUE.fields_by_name['null_value'])
_VALUE.fields_by_name['null_value'].containing_oneof = _VALUE.oneofs_by_name['kind']
_VALUE.oneofs_by_name['kind'].fields.append(
  _VALUE.fields_by_name['bool_value'])
_VALUE.fields_by_name['bool_value'].containing_oneof = _VALUE.oneofs_by_name['kind']
_VALUE.oneofs_by_name['kind'].fields.append(
  _VALUE.fields_by_name['int64_value'])
_VALUE.fields_by_name['int64_value'].containing_oneof = _VALUE.oneofs_by_name['kind']
_VALUE.oneofs_by_name['kind'].fields.append(
  _VALUE.fields_by_name['uint64_value'])
_VALUE.fields_by_name['uint64_value'].containing_oneof = _VALUE.oneofs_by_name['kind']
_VALUE.oneofs_by_name['kind'].fields.append(
  _VALUE.fields_by_name['double_value'])
_VALUE.fields_by_name['double_value'].containing_oneof = _VALUE.oneofs_by_name['kind']
_VALUE.oneofs_by_name['kind'].fields.append(
  _VALUE.fields_by_name['string_value'])
_VALUE.fields_by_name['string_value'].containing_oneof = _VALUE.oneofs_by_name['kind']
_VALUE.oneofs_by_name['kind'].fields.append(
  _VALUE.fields_by_name['bytes_value'])
_VALUE.fields_by_name['bytes_value'].containing_oneof = _VALUE.oneofs_by_name['kind']
_VALUE.oneofs_by_name['kind'].fields.append(
  _VALUE.fields_by_name['duration_value'])
_VALUE.fields_by_name['duration_value'].containing_oneof = _VALUE.oneofs_by_name['kind']
_VALUE.oneofs_by_name['kind'].fields.append(
  _VALUE.fields_by_name['timestamp_value'])
_VALUE.fields_by_name['timestamp_value'].containing_oneof = _VALUE.oneofs_by_name['kind']
_VALUE.oneofs_by_name['kind'].fields.append(
  _VALUE.fields_by_name['message_value'])
_VALUE.fields_by_name['message_value'].containing_oneof = _VALUE.oneofs_by_name['kind']
_VALUE.oneofs_by_name['kind'].fields.append(
  _VALUE.fields_by_name['map_value'])
_VALUE.fields_by_name['map_value'].containing_oneof = _VALUE.oneofs_by_name['kind']
_VALUE.oneofs_by_name['kind'].fields.append(
  _VALUE.fields_by_name['list_value'])
_VALUE.fields_by_name['list_value'].containing_oneof = _VALUE.oneofs_by_name['kind']
_LISTVALUE.fields_by_name['values'].message_type = _VALUE
_MAPVALUE_ENTRY.fields_by_name['key'].message_type = _VALUE
_MAPVALUE_ENTRY.fields_by_name['value'].message_type = _VALUE
_MAPVALUE_ENTRY.containing_type = _MAPVALUE
_MAPVALUE.fields_by_name['entries'].message_type = _MAPVALUE_ENTRY
DESCRIPTOR.message_types_by_name['Value'] = _VALUE
DESCRIPTOR.message_types_by_name['ListValue'] = _LISTVALUE
DESCRIPTOR.message_types_by_name['MapValue'] = _MAPVALUE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Value = _reflection.GeneratedProtocolMessageType('Value', (_message.Message,), dict(
  DESCRIPTOR = _VALUE,
  __module__ = 'google.api.expr.v1.value_pb2'
  # @@protoc_insertion_point(class_scope:google.api.expr.v1.Value)
  ))
_sym_db.RegisterMessage(Value)

ListValue = _reflection.GeneratedProtocolMessageType('ListValue', (_message.Message,), dict(
  DESCRIPTOR = _LISTVALUE,
  __module__ = 'google.api.expr.v1.value_pb2'
  # @@protoc_insertion_point(class_scope:google.api.expr.v1.ListValue)
  ))
_sym_db.RegisterMessage(ListValue)

MapValue = _reflection.GeneratedProtocolMessageType('MapValue', (_message.Message,), dict(

  Entry = _reflection.GeneratedProtocolMessageType('Entry', (_message.Message,), dict(
    DESCRIPTOR = _MAPVALUE_ENTRY,
    __module__ = 'google.api.expr.v1.value_pb2'
    # @@protoc_insertion_point(class_scope:google.api.expr.v1.MapValue.Entry)
    ))
  ,
  DESCRIPTOR = _MAPVALUE,
  __module__ = 'google.api.expr.v1.value_pb2'
  # @@protoc_insertion_point(class_scope:google.api.expr.v1.MapValue)
  ))
_sym_db.RegisterMessage(MapValue)
_sym_db.RegisterMessage(MapValue.Entry)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\026com.google.api.expr.v1B\nValueProtoP\001\370\001\001'))
# @@protoc_insertion_point(module_scope)
