from pelican_plugin_template.emoji import cat_emoji

def test_cat_emoji():
    """a silly test."""
    assert cat_emoji() == '🐱'
