
"""
Random Password Generator  (LF)
-----------------------------------------------------------

Secure: uses the password module cryptographically strong
Flexible: choose lenght, character class and count
Safe: guarantees at least 1 character from each selected class
Informative: print an entropy estimate for each run

"""

from __future__ import annotations

import argparseim
import math
import string
from secrets import choice
from typing import List

# Character sets

LOWERCASE = string.ascii_lowercase
UPPERCASE = string.ascii_uppercase
DIGITS = string.digits
SYMBOLS = "!@#$%^&*()-_=+[]{};:,.<>/?|~"

# Ambiguous characters that are hard to distinguish by sight or dictation
AMBIGUOUS = set ("O0oIl1|`'\"{}[]()<>;:,.\/")

def build_pool(use_lower: bool, use_upper: bool, use_digits: bool, use_symbols: bool, avoid_ambiguous: bool) -> List[str]:
    """Build the character pool based on user options."""
    pool = []
    if use_lower:
        pool.append(LOWER)
    if use_upper:
        pool.append(UPPER)
    if use_digits:
        pool.append(DIGITS)
    if use_symbols:
        pool.append(SYMBOLS)
    if not pool:
        raise ValueError("At least one character class must be selected.")


