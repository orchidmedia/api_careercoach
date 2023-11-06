import json
import re

import utils

response = """
Introduction to the role:
A full stack software developer is a versatile professional who can handle both frontend and backend development. They are responsible for designing, coding, and deploying complete software applications.

Responsibilities and job outlook:
Full stack software developers are involved in all stages of the software development lifecycle, from planning and designing to implementing and testing. They often work in cross-functional teams and are in high demand in the tech industry.

Necessary skills and qualifications:
To become a successful full stack software developer, you need proficiency in both frontend and backend technologies. Key skills include HTML, CSS, JavaScript, database management, and knowledge of frameworks like React or Angular.

Advantages and disadvantages:
The advantage of being a full stack software developer is the ability to work on entire projects independently. However, the breadth of knowledge required can be challenging, and keeping up with evolving technologies is essential.

Learning and growth opportunities:
To pursue a career as a full stack software developer, consider online courses, coding bootcamps, and practice building complete applications. Building a robust portfolio and contributing to open-source projects can also enhance your skills.

Stay up to date with the latest technology trends and consider specializing in specific areas to further your career growth.


"""
#print(utils.extract(response))
#print(utils.extract_titles(response))
#print(utils.extract_data(response))
#print(utils.extract_data_2(response))
print(utils.extract_data_3(response))
