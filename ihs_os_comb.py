import json, re
from itertools import combinations
from deepdiff import DeepDiff
from bs4 import BeautifulSoup

def normalize_string_htmls(html: str):
    return re.sub(r"^\s+|\s+$", "", html, flags=re.MULTILINE)

#Chromes
with open('ihs_chrome_macos.html', 'r', encoding='utf-8') as f1:
        chrome_macos = f1.read()

with open('ihs_chrome_windows.html', 'r', encoding='utf-8') as f2:
    chrome_win = f2.read()

with open('ihs_chrome_ubuntu.html', 'r', encoding='utf-8') as f3:
    chrome_ubuntu = f3.read()

#Firefoxes

with open('ihs_firefox_macos.html', 'r', encoding='utf-8') as f1:
    firefox_macos = f1.read()

with open('ihs_firefox_windows.html', 'r', encoding='utf-8') as f2:
    firefox_win = f2.read()

with open('ihs_firefox_ubuntu.html', 'r', encoding='utf-8') as f3:
    firefox_ubuntu = f3.read()


banks = ["ihs"]
browsers = ["chrome", "firefox",]
oses = ["macos", "win11", "ubuntu"]
os_combinations = ['-'.join(elem) for elem in list(combinations(oses, 2))]

final_comparisons = {}



result = DeepDiff(normalize_string_htmls(chrome_win), normalize_string_htmls(chrome_macos))
diff = result["values_changed"]["root"]["diff"] if result != {} else ""
with open("C:\\Users\\hp\\Desktop\\DOM\\DOM-Parse-Compare\\seperate_results\\win-macos_ihs_chrome.diff", "w", encoding='utf-8') as f:
    if diff == "":
        f.writelines("no change observed")
    else:
        diff = diff.replace("---", "")
        diff = diff.replace("+++", "")
        prefix_string = """diff --git a/sample.js b/sample.js
        index 0000001..0ddf2ba
        --- a/sample.js
        +++ b/sample.js"""
        diff = prefix_string + diff
        f.writelines(diff)

result2 = DeepDiff(normalize_string_htmls(chrome_win), normalize_string_htmls(chrome_ubuntu))
diff = result2["values_changed"]["root"]["diff"] if result != {} else ""
with open("C:\\Users\\hp\\Desktop\\DOM\\DOM-Parse-Compare\\seperate_results\\win-ubuntu_ihs_chrome.diff", "w", encoding='utf-8') as f:
    if diff == "":
        f.writelines("no change observed")
    else:
        diff = diff.replace("---", "")
        diff = diff.replace("+++", "")
        prefix_string = """diff --git a/sample.js b/sample.js
        index 0000001..0ddf2ba
        --- a/sample.js
        +++ b/sample.js"""
        diff = prefix_string + diff
        f.writelines(diff)

result3 = DeepDiff(normalize_string_htmls(chrome_macos), normalize_string_htmls(chrome_ubuntu))
diff = result3["values_changed"]["root"]["diff"] if result != {} else ""
with open("C:\\Users\\hp\\Desktop\\DOM\\DOM-Parse-Compare\\seperate_results\\macos-ubuntu_ihs_chrome.diff", "w", encoding='utf-8') as f:
    if diff == "":
        f.writelines("no change observed")
    else:
        diff = diff.replace("---", "")
        diff = diff.replace("+++", "")
        prefix_string = """diff --git a/sample.js b/sample.js
        index 0000001..0ddf2ba
        --- a/sample.js
        +++ b/sample.js"""
        diff = prefix_string + diff
        f.writelines(diff)

result4 = DeepDiff(normalize_string_htmls(firefox_win), normalize_string_htmls(firefox_macos))
diff = result4["values_changed"]["root"]["diff"] if result != {} else ""
with open("C:\\Users\\hp\\Desktop\\DOM\\DOM-Parse-Compare\\seperate_results\\win-macos_ihs_firefox.diff", "w", encoding='utf-8') as f:
    if diff == "":
        f.writelines("no change observed")
    else:
        diff = diff.replace("---", "")
        diff = diff.replace("+++", "")
        prefix_string = """diff --git a/sample.js b/sample.js
        index 0000001..0ddf2ba
        --- a/sample.js
        +++ b/sample.js"""
        diff = prefix_string + diff
        f.writelines(diff)

result5 = DeepDiff(normalize_string_htmls(firefox_win), normalize_string_htmls(firefox_ubuntu))
diff = result5["values_changed"]["root"]["diff"] if result != {} else ""
with open("C:\\Users\\hp\\Desktop\\DOM\\DOM-Parse-Compare\\seperate_results\\win-ubuntu_ihs_firefox.diff", "w", encoding='utf-8') as f:
    if diff == "":
        f.writelines("no change observed")
    else:
        diff = diff.replace("---", "")
        diff = diff.replace("+++", "")
        prefix_string = """diff --git a/sample.js b/sample.js
        index 0000001..0ddf2ba
        --- a/sample.js
        +++ b/sample.js"""
        diff = prefix_string + diff
        f.writelines(diff)

result6 = DeepDiff(normalize_string_htmls(firefox_macos), normalize_string_htmls(firefox_ubuntu))
diff = result6["values_changed"]["root"]["diff"] if result != {} else ""
with open("C:\\Users\\hp\\Desktop\\DOM\\DOM-Parse-Compare\\seperate_results\\macos-ubuntu_ihs_firefox.diff", "w", encoding='utf-8') as f:
    if diff == "":
        f.writelines("no change observed")
    else:
        diff = diff.replace("---", "")
        diff = diff.replace("+++", "")
        prefix_string = """diff --git a/sample.js b/sample.js
        index 0000001..0ddf2ba
        --- a/sample.js
        +++ b/sample.js"""
        diff = prefix_string + diff
        f.writelines(diff)

