import re
import validators


async def parse_hash(text: str):
    regex_list = {
        "sha1": r"(?<!\w)[a-f\d]{40}(?!\w)",
        "md5": r"(?<!\w)[a-f\d]{32}(?!\w)",
        "sha256": r"(?<!\w)[a-f\d]{64}(?!\w)",
        "sha512": r"(?<!\w)[a-f\d]{128}(?!\w)",
    }

    hashes = []
    for format in regex_list.keys():
        matches = re.findall(regex_list[format], text)

        if matches:
            for hash in matches:
                if validators.hashes(hash):
                    hashes.append({"value": hash, "type": format + "- hash"})

    return hashes
