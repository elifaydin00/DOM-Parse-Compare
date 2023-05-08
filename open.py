import json
import re
import time
from device import Device


def normalize_string_htmls(html: str):
    return re.sub(r"^\s+|\s+$", "", html, flags=re.MULTILINE)


def get_delimeter(os_info):
    return "\\" if os_info == "windows" else "/"


if __name__ == "__main__":
    os_info = input("Please enter your OS (windows, macos, linux): ")
    version = input("Please enter your OS version: ")

    pc = Device(os_info, version)

    with open("script.txt", "r") as f:
        jsscript = f.read()

    pages_lines = open("pages.txt", "r").readlines()
    pages = {}
    for line in pages_lines:
        pages[line[0:line.find(";")]] = line[line.find(";") + 1:].strip()

    banks_and_doms = {}

    for bank, page in pages.items():
        banks_and_doms[bank] = {}

        d5 = pc.edge()
        d5.get(page)
        dom = d5.execute_script(jsscript)
        banks_and_doms[bank]["edge"] = dom
        print(dom)
        d5.quit()