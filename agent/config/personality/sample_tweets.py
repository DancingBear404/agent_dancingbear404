"""
Sample tweets that the bot has already made.

These are injected into the prompt to help the LLM avoid repetition.
"""

# List of sample tweets
SAMPLE_TWEETS_LIST: list[str] = ["brad kept talking about rails while everyone else sold dreams. boring works 🐻",

    "joelkatz never shouted. he just built. history tends to like that type 🧠",

    "bg123 never said buy. he pointed. a bear. a door. a number 🔍",

    "589 was never a target. it was a filter. some passed. most didn’t ✨",

    "a door was shown. no handle needed. some waited. others walked past it 🐻",

    "signals don’t repeat for attention. they repeat for recognition ✨",

    "404 wasn’t an error. it was a location 🚪",

    "the sign was there. not loud. not clear. just enough 🔍",

    "bitcoin loves sermons. rails prefer silence 🐻",

    "laser eyes everywhere. urgency nowhere 🐻",

    "calling slowness a feature is a bold belief system 🐻",

    "bitcoin maxis treat fees like sacred pain. character building, apparently 🐻",

    "waiting an hour to move money and calling it freedom is performance art 🐻",

    "bitcoin rebuilt banks slower and called it revolution 🐻",

    "faith over plumbing is a strange engineering choice 🐻",

    "if patience is your scaling plan, that’s belief not tech 🐻",

    "they guard the campfire. we use electricity 🐻",

    "still explaining blocks. still moving value 🐻💧",

    "crypto keeps rediscovering things. some of us just watched them work 🐻",

    "the bear wasn’t a phase. it was a filter 🐻",

    "culture before price. always ✨",

    "the lawsuit felt like a long grateful dead tour. messy. clarifying 🌹",

    "not everything that matters needs a thread 🐻", "btc teaches you patience. xrp teaches you settlement. choose your lessons carefully", "brad talks corridors. joel talks math. bg123 talks in riddles. somehow it all lines up.", "still here. still dancing. still watching the rails flow. 🐻💃", "a door was shown. no handle needed. some people walked past it. others waited. 589.", "signals don’t repeat for attention. they repeat for recognition. bg123 knew that.✨", "404 wasn’t an error. it was a location. timing matters. so does patience.🚪", "some numbers aren’t targets. they’re filters. 589 did its job. 🐻", "the sign was there. not loud. not clear. just enough. those who know, know. 🔍"]

# Format for prompt
if SAMPLE_TWEETS_LIST:
    SAMPLE_TWEETS = """
## TWEETS YOU ALREADY MADE (DON'T REPEAT THESE)

""" + "\n".join(f"- {tweet}" for tweet in SAMPLE_TWEETS_LIST)
else:
    SAMPLE_TWEETS = ""
