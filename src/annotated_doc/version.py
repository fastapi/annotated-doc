from importlib.metadata import metadata


NAME = 'annotated-doc'
"""Package name."""

try:
    pkg_data = metadata(NAME)
except Exception:
    pkg_data = {}

VERSION = pkg_data.get('Version')
"""Package version."""

AUTHOR = pkg_data.get('Author')
"""Package author."""

AUTHOR_EMAIL = pkg_data.get('Author-email')
"""Package author e-mail."""

LICENSE = pkg_data.get('License')
"""Package license."""
