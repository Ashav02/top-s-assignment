#find a zometo_order.json existing in the current directory.

from pathlib import Path

file = Path("session-14/zometo_order.json")

if file.exists():
    print("File Exists")
else:
    print("File Not Found")
