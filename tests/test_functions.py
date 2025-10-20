"""
Test cases for Lab 6 Simon Memory Game functions
CMPSC 100 - For grading purposes only

These tests verify that all required functions work correctly
and handle various input scenarios appropriately.
"""

import sys
import os
from unittest.mock import Mock, patch, MagicMock

# Add current directory to path for mock modules
sys.path.insert(0, os.path.dirname(__file__))

# Import the functions from main.py
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from main import (
    show_sequence, 
    get_button_press, 
    test_memory, 
    calculate_score, 
    show_feedback, 
    wait_for_button
)

def test_show_sequence():
    """Test show_sequence function with mock LEDs."""
    print("Testing show_sequence function...")
    
    # Create simple mock LEDs
    class MockLED:
        def __init__(self):
            self.on_called = False
            self.off_called = False
        
        def on(self):
            self.on_called = True
        
        def off(self):
            self.off_called = True
    
    mock_leds = [MockLED(), MockLED(), MockLED()]
    
    # Test sequence display
    sequence = [0, 2, 1]
    
    with patch('time.sleep'), patch('builtins.print'):
        show_sequence(mock_leds, sequence)
    
    # Verify LEDs were called correctly
    assert mock_leds[0].on_called, "LED 0 should have been turned on"
    assert mock_leds[0].off_called, "LED 0 should have been turned off"
    assert mock_leds[2].on_called, "LED 2 should have been turned on"
    assert mock_leds[2].off_called, "LED 2 should have been turned off"
    assert mock_leds[1].on_called, "LED 1 should have been turned on"
    assert mock_leds[1].off_called, "LED 1 should have been turned off"
    
    print("✓ show_sequence test passed")

def test_get_button_press_timeout():
    """Test get_button_press with timeout."""
    print("Testing get_button_press timeout...")
    
    # Create a simple mock button that never gets pressed
    class MockButton:
        def value(self):
            return 1  # Always not pressed
    
    mock_button = MockButton()
    
    with patch('time.time', side_effect=[0, 0.5, 1.0, 1.5, 2.1]):
        with patch('time.sleep'):
            result = get_button_press(mock_button, timeout=2)
    
    assert result == False, "Should return False on timeout"
    print("✓ get_button_press timeout test passed")

def test_get_button_press_success():
    """Test get_button_press with successful press."""
    print("Testing get_button_press success...")
    
    # Create a simple mock button
    class MockButton:
        def __init__(self):
            self.values = [1, 1, 0, 0, 1]  # Not pressed (1), pressed (0), released (1)
            self.index = 0
        
        def value(self):
            if self.index < len(self.values):
                val = self.values[self.index]
                self.index += 1
                return val
            return 1  # Default: not pressed
    
    mock_button = MockButton()
    
    # Test with very short timeout for faster testing
    with patch('time.time', side_effect=[0, 0.1, 0.2, 0.3]):
        with patch('time.sleep'):
            result = get_button_press(mock_button, timeout=2)
    
    assert result == True, "Should return True on button press"
    print("✓ get_button_press success test passed")

def test_calculate_score():
    """Test calculate_score function with various inputs."""
    print("Testing calculate_score function...")
    
    # Test perfect score with bonus
    score = calculate_score(3, 3, 2)
    expected = 100 + (2 * 5)  # 110
    assert score == expected, f"Perfect score should be {expected}, got {score}"
    
    # Test partial score no bonus
    score = calculate_score(2, 3, 2)
    expected = int((2/3) * 100)  # 66
    assert score == expected, f"Partial score should be {expected}, got {score}"
    
    # Test zero total
    score = calculate_score(0, 0, 1)
    assert score == 0, "Zero total should return 0"
    
    # Test zero correct
    score = calculate_score(0, 3, 1)
    assert score == 0, "Zero correct should return 0"
    
    print("✓ calculate_score test passed")

def test_show_feedback():
    """Test show_feedback function with mock LEDs."""
    print("Testing show_feedback function...")
    
    # Create simple mock LEDs
    class MockLED:
        def __init__(self):
            self.on_count = 0
            self.off_count = 0
        
        def on(self):
            self.on_count += 1
        
        def off(self):
            self.off_count += 1
    
    mock_leds = [MockLED(), MockLED(), MockLED()]
    
    # Test success feedback
    with patch('time.sleep'):
        show_feedback(mock_leds, True)
    
    # All LEDs should be called for success
    for led in mock_leds:
        assert led.on_count > 0, "LED should have been turned on for success"
        assert led.off_count > 0, "LED should have been turned off for success"
    
    # Reset counts
    for led in mock_leds:
        led.on_count = 0
        led.off_count = 0
    
    # Test failure feedback
    with patch('time.sleep'):
        show_feedback(mock_leds, False)
    
    # All LEDs should be called for failure too
    for led in mock_leds:
        assert led.on_count > 0, "LED should have been turned on for failure"
        assert led.off_count > 0, "LED should have been turned off for failure"
    
    print("✓ show_feedback test passed")

def test_wait_for_button():
    """Test wait_for_button function."""
    print("Testing wait_for_button function...")
    
    # Create a mock button that transitions states
    class MockButton:
        def __init__(self):
            self.values = [1, 1, 0, 0, 1]  # Not pressed (1), pressed (0), released (1)
            self.index = 0
        
        def value(self):
            if self.index < len(self.values):
                val = self.values[self.index]
                self.index += 1
                return val
            return 1  # Default: not pressed
    
    mock_button = MockButton()
    
    with patch('time.sleep'), patch('builtins.print'):
        wait_for_button(mock_button)
    
    # Should have checked button value multiple times
    assert mock_button.index > 0, "Should have checked button value"
    print("✓ wait_for_button test passed")

def test_memory_game_integration():
    """Test integration of multiple functions."""
    print("Testing function integration...")
    
    # Create simple mock objects
    class MockLED:
        def __init__(self):
            self.state = False
        
        def on(self):
            self.state = True
        
        def off(self):
            self.state = False
    
    class MockButton:
        def value(self):
            return 1
    
    mock_leds = [MockLED(), MockLED(), MockLED()]
    mock_button = MockButton()
    
    # Test that functions can be called in sequence
    sequence = [0, 1, 2]
    
    with patch('time.sleep'), patch('builtins.print'):
        # Test sequence display
        show_sequence(mock_leds, sequence)
        
        # Test scoring
        score = calculate_score(3, 3, 1)
        assert score > 0, "Score should be positive"
        
        # Test feedback
        show_feedback(mock_leds, True)
    
    print("✓ Integration test passed")

def run_all_tests():
    """Run all test functions."""
    print("="*50)
    print("RUNNING LAB 6 FUNCTION TESTS")
    print("="*50)
    
    try:
        test_show_sequence()
        test_get_button_press_timeout()
        test_get_button_press_success()
        test_calculate_score()
        test_show_feedback()
        test_wait_for_button()
        test_memory_game_integration()
        
        print("="*50)
        print("ALL TESTS PASSED!")
        print("="*50)
        return True
        
    except Exception as e:
        print(f"TEST FAILED: {e}")
        print("="*50)
        return False

if __name__ == "__main__":
    run_all_tests()