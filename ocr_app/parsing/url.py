import re
import validators


async def parse_url(text: str):
    pattern = r"\s(?:www.)?(\w+.com)"
    matches: list = re.findall(pattern, text)
    urls = []
    if matches:
        for url in matches:
            if validators.url(url):
                urls.append({"value": url, "type": "url"})

    return urls
