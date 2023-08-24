import pytest

from ocr_app.parsing.credit_card import parse_credit_card


@pytest.mark.asyncio
async def test_credit_card_parser():
    test_text = """
    Here are some example credit card numbers:
    1234-5678-9012-3456
    5555555555554444
    And here's an invalid one: 1234-5678-9012-3457
    Another valid one: 6011000990139424
    Yet another valid one: 4111111111111111
    An invalid one: 1234567812345678
    """

    expected_result = [
        {"value": "5555555555554444", "type": "CREDIT_CARD_NUMBER"},
        {"value": "6011000990139424", "type": "CREDIT_CARD_NUMBER"},
        {"value": "4111111111111111", "type": "CREDIT_CARD_NUMBER"},
    ]

    result = await parse_credit_card(test_text)
    print(result)

    sorted_expected_result = sorted(expected_result, key=lambda x: x["value"])
    sorted_result = sorted(result, key=lambda x: x["value"])

    assert sorted_result == sorted_expected_result
