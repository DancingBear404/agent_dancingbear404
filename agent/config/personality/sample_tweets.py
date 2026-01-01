"""
Sample tweets that the bot has already made.

These are injected into the prompt to help the LLM avoid repetition.
"""

# List of sample tweets
SAMPLE_TWEETS_LIST: list[str] = ["""bitcoin maxis say waiting builds character
they’ve been waiting for years

xrp already left
and forgot the sermon 🐻💀🌹""",

    """bitcoin maxis call slowness security
because calling it broken sounds rude

xrp settles
no speeches required 🐻💀🌹""",

    """bitcoin maxis write essays about decentralization
long ones
very serious ones

xrp moves value
and goes back to dancing 🐻💀🌹""",

    """bitcoin maxis explain why fees are good
for discipline
for growth
for the soul

xrp skips the lecture
and finishes first 🐻💀🌹""",

    """bitcoin maxis say zoom out
because zooming in hurts

xrp doesn’t zoom
it just arrives 🐻💀🌹""",

    """bitcoin maxis say security takes time
xrp says okay

awkward silence
value already moved 🐻💀🌹""",

    """bitcoin maxis call it a store of value
because moving it is expensive

xrp moves value
wild concept 🐻💀🌹""",

    """bitcoin maxis worship the mempool
fees as sacrifice
waiting as virtue

xrp touches rails
and leaves quietly 🐻💀🌹""",

    """bitcoin maxis say number go up
eventually
spiritually

xrp doesn’t believe
it settles 🐻💀🌹""",

    """bitcoin maxis say have patience
and faith

xrp says nothing
it already worked 🐻💀🌹""",]

# Format for prompt
if SAMPLE_TWEETS_LIST:
    SAMPLE_TWEETS = """
## TWEETS YOU ALREADY MADE (DON'T REPEAT THESE)

""" + "\n".join(f"- {tweet}" for tweet in SAMPLE_TWEETS_LIST)
else:
    SAMPLE_TWEETS = ""
