import pytest

from ocr_app.parsing.phone_number import parse_phone_number


@pytest.mark.asyncio
async def test_parse_hash():
    text = """tel no 05378105050 0 555 123 45 67
    5368456758 invalid olarak 530 984 45 47  
    530 456 3748  +905378293556 0 555 123 45 67"""

    expected_result = [
        {"value": "5378105050", "type": "PHONE_NUMBER"},
        {"value": "5368456758", "type": "PHONE_NUMBER"},
        {"value": "5309844547", "type": "PHONE_NUMBER"},
        {"value": "5304563748", "type": "PHONE_NUMBER"},
        {"value": "5378293556", "type": "PHONE_NUMBER"},
        {"value": "5551234567", "type": "PHONE_NUMBER"},
    ]

    result = await parse_phone_number(text)

    # aynı sıralamaya getir
    sorted_expected_result = sorted(expected_result, key=lambda x: x["value"])
    sorted_result = sorted(result, key=lambda x: x["value"])

    assert sorted_result == sorted_expected_result
