import re
import validators


async def parse_domain(text: str):
    pattern = r"\s(?:www.)?(\w+.com)"
    matches: list = re.findall(pattern, text)
    domains = []
    if matches:
        for domain in matches:
            if validators.domain(domain):
                domains.append({"value": domain, "type": "domain"})

    return domains
