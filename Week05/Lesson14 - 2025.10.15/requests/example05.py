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

# ! Select by class name
print(html_soup.select_one(".container").text)
# Python Course
# Python Programming Language Training

# Variables
# Functions
# Loops


# ! use more then one tag name
print(html_soup.select_one(".container h1").text)
# Python Course

# ! Select by id name
print(html_soup.select_one("#description").text)
# Python Programming Language Training

# ! Select all elements by tag name
print(html_soup.select(".topic"))
# [<li class="topic">Variables</li>, <li class="topic">Functions</li>, <li class="topic">Loops</li>]

print(html_soup.select(".topic")[1].text)
# Functions
