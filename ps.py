import sys
import os
import colorama

def replaceAll(content, replacements):
    for old_value, new_value in replacements.items():
        content = content.replace(old_value, new_value)
    return content

replall = """
import re

def replaceAll(text, pattern, replacement):
    return re.sub(pattern, replacement, text)

"""

args = sys.argv

try:
    if len(args) > 1 and args[1] != '':
        arg = args[1]
        path = os.path.join(os.getcwd(), arg)
        if os.path.exists(path):
            with open(path, 'r') as file:
                original_content = file.read()
                replacements = {
                    "!false": "True",
                    "!true": "False",   
                    "true": "True",
                    "false": "False",
                    "!0": "True",
                    "!1": "False",
                    "null": "None"
                }
                modified_content = replaceAll(original_content, replacements)
                with open("modified_" + arg, 'w') as modified_file:
                    modified_file.write(replall)
                    modified_file.write(modified_content)
                    modified_file.flush()
                    modified_file.close()
                os.system(f'python modified_{arg}')
                os.remove(f'modified_{arg}')
        else:
            print(f'{colorama.Fore.RED}Cannot run PythonScript without a file.{colorama.Style.RESET_ALL}')
    else:
        print(f'{colorama.Fore.RED}Cannot run PythonScript without a file.{colorama.Style.RESET_ALL}')
except Exception:
    print(f'{colorama.Fore.RED}Cannot run PythonScript without a file.{colorama.Style.RESET_ALL}')
