from ocr_app.parsing import (
    url,
    combolist,
    credit_card,
    date,
    domain,
    email,
    hash,
    id_number,
    phone_number,
    plate,
)
import asyncio


async def parse_text(text: str):
    tasks = [
        hash.parse_hash(text),
        url.parse_url(text),
        combolist.parse_combolist(text),
        credit_card.parse_credit_card(text),
        date.parse_date(text),
        domain.parse_domain(text),
        email.parse_email(text),
        id_number.parse_id_number(text),
        phone_number.parse_phone_number(text),
        plate.parse_plate(text),
    ]

    results = await asyncio.gather(*tasks)

    non_empty_results = []

    for result in results:
        if result:
            non_empty_results.extend(result)

    return non_empty_results
