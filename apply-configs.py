import json
import re
import time
from datetime import datetime
from enum import Enum
import logging
import difflib

def find_different_parts(string1, string2):
    diff = difflib.ndiff(string1.split(), string2.split())
    different_parts = [part for part in diff if part.startswith('-') or part.startswith('+')]
    return different_parts

# Define the Rule class
class Rule:
    def __init__(self, rule_type, action, pattern=None, value=None):
        self.type = rule_type
        self.action = action
        self.pattern = pattern
        self.value = value
    
    def apply(self, text):
        if self.type == 'regex':
            if (self.action == 'replace'):
                # print the group 1 with value
                group = re.search(self.pattern, text)
                
                # if multiple groups, then replace all
                if group:
                    logging.info(f'Rule applied')
                    return re.sub(self.pattern, self.value, text)
                else:
                    logging.info(f'Rule case not found')
                    return text
    
    def __str__(self):
        return f'{self.type} {self.action} {self.pattern} {self.value}'

# File
class File():
    def __init__(self, file_name):
        self.file_name = file_name

        # File attributes
        self.domain = None
        self.last_modified = None
        self.rules = []
        self.inherited_files = []

        # Parse the file
        self.parse(file_name)

    def parse(self, file_name):
        with open(file_name) as f:
            data = json.load(f)

        self.domain = data['domain']
        self.last_modified = data['lastUpdated']
        self.inherited_files = data.get('inherits', [])

        for rule in data['rules']:
            self.rules.append(Rule(rule['type'], rule['action'], rule['pattern'], rule['value']))


class Interpreter():
    def __init__(self):
        self.config_files = []
        self.inherited_files = []
        self.rules = []

    def load_config(self, file_name):
        logging.info(f'Loading config file {file_name}')
        self.config_files.append(File(file_name))

    def load_rules(self):
        for config_file in self.config_files:
            self.rules.extend(config_file.rules)

        # load inherited rules
        for config_files in self.config_files:
            for inherited_file in config_files.inherited_files:
                logging.info(f'Loading inherited config file {inherited_file}')
                self.inherited_files.append(File(inherited_file))
        
        for inherited_file in self.inherited_files:
            self.rules.extend(inherited_file.rules)

        logging.info(f'Loaded {len(self.rules)} rules')
    
    def exec(self, file):
        read_string = open(file, 'r').read()
    
        for rule in self.rules:
            if rule.match(read_string):
                logging.info(f'Rule {rule} matched')
                read_string = rule.apply(read_string)
                logging.info(f'Rule {rule} applied')


    def check_two_same(self, file1, file2):

        with open(file1, 'r', encoding='utf-8') as f1:
            read_string1 = f1.read()
        
        with open(file2, 'r', encoding='utf-8') as f2:
            read_string2 = f2.read()

        for rule in self.rules:
            logging.info(f'Rule {rule} matched')
            read_string1 = rule.apply(read_string1)
            read_string2 = rule.apply(read_string2)
        

        if read_string1 == read_string2:
            logging.info(f'Files are same')
        else:
            different_parts = find_different_parts(read_string1, read_string2)

            for part in different_parts:
                print(part)
            logging.info(f'Files are different')


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    interpreter = Interpreter()
    interpreter.load_config('ihs-config.json')
    interpreter.load_rules()

    interpreter.check_two_same('C:\\Users\\hp\Desktop\\DOM\DOM-Parse-Compare\\ihs_chrome_macos.html',
                                'C:\\Users\\hp\Desktop\\DOM\\DOM-Parse-Compare\\ihs_chrome_ubuntu.html')