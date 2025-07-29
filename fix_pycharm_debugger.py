"""This script allows you to patch a debugger error
in PyCharm that occurs in [some versions of PyCharm](https://youtrack.jetbrains.com/issue/PY-73047/Debugger-doesnt-work-with-Python-3.13-MainThread-object-has-no-attribute-isAlive)
with Python 3.13 +
It is useful in restrictive environments
where you cannot modify anything outside of user space

To use:
1. Rename the script to **exactly**: `sitecustomize.py`
2. Copy it into its own folder in your %USERPROFILE%
3. Open Command Prompt (`cmd`) and run the following:
```bash
setx PYTHONPATH "%USERPROFILE%\location\of\sitecustomize\"
```
4. Restart PyCharm
"""
import threading
import sys

# This script is run automatically on Python interpreter startup.
# The `isAlive` method on threads was removed in Python 3.13, but older versions
# of PyCharm's debugger (pydevd) still rely on it.
# This patch adds the method back as an alias for the modern `is_alive()`.

def patch_thread_is_alive():
    """Adds `isAlive` as an alias for `is_alive` to the Thread class."""
    # Check if the Python version is 3.13 or higher and the attribute is missing.
    if sys.version_info >= (3, 13) and not hasattr(threading.Thread, 'isAlive'):
        threading.Thread.isAlive = threading.Thread.is_alive

patch_thread_is_alive()