#!/usr/bin/python3
"""
This method determines if all the boxes in a given
list of lists can be unlocked.

- The function starts with the first box unlocked
and uses the keys found inside to unlock additional boxes.
- Returns True if all boxes can be unlocked, otherwise returns False.
"""


def canUnlockAll(boxes):
    n = len(boxes)  # Number of boxes
    unlocked = [False] * n  # List to track which boxes have been unlocked
    unlocked[0] = True  # The first box is always unlocked

    to_explore = [0]  # Initialize with the first box (index 0)

    while to_explore:
        box = to_explore.pop()  # Get the current box to explore its keys

        # Check all keys in the current box
        for key in boxes[box]:
            if key < n and not unlocked[key]:  # If the key opens a new box
                unlocked[key] = True  # Unlock that box
                to_explore.append(key)  # Add the newly unlocked box

    # If all boxes are unlocked, return True; otherwise, return False
    return all(unlocked)
