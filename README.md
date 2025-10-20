# Lab 6: Interactive Control System with Functions

Welcome to Lab 6! In this lab, you will create a **Simon-style memory game** using **functions** to organize your code while integrating 3 LEDs and 1 button to create an engaging sequence matching challenge.

## Learning Objectives

Master **Python functions** through memory gaming:
- **Function definition and calling** - create reusable code blocks using `def` and function calls
- **Parameters and return values** - pass data to functions and return processed results
- **Code organization** - structure programs using functions for readability and modularity
- **Memory game logic** - work with sequences, timing, and user interaction
- **Hardware integration** - use functions to control multiple LEDs and button input

*This assignment aligns with CMPSC 100 Learning Outcomes 1 and 2, focusing on Python programming fundamentals with an emphasis on code organization and modularity. It builds on Labs 1-5's concepts while introducing functions as a fundamental programming tool. This lab also fulfills Allegheny College's Quantitative Reasoning (QR) distribution requirement through data collection, mathematical analysis, and computational scoring applied to interactive gaming systems.*

## Prerequisites

Before starting this lab, ensure you have:
- VS Code with MicroPico extension installed (from Lab 2)
- Your Pico 2 W board and USB cable ready
- Understanding of variables, loops, and conditionals from Labs 1-5
- Experience with GPIO pin control and LEDs from Labs 2-5
- Understanding of lists and user input from Labs 3-5

### Hardware Components:
- **3 LEDs** (different colors - Red, Green, Blue recommended)
- **1 button** (push button for control)
- **3 × 220Ω or 330Ω resistors** for LEDs
- **1 breadboard** (30-row mini breadboard)
- **6-8 jumper wires** (male-to-male, any colors)

## Functions in Python

### What are Functions?
**Functions** are reusable blocks of code that perform specific tasks:
- **Organization**: Break complex programs into smaller, manageable pieces
- **Reusability**: Write code once, use it multiple times
- **Clarity**: Make programs easier to read and understand
- **Testing**: Test individual pieces of functionality separately

### Function Structure
```python
def function_name(parameters):
    """Optional docstring explaining what the function does"""
    # Function body - the code that runs
    return result  # Optional return value
```

## Simon Memory Game Concepts

### Memory-Based Gaming
**Simon-style games** provide excellent learning through sequence memory:
- **Sequence display**: Show LED patterns that players must memorize
- **Memory testing**: Players recreate sequences by timing button presses correctly
- **Progressive difficulty**: Sequences get longer as rounds advance
- **Immediate feedback**: Visual confirmation of correct/incorrect responses

### Game Logic Processing
Functions help organize memory game workflows:
- **Sequence functions**: Generate and display LED sequences for memorization
- **Input functions**: Capture and validate player button responses
- **Scoring functions**: Calculate performance and provide feedback
- **Control functions**: Manage game flow and progressive difficulty

## Circuit Assembly

### Hardware Setup

**For complete circuit assembly instructions, refer to Lab 5's hardware setup section** - the wiring is identical:
- **3 LEDs** with resistors connected to GPIO pins 15, 14, and 13
- **1 button** connected to GPIO pin 12 with ground connection
- **Power and ground connections** to breadboard rails

### Quick Reference:
- **LED 1 (Red)**: Pin GPIO 15 (row 20)
- **LED 2 (Green)**: Pin GPIO 14 (row 19) 
- **LED 3 (Blue)**: Pin GPIO 13 (row 17)
- **Control Button**: Pin GPIO 12 (row 16)

## Programming with Functions

Open `src/main.py` and work through the concepts to create your interactive control system:

### Core Programming Tasks:
1. **Sequence Functions** - Create functions to generate and display LED memory sequences
2. **Input Functions** - Organize button press detection and timing using functions
3. **Memory Testing** - Use functions to validate player sequence reproduction
4. **Scoring Functions** - Create functions to calculate performance and provide feedback
5. **Game Control** - Use functions to manage rounds and progressive difficulty
6. **Main Program** - Organize everything using a main function structure

### Required Function Descriptions

Your Simon memory game must implement these **7 essential functions**:

#### 1. `show_sequence(leds, sequence)`
- **Purpose**: Display the LED sequence that players need to memorize
- **Parameters**: List of LED objects and sequence of LED indices to flash
- **Behavior**: Lights up each LED in order with appropriate timing for memorization

#### 2. `get_button_press(button, timeout)` - see example below
- **Purpose**: Wait for button press within a time limit
- **Parameters**: Button object and timeout duration in seconds
- **Returns**: True if button pressed within timeout, False otherwise

```
def get_button_press(button, timeout=2):
    """Wait for button press with timeout.
    
    Args:
        button (Pin): Button pin object
        timeout (float): Maximum time to wait
        
    Returns:
        bool: True if button pressed, False if timeout
    """
    start_time = time.time()
    
    while (time.time() - start_time) < timeout:
        if button.value() == 0:  # Button pressed
            while button.value() == 0:  # Wait for release
                time.sleep(0.05)
            time.sleep(0.2)  # Debounce
            return True
        time.sleep(0.05)
    
    return False
    ```

#### 3. `test_memory(leds, sequence, button)`
- **Purpose**: Test if player can reproduce the memorized sequence
- **Parameters**: LED list, target sequence, and button for input
- **Returns**: Number of correct responses or success status

#### 4. `calculate_score(correct, total, round_num)`
- **Purpose**: Calculate player's score based on performance
- **Parameters**: Number correct, total attempts, current round number
- **Returns**: Calculated score with potential round bonuses

#### 5. `show_feedback(leds, success)`
- **Purpose**: Provide visual feedback for success or failure
- **Parameters**: LED list and boolean success status
- **Behavior**: Different LED patterns for success vs. failure

#### 6. `wait_for_button(button)`
- **Purpose**: Pause game progression until player presses button
- **Parameters**: Button object for input detection
- **Behavior**: Blocks execution until button is pressed and released

#### 7. `main()`
- **Purpose**: Organize and control the main game flow
- **Behavior**: Coordinates all other functions to run the complete game

## Required Features for Complete Implementation

Your program must demonstrate **function-based organization**:

#### Essential Functions (exactly 7 required):
1. **`show_sequence(leds, sequence)`** - Display LED sequence for memorization
2. **`get_button_press(button, timeout)`** - Handle button input with timeout
3. **`test_memory(leds, sequence, button)`** - Test player's sequence memory
4. **`calculate_score(correct, total, round_num)`** - Calculate performance score
5. **`show_feedback(leds, success)`** - Provide visual success/failure feedback
6. **`wait_for_button(button)`** - Handle game progression control
7. **`main()`** - Organize the main program flow

#### Function Requirements:
- **Parameters**: Each function must accept appropriate parameters as specified
- **Return values**: Functions must return expected data types and values
- **Docstrings**: Include clear documentation for each function's purpose
- **Modularity**: Each function should perform one specific task
- **Reusability**: Functions should be called multiple times throughout the game

#### Simon Memory Game Features:
- **Progressive sequences**: Memory challenges that grow longer each round
- **Sequence reproduction**: Players press button when correct LED lights up
- **Visual feedback**: LEDs provide immediate response confirmation
- **Memory scoring**: Points based on accuracy and round difficulty
- **Game progression**: Automatic difficulty increase with longer sequences

## Testing Your Code

1. **Test circuit**: Verify all 3 LEDs and button work independently
2. **Test functions**: Verify each function works with correct parameters
3. **Test sequences**: Check LED sequences display correctly and are memorizable
4. **Test memory**: Verify button timing detection works for sequence reproduction
5. **Test feedback**: Confirm LEDs provide appropriate visual success/failure responses

## Troubleshooting

### Circuit Issues:
- **LEDs not lighting**: Verify polarity (long leg to positive), resistor connections
- **Button not responding**: Check ground connection and pull-up setting
- **Inconsistent patterns**: Verify all LED wiring and resistor values

### Function Issues:
- **Function not found**: Check function definition spelling and indentation
- **Wrong parameters**: Verify function calls match function definitions
- **Return value problems**: Ensure functions return expected data types
- **Timing issues**: Check time.sleep() calls and button debouncing

### Pattern Issues:
- **Sequence confusion**: Check LED indexing and sequence generation logic
- **Memory test problems**: Verify button response timing and LED coordination
- **Scoring errors**: Check score calculation and success condition logic

## Assessment Criteria - Total: 3.5 Points

### Technical Implementation (2.0 points)
- **Automated GatorGrade checks**: 1.5 points (based on function usage and LED pattern integration)
- **Hardware execution verification**: 0.5 points (program runs correctly with 3 LED + 1 button circuit)

### Code Quality and Style (1.0 point)  
- **Clear function organization** and **meaningful names** (0.6 pts)
- **Appropriate docstrings** and **comments** explaining function logic (0.4 pts)

### Reflection and Engagement (0.5 points)
- **Thoughtful reflection** on function concepts and Simon memory game implementation

*GatorGrade checks verify: function definitions, parameter usage, return statements, memory game logic, and code organization*

## Sample Output

Example output from your Simon memory game:

```
Simon Memory Game
=========================
Player name: Priya
Rounds (3-6)? 4

Hello Priya!
Watch sequences, then press button for the correct LED!
Press button to continue...

===============
ROUND 1
===============
Sequence length: 2
Watch the sequence:
  Step 1: LED 2
  Step 2: LED 1
Sequence complete!

Your turn! Press button when you see the correct LED:

Step 1: Which LED comes next?
  ✓ Correct! LED 2

Step 2: Which LED comes next?
  ✓ Correct! LED 1

PERFECT! Score: 105

Press button to continue...

===============
ROUND 2
===============
Sequence length: 3
Watch the sequence:
  Step 1: LED 1
  Step 2: LED 3
  Step 3: LED 2
Sequence complete!

Your turn! Press button when you see the correct LED:

Step 1: Which LED comes next?
  ✓ Correct! LED 1

Step 2: Which LED comes next?
  ✗ Missed LED 3

Got 1/3. Score: 33

[Continues for remaining rounds...]

=========================
FINAL RESULTS
=========================
Player: Priya
Perfect rounds: 2/4
Total score: 201

Great memory!

Game complete!
```

*Your LEDs (Red, Green, Blue) will light up in sequences that you must memorize and reproduce by pressing the button at the right moments.*

## Submission Instructions

Submit to GitHub frequently! Use this workflow:

```bash
git add src/main.py writing/reflection.md
git commit -m "Complete Simon memory game with functions"
git push
```

Verify your submission online and ensure GatorGrade passes automated testing.

## Getting Help

### During Lab
- Ask TLs or instructor for help with specific questions or hardware issues
- Work with classmates on understanding concepts (but write your own code)
- Use the lab time to understand function concepts and interactive control

### Outside Lab  
- Post questions in Discord
- Attend [TL office hours](https://www.cis.allegheny.edu/teaching/technicalleaders/) and/or [instructor office hours](https://janyljumadinova.com/schedule/) to seek help outside of class
- Review the slides for concept reinforcement

### Resources
- [Python Documentation](https://docs.python.org/3/)
- [MicroPython Documentation](https://docs.micropython.org/)
- Course slides and examples from class activities

## Hardware Concepts

### Electronic Components
**Interactive control systems and digital input**:
- **Push buttons**: Digital input devices for user interaction
- **Pull-up resistors**: Ensure clean digital signals from buttons
- **Debouncing**: Software techniques to handle mechanical button behavior
- **LED feedback**: Visual output to provide user guidance and response