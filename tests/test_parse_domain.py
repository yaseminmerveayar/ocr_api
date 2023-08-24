import pytest

from ocr_app.parsing.domain import parse_domain


@pytest.mark.asyncio
async def test_credit_card_parser():
    test_text = """
    Merhaba, bugün OpenAI'nin resmi web sitesi 
    olan www.openai.com/ adresini ziyaret 
    edebilirsiniz. Ayrıca, teknoloji haberleri 
    için exampletechnews.com sitesi 
    de oldukça popüler. Eğer rehberlik hizmetlerine 
    ihtiyacınız varsa, https://www.guidancehelpcenter.org/ 
    adresine göz atabilirsiniz.
    """

    expected_result = [
        {"value": "openai.com", "type": "DOMAIN"},
        {"value": "exampletechnews.com", "type": "DOMAIN"},
    ]

    result = await parse_domain(test_text)
    print(result)

    sorted_expected_result = sorted(expected_result, key=lambda x: x["value"])
    sorted_result = sorted(result, key=lambda x: x["value"])

    assert sorted_result == sorted_expected_result
