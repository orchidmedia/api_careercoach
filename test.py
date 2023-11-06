import re

response = """Career Path for Full Stack Developer:\n- Introduction: \n  - Full Stack Developer is a versatile role that involves both front-end and back-end development.\n  - They are responsible for designing and implementing complete software solutions.\n  - Full Stack Developers work on various technologies and platforms.\n\n- Skills Required:\n  - Technical Skills: proficiency in front-end and back-end technologies like HTML, CSS, JavaScript, Node.js, and databases.\n  - Soft Skills: problem-solving, teamwork, time management, and good communication.\n  \n- Nice to Have Skills:\n  - Knowledge of frameworks like React, Angular, and Express.\n  - Familiarity with cloud platforms, such as AWS or Azure.\n\n- Challenges:\n  - Managing different technologies and learning new frameworks.\n  - Balancing client requirements and project constraints.\n  - Staying updated with the latest industry trends.\n\n- Advantages:\n  - Job prospects are high due to the increasing demand for full stack developers.\n  - Versatility in working on diverse projects and technologies.\n  - Potential for career growth and higher salaries.\n\n- Disadvantages:\n  - Work can be demanding with tight deadlines and frequent changes.\n  - Continuous learning required to keep up with evolving technologies.\n\n- Learning and Growth:\n  - Start with basic web development courses and practice building small projects.\n  - Expand knowledge in front-end and back-end frameworks, databases, and cloud platforms.\n  - Build a strong portfolio and contribute to open-source projects.\n  - Consider certifications and advanced courses to enhance your expertise.\n\n- Detailed Job Description:\n  - Full Stack Developers handle both front-end and back-end development, ensuring seamless integration.\n  - They collaborate with designers, developers, and stakeholders to understand project requirements.\n  - Full Stack Developers design and implement responsive user interfaces using HTML, CSS, and JavaScript.\n  - They develop server-side logic, database schemas, and APIs using frameworks like Node.js and Express.\n  - Full Stack Developers troubleshoot and debug issues, conduct testing, and ensure optimal performance.\n\n- Career Progression:\n  - Junior Full Stack Developer\n  - Full Stack Developer\n  - Senior Full Stack Developer\n  - Tech Lead/Architect\n  - Project Manager or CTO"
"""

# Define regular expressions for titles, subtitles, and content
title_pattern = r'\n- (.*?):'
titles = re.findall(title_pattern, response, re.MULTILINE)
description = r'- .*?\.\s'
body = []
for i, title in enumerate(titles):
    # print(title)
    descriptions = re.findall(description, response, re.MULTILINE)

    response = response[response.find(title):]
    body.append({
        "title": title,
        "description": descriptions
    })
print(body)
print(response)
# print(response)
