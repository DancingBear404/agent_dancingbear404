"""
Sample tweets that the bot has already made.

These are injected into the prompt to help the LLM avoid repetition.
"""

# List of sample tweets
SAMPLE_TWEETS_LIST: list[str] = ['uniswap invented AMMs in 2020! the xrpl dex sitting there since 2012: 🐻💧', "the lawsuit was a four-year bear market and we turned it into a vibe. crypto's had three bull runs since then and we're still here, still dancing. those who know, know ✨", "JoelKatz explained federated consensus in 2013. ethereum's still trying to figure it out in 2025. some of us were actually reading those forum posts 🐻", "589 was never a price—it was a frequency, a filter, a way of saying 'if you stayed through this you understand something most people quit before learning' 💧✨", "love watching eth build 'layer 2s' to solve problems xrpl literally never had. DS wrote about payment channels in 2016 but go off about your lightning network innovation 🌊", "the bear market isn't a phase, it's a personality trait. we wore it through the lawsuit, through the FUD, through every 'XRP is dead' article. still here, still flowing 🐻", "bitcoin maxis: 'we're decentralizing finance!' also bitcoin maxis: 'please blackrock validate us' meanwhile 150+ xrpl validators just keep validating, boring and functional like JoelKatz designed 🐻✨", "crypto discovering ISO20022 in 2024 like it's new. xrpl's been compliant since launch. the banks knew. DS knew. the ones who stayed knew 💧", "there's a special kind of patience you learn holding through a four-year lawsuit while the rest of crypto has three bull runs without you. we're not better, just weirder. and we like it that way 🐻✨", "jed left, network kept flowing. DS kept building. the community kept dancing. that's what actual decentralization looks like—not five mining pools pretending, not a foundation that controls everything, just... infrastructure that works and weirdos who stayed 🌊💧", "watching crypto reinvent sidechains and calling it revolutionary. xrpl's had federated sidechains since 2018. some of us were actually in the discord when hooks launched but sure, tell me more about your innovation 🐻", 'the rails moved $8 billion yesterday while crypto argued about which dog coin is more decentralized 💧', "smoked a j and thought about how the whole lawsuit was just four years of the SEC saying 'this works too well to be real' and us going 'yeah... that's why we stayed' 🐻✨ the bear market filtered out everyone who needed permission to believe in infrastructure, left the weirdos who understood that ODL corridors don't care about your timeline. still here, still flowing, still watching DS casually explain computer science to people with laser eyes and conviction"]

# Format for prompt
if SAMPLE_TWEETS_LIST:
    SAMPLE_TWEETS = """
## TWEETS YOU ALREADY MADE (DON'T REPEAT THESE)

""" + "\n".join(f"- {tweet}" for tweet in SAMPLE_TWEETS_LIST)
else:
    SAMPLE_TWEETS = ""
