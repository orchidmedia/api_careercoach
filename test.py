import re

response = {
    "message": "Based on your profile, I recommend the following career path for you:\n\n1. Senior Backend Developer: "
               "With your experience in software and business development, focus on Node JS and Python development, "
               "SQL and NoSQL databases, and test frameworks like mocha and chai. Gain expertise in cloud platforms "
               "like Atlas MongoDB, AWS, and Firebase.\n\n2. Scrum and Business Architect: Utilize your knowledge and "
               "experience in Scrum working methodology, design business architecture, and create developer teams "
               "with appropriate resources and skills. Develop a passion for learning, problem-solving, "
               "and team communication.\n\n3. Mobile and IoT Developer: Expand your skills in geolocation, Bluetooth, "
               "BLE (Beacons and IoT), WIFI, and resource optimization. Learn about digital marketing, CEO, SEM, "
               "and NPL. Gain experience with platforms like Firebase, GCP, and Mongo Atlas.\n\n4. Technical Lead and "
               "Manager: With your leadership experience, focus on structuring and making robust backend services. "
               "Manage teams and projects, create business models, and work with payment platforms and ERP "
               "systems.\n\nConsider taking online courses and certifications in NestJS, Scrum, and cloud platforms. "
               "You can also explore research and development opportunities in areas like AI, NPL, "
               "and Ecommerce.\n\nNote: This is just a recommendation based on your profile. Choose the career path "
               "that aligns with your interests and career goals."
}

descriptions = response['message'].split('\n\n')

regex = r'\d+\.\s([^:]+):'

# Buscar los títulos en el texto
titulos = re.findall(regex, response['message'])

for title in range(0, len(titulos)):
    print(titulos[title])
    print(descriptions[title + 1].replace(titulos[title], ''))
    print('-------------------')