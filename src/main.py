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
    
    # TODO: Loop through the sequence using range(sequence) to get index
    # At each step:
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
    # TODO: Create a variable to store the start time and assign it to time.time(), which gives current time
    
    # TODO: Create a loop that continues until (current time - start time < timeout)
    # - Check if button is pressed (button pressed condition)
    # - If pressed, wait until release with another loop until button released
    # - Add time.sleep to prevent bouncing and return True
    
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
    
    # TODO: Loop through sequence using range(length) to get index
    # At each step:
    # - Get expected_led = sequence[i]
    # - Print something like f"\nStep {i+1}: Which LED comes next?"
    # - Loop through all LEDs (range(leds))
    #   - Turn on current LED
    #   - Check if this is the expected LED (led_index matches expected_led)
    #     - If correct (they match): 
    #       - Check if button was pressed using the correct function
    #           - If button was pressed: print success, increment correct, do success flash
    #           - Else (timed out): print miss message, turn off LED, return correct
    #     - Else (wrong LED): just wait 0.4 seconds, turn off, wait 0.2 seconds
    
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
    # TODO: Check if total is zero, return 0 if so
    
    # TODO: Calculate accuracy = correct / total
    # TODO: Calculate base_score = int(accuracy * 100)
    # TODO: Calculate bonus using if-else:
    # TODO: If accuracy is 1.0, set bonus = round_num * 5
    # TODO: Otherwise, set bonus = 0
    
    # TODO: Return base_score + bonus

def show_feedback(leds, success):
    """Show visual feedback.
    
    Args:
        leds (list): LED pin objects
        success (bool): Round success
    """
    # TODO: If success is True:
    # - Flash all LEDs together 3 times
    # - At each flash: turn all LEDs on, wait 0.3s, turn all off, wait 0.2s
    
    # TODO: If success is False:
    # - Create a chase pattern 2 times
    # - At each LED: turn on, wait 0.15s, turn off

def wait_for_button(button):
    """Wait for button press to continue.
    
    Args:
        button (Pin): Button pin object
    """
    # TODO: Wait 1.5 seconds, then print "Press button to continue..."
    # TODO: Wait until button is not pressed (loop until pressed)
    # TODO: Wait until button is pressed (loop until released) 
    # TODO: Wait 0.3 seconds to prevent bouncing

def main():
    """Main function to run the Simon memory game."""
    
    # TODO: Print game title and separator line
    
    # TODO: Initialize hardware - create LED pins for GPIO 15, 14, 13 with Pin.OUT
    # TODO: Create button pin for GPIO 12 with Pin.IN and Pin.PULL_UP
    
    # TODO: Get player name and number of rounds (3-6)
    # TODO: Ensure rounds is between 3 and 6 using max() and min()
    
    # TODO: Print welcome message and instructions
    # TODO: Call the function* to wait for button press to start
    
    # TODO: Initialize total_score = 0 and perfect_rounds = 0
    
    # TODO: Create game loop that iterates through each round (1 to rounds+1):
    # - Print round header with separators
    # - Calculate sequence length = round_num + 1
    # - Generate random sequence by creating empty list, then using for loop to append random.randint(0, 2)
    # - Print sequence length
    # - Call show_sequence()* and test_memory()* functions
    # - Calculate score using calculate_score()* function
    # - Add to total_score
    # - Check if perfect (correct matches seq_length) and increment perfect_rounds
    # - Print score result
    # - Call show_feedback()*
    # - If not last round, call wait_for_button()*
    
    # TODO: Print final results section
    # TODO: Print player stats and total score
    
    # TODO: Victory celebration based on performance
    # - If perfect_rounds matches rounds: print something positive and special LED pattern
    # - Elif perfect_rounds >= rounds // 2: print something else positive and call function* to show feedback
    
    # TODO: Clean up - turn off all LEDs
    # TODO: Print "Game complete!"

if __name__ == "__main__": 
    main()
