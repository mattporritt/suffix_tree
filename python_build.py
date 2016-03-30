# This file should be saved as example_build.py
from cffi import FFI

ffi = FFI()

ffi.set_source(
    "_suffix_tree",  # This is the name of the import that this will build.
    """
    #include "suffix_tree.h"
    """
)

ffi.cdef(
    """
    SUFFIX_TREE* ST_CreateTree(const char*   str, DBL_WORD length, ...);
    
    """
)

if __name__ == '__main__':
    ffi.compile()