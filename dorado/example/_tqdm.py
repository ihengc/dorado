"""
@author:Ihc
@file:_tqdm.py
@date:2022/7/6 0:41
@description:
"""
import time

from tqdm import tqdm


def main():
    for i in tqdm(range(1000)):
        time.sleep(.01)


main()
