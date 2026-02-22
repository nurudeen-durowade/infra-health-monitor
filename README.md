# 🖥️ Infra Health Monitor

A lightweight infrastructure health monitoring tool built with Python, designed to simulate real-world DevOps automation workflows.


# 📌 Project Overview

Infra Health Monitor is a modular monitoring tool that:

Checks system health metrics (CPU, Memory, Disk)

Validates application/API health endpoints

Logs results in structured format

Triggers alerts when thresholds are exceeded

Runs locally or inside Docker

Can be deployed to cloud infrastructure using Terraform

Integrates with CI/CD pipelines for automated deployment

This project is built incrementally to demonstrate practical DevOps skills including automation, infrastructure-as-code, containerization, monitoring, and CI/CD.



# 🎯 Objectives

Practice real-world automation using Python

Build a monitoring tool similar to production infrastructure health checks

Demonstrate DevOps engineering workflow end-to-end

Showcase cloud deployment and CI/CD integration



# 🧱 Architecture (Planned)

infra-health-monitor/
│
├── monitor/
│   ├── health.py
│   ├── alerts.py
│   ├── config.py
│
├── logs/
│   └── health.log
│
├── Dockerfile
├── docker-compose.yml
├── main.py
├── requirements.txt
├── terraform/
│   └── main.tf
│
└── README.md


🚀 Features Roadmap
# Phase 1 – Core Monitoring (MVP)

 Check CPU usage

 Check memory usage

 Check disk usage

 Print metrics to console

 Log results to file

# Phase 2 – Intelligent Alerts

 Configurable thresholds

 Email or Slack alerting

 Structured logging

 Error handling & resilience

# Phase 3 – Containerization

 Dockerfile

 Environment-based configuration

 CLI arguments (e.g., --interval)

 Docker Compose support

# Phase 4 – Cloud Deployment

 Provision Azure VM using Terraform

 Deploy Docker container automatically

 Configure monitoring service

 Add CI/CD pipeline (GitHub Actions or Azure DevOps)


# ⚙️ Tech Stack

Python 3.x

psutil (system metrics)

Docker

Terraform (Azure Infrastructure)

GitHub Actions / Azure DevOps

Linux shell scripting


🐳 Running with Docker (Planned)

docker build -t infra-health-monitor .
docker run infra-health-monitor


☁️ Cloud Deployment (Planned)

cd terraform
terraform init
terraform apply

**The monitoring service will be deployed to an Azure VM via automated pipeline.**


📊 Example Output
CPU Usage: 34%
Memory Usage: 61%
Disk Usage: 45%
Status: Healthy


If thresholds are exceeded:

ALERT: CPU usage above 85%


# Why This Project?

This project demonstrates:

Practical automation

Infrastructure monitoring concepts

DevOps workflow thinking

Infrastructure as Code

CI/CD implementation

Production-style project structuring

It is designed to simulate real operational tooling used in production environments.


# Future Improvements

Web dashboard (Flask/FastAPI)

Prometheus metrics export

Kubernetes deployment

Role-based configuration

Advanced alerting system

👩🏽‍💻 Author

Nurudeen Durowade — DevOps Engineer focused on cloud architecture, automation, and continuous improvement.