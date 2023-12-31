import re


async def parse_hash(text: str):
    """
    Parse the text with pattern and extract hash

    Args:
        text : given text
    
    Return:
        List included all hashes and type
    """

    regex_list = {
        "sha1": r"(?<!\w)[a-f\d]{40}(?!\w)",
        "md5": r"(?<!\w)[a-f\d]{32}(?!\w)",
        "sha256": r"(?<!\w)[a-f\d]{64}(?!\w)",
        "sha512": r"(?<!\w)[a-f\d]{128}(?!\w)",
    }

    hashes = set()
    for format in regex_list.keys():
        matches = re.findall(regex_list[format], text)

        if matches:
            hashes.update(matches)

    return [{"value": hash, "type": "HASH"} for hash in hashes]
