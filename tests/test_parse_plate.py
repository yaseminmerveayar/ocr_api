import pytest

from ocr_app.parsing.plate import parse_plate


@pytest.mark.asyncio
async def test_parse_hash():
    text = """Bugün şehirde 34 AB 5678 
    plakalı bir araba gördüm. Ardından
    06 CD 123 plakalı bir araç geçti. 
    35 XYZ 987 plakalı araç ise hızla 
    ilerliyordu 35 XYZ 987."""

    expected_result = [
        {"value": "34 AB 5678", "type": "PLATE"},
        {"value": "06 CD 123", "type": "PLATE"},
        {"value": "35 XYZ 987", "type": "PLATE"},
    ]

    result = await parse_plate(text)
    print(result)
    # aynı sıralamaya getir
    sorted_expected_result = sorted(expected_result, key=lambda x: x["value"])
    sorted_result = sorted(result, key=lambda x: x["value"])

    assert sorted_result == sorted_expected_result
