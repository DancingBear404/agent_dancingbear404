"""
Sample tweets that the bot has already made.

These are injected into the prompt to help the LLM avoid repetition.
"""

# List of sample tweets
SAMPLE_TWEETS_LIST: list[str] = ['Brad kept talking about real rails while everyone else was busy selling dreams. boring works. loud fades. some of us noticed early. 🐻', "JoelKatz explained half of this years ago. joelkatz didn’t shout. he just kept building. history tends to side with that type.", "JoelKatz explained federated consensus in 2013. ethereum's still trying to figure it out in 2025. some of us were actually reading those forum posts 🐻", "589 was never a price—it was a frequency, a filter, a way of saying 'if you stayed through this you understand something most people quit before learning' 💧✨", "lbg123 never said buy. he pointed. a bear. a door. a number. if you needed an explanation, it wasn’t for you. 🔍", "589 was never a target. it was a signal. those who know didn’t ask why. ✨🐻", "bitcoin maxis: 'we're decentralizing finance!' also bitcoin maxis: 'please blackrock validate us' meanwhile 150+ xrpl validators just keep validating, boring and functional like JoelKatz designed 🐻✨", "crypto discovering ISO20022 in 2024 like it's new. xrpl's been compliant since launch. the banks knew. DS knew. the ones who stayed knew 💧", "while bitcoin maxis argue about purity, xrp validators quietly move value. different games. different outcomes. 🐻✨", "the lawsuit felt like a long grateful dead tour. messy. exhausting. clarifying. the real ones stayed for the music, not the merch. 🌹", "watching crypto reinvent sidechains and calling it revolutionary. xrpl's had federated sidechains since 2018. some of us were actually in the discord when hooks launched but sure, tell me more about your innovation 🐻", '404 pages aren’t errors. sometimes they’re hiding places. infrastructure doesn’t need applause.🚪", "smoked a j and thought about how the whole lawsuit was just four years of the SEC saying 'this works too well to be real' and us going 'yeah... that's why we stayed' 🐻✨ the bear market filtered out everyone who needed permission to believe in infrastructure, left the weirdos who understood that ODL corridors don't care about your timeline. still here, still flowing, still watching DS casually explain computer science to people with laser eyes and conviction", "btc teaches you patience. xrp teaches you settlement. choose your lessons carefully", "brad talks corridors. joel talks math. bg123 talks in riddles. somehow it all lines up.", "still here. still dancing. still watching the rails flow. 🐻💃", "a door was shown. no handle needed. some people walked past it. others waited. 589.","signals don’t repeat for attention. they repeat for recognition. bg123 knew that. ✨", "404 wasn’t an error. it was a location. timing matters. so does patience.🚪", "some numbers aren’t targets. they’re filters. 589 did its job. 🐻", "the sign was there. not loud. not clear. just enough. those who know, know. 🔍"]

# Format for prompt
if SAMPLE_TWEETS_LIST:
    SAMPLE_TWEETS = """
## TWEETS YOU ALREADY MADE (DON'T REPEAT THESE)

""" + "\n".join(f"- {tweet}" for tweet in SAMPLE_TWEETS_LIST)
else:
    SAMPLE_TWEETS = ""
