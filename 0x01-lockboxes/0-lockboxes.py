#!/usr/bin/python3
def canUnlockAll(boxes):
    n = len(boxes)  # Total number of boxes
    unlocked = [False] * n  # List to track unlocked boxes
    unlocked[0] = True  # Box 0 is initially unlocked
    keys = [0]  # Start with the key to the first box
    
    while keys:
        current_box = keys.pop()  # Get the key to the current box
        for key in boxes[current_box]:  # Explore all keys in the current box
            if key < n and not unlocked[key]:  # Check if the key opens a new box
                unlocked[key] = True  # Mark the box as unlocked
                keys.append(key)  # Add the key to the list to explore further
    
    return all(unlocked)  # Return True if all boxes are unlocked
