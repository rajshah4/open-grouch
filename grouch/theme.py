"""Oscar the Grouch theme for textual UI.

Trash can green aesthetic with grouchy vibes.
"""

from textual.theme import Theme


def create_grouch_theme() -> Theme:
    """Create and return the custom Grouch theme."""
    return Theme(
        name="grouch",
        # Trash can / Oscar green tones
        primary="#7CB342",       # Grouch green (Oscar's color)
        secondary="#A5D6A7",     # Lighter green for borders
        accent="#8BC34A",        # Accent green
        foreground="#E8F5E9",    # Light green-white text
        background="#1B2E1B",    # Dark green background (inside trash can)
        surface="#243324",       # Slightly lighter surface
        panel="#1B2E1B",         # Panel matches background
        success="#7CB342",       # Success in grouch green
        warning="#FDD835",       # Warning in yellow (banana peel)
        error="#E57373",         # Errors in muted red
        dark=True,
        variables={
            # Placeholder text - dimmed green
            "input-placeholder-foreground": "#5D7A5D",
            # Selection colors
            "input-selection-background": "#7CB342 30%",
        },
    )


# Create the theme instance
GROUCH_THEME = create_grouch_theme()


# Color constants for use in Rich markup
class Colors:
    """Color constants for Rich markup in strings."""
    PRIMARY = "#7CB342"
    SECONDARY = "#A5D6A7"
    ACCENT = "#8BC34A"
    WARNING = "#FDD835"
    ERROR = "#E57373"
    DIM = "#5D7A5D"
    TRASH_CAN = "#4E6B4E"  # Darker green for trash can elements
