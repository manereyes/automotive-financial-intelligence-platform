# Automotive Financial Intelligence Platform

## Product Requirements Document (PRD)

**Version:** 1.0

---

# 1. Project Overview

The **Automotive Financial Intelligence Platform** is a portfolio project designed to simulate an internal Business Intelligence application used by Mercedes-Benz Financial Services to monitor, analyze and support decision-making for an automotive lending portfolio.

Unlike a traditional data analytics portfolio, this project aims to reproduce the structure, architecture and workflows of an enterprise-grade analytical platform.

The platform will progressively evolve through five interconnected projects, beginning with Business Intelligence dashboards and culminating in a Decision Support Platform capable of forecasting, scenario analysis and advanced financial analytics.

---

# 2. Business Problem

Financial institutions generate large volumes of operational data related to customers, loans and financed vehicles.

Although this information is available, decision-makers often struggle to obtain timely and actionable insights regarding:

* Portfolio growth
* Credit approval performance
* Customer segmentation
* Financial performance
* Credit risk exposure
* Commercial opportunities

The objective of this platform is to centralize those insights into a single analytical application designed for executive decision-making.

---

# 3. Project Objectives

The platform pursues the following objectives:

* Build a realistic Business Intelligence platform for automotive finance.
* Demonstrate professional SQL and Python development practices.
* Simulate enterprise analytical workflows.
* Provide executive dashboards focused on business decisions.
* Establish a scalable architecture for future forecasting, financial modeling and machine learning capabilities.

---

# 4. Stakeholders

The platform is designed to support the following business areas:

* Commercial Management
* Finance
* Portfolio Management
* Risk Management
* Business Intelligence
* Executive Leadership

---

# 5. Target Users

### Commercial Director

Responsible for monitoring credit originations, customer acquisition and commercial performance.

### Chief Financial Officer (CFO)

Responsible for monitoring financial performance, portfolio profitability and business growth.

### Business Finance Partner

Responsible for translating analytical findings into business recommendations.

### FP&A Analyst

Responsible for financial planning, forecasting and scenario analysis.

### Portfolio Manager

Responsible for monitoring the health and composition of the lending portfolio.

### Risk Analyst

Responsible for monitoring portfolio risk and expected default exposure.

### Business Analyst

Responsible for operational analysis, segmentation and business reporting.

---

# 6. Business Questions

The platform should answer questions such as:

* How is the lending portfolio evolving?
* What is the current approval rate?
* Which customer segments generate the highest loan volume?
* Which regions contribute the most to portfolio growth?
* Which vehicle categories represent the highest exposure?
* How is credit risk distributed across the portfolio?
* What commercial opportunities exist?
* Which KPIs require immediate executive attention?

---

# 7. Project Scope

Version 1 focuses on descriptive analytics through Business Intelligence dashboards.

Included:

* Executive dashboards
* SQL-based analytics
* Interactive visualizations
* Business KPIs
* Executive insights

Excluded:

* Forecasting
* Machine Learning
* Optimization
* Monte Carlo simulation
* Scenario analysis

These capabilities will be incorporated in later project phases.

---

# 8. Data Sources

The platform currently integrates three business entities:

## Customers

Represents customer demographic, financial and risk information.

## Loans

Represents lending contracts and portfolio performance.

## Vehicles

Represents financed assets and collateral information.

Synthetic data is generated through proprietary simulation scripts and loaded into Supabase using automated ingestion pipelines.

---

# 9. High-Level Architecture

The platform follows a layered architecture:

Simulation Layer

↓

Data Ingestion Layer

↓

Database Layer (Supabase)

↓

SQL Business Layer

↓

Python Analytics Layer

↓

Visualization Layer

↓

Executive Dashboard (Streamlit)

---

# 10. Functional Requirements

The platform shall:

* Display executive KPIs.
* Support interactive filtering.
* Present portfolio performance metrics.
* Display customer segmentation.
* Display commercial performance.
* Display financial performance.
* Display portfolio risk metrics.
* Generate executive insights.
* Generate executive recommendations.

---

# 11. Non-Functional Requirements

The platform should be:

* Modular
* Reusable
* Scalable
* Well documented
* Maintainable
* Easily extensible
* Suitable for future advanced analytics capabilities.

---

# 12. Success Metrics

The project will be considered successful if it:

* Demonstrates professional software architecture.
* Supports realistic business decision-making.
* Reuses components across all five project phases.
* Provides clear documentation.
* Simulates an enterprise Business Intelligence application.

---

# 13. Roadmap

The platform will evolve through five interconnected projects:

**Project 1:** Business Intelligence Executive Dashboard

**Project 2:** Business Analytics

**Project 3:** Business Finance Analytics

**Project 4:** FP&A Forecasting & Scenario Analysis

**Project 5:** Executive Decision Support Platform
