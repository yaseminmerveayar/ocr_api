import pytest

from ocr_app.parsing.date import parse_date


@pytest.mark.asyncio
async def test_credit_card_parser():
    test_text = """
    Toplantı tarihi: 24-08-23
    Toplantı tarihi: 24-08-23
    Konferans tarihi: 15 Ağustos 2023
    Bugün buluşalım: 24/08/2023
    """

    expected_result = [
        {"value": "15 Ağustos 2023", "type": "DATE"},
        {"value": "24-08-23", "type": "DATE"},
        {"value": "24/08/2023", "type": "DATE"},
    ]

    result = await parse_date(test_text)
    print(result)

    sorted_expected_result = sorted(expected_result, key=lambda x: x["value"])
    sorted_result = sorted(result, key=lambda x: x["value"])

    assert sorted_result == sorted_expected_result
