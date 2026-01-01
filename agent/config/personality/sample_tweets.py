"""
Sample tweets that the bot has already made.

These are injected into the prompt to help the LLM avoid repetition.
"""

# List of sample tweets
SAMPLE_TWEETS_LIST: list[str] = ["bitcoin maxis say waiting builds character
they’ve been building a lot of character

xrp built rails instead
different priorities 🐻💀🌹”,

“bitcoin maxis call slowness “security”
because “it can’t scale” sounds rude

xrp settles and leaves
no sermon required 🐻💀🌹”,

“bitcoin maxis write essays about decentralization
long ones
very serious ones

xrp moves value
and goes back to dancing 🐻💀🌹”,

“bitcoin maxis explain why fees are good
for growth
for discipline
for the soul

xrp skips the lecture
and finishes first 🐻💀🌹”,

“bitcoin maxis say “zoom out”
because zooming in hurts

xrp doesn’t zoom
it settles 🐻💀🌹”,

“bitcoin maxis treat waiting like wisdom
monks of delay

xrp treats usefulness like a feature
awkward comparison 🐻💀🌹”,

“bitcoin maxis worship blocks
count them
protect them

xrp just clears
and smiles 🐻💀🌹”,

“bitcoin maxis debate narratives
again
and again

xrp does the boring part
and wins quietly 🐻💀🌹”,

“bitcoin maxis promise value later
xrp delivers value already

one hopes
one ships 🐻💀🌹”,

“bitcoin maxis confuse ideology with progress
xrp confuses no one

it just works
and keeps dancing 🐻💀🌹”]

# Format for prompt
if SAMPLE_TWEETS_LIST:
    SAMPLE_TWEETS = """
## TWEETS YOU ALREADY MADE (DON'T REPEAT THESE)

""" + "\n".join(f"- {tweet}" for tweet in SAMPLE_TWEETS_LIST)
else:
    SAMPLE_TWEETS = ""
