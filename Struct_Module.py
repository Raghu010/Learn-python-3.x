#Struct module in python.

"""This module make conversions between python values and C struct represented as python bytes object. Format strings are the mechanism used to specify the expected
layout when packing and unpacking the data."""

"""packing: Return a string containing the values v1, v2, … , that are packed according to the given format (Format strings are the mechanism used to specify the
expected layout when packing and unpacking data).The values followed by the format must be as per the format only, else struct.error is raised."""


import struct
var = struct.pack('hhl', 1, 2, 3)
print(var)

#example2:
import struct
var = struct.pack('iii', 1, 2, 3)
print(var)

"""Unpacking: Return the values v1, v2, … , that are unpacked according to the given format(1st argument). Values returned by this function are returned as tuples of
size that is equal to the number of values passed through struct.pack() during packing."""


#examples for packing and unpacking.
import struct
var = struct.pack('?hil', True, 2, 5, 445)
print(var)

var = struct.unpack('?hil', var)
print(var)

var = struct.pack('qf', 2, 3.2)
print(var)

tup = struct.unpack('qf', var)
print(tup)

"""clacsize(): Return the size of the struct (and hence of the string) corresponding to the given format. calcsize() is important function, and is required for
function such as struct.pack_into() and struct.unpack_from(), which require offset value and buffer as well."""

#examples for struct.calcsize()

import struct
a = struct.pack('?hil', True, 2, 5, 445)
print(a)
print(struct.calcsize('?hil'))
print(struct.calcsize('qf'))

#More examples:
import struct
b = struct.pack('bi', 56, 0x12131415)
print(b)
print(struct.calcsize('bi'))

c = struct.pack('ib', 0x12131415, 56)
print(c)
print(struct.calcsize('ib'))

#Exception struct.error.
#Exception struct.error describes what is wrong at the passing arguments, when a wrong argument is passed struct.error is raised.

from struct import error
print(error)

"""struct.passinfo():
Syntax:
struct.pack_into(fmt, buffer, offset, v1, v2, ...)
fmt: data type format
buffer: writable buffer which starts at offset (optional)
v1,v2.. : values."""

"""struct.unpack_from():
Syntax:
struct.unpack_from(fmt, buffer[,offset = 0])fmt: data type format
buffer: writable buffer which starts at offset (optional)."""

import struct
import ctypes

siz = struct.calcsize('hhl')
print(siz)

buf = ctypes.create_string_buffer(siz)
x = struct.pack('hhl', 1, 2, 3)
print(x)
print(struct.unpack('hhl', x))
struct.pack_into('hhl', buf, 0, 1, 2, 3) # struct.pack_into() packs data into buff, doesn't return any value.
print(struct.unpack_from('hhl', buf, 0)) # struct.unpack_from() unpacks data from buff, returns a tuple of values.
