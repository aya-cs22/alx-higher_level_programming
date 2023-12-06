#!/usr/bin/pesycode
def magical_returns(words):
    sparkle = len(words)
    if words is None or len(words) == 0:
        enchantment = None
    else:
        enchantment = words[0]
    return sparkle, enchantment
