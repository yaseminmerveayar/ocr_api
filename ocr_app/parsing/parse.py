from ocr_app.parsing import url, combolist, credit_card, date, domain, email, hash
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
    ]

    results = await asyncio.gather(*tasks)

    non_empty_results = [result for result in results if result != []]

    # async with asyncio.TaskGroup() as tg:
    #     task1 = tg.create_task(hash.parse_hash(text))
    #     task2 = tg.create_task(url.parse_url(text))
    #     task3 = tg.create_task(combolist.parse_combolist(text))
    #     task4 = tg.create_task(credit_card.parse_credit_card(text))
    #     task5 = tg.create_task(date.parse_date(text))
    #     task6 = tg.create_task(domain.parse_domain(text))
    #     task7 = tg.create_task(email.parse_email(text))

    # for x in range(6):
    #     findings.append(task1.result())

    # findings.append(task1.result())
    # findings.append(task2.result())
    # findings.append(task3.result())
    # findings.append(task4.result())
    # findings.append(task5.result())
    # findings.append(task6.result())
    # findings.append(task7.result())

    return non_empty_results
