import os
import random

import jdatetime
from termcolor import colored


def generate_random_number(length: int):
    result = ""
    for i in range(length):
        result += str(random.randint(1, 9))
    return result


def get_extension_file(filename):
    return os.path.splitext(filename)[-1]


def generate_otp(length=6):
    result = ""
    for i in range(length):
        result += str(random.randint(1, 9))
    return result


def numeric_month_to_name(month: int):
    jalali_month = {
        1: "فروردین",
        2: "اردیبهشت",
        3: "خرداد",
        4: "تیر",
        5: "مرداد",
        6: "شهریور",
        7: "مهر",
        8: "آبان",
        9: "آذر",
        10: "دی",
        11: "بهمن",
        12: "اسفند",
    }
    return jalali_month[month]


def format_text_color(text, color="white", bg_color="black"):
    on_color = "on_" + bg_color
    return colored(
        text=text,
        color=color,
        on_color=on_color,
    )


def convert_jalali_fw_sep_to_gregorian(jalali_date):
    year, month, day = jalali_date.split("/")
    gregorian_date = jdatetime.date(int(year), int(month), int(day)).togregorian()
    return gregorian_date
