"""
Use this file to write your solution for the Summer Code Jam 2020 Qualifier.

Important notes for submission:

- Do not change the names of the two classes included below. The test suite we
  will use to test your submission relies on existence these two classes.

- You can leave the `ArticleField` class as-is if you do not wish to tackle the
  advanced requirements.

- Do not include "debug"-code in your submission. This means that you should
  remove all debug prints and other debug statements before you submit your
  solution.
"""
import datetime
import itertools
import string
import typing
from collections import defaultdict
from dataclasses import dataclass, field


class ArticleField:
    """The `ArticleField` class for the Advanced Requirements."""


@dataclass
class Article:
    """The `Article` class you need to write for the qualifier."""
    id_iter = itertools.count()
    title: str
    author: str
    publication_date: datetime.datetime
    content: str
    _content: str = field(init=False, repr=False)
    last_edited: datetime.datetime = None

    def __post_init__(self):
        # self.id = next(Article.id_iter)
        self.id = next(Article.id_iter)

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, new_content):
        self.last_edited = datetime.datetime.now()
        self._content = new_content

    def short_introduction(self, n_characters: int = 30) -> str:
        """Will return up to the first `n_characters` characters,
        stopping at the last possible white-space character."""
        first_n_characters = self.content[:n_characters]
        last_white_space = 0
        for i, char in enumerate(first_n_characters):
            if char in [' ', '\n']:
                last_white_space = i
        return self.content[:last_white_space].strip()

    def most_common_words(self, n_most_words: int) -> dict:
        """Returns a dictionary of the most common `n_most_words` words. Words
        are case insensitive, and all non-ascii letters count as a line break"""
        word_counts = defaultdict(lambda: 0)
        lower_case = self.content.casefold()
        # replace all non-ascii letters with spaces
        corrected_words = ''.join([char if char in string.ascii_letters else ' ' for char in lower_case])
        split_words = corrected_words.split()
        for word in split_words:
            word_counts[word] += 1
        word_counts = {k: v for k, v in sorted(word_counts.items(), key=lambda x: x[1], reverse=True)}
        return {k: v for k, v in list(word_counts.items())[:n_most_words]}

    def __repr__(self):
        return f'<Article title={self.title.__repr__()} author={self.author.__repr__()} ' \
               f"publication_date={self.publication_date.isoformat().__repr__()}>"

    def __len__(self):
        return len(self.content)

    def __lt__(self, other):
        return self.publication_date < other.publication_date
