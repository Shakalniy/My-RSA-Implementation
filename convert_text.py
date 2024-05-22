from bidict import bidict  # библиотека для создания двустороннего словаря


letter_to_num = {
    "А": "10",
    "Б": "11",
    "В": "12",
    "Г": "13",
    "Д": "14",
    "Е": "15",
    "Ё": "16",
    "Ж": "17",
    "З": "18",
    "И": "19",
    "Й": "20",
    "К": "21",
    "Л": "22",
    "М": "23",
    "Н": "24",
    "О": "25",
    "П": "26",
    "Р": "27",
    "С": "28",
    "Т": "29",
    "У": "30",
    "Ф": "31",
    "Х": "32",
    "Ц": "33",
    "Ч": "34",
    "Ш": "35",
    "Щ": "36",
    "Ъ": "37",
    "Ы": "38",
    "Ь": "39",
    "Э": "40",
    "Ю": "41",
    "Я": "42",
    " ": "99",
}


letter_dict = bidict(letter_to_num)


def convert_text_to_number(text):
    num = ""
    text = text.upper()
    for c in text:
        num += letter_dict[c]  # используя словарь, переводим символ в число
    return num


def convert_number_to_text(nums):
    bidict_num = letter_dict.inverse
    text = ""

    for i in range(0, len(nums), 2):
        text += bidict_num[nums[i: i + 2]]

    return text
