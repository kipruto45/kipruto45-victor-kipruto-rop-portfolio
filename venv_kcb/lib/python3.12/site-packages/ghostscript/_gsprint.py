#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
ghostscript._gsprint - A low-lewel interface to the Ghostscript C-API using ctypes
"""
#
# This file is part of python-ghostscript.
# Copyright 2010-2023 by Hartmut Goebel <h.goebel@crazy-compilers.com>
#
# Display_callback Structure by Lasse Fister <commander@graphicore.de> in 2013
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
#

__author__ = "Hartmut Goebel <h.goebel@crazy-compilers.com>"
__copyright__ = "Copyright 2010-2023 by Hartmut Goebel <h.goebel@crazy-compilers.com>"
__licence__ = "GNU General Public License version 3 (GPL v3)"
__version__ = "0.8.1"

from ctypes import *
import sys

from ._errors import *

MAX_STRING_LENGTH = 65535

ARG_ENCODING_LOCAL = 0
ARG_ENCODING_UTF8 = 1
ARG_ENCODING_UTF16LE = 2

DISPLAY_VERSION_MAJOR = 2
DISPLAY_VERSION_MINOR = 0

DISPLAY_VERSION_MAJOR_V1 = 1  # before separation format was added
DISPLAY_VERSION_MINOR_V1 = 0

# The display format is set by a combination of the following bitfields

# Define the color space alternatives
# DISPLAY_FORMAT_COLOR
DISPLAY_COLORS_NATIVE     = (1 << 0)
DISPLAY_COLORS_GRAY       = (1 << 1)
DISPLAY_COLORS_RGB        = (1 << 2)
DISPLAY_COLORS_CMYK       = (1 << 3)
DISPLAY_COLORS_SEPARATION = (1 << 19)

DISPLAY_COLORS_MASK = 0x8000f

# Define whether alpha information, or an extra unused bytes is included
# DISPLAY_ALPHA_FIRST and DISPLAY_ALPHA_LAST are not implemented
# DISPLAY_FORMAT_ALPHA
DISPLAY_ALPHA_NONE   = (0 << 4)
DISPLAY_ALPHA_FIRST  = (1 << 4)
DISPLAY_ALPHA_LAST   = (1 << 5)
DISPLAY_UNUSED_FIRST = (1 << 6)  # e.g. Mac xRGB
DISPLAY_UNUSED_LAST  = (1 << 7)  # e.g. Windows BGRx

DISPLAY_ALPHA_MASK = 0x00f0

# Define the depth per component for DISPLAY_COLORS_GRAY,
# DISPLAY_COLORS_RGB and DISPLAY_COLORS_CMYK,
# or the depth per pixel for DISPLAY_COLORS_NATIVE
# DISPLAY_DEPTH_2 and DISPLAY_DEPTH_12 have not been tested.
# DISPLAY_FORMAT_DEPTH
DISPLAY_DEPTH_1  = (1 << 8)
DISPLAY_DEPTH_2  = (1 << 9)
DISPLAY_DEPTH_4  = (1 << 10)
DISPLAY_DEPTH_8  = (1 << 11)
DISPLAY_DEPTH_12 = (1 << 12)
DISPLAY_DEPTH_16 = (1 << 13)
# unused (1<<14)
# unused (1<<15)

DISPLAY_DEPTH_MASK = 0xff00

# Define whether Red/Cyan should come first,
# or whether Blue/Black should come first
# DISPLAY_FORMAT_ENDIAN
DISPLAY_BIGENDIAN    = (0 << 16)  # Red/Cyan first
DISPLAY_LITTLEENDIAN = (1 << 16)  # Blue/Black first

DISPLAY_ENDIAN_MASK = 0x00010000

# Define whether the raster starts at the top or bottom of the bitmap
# DISPLAY_FORMAT_FIRSTROW
DISPLAY_TOPFIRST    = (0 << 17)  # Unix, Mac
DISPLAY_BOTTOMFIRST = (1 << 17)  # Windows

DISPLAY_FIRSTROW_MASK = 0x00020000

# Define whether packing RGB in 16-bits should use 555
# or 565 (extra bit for green)
# DISPLAY_FORMAT_555
DISPLAY_NATIVE_555 = (0 << 18)
DISPLAY_NATIVE_565 = (1 << 18)

DISPLAY_555_MASK = 0x00040000

# Define the row alignment, which must be equal to or greater than
# the size of a pointer.
# The default (DISPLAY_ROW_ALIGN_DEFAULT) is the size of a pointer,
# 4 bytes (DISPLAY_ROW_ALIGN_4) on 32-bit systems or 8 bytes
# (DISPLAY_ROW_ALIGN_8) on 64-bit systems.
# DISPLAY_FORMAT_ROW_ALIGN
DISPLAY_ROW_ALIGN_DEFAULT = (0 << 20)
# DISPLAY_ROW_ALIGN_1 = (1 << 20),  # not currently possible
# DISPLAY_ROW_ALIGN_2 = (2 << 20),  # not currently possible
DISPLAY_ROW_ALIGN_4  = (3 << 20)
DISPLAY_ROW_ALIGN_8  = (4 << 20)
DISPLAY_ROW_ALIGN_16 = (5 << 20)
DISPLAY_ROW_ALIGN_32 = (6 << 20)
DISPLAY_ROW_ALIGN_64 = (7 << 20)

DISPLAY_ROW_ALIGN_MASK = 0x00700000


class Revision(Structure):
    _fields_ = [
        ("product", c_char_p),
        ("copyright", c_char_p),
        ("revision", c_long),
        ("revisiondate", c_long)
        ]


gs_main_instance = c_void_p
display_callback = c_void_p


class GhostscriptError(Exception):
    def __init__(self, ecode):
        # :todo:
        Exception.__init__(self, error2name(ecode))
        self.code = ecode


def revision():
    """
    Get version numbers and strings.

    This is safe to call at any time.
    You should call this first to make sure that the correct version
    of the Ghostscript is being used.

    Returns a Revision instance
    """
    revision = Revision()
    rc = libgs.gsapi_revision(pointer(revision), sizeof(revision))
    if rc:
        raise ArgumentError("Revision structure size is incorrect, "
                            "requires %s bytes" % rc)
    return revision


def new_instance():  # display_callback=None):
    """
    Create a new instance of Ghostscript

    This instance is passed to most other API functions.
    """
    # :todo: The caller_handle will be provided to callback functions.
    display_callback = None
    instance = gs_main_instance()
    rc = libgs.gsapi_new_instance(pointer(instance), display_callback)
    if rc != 0:
        raise GhostscriptError(rc)
    return instance


def delete_instance(instance):
    """
    Destroy an instance of Ghostscript

    Before you call this, Ghostscript must have finished.
    If Ghostscript has been initialised, you must call exit()
    before delete_instance()
    """
    return libgs.gsapi_delete_instance(instance)


c_stdstream_call_t = CFUNCTYPE(c_int, gs_main_instance, POINTER(c_char), c_int)


def _wrap_stdin(infp):
    """
    Wrap a filehandle into a C function to be used as `stdin` callback
    for ``set_stdio``. The filehandle has to support the readline() method.
    """

    def _wrap(instance, dest, count):
        try:
            data = infp.readline(count)
        except:
            count = -1
        else:
            if not data:
                count = 0
            else:
                count = len(data)
                memmove(dest, c_char_p(data), count)
        return count

    return c_stdstream_call_t(_wrap)


def _wrap_stdout(outfp):
    """
    Wrap a filehandle into a C function to be used as `stdout` or
    `stderr` callback for ``set_stdio``. The filehandle has to support the
    write() and flush() methods.
    """

    def _wrap(instance, str, count):
        outfp.write(str[:count])
        outfp.flush()
        return count

    return c_stdstream_call_t(_wrap)


_wrap_stderr = _wrap_stdout


def set_stdio(instance, stdin, stdout, stderr):
    """
    Set the callback functions for stdio.

    ``stdin``, ``stdout`` and ``stderr`` have to be ``ctypes``
    callback functions matching the ``_gsprint.c_stdstream_call_t``
    prototype. You may want to use _wrap_* to wrap file handles.

    Note 1: This function only changes stdio of the Postscript
    interpreter, not that of the devices.

    Note 2: Make sure you keep references to C function objects
    as long as they are used from C code. Otherwise they may be
    garbage collected, crashing your program when a callback is made.

    The ``stdin`` callback function should return the number of
    characters read, `0` for EOF, or `-1` for error. The `stdout` and
    `stderr` callback functions should return the number of characters
    written.

    You may pass ``None`` for any of stdin, stdout or stderr , in which
    case the system stdin, stdout resp. stderr will be used.
    """
    rc = libgs.gsapi_set_stdio(instance, stdin, stdout, stderr)
    if rc not in (0, e_Quit, e_Info):
        raise GhostscriptError(rc)
    return rc


# :todo:  set_poll (instance, int(*poll_fn)(void *caller_handle));
# :todo:  set_display_callback(instance, callback):

def set_arg_encoding(instance, encoding):
    assert encoding in (
        ARG_ENCODING_LOCAL,
        ARG_ENCODING_UTF8,
        ARG_ENCODING_UTF16LE,
    )
    rc = libgs.gsapi_set_arg_encoding(instance, c_int(encoding))
    if rc < 0:
        raise GhostscriptError(rc)
    return rc


def init_with_args(instance, argv):
    """
    Initialise the interpreter.

    1. If quit or EOF occur during init_with_args(), the return value
       will be e_Quit. This is not an error. You must call exit() and
       must not call any other functions.

    2. If usage info should be displayed, the return value will be
       e_Info which is not an error. Do not call exit().

    3. Under normal conditions this returns 0. You would then call one
       or more run_*() functions and then finish with exit()

    Please note that the first element of ``argv`` must be the
    program-name, e.g.
    ``init_with_args(myinstance, ["text2pdf", "-q", …])``
    """
    ArgArray = c_char_p * len(argv)
    c_argv = ArgArray(*argv)
    rc = libgs.gsapi_init_with_args(instance, len(argv), c_argv)
    if rc not in (0, e_Info):
        raise GhostscriptError(rc)
    return rc


def exit(instance):
    """
    Exit the interpreter

    This must be called on shutdown if init_with_args() has been
    called, and just before delete_instance()
    """
    rc = libgs.gsapi_exit(instance)
    if rc != 0:
        raise GhostscriptError(rc)
    return rc


def run_string_begin(instance, user_errors=False):
    user_errors = -1 if user_errors else 0
    exit_code = c_int()
    rc = libgs.gsapi_run_string_begin(instance, c_int(user_errors),
                                      pointer(exit_code))
    if rc != 0:
        raise GhostscriptError(rc)
    return exit_code.value


def run_string_continue(instance, str, user_errors=False):
    user_errors = -1 if user_errors else 0
    exit_code = c_int()
    rc = libgs.gsapi_run_string_continue(
        instance, c_char_p(str), c_int(len(str)),
        c_int(user_errors), pointer(exit_code))
    if rc != e_NeedInput and rc != 0:
        raise GhostscriptError(rc)
    return exit_code.value


def run_string_end(instance, user_errors=False):
    user_errors = -1 if user_errors else 0
    exit_code = c_int()
    rc = libgs.gsapi_run_string_end(instance, c_int(user_errors),
                                    pointer(exit_code))
    if rc != 0:
        raise GhostscriptError(rc)
    return exit_code.value


def run_string_with_length(*args, **kw):
    raise NotImpelmentedError('Use run_string() instead')


def run_string(instance, str, user_errors=False):
    user_errors = -1 if user_errors else 0
    exit_code = c_int()
    rc = libgs.gsapi_run_string_with_length(
        instance, c_char_p(str), c_int(len(str)),
        c_int(user_errors), pointer(exit_code))
    if rc != 0:
        raise GhostscriptError(rc)
    return exit_code.value


def run_file(instance, filename, user_errors=False):
    user_errors = -1 if user_errors else 0
    exit_code = c_int()
    rc = libgs.gsapi_run_file(instance, c_char_p(filename),
                              c_int(user_errors), pointer(exit_code))
    if rc != 0:
        raise GhostscriptError(rc)
    return exit_code.value


def set_visual_tracer(I):
    raise NotImplementedError


# New device has been opened
# This is the first event from this device.
# int (*display_open)(void *handle, void *device);
c_display_open = CFUNCTYPE(c_int, c_void_p, c_void_p)

# Device is about to be closed.
# Device will not be closed until this function returns.
# int (*display_preclose)(void *handle, void *device);
c_display_preclose = CFUNCTYPE(c_int, c_void_p, c_void_p)

# Device has been closed.
# This is the last event from this device.
# int (*display_close)(void *handle, void *device);
c_display_close = CFUNCTYPE(c_int, c_void_p, c_void_p)

# Device is about to be resized.
# Resize will only occur if this function returns 0.
# raster is byte count of a row.
# int (*display_presize)(void *handle, void *device,
# int width, int height, int raster, unsigned int format);
c_display_presize = CFUNCTYPE(c_int, c_void_p, c_void_p,
    c_int, c_int, c_int, c_uint)

# Device has been resized.
# New pointer to raster returned in pimage
# int (*display_size)(void *handle, void *device, int width, int height,
# int raster, unsigned int format, unsigned char *pimage);
c_display_size = CFUNCTYPE(c_int, c_void_p, c_void_p,
    c_int, c_int, c_int, c_uint, POINTER(c_ubyte))

# flushpage
# int (*display_sync)(void *handle, void *device);
c_display_sync = CFUNCTYPE(c_int, c_void_p, c_void_p)

# showpage
# If you want to pause on showpage, then don't return immediately
# int (*display_page)(void *handle, void *device, int copies, int flush);
c_display_page = CFUNCTYPE(c_int, c_void_p, c_void_p,
    c_int, c_int)

# Notify the caller whenever a portion of the raster is updated.
# This can be used for cooperative multitasking or for
# progressive update of the display.
# This function pointer may be set to NULL if not required.
# int (*display_update)(void *handle, void *device, int x, int y,
# int w, int h);
c_display_update = CFUNCTYPE(c_int, c_void_p, c_void_p,
    c_int, c_int, c_int, c_int)

# Allocate memory for bitmap
# This is provided in case you need to create memory in a special
# way, e.g. shared.  If this is NULL, the Ghostscript memory device
# allocates the bitmap. This will only called to allocate the
# image buffer. The first row will be placed at the address
# returned by display_memalloc.
# void *(*display_memalloc)(void *handle, void *device, unsigned long size);
c_display_memalloc = CFUNCTYPE(c_void_p, c_void_p, c_void_p, c_ulong)

# Free memory for bitmap
# If this is NULL, the Ghostscript memory device will free the bitmap
# int (*display_memfree)(void *handle, void *device, void *mem);
c_display_memfree = CFUNCTYPE(c_int, c_void_p, c_void_p, c_void_p)

# Added in V2 */
# When using separation color space (DISPLAY_COLORS_SEPARATION),
# give a mapping for one separation component.
# This is called for each new component found.
# It may be called multiple times for each component.
# It may be called at any time between display_size
# and display_close.
# The client uses this to map from the separations to CMYK
# and hence to RGB for display.
# GS must only use this callback if version_major >= 2.
# The unsigned short c,m,y,k values are 65535 = 1.0.
# This function pointer may be set to NULL if not required.
#
# int (*display_separation)(void *handle, void *device,
# int component, const char *component_name,
# unsigned short c, unsigned short m,
# unsigned short y, unsigned short k);
c_display_separation = CFUNCTYPE(c_int, c_void_p, c_void_p,
    c_int, c_char_p, c_ushort, c_ushort, c_ushort, c_ushort)


class Display_callback_s (Structure):
    _fields_ = [
        # Size of this structure
        # Used for checking if we have been handed a valid structure
        # int size;
        ("size", c_int),

        # Major version of this structure
        # The major version number will change if this structure changes.
        # int version_major;
        ("version_major", c_int),

        # Minor version of this structure
        # The minor version number will change if new features are added
        # without changes to this structure.  For example, a new color
        # format.
        # int version_minor;
        ("version_minor", c_int),
        ("display_open", c_display_open),
        ("display_preclose", c_display_preclose),
        ("display_close", c_display_close),
        ("display_presize", c_display_presize),
        ("display_size", c_display_size),
        ("display_sync", c_display_sync),
        ("display_page", c_display_page),
        ("display_update", c_display_update),
        ("display_memalloc", c_display_memalloc),
        ("display_memfree", c_display_memfree),
        ("display_separation", c_display_separation)
    ]


def set_display_callback(instance, callback):
    rc = libgs.gsapi_set_display_callback(instance, callback)
    if rc != 0:
        raise GhostscriptError(rc)
    return rc


def __win32_finddll():
    import os
    import re
    from winreg import OpenKey, CloseKey, EnumKey, QueryValueEx, \
        QueryInfoKey, HKEY_LOCAL_MACHINE

    def looseVersion(vstring):
        # Taken from distutils.LooseVersion.parse()
        component_re = re.compile(r'(\d+ | [a-z]+ | \.)', re.VERBOSE)
        components = [x for x in component_re.split(vstring) if x and x != '.']
        for i, obj in enumerate(components):
            try:
                components[i] = int(obj)
            except ValueError:
                pass
        return components

    dlls = []
    # Look up different variants of Ghostscript and take the highest
    # version for which the DLL is to be found in the filesystem.
    for key_name in ('AFPL Ghostscript', 'Aladdin Ghostscript',
                     'GPL Ghostscript', 'GNU Ghostscript'):
        try:
            k1 = OpenKey(HKEY_LOCAL_MACHINE, "Software\\%s" % key_name)
            for num in range(0, QueryInfoKey(k1)[0]):
                version = EnumKey(k1, num)
                try:
                    k2 = OpenKey(k1, version)
                    dll_path = QueryValueEx(k2, 'GS_DLL')[0]
                    CloseKey(k2)
                    if os.path.exists(dll_path):
                        dlls.append((looseVersion(version), dll_path))
                except WindowsError:
                    pass
            CloseKey(k1)
        except WindowsError:
            pass
    if dlls:
        dlls.sort()
        return dlls[-1][-1]
    else:
        return None


if sys.platform == 'win32':
    libgs = __win32_finddll()
    if not libgs:
        raise RuntimeError('Can not find Ghostscript DLL in registry')
    libgs = windll.LoadLibrary(libgs)
else:
    try:
        libgs = cdll.LoadLibrary("libgs.so")
    except OSError:
        # shared object file not found
        import ctypes.util
        libgs = ctypes.util.find_library('gs')
        if not libgs:
            raise RuntimeError('Can not find Ghostscript library (libgs)')
        libgs = cdll.LoadLibrary(libgs)

del __win32_finddll
