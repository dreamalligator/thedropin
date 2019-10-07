"""
Handle registration and setup for plugin.
"""

from pelican import signals
from .emoji import cat_emoji

def add_exciting_metadata(_generator, metadata):
    metadata.emoji = cat_emoji()

# signals list: https://docs.getpelican.com/en/latest/plugins.html#list-of-signals
def register():
    signals.article_generator_context.connect(add_exciting_metadata)
