import random
import re
from urllib.request import urlopen

# Previous Wordle words
URL = "https://www.rockpapershotgun.com/wordle-past-answers"


def download_page() -> str:
    """Download the webpage and return it as a string."""
    with urlopen(URL) as response:
        return response.read().decode()


def get_word_list(page: str) -> list[str]:
    """Extract the list of previous Wordle answers."""
    start = page.find('<ul class="inline">')
    end = page.find("</ul>", start)

    word_section = page[start:end]

    return re.findall(r"<li>(.*?)</li>", word_section)


def get_random_words(count: int = 25) -> list[str]:
    """Return a random selection of previous Wordle answers."""
    words = get_word_list(download_page())

    return random.sample(words, count)
