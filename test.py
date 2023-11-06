import json
import re

response = """
Title: Career Path for CTO VP Job

- Introduction:
CTO VP (Chief Technology Officer Vice President) is a high-level executive role in a company, responsible for leading the technology department and driving the organization's technology strategy. This position requires a strong blend of technical expertise, leadership skills, and strategic thinking.

- Job Description:
The CTO VP oversees all aspects of the company's technology infrastructure, including software development, IT operations, and data management. They collaborate with other executives to align technology initiatives with business goals and drive innovation. CTO VPs also manage technology budgets, evaluate emerging technologies, and ensure the security and scalability of the company's systems.

- Required Skills:
1. Leadership: Proven ability to lead and inspire teams, set technology vision, and drive organizational change.
2. Technical Expertise: Deep understanding of software development, infrastructure, cloud platforms, and emerging technologies.
3. Strategic Thinking: Ability to align technology initiatives with business objectives and create a long-term technology roadmap.
4. Business Acumen: Understanding of industry trends, market dynamics, and ability to translate technology into business value.
5. Collaboration and Communication: Strong interpersonal skills to collaborate with cross-functional teams and effectively communicate complex technology concepts.

- Soft Skills:
1. Leadership and Team Building: Ability to build and lead high-performing technology teams.
2. Strategic Planning: Capability to develop and execute technology strategies aligned with business goals.
3. Problem-Solving: Proficiency in analyzing complex technology challenges and identifying effective solutions.
4. Decision-Making: Aptitude for making informed technology decisions and evaluating risks.

- Technical Skills:
1. Software Development: Proficiency in multiple programming languages, frameworks, and architecture patterns.
2. Cloud Platforms: Experience with cloud infrastructure, scalability, and DevOps practices.
3. Data Management: Knowledge of database systems, data warehousing, and analytics.
4. IT Operations: Understanding of network infrastructure, cybersecurity, and IT governance.
5. Emerging Technologies: Familiarity with AI, blockchain, IoT, and their potential business applications.

- Nice to Have:
1. Previous executive-level experience in a technology-oriented company.
2. Experience in technology-driven industries, such as software development, SaaS, or IT services.
3. Track record of successfully implementing digital transformation initiatives.
4. Understanding of regulatory compliance in the technology space.

- Challenges:
1. Balancing technical depth with strategic leadership responsibilities.
2. Navigating rapid technological advancements and evolving industry landscapes.
3. Managing complex technology projects, budgets, and stakeholder expectations.

- Advantages:
1. Influence and shape the company's technology vision and strategy.
2. Drive impactful technology initiatives and innovation.
3. Collaborate with cross-functional teams and senior executives.
4. Continuous learning and growth in a dynamic technology landscape.

- Disadvantages:
1. High-pressure environment with significant responsibilities and expectations.
2. Need to stay updated with rapidly changing technology trends.
3. Balancing technology-driven objectives with budget limitations.

- Learning and Growth​:
1. Develop leadership and strategic thinking skills through executive programs.
2. Gain practical experience by leading technology initiatives and projects.
3. Continuously learn about emerging technologies and industry best practices.
4. Consider pursuing advanced degrees or certifications in business and technology.

Remember, the path to becoming a CTO VP requires a combination of technical expertise, leadership skills, and strategic thinking. Prioritize continuous learning, focus on building a strong leadership track record, and seek opportunities to lead technology-driven initiatives. Good luck!

"""

# Define regular expressions for titles, subtitles, and content
title_pattern = r'\n- (.*?):'
titles = re.findall(title_pattern, response, re.MULTILINE)
titles=titles[1:]

description = r'^\d+\.\s(.*?\.)$'
body = []
for i, title in enumerate(titles):
    # print(title)

    response = response[response.find(title):response.find('\n')]
    descriptions = re.findall(description, response, re.MULTILINE)

    body.append({
        "title": title,
        "description": descriptions
    })
print(json.dumps(body, indent=4))
# print(response)
