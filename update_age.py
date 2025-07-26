import datetime

# your year of birth
birth_year = 2003
current_year = datetime.datetime.now().year
age = current_year - birth_year

# read README.md
with open("README.md", "r", encoding="utf-8") as file:
    content = file.read()

# Update age (behive 2 tag <!--AGE-->)
import re
new_content = re.sub(r"<!--AGE-->.*?<!--AGE-->", f"<!--AGE-->{age}<!--AGE-->", content)

# write README.md
with open("README.md", "w", encoding="utf-8") as file:
    file.write(new_content)
