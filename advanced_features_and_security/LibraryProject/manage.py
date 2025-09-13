#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""

#!/usr/bin/env python
import os
import sys

if __name__ == "_main_":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # If Django is not installed, raise an error.
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable?"
        )
    execute_from_command_line(sys.argv)
