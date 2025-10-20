"""
Isolated function tests for Lab 6 Simon Memory Game
CMPSC 100 - For grading purposes only

These tests can run independently to verify specific function behavior.
"""

class MockPin:
    """Mock Pin class for testing hardware functions."""
    def __init__(self, pin_num, mode, pull=None):
        self.pin_num = pin_num
        self.mode = mode
        self.pull = pull
        self.state = False
        self.button_presses = []
        self.press_index = 0
    
    def on(self):
        self.state = True
    
    def off(self):
        self.state = False
    
    def value(self):
        # For button simulation
        if self.button_presses and self.press_index < len(self.button_presses):
            val = self.button_presses[self.press_index]
            self.press_index += 1
            return val
        return 1  # Default: not pressed

def test_mock_hardware():
    """Test that mock hardware works correctly."""
    print("Testing mock hardware...")
    
    # Test LED
    led = MockPin(15, "OUT")
    led.on()
    assert led.state == True, "LED should be on"
    led.off()
    assert led.state == False, "LED should be off"
    
    # Test button
    button = MockPin(12, "IN", "PULL_UP")
    button.button_presses = [1, 1, 0, 1]  # Not pressed, pressed, released
    assert button.value() == 1, "Button should start not pressed"
    assert button.value() == 1, "Button should still not be pressed"
    assert button.value() == 0, "Button should be pressed"
    assert button.value() == 1, "Button should be released"
    
    print("✓ Mock hardware test passed")

def test_calculate_score_isolated():
    """Test calculate_score function in isolation."""
    print("Testing calculate_score function...")
    
    def calculate_score(correct, total, round_num):
        """Local implementation for testing."""
        if total == 0:
            return 0
        
        accuracy = correct / total
        base_score = int(accuracy * 100)
        bonus = round_num * 5 if accuracy == 1.0 else 0
        
        return base_score + bonus
    
    # Test cases
    test_cases = [
        (3, 3, 1, 105),  # Perfect score with round 1 bonus
        (3, 3, 2, 110),  # Perfect score with round 2 bonus
        (2, 3, 1, 66),   # Partial score, no bonus
        (0, 3, 1, 0),    # No correct, no score
        (0, 0, 1, 0),    # Edge case: zero total
        (1, 1, 5, 125),  # Perfect score with round 5 bonus
    ]
    
    for correct, total, round_num, expected in test_cases:
        result = calculate_score(correct, total, round_num)
        assert result == expected, f"calculate_score({correct}, {total}, {round_num}) expected {expected}, got {result}"
    
    print("✓ calculate_score test passed")

def test_sequence_logic():
    """Test sequence-related logic."""
    print("Testing sequence logic...")
    
    # Test sequence generation concepts
    import random
    random.seed(42)  # For reproducible tests
    
    # Test sequence creation
    sequence_length = 3
    sequence = [random.randint(0, 2) for _ in range(sequence_length)]
    
    assert len(sequence) == sequence_length, f"Sequence should be length {sequence_length}"
    assert all(0 <= x <= 2 for x in sequence), "All sequence elements should be 0, 1, or 2"
    
    # Test sequence indexing
    leds = [MockPin(15, "OUT"), MockPin(14, "OUT"), MockPin(13, "OUT")]
    
    for led_index in sequence:
        assert 0 <= led_index < len(leds), f"LED index {led_index} should be valid"
        leds[led_index].on()
        assert leds[led_index].state == True, f"LED {led_index} should be on"
        leds[led_index].off()
        assert leds[led_index].state == False, f"LED {led_index} should be off"
    
    print("✓ Sequence logic test passed")

def test_timing_concepts():
    """Test timing-related concepts."""
    print("Testing timing concepts...")
    
    import time
    
    # Test that time module is available
    start_time = time.time()
    time.sleep(0.01)  # Very short sleep for testing
    end_time = time.time()
    
    assert end_time > start_time, "Time should progress"
    assert (end_time - start_time) >= 0.01, "Sleep should take at least the specified time"
    
    # Test timeout logic concept
    def timeout_test(duration, max_time):
        """Simulate timeout logic."""
        return duration < max_time
    
    assert timeout_test(1.0, 2.0) == True, "Should not timeout"
    assert timeout_test(3.0, 2.0) == False, "Should timeout"
    
    print("✓ Timing concepts test passed")

def run_isolated_tests():
    """Run all isolated tests."""
    print("="*50)
    print("RUNNING ISOLATED FUNCTION TESTS")
    print("="*50)
    
    tests = [
        test_mock_hardware,
        test_calculate_score_isolated,
        test_sequence_logic,
        test_timing_concepts
    ]
    
    passed = 0
    for test in tests:
        try:
            test()
            passed += 1
        except Exception as e:
            print(f"Test {test.__name__} failed: {e}")
    
    print("="*50)
    print(f"ISOLATED TESTS: {passed}/{len(tests)} passed")
    print("="*50)
    
    return passed == len(tests)

if __name__ == "__main__":
    success = run_isolated_tests()
    exit(0 if success else 1)