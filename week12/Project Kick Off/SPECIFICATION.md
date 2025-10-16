## Project Overview

You are building a data-driven Django web application that integrates an AI or ML model.  
The system should:

-   Provide meaningful predictions or insights.
-   Allow admin control (retraining over time not required)
-   Be structured for future scalability and deployment.

Your project will evolve across multiple phases (from model research to production readiness).  
This README covers Stage 1: Planning, with future milestones listed below.

---

## Required Folder Structure

Organise your Django + ML project as follows:

project_root/
│
├── ml/ # Machine Learning utilities (loading, inference, version control)
│ └── predict.py # Example inference entry point
│
├── classifier/ # Django app: forms, views, serializers
│ ├── models.py
│ ├── views.py
│ ├── serializers.py
│ └── forms.py
│ └──templates/classifier/ # HTML templates for user forms and result pages
│   └── results.html
│
├── api/ # Django REST Framework endpoints (Optional - v2)
│ ├── views.py
│ ├── serializers.py
│ └── urls.py
│
├── logs/ # Custom logging configuration and prediction audit trail
│ └── app.log
│
├── manage.py
└── requirements.txt

Tip: Keep the `ml/` module decoupled from Django so it can be tested in Jupyter or Pytest independently.

---

## Model Research and Justification

Choose and research one AI or ML model relevant to your use case.  
For example:

-   Text Classifier: Sentiment, topic, or intent detection
-   Regression Model: Predictive analytics for numeric outcomes
-   Image Classifier: Object detection or environmental monitoring

Your research notes should include:

1. Problem statement and dataset source.
2. Chosen model or algorithm (e.g., Naive Bayes, SVM, Logistic Regression, CNN).
3. Strengths and limitations for your data type.
4. Plan for model versioning (how you’ll update or if you will retrain).

---

## Minimum Viable Product (MVP) Definition

Your MVP should meet these initial goals:

-   Accurate predictions across common input types.
-   Response time under one second per inference.
-   Explainable and versioned results.
-   Real-time feedback to users.
-   Minimal downtime during updates.

**Version 2** 
- Admins can reclassify, relabel, or retrain as needed (custom permission only)
- API route exposure

Deliverable: Create a short description of your MVP goals in your GitHub repository’s `README.md` or `docs/` folder.

---

## Required Technical Requirements

Your final submission must include the following:

1. **Robust Testing** – Unit and integration tests for logic and APIs; minimum 80% coverage.
2. **Authentication** – Django or DRF authentication with role-based permissions.
3. **Observer Pattern** – Event-driven behaviour (e.g., logging, notification, or analytics triggers).
4. **Logging Decorator** – A decorator that records inputs, outputs, and errors to the log file.
5. **Database Model** – At least one persistent model which stores metadata for the process including file name, user, data/time, model version, model results/metrics
6. **Responsive UI** – Mobile-friendly templates using Bulma or Tailwind CSS.
7. **User Error Messaging** – Graceful feedback for invalid input and exceptions.
8. **Separation of Concerns** – ML code isolated from Django web logic.
9. **Full Deployment to Proxmox VM** – Production-ready app running on your assigned server.
10. **Optimatsation** - Once deployed a recorded optimsation period is completed including change & effect
11. **Completed Journal** – A dated record of design choices and iterations.
12. **GitHub Repository with Issues and Pull Requests** – Organised project workflow and traceable commits which includes a final passing actions workflow.

---

## Stage 1 Deliverables

By the end of this stage, you should have:

-   A clearly defined project goal (problem + model choice).
-   A structured Django folder layout.
-   A summary of your MVP criteria.
-   An outline of dataset sources and expected features.
-   A GitHub Project board with issues for the next steps.
-   A draft of your project journal (`docs/journal.md`).

---

## Using GitHub Projects for Planning

Open your GitHub repository and use the **Projects** tab to plan your workflow.

Instructions:

1. Create a new project board titled `Final Project Plan`.
2. Add the following default columns:
    - Backlog – ideas and future features
    - In Progress – tasks currently being developed
    - Testing – validation and debugging tasks
    - Complete – finished features and documentation
3. Convert each major item (e.g., dataset setup, model selection, template design) into issues.
4. Link each issue to a milestone (e.g., “8.2 Data Ingestion”).

This should be recorded part of your project management and planning record.

---

## Upcoming Project Phases

Below are the stages of your project to be assessed.

### 8.1 Defining the Project (e.g., Text Classifier)

Outline the ML goal, business context, and evaluation metrics.

### 8.2 Data Ingestion and Preparation via Django

Students now begin this stage independently:

-   Design and implement Django forms or APIs to collect data for training or inference.
-   Preprocess input data (e.g., cleaning, validation, or normalisation).
-   Save input records to your project’s database and prepare them for model training.
-   Document your process clearly in your repository’s README or `docs/` folder.
-   Create and assign GitHub issues for each development task.
-   Use milestones to represent features such as “Model Loading” “Auth System,” or “UI Layout.”

### 8.3 Model Training, Serialisation, and Versioning

Train and version your model using joblib or pickle; integrate with Django for inference.

### 8.4 Backend API and Frontend Integration

Connect REST endpoints with UI templates for prediction requests and display.

### 8.5 Testing, Deployment, and Logging

Add automated tests, configure Django logging, and verify prediction logs.

---

### 9.1 Deployment to Proxmox Virtual Machine (VM)

Deploy your Django application to a Proxmox-managed Ubuntu or Debian virtual machine.  
Students will:

-   Set up a Python virtual environment and install dependencies.
-   Configure Django’s `ALLOWED_HOSTS` and `DEBUG` for production.
-   Collect and serve static files using `collectstatic`.
-   Create a systemd service file to run the Django app persistently.
-   Configure basic firewall and SSH access. (DONE)
-   Document the VM IP address and access procedure.

### 9.3 Managing Secrets and Environment Variables

Securely store any relevent API keys, model paths, and database credentials.

### 9.4 Logging, Monitoring, and Crash Recovery

Monitor prediction performance, uptime, and exceptions.

### 9.5 Scaling and Performance Best Practices

Optimise for SOC, caching, and lazy loading to handle more users.

---

### 10.1 Testing in AI Contexts (Unit, Integration, ML-specific)

Write tests for Django logic and ML pipeline correctness.

### 10.2 CI/CD Pipelines for Django and Models

Implement GitHub Actions or similar workflows for continuous testing and deployment.

### 10.3 Version Control for Code and Data

Use Git and DVC (Data Version Control) or similar tools to manage any model updates.

### 10.4 Documentation, API Contracts, and Code Comments

Maintain high-quality documentation for models, routes, and contributors.

---

## Submission Checklist – Stage 1

-   [ ] Project repository created
-   [ ] Folder structure implemented
-   [ ] Model research notes added
-   [ ] MVP defined in README
-   [ ] GitHub Project board created and populated with issues (Template used)
-   [ ] Journal scaffold added in `docs/journal.md`
-   [ ] All commits pushed and documented

---

### Next Stage: Planning and Issue Creation

-   Review your project plan and identify concrete development tasks.
-   Create GitHub issues for each upcoming feature (e.g., data ingestion, authentication, observer implementation).
-   Assign priorities and milestones.
-   Begin implementing the **Data Ingestion and Preparation** phase in Django.
