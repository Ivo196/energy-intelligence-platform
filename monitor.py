"""Compatibility import for the monitoring module.

The implementation lives in ``src.monitoring.monitor``. This module keeps
legacy imports such as ``from monitor import compute_drift`` working.
"""

import sys

from src.monitoring import monitor as _monitor

sys.modules[__name__] = _monitor
