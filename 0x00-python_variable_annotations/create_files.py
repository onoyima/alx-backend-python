import os

# Define the directory and filenames
repo_dir = "alx-backend-python/0x00-python_variable_annotations"
os.makedirs(repo_dir, exist_ok=True)

files_content = {
    "0-add.py": """#!/usr/bin/env python3
\"\"\"Module for addition function\"\"\"

def add(a: float, b: float) -> float:
    \"\"\"Returns the sum of a and b\"\"\"
    return a + b
""",

    "1-concat.py": """#!/usr/bin/env python3
\"\"\"Module for concatenation function\"\"\"

def concat(str1: str, str2: str) -> str:
    \"\"\"Returns the concatenation of str1 and str2\"\"\"
    return str1 + str2
""",

    "2-floor.py": """#!/usr/bin/env python3
\"\"\"Module for floor function\"\"\"
import math

def floor(n: float) -> int:
    \"\"\"Returns the floor of n\"\"\"
    return math.floor(n)
""",

    "3-to_str.py": """#!/usr/bin/env python3
\"\"\"Module for to_str function\"\"\"

def to_str(n: float) -> str:
    \"\"\"Returns the string representation of n\"\"\"
    return str(n)
""",

    "4-define_variables.py": """#!/usr/bin/env python3
\"\"\"Module for defining variables\"\"\"

a: int = 1
pi: float = 3.14
i_understand_annotations: bool = True
school: str = "Holberton"
""",

    "5-sum_list.py": """#!/usr/bin/env python3
\"\"\"Module for sum_list function\"\"\"
from typing import List

def sum_list(input_list: List[float]) -> float:
    \"\"\"Returns the sum of a list of floats\"\"\"
    return sum(input_list)
""",

    "6-sum_mixed_list.py": """#!/usr/bin/env python3
\"\"\"Module for sum_mixed_list function\"\"\"
from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    \"\"\"Returns the sum of a mixed list of integers and floats\"\"\"
    return sum(mxd_lst)
""",

    "7-to_kv.py": """#!/usr/bin/env python3
\"\"\"Module for to_kv function\"\"\"
from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    \"\"\"Returns a tuple with k and the square of v\"\"\"
    return (k, float(v ** 2))
""",

    "8-make_multiplier.py": """#!/usr/bin/env python3
\"\"\"Module for make_multiplier function\"\"\"
from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    \"\"\"Returns a function that multiplies a float by multiplier\"\"\"
    def multiply(x: float) -> float:
        return x * multiplier
    return multiply
""",

    "9-element_length.py": """#!/usr/bin/env python3
\"\"\"Module for element_length function\"\"\"
from typing import Iterable, Sequence, List, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    \"\"\"Returns a list of tuples with each element and its length\"\"\"
    return [(i, len(i)) for i in lst]
""",

    "100-safe_first_element.py": """#!/usr/bin/env python3
\"\"\"Module for safe_first_element function\"\"\"
from typing import Sequence, Any, Union

def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    \"\"\"Returns the first element of lst or None if lst is empty\"\"\"
    if lst:
        return lst[0]
    else:
        return None
""",

    "101-safely_get_value.py": """#!/usr/bin/env python3
\"\"\"Module for safely_get_value function\"\"\"
from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')

def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    \"\"\"Returns the value of dct[key] or default if key is not in dct\"\"\"
    if key in dct:
        return dct[key]
    else:
        return default
""",

    "102-type_checking.py": """#!/usr/bin/env python3
\"\"\"Module for zoom_array function\"\"\"
from typing import Tuple, List

def zoom_array(lst: Tuple, factor: int = 2) -> List:
    \"\"\"Returns a zoomed in list from a tuple\"\"\"
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in

array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
"""
}

# Create README.md file
readme_content = """# alx-backend-python

This repository contains solutions to tasks related to Python variable annotations.
"""

with open(os.path.join(repo_dir, "README.md"), "w") as readme_file:
    readme_file.write(readme_content)

# Create each task file with the specified content
for filename, content in files_content.items():
    file_path = os.path.join(repo_dir, filename)
    with open(file_path, "w") as file:
        file.write(content)
    os.chmod(file_path, 0o755)  # Make the file executable

print("All files have been created successfully.")

