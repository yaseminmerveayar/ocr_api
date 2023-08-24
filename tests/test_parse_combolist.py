import pytest

from ocr_app.parsing.combolist import parse_combolist


@pytest.mark.asyncio
async def test_parse_combolist():
    text = """Bu bir örnek metin içerisinde 
    user:pass formatlı combolist ve 
    http://example.com örnekleri bulunmaktadır. 
    user1@example.com:pass1 user2:pass2 https://google.com"""

    expected_result = [
        # {"value": "user:pass", "type": "COMBOLIST"},
        {"value": "user1@example.com:pass1", "type": "COMBOLIST"},
        # {"value": "user2:pass2", "type": "COMBOLIST"},
    ]

    result = await parse_combolist(text)

    print(result)

    sorted_expected_result = sorted(expected_result, key=lambda x: x["value"])
    sorted_result = sorted(result, key=lambda x: x["value"])

    assert sorted_result == sorted_expected_result
