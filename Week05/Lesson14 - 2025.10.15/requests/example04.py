from bs4 import BeautifulSoup

html_content = """
<div class="container">
    <h1>Python Course</h1>
    <p id="description">Python Programming Language Training</p>
    <ul>
        <li class="topic">Variables</li>
        <li class="topic">Functions</li>
        <li class="topic">Loops</li>
    </ul>
</div>
"""

html_soup = BeautifulSoup(html_content, "html.parser")

# ! Finding the title of the h1 tag and description of the course.
print("Title of the h1 tag: ", html_soup.h1.text)
# Title of the h1 tag:  Python Course

# ! Finding the description of the course.
print("Description of the course: ", html_soup.find(id="description").text)
# Description of the course:  Python Programming Language Training

# ! Finding all the topics covered in the course.
print("Topics covered in the course:")
for topic in html_soup.find_all(class_="topic"):
  print(topic.text)
# Topics covered in the course:
# Variables
# Functions
# Loops

# ! Finding the container div using class attribute.
print("Container div:")
print(html_soup.find(attrs={"class": "container"}).text)
# Container div:
# Python Course
# Python Programming Language Training

# Variables
# Functions
# Loops

# ! Finding all the li tags.
print("List of all the li tags:")
topics = html_soup.find_all("li")
for i, topic in enumerate(topics, 1):
  print(f"{i}. {topic.text}")
# List of all the li tags:
# 1. Variables
# 2. Functions
# 3. Loops
