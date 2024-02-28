1.
import re

def match_pattern(input_string):
    pattern = re.compile(r'a[b]*')
    match = pattern.fullmatch(input_string)
    
    if match:
        print(f'"{input_string}" matches the pattern.')
    else:
        print(f'"{input_string}" does not match the pattern.')
input_string = input("Enter a string: ")
match_pattern(input_string)

2.
import re

def match_pattern(input_string):
    pattern = re.compile(r'a[b]{2,3}')
    match = pattern.findall(input_string)
    
    if match:
        print(f'"{input_string}" matches the pattern.')
    else:
        print(f'"{input_string}" does not match the pattern.')

3.
import re

def find_sequences(input_string):
    pattern = re.compile(r'[a-z]+_[a-z]+')
    matches = pattern.findall(input_string)
    
    if matches:
        print(f'Sequences found: {matches}')
    else:
        print('No sequences found.')

4.
import re

def find_sequences(input_string):
    pattern = re.compile(r'[A-Z][a-z]+')
    matches = pattern.findall(input_string)
    
    if matches:
        print(f'Sequences found: {matches}')
    else:
        print('No sequences found.')

5.
import re

def match_pattern(input_string):
    pattern = re.compile(r'a.*b$')
    match = pattern.match(input_string)
    
    if match:
        print(f'"{input_string}" matches the pattern.')
    else:
        print(f'"{input_string}" does not match the pattern.')

6.
import re

def replace_characters(input_string):
    pattern = re.compile(r'[ ,.]')
    replaced_string = pattern.sub(':', input_string)
    
    print(replaced_string)

7.
import re

def snake_to_camel(snake_case_string):
    camel_case_string = re.sub(r'_([a-z])', lambda match: match.group(1).upper(), snake_case_string)
    return camel_case_string

8.
import re

def split_at_uppercase(input_string):
    split_list = re.findall(r'[A-Z][^A-Z]*', input_string)
    return split_list

9.
import re

def insert_spaces(input_string):
    modified_string = re.sub(r'([a-z])([A-Z])', r'\1 \2', input_string)
    return modified_string

10.
import re

def camel_to_snake(camel_case_string):
    snake_case_string = re.sub(r'([a-z])([A-Z])', r'\1_\2', camel_case_string)
    return snake_case_string.lower()
