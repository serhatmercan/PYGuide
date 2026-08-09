# Minimal stub package supporting Module.py's import examples.
# serhat_function lives here (rather than in a separate serhatmodule.py)
# because serhatmodule also needs to be a package, for the
# serhatmodule.serhatsubmodule import a few lines down in Module.py -
# a plain module can't have dotted submodules, so this is the only
# layout that satisfies every import in that file unchanged.

def serhat_function():
    print("serhat_function() called from serhatmodule.")
