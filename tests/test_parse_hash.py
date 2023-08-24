import pytest

from ocr_app.parsing.hash import parse_hash


@pytest.mark.asyncio
async def test_parse_hash():
    text = """Bu bir örnek metin içerisinde
    md5:5eb63bbbe01eeed093cb22bb8f5acdc3 
    ve sha256:7815696ecbf1c96e6894b779456d330e
    ile sha1:2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c
    sha512:0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef 
    örnek hash değerleri bulunmaktadır."""

    expected_result = [
        {"value": "5eb63bbbe01eeed093cb22bb8f5acdc3", "type": "HASH"},
        {"value": "7815696ecbf1c96e6894b779456d330e", "type": "HASH"},
        {"value": "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c", "type": "HASH"},
        {
            "value": "0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef",
            "type": "HASH",
        },
    ]

    result = await parse_hash(text)

    # aynı sıralamaya getir
    sorted_expected_result = sorted(expected_result, key=lambda x: x["value"])
    sorted_result = sorted(result, key=lambda x: x["value"])

    assert sorted_result == sorted_expected_result
