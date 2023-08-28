import re
import validators


async def parse_url(text: str):
    """
    Parse the text with pattern and extract url

    Args:
        text : given text
    
    Return:
        List included all valid urls and type
    """

    pattern = r"https?://[^\s/$.?#].[^\s]*"
    matches: list = re.findall(pattern, text)
    urls = set()
    if matches:
        for url in matches:
            if validators.url(url):
                urls.add(url)  # Benzersiz URL'leri set'e ekliyoruz

    urls_list = list(urls)  # Set'i liste olarak çeviriyoruz

    urls_data = [{"value": url, "type": "URL"} for url in urls_list]
    return urls_data
