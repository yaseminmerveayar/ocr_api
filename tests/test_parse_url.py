import pytest

from ocr_app.parsing.url import parse_url


@pytest.mark.asyncio
async def test_parse_hash():
    text = """Bugün internet üzerinde gezerken 
    https://www.example.com sitesine girdim 
    ve kullanıcı adı:parola şeklinde bir 
    combolist gördüm. Sonra http://www.testdomain.net
      adresine geçtim ve farklı bir combolist 
      ile karşılaştım: user1:pass1, user2:pass2. 
      Bu sırada https://www.samplewebsite.com'da 
      dolaşırken başka bir combolist daha 
      gördüm: admin:admin123, test:test456."""

    expected_result = [
        {"value": "https://www.example.com", "type": "URL"},
        {"value": "http://www.testdomain.net", "type": "URL"},
    ]

    result = await parse_url(text)
    print(result)
    # aynı sıralamaya getir
    sorted_expected_result = sorted(expected_result, key=lambda x: x["value"])
    sorted_result = sorted(result, key=lambda x: x["value"])

    assert sorted_result == sorted_expected_result
