"""
Simplified test verification for Lab 6 Simon Memory Game functions
CMPSC 100 - For grading purposes only

This file contains basic tests to verify function implementations
without requiring external testing frameworks.
"""

def test_calculate_score_basic():
    """Basic test for calculate_score function."""
    try:
        # Import the function
        import sys
        import os
        sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
        from main import calculate_score
        
        # Test perfect score
        result = calculate_score(3, 3, 1)
        assert result == 105, f"Expected 105, got {result}"
        
        # Test partial score
        result = calculate_score(2, 3, 1)
        expected = int((2/3) * 100)
        assert result == expected, f"Expected {expected}, got {result}"
        
        # Test zero case
        result = calculate_score(0, 0, 1)
        assert result == 0, f"Expected 0, got {result}"
        
        return True
    except Exception as e:
        print(f"calculate_score test failed: {e}")
        return False

def test_function_definitions():
    """Test that all required functions are defined."""
    try:
        import sys
        import os
        sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
        import main
        
        required_functions = [
            'show_sequence',
            'get_button_press', 
            'test_memory',
            'calculate_score',
            'show_feedback',
            'wait_for_button',
            'main'
        ]
        
        for func_name in required_functions:
            assert hasattr(main, func_name), f"Function {func_name} not found"
            func = getattr(main, func_name)
            assert callable(func), f"{func_name} is not callable"
        
        return True
    except Exception as e:
        print(f"Function definition test failed: {e}")
        return False

def test_function_parameters():
    """Test that functions accept correct number of parameters."""
    try:
        import sys
        import os
        import inspect
        sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
        import main
        
        # Test parameter counts
        func_params = {
            'show_sequence': 2,
            'get_button_press': 2,  # button, timeout (with default)
            'test_memory': 3,
            'calculate_score': 3,
            'show_feedback': 2,
            'wait_for_button': 1,
            'main': 0
        }
        
        for func_name, expected_params in func_params.items():
            func = getattr(main, func_name)
            sig = inspect.signature(func)
            param_count = len(sig.parameters)
            
            # Allow for default parameters
            if func_name == 'get_button_press':
                assert param_count >= 1, f"{func_name} should have at least 1 parameter"
            else:
                assert param_count == expected_params, f"{func_name} should have {expected_params} parameters, got {param_count}"
        
        return True
    except Exception as e:
        print(f"Parameter test failed: {e}")
        return False

def test_docstrings():
    """Test that functions have docstrings."""
    try:
        import sys
        import os
        sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
        import main
        
        required_functions = [
            'show_sequence',
            'get_button_press', 
            'test_memory',
            'calculate_score',
            'show_feedback',
            'wait_for_button',
            'main'
        ]
        
        for func_name in required_functions:
            func = getattr(main, func_name)
            assert func.__doc__ is not None, f"Function {func_name} missing docstring"
            assert len(func.__doc__.strip()) > 10, f"Function {func_name} docstring too short"
        
        return True
    except Exception as e:
        print(f"Docstring test failed: {e}")
        return False

def run_tests():
    """Run all verification tests."""
    print("Running Lab 6 function verification tests...")
    
    tests = [
        ("Function Definitions", test_function_definitions),
        ("Function Parameters", test_function_parameters),
        ("Function Docstrings", test_docstrings),
        ("Calculate Score Logic", test_calculate_score_basic)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"Testing {test_name}...", end=" ")
        if test_func():
            print("PASS")
            passed += 1
        else:
            print("FAIL")
    
    print(f"\nTest Results: {passed}/{total} passed")
    return passed == total

if __name__ == "__main__":
    success = run_tests()
    exit(0 if success else 1)