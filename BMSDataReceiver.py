import sys

print("Output from Python Receiver!!", end="")
for line in sys.stdin:
    print(line.replace('\n', ''))
