from bs4 import BeautifulSoup

html_doc = """
<html>
<head><title>Students List</title></head>
<body>
    <div class="students">
        <h1 id="class-title">Class 10-A</h1>
        <ul>
            <li class="student">John Doe</li>
            <li class="student">Mick Jagger</li>
            <li class="student">Michael Jordan</li>
        </ul>
    </div>
</body>
</html>
"""


soup = BeautifulSoup(html_doc, "html.parser")

# ! Fetching data based on HTML tag name
print("Title of the Web Page: ", soup.title.text)
# Title of the Web Page:  Students List

print("Information of the div: ", soup.div.text)
# Information of the div:
# Class 10-A

# John Doe
# Mick Jagger
# Michael Jordan

# ! Fetching data based on ID name
print("Information by ID:", soup.find(id="class-title").text)
# Information by ID: Class 10-A

# ! Fetching data based on class name
# If we want to retrieve only the first piece of information, we use FIND
print("Information by Class Name: ", soup.find(class_="student").text)
# Information by Class Name:  John Doe

# If we want to retrieve all the information, we use FIND_ALL
all_students = soup.find_all(class_="student")
for student in all_students:
  print("Student:", student.text)
# Student: John Doe
# Student: Mick Jagger
# Student: Michael Jordan
