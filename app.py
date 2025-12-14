import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    """Serve the personal branding page."""
    profile = {
        "name": "Bharat Verma",
        "headline": "Director / Senior Engineering Leader · Microservices · Payments · Cloud",
        "location": "West India",
        "email": "bharatv@outlook.in",
        "linkedin": "https://www.linkedin.com/in/bharatverma/",
        "summary": [
            "Technology leader balancing engineering management, architecture, and product development for customer-centric organizations.",
            "15+ years in software engineering, growing from backend developer to architect to hands-on leader.",
            "Industry exposure across fintech, e-commerce, expert networks, and SaaS; experienced in microservices and legacy-to-service migrations.",
            "Conscientious, empathetic leadership style focused on delegation, motivation, and career growth.",
        ],
        "last_updated": "Nov 2025",
    }

    skills = [
        {
            "title": "Languages & Scripting",
            "items": ["Java", "PHP", "Go", "Python 3", "Shell scripting"],
        },
        {
            "title": "Data & Storage",
            "items": ["MySQL", "Postgres", "MS SQL Server", "MongoDB", "Cassandra"],
        },
        {
            "title": "Frameworks & APIs",
            "items": ["Spring Boot", "API Platform", "Symfony", "Echo (Go)"],
        },
        {
            "title": "Messaging & Caching",
            "items": ["Kafka", "RabbitMQ", "Amazon SQS", "Redis / AWS ElastiCache"],
        },
        {
            "title": "Search & Observability",
            "items": ["Elasticsearch", "ELK", "Datadog", "Grafana", "PagerDuty", "Sentry", "BugSnag"],
        },
        {
            "title": "Cloud & Infra",
            "items": [
                "AWS (EC2, S3, ELB, Elastic Beanstalk, EKS, VPC, IAM)",
                "GCP Maps API",
                "Docker, Kubernetes, Terraform, Ansible",
            ],
        },
        {
            "title": "Delivery & Tooling",
            "items": [
                "Git (GitHub, Bitbucket), Swagger",
                "Maven, Helm, JFrog Artifactory, Make, Azure Container Registry",
                "Jenkins, Azure DevOps, GitHub Actions, Argo CD",
                "SonarQube, Snyk, JUnit, PHPUnit, Selenium, Postman",
            ],
        },
        {
            "title": "Web Servers & OS",
            "items": ["Apache Tomcat", "Apache", "Nginx", "Linux (Debian/RedHat)", "Windows 10/11", "macOS"],
        },
    ]

    experience = [
        {
            "company": "Razorpay Software Pvt Ltd.",
            "role": "Senior Engineering Manager – Card Recurring & E-mandate, Card Growth",
            "location": "Bengaluru (Hybrid)",
            "dates": "03/2025 – Present",
            "highlights": [
                "Own recurring/e-mandate transactions and card growth teams with partner integrations.",
                "Lead re-architecture initiatives aligned to SaCRED priorities (security, reliability, efficiency, innovation).",
                "Delivered Cred Pay and Apple Pay on Razorpay platforms as critical business OKRs.",
            ],
        },
        {
            "company": "Guidepoint Global",
            "role": "Director, Software Engineering – India Engineering Pods",
            "location": "Pune (Hybrid)",
            "dates": "06/2023 – 02/2025",
            "highlights": [
                "Modernized CRM, advisor, and client portals by moving to microservices.",
                "Completed PHP 8 transformation for SOC2 compliance within two months of joining.",
                "Revamped Guidepoint Now portal with microservice backend and Databricks ETL pipelines.",
                "Designed module-federated micro-frontends to unify Advisor Search, Guidepoint Insights 2.0, and Ask AI Co-pilot.",
            ],
        },
        {
            "company": "Acquia",
            "role": "Manager, Engineering – Cloud Data and ACN Upgrades",
            "location": "Pune (Remote)",
            "dates": "02/2021 – 06/2023",
            "highlights": [
                "Hired and developed high-performing SDE and SDET teams across experience bands.",
                "Delivered ~660K COGS savings by migrating customers from Cloud Classic to ACN.",
                "Managed end-to-end delivery of Cloud Next feature sets to drive adoption.",
            ],
        },
        {
            "company": "One MobiKwik Systems Private Limited",
            "role": "Java Tech Lead (Architect) and Engineering Manager",
            "location": "Gurgaon",
            "dates": "11/2016 – 02/2021",
            "highlights": [
                "Built hotels backend, admin dashboard, schedulers, and customer ops tools in three months; integrated Cleartrip inventory.",
                "Shifted payment flow from wallet-only to wallet-as-payment gateway to meet new RBI guidelines.",
                "Delivered OLA-based bike rentals and cab bookings plus insurance products with wallet integration in weeks.",
                "Introduced ELK monitoring and ran Bug-a-thon, lifting GMV from 181 to 210 crores per month.",
            ],
        },
        {
            "company": "Clues Network Private Limited",
            "role": "Staff Software Engineer (TLM, Catalogue Team)",
            "location": "Gurgaon",
            "dates": "09/2015 – 11/2016",
            "highlights": [
                "Raised new product creation throughput from 30K/day to 100K/day via bulk upload.",
                "Moved product CRUD to RESTful services with dedicated inventory API using PHP Phalcon.",
                "Refactored banned-product detection to remove violations within one day (down from five).",
            ],
        },
        {
            "company": "InfoEdge (India) Public Limited",
            "role": "Senior Software Engineer and Lead Engineer",
            "location": "Noida",
            "dates": "11/2011 – 05/2015",
            "highlights": [
                "Refactored FastForward team stack from legacy Symfony to 2.x and championed Agile + Git.",
                "Built Naukri Background Check and Priority Application products from scratch.",
                "Optimized applications and slow queries; improved CRM email/SMS SLA to before 11 AM for 1M profiles.",
                "Advanced CI/CD with PHPUnit test coverage to reduce release risk.",
            ],
        },
        {
            "company": "Comviva Technologies",
            "role": "Software Engineer",
            "location": "Gurgaon",
            "dates": "12/2009 – 03/2011",
            "highlights": [
                "Developed PreTUPS (prepaid top-up system) serving 50+ global telecom clients.",
                "Managed version 4.x for major Indian clients (Idea, Vodafone, Aircel) and acted as onsite SPOC.",
            ],
        },
    ]

    education = [
        {
            "school": "Jamia Millia Islamia, Central University, New Delhi",
            "years": "2005 – 2009",
            "degree": "B.Tech, Computer Engineering",
        },
        {
            "school": "SKD Academy Inter College, Lucknow (U.P. Board)",
            "years": "2002 – 2004",
            "degree": "Higher Secondary, Physics · Chemistry · Maths",
        },
    ]

    languages = [
        {"name": "English", "level": "Professional (read, write, speak) – US and India"},
        {"name": "Hindi", "level": "Native"},
        {"name": "Spanish", "level": "Hobby (read and understand)"},
    ]

    return render_template(
        "index.html",
        title="Bharat Verma | Engineering Leader",
        profile=profile,
        skills=skills,
        experience=experience,
        education=education,
        languages=languages,
    )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port, debug=True)

