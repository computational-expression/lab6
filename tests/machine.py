"""
Mock machine module for testing Lab 6 functions on regular Python
This allows tests to run without MicroPython hardware dependencies
"""

class Pin:
    """Mock Pin class that simulates MicroPython Pin behavior."""
    
    # Pin modes
    IN = "IN"
    OUT = "OUT"
    
    # Pull resistor options
    PULL_UP = "PULL_UP"
    PULL_DOWN = "PULL_DOWN"
    
    def __init__(self, pin_number, mode, pull=None):
        """Initialize a mock pin."""
        self.pin_number = pin_number
        self.mode = mode
        self.pull = pull
        self._value = 1 if pull == Pin.PULL_UP else 0
        self._state = False
        
        # For testing button sequences
        self._button_sequence = []
        self._sequence_index = 0
    
    def on(self):
        """Turn the pin on (for output pins)."""
        if self.mode == Pin.OUT:
            self._state = True
    
    def off(self):
        """Turn the pin off (for output pins)."""
        if self.mode == Pin.OUT:
            self._state = False
    
    def value(self, val=None):
        """Get or set the pin value."""
        if val is not None:
            self._value = val
            return None
        
        # For input pins (buttons), simulate button presses
        if self.mode == Pin.IN:
            if self._button_sequence and self._sequence_index < len(self._button_sequence):
                value = self._button_sequence[self._sequence_index]
                self._sequence_index += 1
                return value
            return self._value
        
        # For output pins, return current state
        return 1 if self._state else 0
    
    def set_button_sequence(self, sequence):
        """Set a sequence of button values for testing."""
        self._button_sequence = sequence
        self._sequence_index = 0