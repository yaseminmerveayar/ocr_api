import re
import validators


async def parse_domain(text: str):
    pattern = r"\s(?:www\.)?(\w+\.\w{2,6})"
    matches: list = re.findall(pattern, text)
    domains = set()
    if matches:
        for domain in matches:
            if validators.domain(domain):
                domains.add(domain)  # Benzersiz URL'leri set'e ekliyoruz

    domain_list = list(domains)  # Set'i liste olarak çeviriyoruz

    urls_data = [{"value": domain, "type": "DOMAIN"} for domain in domain_list]
    return urls_data
