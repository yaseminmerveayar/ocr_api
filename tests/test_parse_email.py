import pytest

from ocr_app.parsing.email import parse_email


@pytest.mark.asyncio
async def test_credit_card_parser():
    test_text = """Merhaba, e-posta adresim john.doe@example.com
      ve e-posta şifrem ise 
      john2.doe@example.com:secret123. 
      Lütfen bu bilgileri güvende tutunuz 
      ve kimseyle paylaşmayınız john.doe@example.com.
    """

    expected_result = [
        {"value": "john.doe@example.com", "type": "EMAIL"},
        {"value": "john2.doe@example.com", "type": "EMAIL"},
    ]

    result = await parse_email(test_text)
    print(result)

    sorted_expected_result = sorted(expected_result, key=lambda x: x["value"])
    sorted_result = sorted(result, key=lambda x: x["value"])

    assert sorted_result == sorted_expected_result
