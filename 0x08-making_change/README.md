# 0x08. Making Change

This project focuses on solving the classic **coin change problem** using algorithms in Python. The goal is to determine the minimum number of coins needed to achieve a given total using a list of coin denominations.

## Learning Objectives

By completing this project, you will:

- Understand and implement **greedy algorithms**.
- Explore **dynamic programming** solutions for optimization problems.
- Analyze **time and space complexity** of algorithms.
- Enhance your Python programming skills.

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`.
- All files will be interpreted/compiled on **Ubuntu 20.04 LTS** using Python 3.4.3.
- Code must follow **PEP 8** style (version 1.7.x).
- All scripts must be executable and start with `#!/usr/bin/python3`.
- A `README.md` file is mandatory at the root of the project.

## Task Description

### 0. Change comes from within

Implement the `makeChange` function:

#### Prototype:

```python
def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet the total amount.

    Args:
        coins (list): List of coin denominations.
        total (int): The total amount to achieve.

    Returns:
        int: The fewest number of coins, or -1 if not possible.
    """
```
