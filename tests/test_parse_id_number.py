import pytest

from ocr_app.parsing.id_number import parse_id_number


@pytest.mark.asyncio
async def test_parse_hash():
    text = """tc kimlik numarası 12345678900
    53851598172 invalid olarak 12345678910"""

    expected_result = [
        {"value": "53851598172", "type": "ID_NUMBER"},
    ]

    result = await parse_id_number(text)

    # aynı sıralamaya getir
    sorted_expected_result = sorted(expected_result, key=lambda x: x["value"])
    sorted_result = sorted(result, key=lambda x: x["value"])

    assert sorted_result == sorted_expected_result
