import requests as rq


def rhyme(word: str, maxResults: str = "5"):
    if word is None:
        return None

    maxResults = str(maxResults)
    base_url = f'https://rhymebrain.com/talk?function=getRhymes&word={word}&maxResults={maxResults}'
    response = rq.get(base_url)
    data = response.json()
    return data
  
