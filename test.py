import re

response = """
CAREER PATH FOR SENIOR DEVELOPER:
- Junior Developer: Gain experience in programming languages and basic software development.
- Mid-level Developer: Expand knowledge in backend development, databases, and project management.
- Senior Developer: Lead complex projects, mentor junior developers, and possess in-depth technical expertise.

SKILLS REQUIRED:
- Technical: Proficiency in backend programming languages (Node.js, Python) and database management.
- Soft: Strong problem-solving, teamwork, leadership, and project management skills.
- Challenges: Solving complex technical issues, leading development teams, and architecting scalable solutions.
- Advantages: High salary, autonomy, and opportunities for personal and professional growth.

HOW TO LEARN AND GROW:
- Acquire certifications in relevant technologies (e.g., MongoDB, AWS).
- Contribute to open-source projects and build a strong online developer presence.
- Attend workshops and industry conferences to stay updated on the latest technologies and trends.
- Pursue advanced courses in software architecture and project management.

DISADVANTAGES:
- High-pressure situations and tight deadlines.
- Continuous learning and staying updated with evolving technologies.

CONCLUSION:
Becoming a Senior Developer requires a combination of technical expertise, leadership abilities, and project management skills. Continuous learning and hands-on experience are crucial for career growth in this role.

"""

# Define regular expressions for titles, subtitles, and content
title_pattern = r'[A-Z]+:$'
titles = re.findall(title_pattern, response, re.MULTILINE)
pattern = r'^-.*\.$'

body = []
for i, title in enumerate(titles):
    #print(title)
    descriptions = re.findall(pattern, response, re.MULTILINE)

    response = response[response.find(title):]
    body.append({
        "title": title,
        "description": descriptions
    })
print(body)
print(response)
    # print(response)
