"""
Definition of Ghostscript error codes
"""
#
# This file is part of python-ghostscript.
# Copyright (C) 2010-2018 by Hartmut Goebel
#
# Based on iapi.h which is
# Copyright (C) 1989, 1995, 1998, 1999 Aladdin Enterprises. All rights reserved.
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

#
# A procedure that may return an error always returns
# a non-negative value (zero, unless otherwise noted) for success,
# or negative for failure.
# We use ints rather than an enum to avoid a lot of casting.
#

# ------ PostScript Level 1 errors ------

e_unknownerror = -1 # unknown error
e_dictfull = -2
e_dictstackoverflow = -3
e_dictstackunderflow = -4
e_execstackoverflow = -5
e_interrupt = -6
# We also need to define gs_error_interrupt, for gpcheck.h
gs_error_interrupt = e_interrupt
e_invalidaccess = -7
e_invalidexit = -8
e_invalidfileaccess = -9
e_invalidfont = -10
e_invalidrestore = -11
e_ioerror = -12
e_limitcheck = -13
e_nocurrentpoint = -14
e_rangecheck = -15
e_stackoverflow = -16
e_stackunderflow = -17
e_syntaxerror = -18
e_timeout = -19
e_typecheck = -20
e_undefined = -21
e_undefinedfilename = -22
e_undefinedresult = -23
e_unmatchedmark = -24
e_VMerror = -25

LEVEL1_ERROR_NAMES = ["unknownerror", "dictfull", "dictstackoverflow",
                      "dictstackunderflow", "execstackoverflow",
                      "interrupt", "invalidaccess", "invalidexit",
                      "invalidfileaccess", "invalidfont",
                      "invalidrestore", "ioerror", "limitcheck",
                      "nocurrentpoint", "rangecheck", "stackoverflow",
                      "stackunderflow", "syntaxerror", "timeout",
                      "typecheck", "undefined", "undefinedfilename",
                      "undefinedresult", "unmatchedmark", "VMerror"]

# ------ Additional Level 2 and DPS errors ------

e_configurationerror = -26
e_invalidcontext = -27
e_undefinedresource = -28
e_unregistered = -29
# invalidid is for the NeXT DPS extension.
e_invalidid = -30

LEVEL2_ERROR_NAMES = ["configurationerror", "invalidcontext",
                      "undefinedresource", "unregistered",
                      "invalidid"]

ERROR_NAMES = LEVEL1_ERROR_NAMES + LEVEL2_ERROR_NAMES


_PSEUDO_ERRORS = ['Fatal', 'Quit', 'InterpreterExit', 'RemapColor',
                  'ExecStackUnderflow', 'VMreclaim', 'NeedInput',
                  'NeedStdin', 'NeedStdout', 'NeedStderr', 'Info']


def error2name(ecode):
    if ecode <= e_Fatal:
        return _PSEUDO_ERRORS[-ecode-100]
    else:
        return ERROR_NAMES[-ecode-1]


# ------ Pseudo-errors used internally ------

#
# Internal code for a fatal error.
# gs_interpret also returns this for a .quit with a positive exit code.
#
e_Fatal = -100

#
# Internal code for the .quit operator.
# The real quit code is an integer on the operand stack.
# gs_interpret returns this only for a .quit with a zero exit code.
#
e_Quit = -101

#
# Internal code for a normal exit from the interpreter.
# Do not use outside of interp.c.
#
e_InterpreterExit = -102

#
# Internal code that indicates that a procedure has been stored in the
# remap_proc of the graphics state, and should be called before retrying
# the current token. This is used for color remapping involving a call
# back into the interpreter -- inelegant, but effective.
#
e_RemapColor = -103

#
# Internal code to indicate we have underflowed the top block
# of the e-stack.
#
e_ExecStackUnderflow = -104

#
# Internal code for the vmreclaim operator with a positive operand.
# We need to handle this as an error because otherwise the interpreter
# won't reload enough of its state when the operator returns.
#
e_VMreclaim = -105

#
# Internal code for requesting more input from run_string.
#
e_NeedInput = -106

#
# Internal code for stdin callout.
#
e_NeedStdin = -107

#
# Internal code for stdout callout.
#
e_NeedStdout = -108

#
# Internal code for stderr callout.
#
e_NeedStderr = -109

#
# Internal code for a normal exit when usage info is displayed.
# This allows Window versions of Ghostscript to pause until
# the message can be read.
#
e_Info = -110


#
# Define which error codes require re-executing the current object.
#
def ERROR_IS_INTERRUPT(ecode):
    return ecode == e_interrupt or ecode == e_timeout


if __name__ == '__main__':
    print(error2name(e_unknownerror) == "unknownerror")
    print(error2name(e_VMerror) == "VMerror")
    print(error2name(e_invalidid) == "invalidid")
    print(error2name(e_VMreclaim) == "VMreclaim")
