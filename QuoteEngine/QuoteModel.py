"""Module to create quotes."""
class QuoteModel:
    """Represent models for Quote."""

    def __init__(self, body, author):
        """Create a new `Quote Model`."""
        self.body = body
        self.author = author

    def __repr__(self):
        """Return a representation of Quote Model, which is 'text - author'."""
        return f"{self.body} - {self.author}"
