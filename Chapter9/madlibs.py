import sys, os, re
import pyinputplus as pyip
if len(sys.argv) == 2:
    madlibsFile = open(sys.argv[1])
    text = madlibsFile.read()
    madlibsFile.close()
    for wordType in re.compile('ADJECTIVE|NOUN|VERB|ADVERB').findall(text):
        replaced = pyip.inputStr(prompt = f'Enter a{"n" if wordType[0] == "A" else ""} {wordType.lower()}:\n')
        text = text.replace(wordType, replaced, 1)
    print(text)
    madlibsFile = open(sys.argv[1]+'_madlibbed', 'w')
    madlibsFile.write(text)
