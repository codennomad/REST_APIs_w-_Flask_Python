"""
blocklist.py

This file just contains the blocklist of the JWT tokens. 
It will be imported by app and the logout resource so that toknes
can be added to the blocklist when the user logs out.

feature - use redis for store blocklist
"""

BLOCKLIST = set()

