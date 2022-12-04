# insipired by SamDja
import os
from datetime import datetime

for item in [("0" if day < 10 else "") + str(day) for day in range(1, datetime.now().day+1)]:
    if not os.path.exists("./Day" + item):
        os.mkdir("./Day" + item)
        open("./Day"+item+"/input.txt", "w").close()
        open("./Day"+item+"/input_easy.txt", "w").close()

        main = open("./Day"+item+"/main.py", "w")
        main.write('def main(test):\n\trows = open("input_easy.txt").read()\n\tif not test:')
        main.write('\n\t\trows = open("input.txt").read()\n\n\nif __name__ == \'__main__\':\n\tmain(True)\n')
        main.close()
