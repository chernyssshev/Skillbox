import re
from typing import List

text = """ Lorem ipsum dolor sit amet, consectetuer adipiscing elit. 
Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, 
nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. 
Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate 
"""


def choose_words(text: str, world_length: int) -> List[str]:
    pattern = r'\b\w{%i}\b' % (world_length)
    res = re.findall(pattern, text)
    # print(res)
    if res:
        return res
    else:
        return []


if __name__ == '__main__':
    print(choose_words(text, 3))
    print(choose_words(text, 4))
    print(choose_words(text, 5))
