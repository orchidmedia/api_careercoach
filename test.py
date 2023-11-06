import json
import re

import utils

response = """
Full Stack Software Developer:

- Entry Level Positions: Junior Software Developer, Front-end Developer, Back-end Developer;
- Mid-Level Positions: Full Stack Developer, Web Developer, Software Engineer;
- Senior Level Positions: Technical Lead, System Architect, Software Development Manager;

Description of the Skills Required:

- Soft Skills: Problem-solving, Teamwork, Attention to Detail, Time Management;
- Technical Skills: HTML, CSS, JavaScript, Front-end Frameworks (React, Angular), Back-end Technologies (Node.js, Express), Databases (SQL, MongoDB), RESTful APIs;

Nice to Have Skills:

- Mobile App Development (React Native, Flutter), Version Control (Git), DevOps (CI/CD), Cloud Platforms (AWS, Azure), Agile Methodology;

Challenges of Full Stack Development:

- Keeping up with rapidly evolving technologies and frameworks;
- Balancing between front-end and back-end development tasks;
- Finding efficient solutions to optimize performance and load times;

Advantages of Full Stack Development:

- Versatility to work on both front-end and back-end projects;
- Ability to independently develop complete web applications;
- Strong problem-solving skills and a holistic understanding of software development;

Disadvantages of Full Stack Development:

- The need to constantly update knowledge and learn new technologies;
- Higher workload and responsibility for entire application development;

Learning and Growth Path:

- Start with front-end development, learn HTML, CSS, and JavaScript;
- Move to back-end development and learn server-side languages and frameworks;
- Gain experience with databases, APIs, and deploy applications to cloud platforms;
- Continuously update skills, join coding bootcamps or online courses;
- Build a strong portfolio of full-stack applications to showcase your abilities;

To reach this job:

- Develop a passion for coding and problem-solving;
- Complete relevant coursework or a computer science degree;
- Gain practical experience through internships or personal projects;
- Network with professionals in the industry and attend tech events;
- Continuously learn and adapt to new technologies and industry trends.


"""
print(utils.extract(response))
print(utils.extract_titles(response))
print(utils.extract_data(response))
print(utils.extract_data_2(response))
