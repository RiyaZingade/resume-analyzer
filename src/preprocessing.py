#acceptable things
"""
allowed --> numbers, letters, +, #, :, -, \, . --> thats it, everything else removed
"""

from typing import List


def normalize(resume: str) -> str:
    acceptedSymbols = ["+", "#", ":", "-", "\"", "."," ", "@", "/", "\n"]
    resume = resume.lower()
    for char in resume:
        if not char.isalnum() and char not in acceptedSymbols:
            resume = resume.replace(char, '')
    return resume
