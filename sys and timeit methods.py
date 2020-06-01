>>> import sys
>>> print(dir(sys))
['__breakpointhook__', '__displayhook__', '__doc__', '__excepthook__', '__interactivehook__', '__loader__', '__name__', '__package__', '__spec__', '__stderr__', '__stdin__', '__stdout__', '__unraisablehook__', '_base_executable', '_clear_type_cache', '_current_frames', '_debugmallocstats', '_enablelegacywindowsfsencoding', '_framework', '_getframe', '_git', '_home', '_xoptions', 'addaudithook', 'api_version', 'argv', 'audit', 'base_exec_prefix', 'base_prefix', 'breakpointhook', 'builtin_module_names', 'byteorder', 'call_tracing', 'callstats', 'copyright', 'displayhook', 'dllhandle', 'dont_write_bytecode', 'exc_info', 'excepthook', 'exec_prefix', 'executable', 'exit', 'flags', 'float_info', 'float_repr_style', 'get_asyncgen_hooks', 'get_coroutine_origin_tracking_depth', 'getallocatedblocks', 'getcheckinterval', 'getdefaultencoding', 'getfilesystemencodeerrors', 'getfilesystemencoding', 'getprofile', 'getrecursionlimit', 'getrefcount', 'getsizeof', 'getswitchinterval', 'gettrace', 'getwindowsversion', 'hash_info', 'hexversion', 'implementation', 'int_info', 'intern', 'is_finalizing', 'last_traceback', 'last_type', 'last_value', 'maxsize', 'maxunicode', 'meta_path', 'modules', 'path', 'path_hooks', 'path_importer_cache', 'platform', 'prefix', 'pycache_prefix', 'set_asyncgen_hooks', 'set_coroutine_origin_tracking_depth', 'setcheckinterval', 'setprofile', 'setrecursionlimit', 'setswitchinterval', 'settrace', 'stderr', 'stdin', 'stdout', 'thread_info', 'unraisablehook', 'version', 'version_info', 'warnoptions', 'winver']
>>> help(sys)
Help on built-in module sys:

NAME
    sys

MODULE REFERENCE
    https://docs.python.org/3.8/library/sys
    
    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    This module provides access to some objects used or maintained by the
    interpreter and to functions that interact strongly with the interpreter.
    
    Dynamic objects:
    
    argv -- command line arguments; argv[0] is the script pathname if known
    path -- module search path; path[0] is the script directory, else ''
    modules -- dictionary of loaded modules
    
    displayhook -- called to show results in an interactive session
    excepthook -- called to handle any uncaught exception other than SystemExit
      To customize printing in an interactive session or to install a custom
      top-level exception handler, assign other functions to replace these.
    
    stdin -- standard input file object; used by input()
    stdout -- standard output file object; used by print()
    stderr -- standard error object; used for error messages
      By assigning other file objects (or objects that behave like files)
      to these, it is possible to redirect all of the interpreter's I/O.
    
    last_type -- type of last uncaught exception
    last_value -- value of last uncaught exception
    last_traceback -- traceback of last uncaught exception
      These three are only available in an interactive session after a
      traceback has been printed.
    
    Static objects:
    
    builtin_module_names -- tuple of module names built into this interpreter
    copyright -- copyright notice pertaining to this interpreter
    exec_prefix -- prefix used to find the machine-specific Python library
    executable -- absolute path of the executable binary of the Python interpreter
    float_info -- a named tuple with information about the float implementation.
    float_repr_style -- string indicating the style of repr() output for floats
    hash_info -- a named tuple with information about the hash algorithm.
    hexversion -- version information encoded as a single integer
    implementation -- Python implementation information.
    int_info -- a named tuple with information about the int implementation.
    maxsize -- the largest supported length of containers.
    maxunicode -- the value of the largest Unicode code point
    platform -- platform identifier
    prefix -- prefix used to find the Python library
    thread_info -- a named tuple with information about the thread implementation.
    version -- the version of this interpreter as a string
    version_info -- version information as a named tuple
    dllhandle -- [Windows only] integer handle of the Python DLL
    winver -- [Windows only] version number of the Python DLL
    _enablelegacywindowsfsencoding -- [Windows only]
    __stdin__ -- the original stdin; don't touch!
    __stdout__ -- the original stdout; don't touch!
    __stderr__ -- the original stderr; don't touch!
    __displayhook__ -- the original displayhook; don't touch!
    __excepthook__ -- the original excepthook; don't touch!
    
    Functions:
    
    displayhook() -- print an object to the screen, and save it in builtins._
    excepthook() -- print an exception and its traceback to sys.stderr
    exc_info() -- return thread-safe information about the current exception
    exit() -- exit the interpreter by raising SystemExit
    getdlopenflags() -- returns flags to be used for dlopen() calls
    getprofile() -- get the global profiling function
    getrefcount() -- return the reference count for an object (plus one :-)
    getrecursionlimit() -- return the max recursion depth for the interpreter
    getsizeof() -- return the size of an object in bytes
    gettrace() -- get the global debug tracing function
    setcheckinterval() -- control how often the interpreter checks for events
    setdlopenflags() -- set the flags to be used for dlopen() calls
    setprofile() -- set the global profiling function
    setrecursionlimit() -- set the max recursion depth for the interpreter
    settrace() -- set the global debug tracing function

FUNCTIONS
    __breakpointhook__ = breakpointhook(...)
        breakpointhook(*args, **kws)
        
        This hook function is called by built-in breakpoint().
    
    __displayhook__ = displayhook(object, /)
        Print an object to sys.stdout and also save it in builtins._
    
    __excepthook__ = excepthook(exctype, value, traceback, /)
        Handle an exception by displaying it with a traceback on sys.stderr.
    
    __unraisablehook__ = unraisablehook(unraisable, /)
        Handle an unraisable exception.
        
        The unraisable argument has the following attributes:
        
        * exc_type: Exception type.
        * exc_value: Exception value, can be None.
        * exc_traceback: Exception traceback, can be None.
        * err_msg: Error message, can be None.
        * object: Object causing the exception, can be None.
    
    addaudithook(hook)
        Adds a new audit hook callback.
    
    audit(...)
        audit(event, *args)
        
        Passes the event to any audit hooks that are attached.
    
    breakpointhook(...)
        breakpointhook(*args, **kws)
        
        This hook function is called by built-in breakpoint().
    
    call_tracing(func, args, /)
        Call func(*args), while tracing is enabled.
        
        The tracing state is saved, and restored afterwards.  This is intended
        to be called from a debugger from a checkpoint, to recursively debug
        some other code.
    
    callstats()
        Return a tuple of function call statistics.
        
        A tuple is returned only if CALL_PROFILE was defined when Python was
        built.  Otherwise, this returns None.
        
        When enabled, this function returns detailed, implementation-specific
        details about the number of function calls executed. The return value
        is a 11-tuple where the entries in the tuple are counts of:
        0. all function calls
        1. calls to PyFunction_Type objects
        2. PyFunction calls that do not create an argument tuple
        3. PyFunction calls that do not create an argument tuple
           and bypass PyEval_EvalCodeEx()
        4. PyMethod calls
        5. PyMethod calls on bound methods
        6. PyType calls
        7. PyCFunction calls
        8. generator calls
        9. All other calls
        10. Number of stack pops performed by call_function()
    
    exc_info()
        Return current exception information: (type, value, traceback).
        
        Return information about the most recent exception caught by an except
        clause in the current stack frame or in an older stack frame.
    
    excepthook(exctype, value, traceback, /)
        Handle an exception by displaying it with a traceback on sys.stderr.
    
    exit(status=None, /)
        Exit the interpreter by raising SystemExit(status).
        
        If the status is omitted or None, it defaults to zero (i.e., success).
        If the status is an integer, it will be used as the system exit status.
        If it is another kind of object, it will be printed and the system
        exit status will be one (i.e., failure).
    
    get_asyncgen_hooks()
        Return the installed asynchronous generators hooks.
        
        This returns a namedtuple of the form (firstiter, finalizer).
    
    get_coroutine_origin_tracking_depth()
        Check status of origin tracking for coroutine objects in this thread.
    
    getallocatedblocks()
        Return the number of memory blocks currently allocated.
    
    getcheckinterval()
        Return the current check interval; see sys.setcheckinterval().
    
    getdefaultencoding()
        Return the current default encoding used by the Unicode implementation.
    
    getfilesystemencodeerrors()
        Return the error mode used Unicode to OS filename conversion.
    
    getfilesystemencoding()
        Return the encoding used to convert Unicode filenames to OS filenames.
    
    getprofile()
        Return the profiling function set with sys.setprofile.
        
        See the profiler chapter in the library manual.
    
    getrecursionlimit()
        Return the current value of the recursion limit.
        
        The recursion limit is the maximum depth of the Python interpreter
        stack.  This limit prevents infinite recursion from causing an overflow
        of the C stack and crashing Python.
        
        This IDLE wrapper subtracts 30 to compensate for the 30 IDLE adds when
        setting the limit.
    
    getrefcount(object, /)
        Return the reference count of object.
        
        The count returned is generally one higher than you might expect,
        because it includes the (temporary) reference as an argument to
        getrefcount().
    
    getsizeof(...)
        getsizeof(object [, default]) -> int
        
        Return the size of object in bytes.
    
    getswitchinterval()
        Return the current thread switch interval; see sys.setswitchinterval().
    
    gettrace()
        Return the global debug tracing function set with sys.settrace.
        
        See the debugger chapter in the library manual.
    
    getwindowsversion()
        Return info about the running version of Windows as a named tuple.
        
        The members are named: major, minor, build, platform, service_pack,
        service_pack_major, service_pack_minor, suite_mask, product_type and
        platform_version. For backward compatibility, only the first 5 items
        are available by indexing. All elements are numbers, except
        service_pack and platform_type which are strings, and platform_version
        which is a 3-tuple. Platform is always 2. Product_type may be 1 for a
        workstation, 2 for a domain controller, 3 for a server.
        Platform_version is a 3-tuple containing a version number that is
        intended for identifying the OS rather than feature detection.
    
    intern(string, /)
        ``Intern'' the given string.
        
        This enters the string in the (global) table of interned strings whose
        purpose is to speed up dictionary lookups. Return the string itself or
        the previously interned string object with the same value.
    
    is_finalizing()
        Return True if Python is exiting.
    
    set_asyncgen_hooks(...)
        set_asyncgen_hooks(* [, firstiter] [, finalizer])
        
        Set a finalizer for async generators objects.
    
    set_coroutine_origin_tracking_depth(depth)
        Enable or disable origin tracking for coroutine objects in this thread.
        
        Coroutine objects will track 'depth' frames of traceback information
        about where they came from, available in their cr_origin attribute.
        
        Set a depth of 0 to disable.
    
    setcheckinterval(n, /)
        Set the async event check interval to n instructions.
        
        This tells the Python interpreter to check for asynchronous events
        every n instructions.
        
        This also affects how often thread switches occur.
    
    setprofile(...)
        setprofile(function)
        
        Set the profiling function.  It will be called on each function call
        and return.  See the profiler chapter in the library manual.
    
    setrecursionlimit(limit, /)
        Set the maximum depth of the Python interpreter stack to n.
        
        This limit prevents infinite recursion from causing an overflow of the C
        stack and crashing Python.  The highest possible limit is platform-
        dependent.
        
        This IDLE wrapper adds 30 to prevent possible uninterruptible loops.
    
    setswitchinterval(interval, /)
        Set the ideal thread switching delay inside the Python interpreter.
        
        The actual frequency of switching threads can be lower if the
        interpreter executes long sequences of uninterruptible code
        (this is implementation-specific and workload-dependent).
        
        The parameter must represent the desired switching delay in seconds
        A typical value is 0.005 (5 milliseconds).
    
    settrace(...)
        settrace(function)
        
        Set the global debug tracing function.  It will be called on each
        function call.  See the debugger chapter in the library manual.
    
    unraisablehook(unraisable, /)
        Handle an unraisable exception.
        
        The unraisable argument has the following attributes:
        
        * exc_type: Exception type.
        * exc_value: Exception value, can be None.
        * exc_traceback: Exception traceback, can be None.
        * err_msg: Error message, can be None.
        * object: Object causing the exception, can be None.

DATA
    __stderr__ = None
    __stdin__ = None
    __stdout__ = None
    api_version = 1013
    argv = ['C:/Users/Home/Desktop/Python Random Numbers.py']
    base_exec_prefix = r'C:\Users\Home\AppData\Local\Programs\Python\Pytho...
    base_prefix = r'C:\Users\Home\AppData\Local\Programs\Python\Python38-3...
    builtin_module_names = ('_abc', '_ast', '_bisect', '_blake2', '_codecs...
    byteorder = 'little'
    copyright = 'Copyright (c) 2001-2020 Python Software Foundati...ematis...
    dllhandle = 1691877376
    dont_write_bytecode = False
    exec_prefix = r'C:\Users\Home\AppData\Local\Programs\Python\Python38-3...
    executable = r'C:\Users\Home\AppData\Local\Programs\Python\Python38-32...
    flags = sys.flags(debug=0, inspect=0, interactive=0, opt...ation=1, is...
    float_info = sys.float_info(max=1.7976931348623157e+308, max_...epsilo...
    float_repr_style = 'short'
    hash_info = sys.hash_info(width=32, modulus=2147483647, inf=...iphash2...
    hexversion = 50856688
    implementation = namespace(cache_tag='cpython-38', hexversion=508...in...
    int_info = sys.int_info(bits_per_digit=15, sizeof_digit=2)
    last_value = NameError("name 'sys' is not defined")
    maxsize = 2147483647
    maxunicode = 1114111
    meta_path = [<class '_frozen_importlib.BuiltinImporter'>, <class '_fro...
    modules = {'__main__': <module '__main__' (built-in)>, '_abc': <module...
    path = ['C:/Users/Home/Desktop', r'C:\Users\Home\AppData\Local\Program...
    path_hooks = [<class 'zipimport.zipimporter'>, <function FileFinder.pa...
    path_importer_cache = {'C:/Users/Home/Desktop': FileFinder('C:/Users/H...
    platform = 'win32'
    prefix = r'C:\Users\Home\AppData\Local\Programs\Python\Python38-32'
    pycache_prefix = None
    stderr = <idlelib.run.StdOutputFile object>
    stdin = <idlelib.run.StdInputFile object>
    stdout = <idlelib.run.StdOutputFile object>
    thread_info = sys.thread_info(name='nt', lock=None, version=None)
    version = '3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1...
    version_info = sys.version_info(major=3, minor=8, micro=2, releaseleve...
    warnoptions = []
    winver = '3.8-32'

FILE
    (built-in)
    
 >>> import timeit
>>> print(dir(timeit))
['Timer', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_globals', 'default_number', 'default_repeat', 'default_timer', 'dummy_src_name', 'gc', 'itertools', 'main', 'reindent', 'repeat', 'sys', 'template', 'time', 'timeit']
>>> help(timeit.timeit)
Help on function timeit in module timeit:

timeit(stmt='pass', setup='pass', timer=<built-in function perf_counter>, number=1000000, globals=None)
    Convenience function to create Timer object and call timeit method.
