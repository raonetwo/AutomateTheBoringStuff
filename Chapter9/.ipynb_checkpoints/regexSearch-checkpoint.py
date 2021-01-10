import sys, os, re
from pathlib import Path
import pyinputplus as pyip
folder = Path(pyip.inputFilepath(prompt="Provide folder to search for .txt files\n"))
regex = pyip.inputRegexStr('Provide regex string to search\n')
for filePath in folder.glob('*.txt'):
    print(regex.findall(filePath.read_text()))