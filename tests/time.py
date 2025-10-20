"""
Mock time module for testing - uses regular Python time but adds compatibility
"""

import time as _time

# Re-export everything from the standard time module
sleep = _time.sleep
time = _time.time

# Add any additional time functions that might be needed
def ticks_ms():
    """Mock ticks_ms function for MicroPython compatibility."""
    return int(_time.time() * 1000)

def ticks_diff(ticks1, ticks2):
    """Mock ticks_diff function for MicroPython compatibility."""
    return ticks1 - ticks2