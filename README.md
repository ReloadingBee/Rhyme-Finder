# Rhyme Finder

Rhyme Finder is a Python project that helps you find words that rhyme with a given word.

## Description

Rhyme Finder is a simple tool that uses the RhymeBrain API to fetch rhyming words for a given word. It provides an easy way to explore and discover words that have similar sounds.

## Installation

1. Make sure you have [Python](https://www.python.org/) installed.
2. Install the required dependencies by running the following command:
    ```pip install requests```

## Usage

To use Rhyme Finder, you can call the `rhyme` function and provide a word to find rhymes for. Optionally, you can specify the maximum number of results to retrieve.

```python
from rhyme_finder import rhyme

result = rhyme("example", maxResults=10)
print(result)```

The rhyme function takes a word as the first argument and an optional maxResults parameter to specify the maximum number of rhymes to retrieve (default is 5). It returns a list of rhyming words in JSON format.
