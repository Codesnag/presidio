# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: scheduler.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import stream_pb2 as stream__pb2
import scan_pb2 as scan__pb2
import template_pb2 as template__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='scheduler.proto',
  package='types',
  syntax='proto3',
  serialized_pb=_b('\n\x0fscheduler.proto\x12\x05types\x1a\x0cstream.proto\x1a\nscan.proto\x1a\x0etemplate.proto\"y\n\x18ScannerCronJobApiRequest\x12 \n\x18ScannerCronJobTemplateId\x18\x01 \x01(\t\x12;\n\x15scannerCronJobRequest\x18\x02 \x01(\x0b\x32\x1c.types.ScannerCronJobRequest\"o\n\x15ScannerCronJobRequest\x12\x0c\n\x04Name\x18\x01 \x01(\t\x12\x1f\n\x07trigger\x18\x02 \x01(\x0b\x32\x0e.types.Trigger\x12\'\n\x0bscanRequest\x18\x03 \x01(\x0b\x32\x12.types.ScanRequest\"\x18\n\x16ScannerCronJobResponse\"i\n\x14StreamsJobApiRequest\x12\x1c\n\x14StreamsJobTemplateId\x18\x01 \x01(\t\x12\x33\n\x11streamsJobRequest\x18\x02 \x01(\x0b\x32\x18.types.StreamsJobRequest\"O\n\x11StreamsJobRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12,\n\x0estreamsRequest\x18\x02 \x01(\x0b\x32\x14.types.StreamRequest\"\x14\n\x12StreamsJobResponse2\xa4\x01\n\x10SchedulerService\x12\x44\n\x0b\x41pplyStream\x12\x18.types.StreamsJobRequest\x1a\x19.types.StreamsJobResponse\"\x00\x12J\n\tApplyScan\x12\x1c.types.ScannerCronJobRequest\x1a\x1d.types.ScannerCronJobResponse\"\x00\x62\x06proto3')
  ,
  dependencies=[stream__pb2.DESCRIPTOR,scan__pb2.DESCRIPTOR,template__pb2.DESCRIPTOR,])




_SCANNERCRONJOBAPIREQUEST = _descriptor.Descriptor(
  name='ScannerCronJobApiRequest',
  full_name='types.ScannerCronJobApiRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ScannerCronJobTemplateId', full_name='types.ScannerCronJobApiRequest.ScannerCronJobTemplateId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scannerCronJobRequest', full_name='types.ScannerCronJobApiRequest.scannerCronJobRequest', index=1,
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
  serialized_start=68,
  serialized_end=189,
)


_SCANNERCRONJOBREQUEST = _descriptor.Descriptor(
  name='ScannerCronJobRequest',
  full_name='types.ScannerCronJobRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Name', full_name='types.ScannerCronJobRequest.Name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='trigger', full_name='types.ScannerCronJobRequest.trigger', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scanRequest', full_name='types.ScannerCronJobRequest.scanRequest', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=191,
  serialized_end=302,
)


_SCANNERCRONJOBRESPONSE = _descriptor.Descriptor(
  name='ScannerCronJobResponse',
  full_name='types.ScannerCronJobResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=304,
  serialized_end=328,
)


_STREAMSJOBAPIREQUEST = _descriptor.Descriptor(
  name='StreamsJobApiRequest',
  full_name='types.StreamsJobApiRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='StreamsJobTemplateId', full_name='types.StreamsJobApiRequest.StreamsJobTemplateId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='streamsJobRequest', full_name='types.StreamsJobApiRequest.streamsJobRequest', index=1,
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
  serialized_start=330,
  serialized_end=435,
)


_STREAMSJOBREQUEST = _descriptor.Descriptor(
  name='StreamsJobRequest',
  full_name='types.StreamsJobRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='types.StreamsJobRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='streamsRequest', full_name='types.StreamsJobRequest.streamsRequest', index=1,
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
  serialized_start=437,
  serialized_end=516,
)


_STREAMSJOBRESPONSE = _descriptor.Descriptor(
  name='StreamsJobResponse',
  full_name='types.StreamsJobResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=518,
  serialized_end=538,
)

_SCANNERCRONJOBAPIREQUEST.fields_by_name['scannerCronJobRequest'].message_type = _SCANNERCRONJOBREQUEST
_SCANNERCRONJOBREQUEST.fields_by_name['trigger'].message_type = template__pb2._TRIGGER
_SCANNERCRONJOBREQUEST.fields_by_name['scanRequest'].message_type = scan__pb2._SCANREQUEST
_STREAMSJOBAPIREQUEST.fields_by_name['streamsJobRequest'].message_type = _STREAMSJOBREQUEST
_STREAMSJOBREQUEST.fields_by_name['streamsRequest'].message_type = stream__pb2._STREAMREQUEST
DESCRIPTOR.message_types_by_name['ScannerCronJobApiRequest'] = _SCANNERCRONJOBAPIREQUEST
DESCRIPTOR.message_types_by_name['ScannerCronJobRequest'] = _SCANNERCRONJOBREQUEST
DESCRIPTOR.message_types_by_name['ScannerCronJobResponse'] = _SCANNERCRONJOBRESPONSE
DESCRIPTOR.message_types_by_name['StreamsJobApiRequest'] = _STREAMSJOBAPIREQUEST
DESCRIPTOR.message_types_by_name['StreamsJobRequest'] = _STREAMSJOBREQUEST
DESCRIPTOR.message_types_by_name['StreamsJobResponse'] = _STREAMSJOBRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ScannerCronJobApiRequest = _reflection.GeneratedProtocolMessageType('ScannerCronJobApiRequest', (_message.Message,), dict(
  DESCRIPTOR = _SCANNERCRONJOBAPIREQUEST,
  __module__ = 'scheduler_pb2'
  # @@protoc_insertion_point(class_scope:types.ScannerCronJobApiRequest)
  ))
_sym_db.RegisterMessage(ScannerCronJobApiRequest)

ScannerCronJobRequest = _reflection.GeneratedProtocolMessageType('ScannerCronJobRequest', (_message.Message,), dict(
  DESCRIPTOR = _SCANNERCRONJOBREQUEST,
  __module__ = 'scheduler_pb2'
  # @@protoc_insertion_point(class_scope:types.ScannerCronJobRequest)
  ))
_sym_db.RegisterMessage(ScannerCronJobRequest)

ScannerCronJobResponse = _reflection.GeneratedProtocolMessageType('ScannerCronJobResponse', (_message.Message,), dict(
  DESCRIPTOR = _SCANNERCRONJOBRESPONSE,
  __module__ = 'scheduler_pb2'
  # @@protoc_insertion_point(class_scope:types.ScannerCronJobResponse)
  ))
_sym_db.RegisterMessage(ScannerCronJobResponse)

StreamsJobApiRequest = _reflection.GeneratedProtocolMessageType('StreamsJobApiRequest', (_message.Message,), dict(
  DESCRIPTOR = _STREAMSJOBAPIREQUEST,
  __module__ = 'scheduler_pb2'
  # @@protoc_insertion_point(class_scope:types.StreamsJobApiRequest)
  ))
_sym_db.RegisterMessage(StreamsJobApiRequest)

StreamsJobRequest = _reflection.GeneratedProtocolMessageType('StreamsJobRequest', (_message.Message,), dict(
  DESCRIPTOR = _STREAMSJOBREQUEST,
  __module__ = 'scheduler_pb2'
  # @@protoc_insertion_point(class_scope:types.StreamsJobRequest)
  ))
_sym_db.RegisterMessage(StreamsJobRequest)

StreamsJobResponse = _reflection.GeneratedProtocolMessageType('StreamsJobResponse', (_message.Message,), dict(
  DESCRIPTOR = _STREAMSJOBRESPONSE,
  __module__ = 'scheduler_pb2'
  # @@protoc_insertion_point(class_scope:types.StreamsJobResponse)
  ))
_sym_db.RegisterMessage(StreamsJobResponse)



_SCHEDULERSERVICE = _descriptor.ServiceDescriptor(
  name='SchedulerService',
  full_name='types.SchedulerService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=541,
  serialized_end=705,
  methods=[
  _descriptor.MethodDescriptor(
    name='ApplyStream',
    full_name='types.SchedulerService.ApplyStream',
    index=0,
    containing_service=None,
    input_type=_STREAMSJOBREQUEST,
    output_type=_STREAMSJOBRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ApplyScan',
    full_name='types.SchedulerService.ApplyScan',
    index=1,
    containing_service=None,
    input_type=_SCANNERCRONJOBREQUEST,
    output_type=_SCANNERCRONJOBRESPONSE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SCHEDULERSERVICE)

DESCRIPTOR.services_by_name['SchedulerService'] = _SCHEDULERSERVICE

# @@protoc_insertion_point(module_scope)
