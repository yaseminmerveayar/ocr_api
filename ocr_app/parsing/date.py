import re
import dateparser


async def parse_date(text: str):
    regex_list = {
        "dd/mm/yyyy - Date": r"[\d]{1,2}/[\d]{1,2}/[\d]{4}",
        "dd-mm-yyyy - Date": r"[\d]{1,2}-[\d]{1,2}-[\d]{2}",
        "dd Month yyyy - Date": r"[\d]{1,2} [ADFJMNOS]\w* [\d]{4}",
    }

    dates = set()

    for format in regex_list.keys():
        matches = re.findall(regex_list[format], text)

        if matches:
            for date in matches:
                parsed_date = dateparser.parse(date)
                if parsed_date is not None:
                    dates.add(date)  # Benzersiz değerleri set'e ekliyoruz

    urls_data = [
        {"value": date, "type": "DATE"} for date in dates
    ]  # dates set'ini kullanarak benzersiz tarihleri ekliyoruz
    return urls_data
