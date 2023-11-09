import json

import utils

response = """"{
  "job1": {
    "title": "Senior Backend Developer",
    "description": [
      "Experience since 2015 in software and business development",
      "Design, build, and create MVPs for Apps and API's",
      "Proficient in Node.js, Python, SQL and NoSQL databases",
      "Knowledge in Scrum working methodology"
    ]
  },
  "job2": {
    "title": "Software Technical Lead",
    "description": [
      "Lead technical teams to improve shipping processes",
      "Develop and optimize backend services",
      "Proficient in TypeScript, GraphQL, and AWS",
      "Strong problem-solving and communication skills"
    ]
  },
  "job3": {
    "title": "Semi Senior Backend Developer",
    "description": [
      "Structure and optimize backend services",
      "Work with webhooks and payment platforms",
      "Experience in creating business models and KPIs",
      "Proficient in TypeScript, Golang, and Firebase"
    ]
  },
  "job4": {
    "title": "Business and Research Developer",
    "description": [
      "Experience with proximity and location-based technologies",
      "Quick creation of demos and MVPs",
      "Knowledge in AI, NLP, and E-commerce",
      "Proficient in AWS, DialogFlow, and TensorFlow"
    ]
  }
}"""
text = json.loads(response)
print(text)

