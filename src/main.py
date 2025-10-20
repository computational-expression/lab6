"""
Lab 6: Simon Memory Game with Functions
CMPSC 100 - Computational Expression

Purpose: Create a Simon-style memory game using functions to organize code
and integrate 3 LEDs with 1 button for sequence matching.
"""

from machine import Pin
import time
import random

def show_sequence(leds, sequence):
    """Display LED sequence for player to memorize.
    
    Args:
        leds (list): List of LED pin objects
        sequence (list): List of LED indices to flash
    """
    # TODO: Print "Watch the sequence:" and wait 1 second
    
    # TODO: Loop through the sequence using range(len(sequence)) to get index
    # For each step:
    # - Get led_index = sequence[i]
    # - Print f"  Step {i+1}: LED {led_index + 1}"
    # - Turn on the LED at led_index
    # - Wait 0.6 seconds
    # - Turn off the LED
    # - Wait 0.3 seconds
    
    # TODO: Print "Sequence complete!" and wait 2 seconds for longer pause

def get_button_press(button, timeout=2):
    """Wait for button press with timeout.
    
    Args:
        button (Pin): Button pin object
        timeout (float): Maximum time to wait
        
    Returns:
        bool: True if button pressed, False if timeout
    """
    # TODO: Create a variable for the start time and assign it to time.time(), which gives current time
    
    # TODO: Create a while loop that continues while current time - start time < timeout
    # - Check if button.value() == 0 (button pressed)
    # - If pressed, wait for release with another while loop for button.value() == 0
    # - Add time.sleep(0.2) for debounce and return True
    
    # TODO: Return False if timeout reached

def test_memory(leds, sequence, button):
    """Test if player can match the sequence.
    
    Args:
        leds (list): List of LED pin objects
        sequence (list): Expected sequence
        button (Pin): Button pin object
        
    Returns:
        int: Number of correct responses
    """
    # TODO: Print instructions and wait 2 seconds
    
    # TODO: Initialize correct counter to 0
    
    # TODO: Loop through sequence using range(len(sequence)) to get index
    # For each step:
    # - Get expected_led = sequence[i]
    # - Print f"\nStep {i+1}: Which LED comes next?"
    # - Loop through all LEDs (range(len(leds)))
    #   - Turn on current LED
    #   - Check if this is the expected LED (led_index == expected_led)
    #     - If correct: wait for button press with get_button_press()
    #       - If button pressed: print success, increment correct, do success flash, break
    #       - If timeout: print miss message, turn off LED, return correct
    #     - If wrong LED: just wait 0.4 seconds, turn off, wait 0.2 seconds
    
    # TODO: Return the correct count

def calculate_score(correct, total, round_num):
    """Calculate score for the round.
    
    Args:
        correct (int): Correct responses
        total (int): Total steps
        round_num (int): Current round
        
    Returns:
        int: Score points
    """
    # TODO: Check if total == 0, return 0 if so
    
    # TODO: Calculate accuracy = correct / total
    # TODO: Calculate base_score = int(accuracy * 100)
    # TODO: Calculate bonus = round_num * 5 if accuracy == 1.0 else 0
    
    # TODO: Return base_score + bonus

def show_feedback(leds, success):
    """Show visual feedback.
    
    Args:
        leds (list): LED pin objects
        success (bool): Round success
    """
    # TODO: If success is True:
    # - Flash all LEDs together 3 times
    # - For each flash: turn all LEDs on, wait 0.3s, turn all off, wait 0.2s
    
    # TODO: If success is False:
    # - Create a chase pattern 2 times
    # - For each LED: turn on, wait 0.15s, turn off

def wait_for_button(button):
    """Wait for button press to continue.
    
    Args:
        button (Pin): Button pin object
    """
    # TODO: Wait 1.5 seconds, then print "Press button to continue..."
    # TODO: Wait while button.value() == 1 (not pressed)
    # TODO: Wait while button.value() == 0 (pressed - wait for release)
    # TODO: Wait 0.3 seconds for debounce

def main():
    """Main function to run the Simon memory game."""
    
    # TODO: Print game title and separator line
    
    # TODO: Initialize hardware - create LED pins for GPIO 15, 14, 13 with Pin.OUT
    # TODO: Create button pin for GPIO 12 with Pin.IN and Pin.PULL_UP
    
    # TODO: Get player name and number of rounds (3-6)
    # TODO: Ensure rounds is between 3 and 6 using max() and min()
    
    # TODO: Print welcome message and instructions
    # TODO: Wait for button press to start
    
    # TODO: Initialize total_score = 0 and perfect_rounds = 0
    
    # TODO: Create game loop for each round (1 to rounds+1):
    # - Print round header with separators
    # - Calculate sequence length = round_num + 1
    # - Generate random sequence using list comprehension and random.randint(0, 2)
    # - Print sequence length
    # - Call show_sequence() and test_memory()
    # - Calculate score using calculate_score()
    # - Add to total_score
    # - Check if perfect (correct == seq_length) and increment perfect_rounds
    # - Print score result
    # - Call show_feedback()
    # - If not last round, call wait_for_button()
    
    # TODO: Print final results section
    # TODO: Print player stats and total score
    
    # TODO: Victory celebration based on performance
    # - If perfect_rounds == rounds: print "SIMON MASTER!" and special LED pattern
    # - Elif perfect_rounds >= rounds // 2: print "Great memory!" and show success feedback
    
    # TODO: Clean up - turn off all LEDs
    # TODO: Print "Game complete!"

if __name__ == "__main__": 
    main()
