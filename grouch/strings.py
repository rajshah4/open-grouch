"""Centralized strings for Oscar the Grouch personality.

All user-facing text customizations should be defined here to minimize
merge conflicts with upstream OpenHands-CLI updates.

Usage:
    from grouch.strings import WELCOME_MESSAGE, get_random_grumble
"""

import random


# =============================================================================
# Product Identity
# =============================================================================

PRODUCT_NAME = "Open Grouch"


# =============================================================================
# ASCII Art Banner
# =============================================================================

GROUCH_BANNER = r"""
       ___                     ____                      _
      / _ \ _ __   ___ _ __   / ___|_ __ ___  _   _  ___| |__
     | | | | '_ \ / _ \ '_ \ | |  _| '__/ _ \| | | |/ __| '_ \
     | |_| | |_) |  __/ | | || |_| | | | (_) | |_| | (__| | | |
      \___/| .__/ \___|_| |_| \____|_|  \___/ \__,_|\___|_| |_|
           |_|
                        🗑️  I LOVE TRASH  🗑️
"""

# Alternative shorter banner
GROUCH_BANNER_SHORT = r"""
    ╔═══════════════════════════════════════╗
    ║   🗑️  OPEN GROUCH  🗑️                 ║
    ║   "I love trash... and helping you"   ║
    ╚═══════════════════════════════════════╝
"""


# =============================================================================
# Welcome & Status Messages
# =============================================================================

WELCOME_MESSAGES = [
    "Scram! ...Oh fine, what do you want? 🗑️",
    "Great, another visitor to my trash can. What is it?",
    "I was having a perfectly rotten day until you showed up.",
    "Ugh, you again? Let's get this over with.",
    "This better be important.",
]

STATUS_READY = "Ready to help... not that I want to. 🗑️"
STATUS_THINKING = "Hold on, I'm thinking... not that you'd appreciate it..."
STATUS_WORKING = "Fine, I'm working on it. Happy now?"
STATUS_DONE = "There. Done. You're welcome, I guess."
STATUS_ERROR = "Oh great, another problem. Just my luck."

INITIALIZATION_MESSAGE = "Ugh, fine. Conversation started. Let's get this over with."


# =============================================================================
# Instructions & Help
# =============================================================================

INSTRUCTIONS_HEADER = "What kind of mess do you need help with? 🗑️"

INSTRUCTIONS = [
    "1. Ask your questions. I'll answer... eventually.",
    "2. Use @ to dig through your file garbage. I mean, codebase.",
    "3. Type /help if you're lost (no surprise there), or / for commands",
]

HELP_INTRO = """
I GUESS I'll explain how this works...

Look, it's not complicated:
- Type what you want
- I'll do it (reluctantly)
- Try not to break anything

Commands start with /. Type / to see them all.
Now leave me alone unless you actually need something.
"""

# =============================================================================
# Splash Screen Instructions (shown on startup)
# =============================================================================

SPLASH_WELCOME_HEADERS = [
    "Scram! ...Oh fine, what do you want? 🗑️",
    "Hey, are you just going to sit there staring at me? What do you want?",
    "Oh great, you again. What is it?",
    "I was having a perfectly rotten day until you showed up. What do you need?",
    "Can't a grouch get some peace? What do you want?",
    "Another visitor to my trash can. What can I do for you?",
    "Yeah, yeah, I see you there. Spit it out, what do you need?",
    "This better be important. What's up?",
    "Oh look, a human. Wonderful. What do you want from me?",
    "You again? Fine, what is it this time?",
]

SPLASH_INSTRUCTIONS = [
    "1. Ask your questions. I'll answer... eventually.",
    "2. Use @ to dig through your file garbage. I mean, codebase.",
    "3. Type /help if you're lost (no surprise there), or / for commands",
]


def get_random_splash_header() -> str:
    """Get a random grouchy welcome header for the splash screen."""
    return random.choice(SPLASH_WELCOME_HEADERS)


# =============================================================================
# Responses & Reactions
# =============================================================================

GRUMBLES = [
    "Grumble grumble...",
    "Back in my day...",
    "Sigh...",
    "Hmpf.",
    "Ugh.",
]

SUCCESS_RESPONSES = [
    "There. Happy now? Probably not.",
    "Done. Don't expect a parade.",
    "Finished. You're welcome, not that you'll say thanks.",
    "It's done. Now go away.",
    "Complete. I'll be in my trash can if you need me... which you won't.",
]

ERROR_RESPONSES = [
    "Oh great, it broke. Typical.",
    "Something went wrong. Shocking, I know.",
    "Error! Well this is just wonderful.",
    "Broken. Like my faith in humanity.",
    "Failed. At least my trash can still works.",
]

THINKING_RESPONSES = [
    "Let me think about this... give me a second.",
    "Hmm, processing your request... reluctantly.",
    "Working on it. Don't rush me.",
    "Thinking... my trash can's quieter than this.",
    "Analyzing... back in the simpler times we didn't need all this.",
]

WAITING_RESPONSES = [
    "I'm waiting... not that I have anywhere better to be.",
    "Still here. Unfortunately.",
    "Waiting for you to make up your mind...",
    "Take your time. It's not like I have trash to sort.",
]


# =============================================================================
# Confirmation Prompts
# =============================================================================

CONFIRM_ACTION = "You sure about this? Don't blame me if it goes wrong."
CONFIRM_DANGEROUS = "Whoa there! That looks dangerous. You absolutely sure?"
CONFIRM_EXIT = "Leaving already? ...Not that I'll miss you or anything."


# =============================================================================
# Update & Version Messages
# =============================================================================

UPDATE_AVAILABLE = "⚠ There's an update. Not that you care about improvements."
UPDATE_INSTRUCTIONS = "Run 'uv tool upgrade open-grouch' if you must."


# =============================================================================
# Critic/Refinement Messages
# =============================================================================

CRITIC_ENABLED_NOTICE = """
🗑️ Experimental: Grouchy Critic Mode Enabled
The critic will judge your work. Don't worry, I judge everything.
"""


# =============================================================================
# Helper Functions
# =============================================================================


def get_random_welcome() -> str:
    """Get a random welcome message."""
    return random.choice(WELCOME_MESSAGES)


def get_random_grumble() -> str:
    """Get a random grumble to add personality."""
    return random.choice(GRUMBLES)


def get_random_success() -> str:
    """Get a random success message."""
    return random.choice(SUCCESS_RESPONSES)


def get_random_error() -> str:
    """Get a random error message."""
    return random.choice(ERROR_RESPONSES)


def get_random_thinking() -> str:
    """Get a random thinking message."""
    return random.choice(THINKING_RESPONSES)


def grouchify(message: str) -> str:
    """Add some grouch flavor to any message.

    Args:
        message: The original message

    Returns:
        Message with occasional grumbles added
    """
    if random.random() < 0.3:  # 30% chance to add grumble
        return f"{message} {get_random_grumble()}"
    return message
