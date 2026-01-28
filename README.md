# InstaLife: High-Scale Behavioral Analysis of 1 Million Social Media Profiles
### Business Intelligence, Predictive Modeling, and Digital Wellbeing Strategy

---

## Project Overview
This project performs a comprehensive analysis of a synthetic dataset containing 1,000,000 Instagram user profiles (2025–2026 dataset). The objective is to evaluate the intersection of social media engagement, demographic factors, and self-reported health metrics.

As a Project Manager and Data Analyst, I have structured this repository to solve 10 specific business challenges. The analysis demonstrates how high-volume data can be leveraged to drive corporate growth while maintaining a focus on user health and ethical product design.

---

## Strategic Use Cases
This project demonstrates the practical application of data science across several key functional areas:

* **Exploratory Data Analysis (EDA):** Discovering complex links between screen time and user well-being to inform product policy.
* **Predictive Modeling:** Utilizing machine learning to predict user happiness, stress, and sleep patterns based on digital usage signatures.
* **Clustering & Persona Identification:** Segmenting the user base into distinct archetypes (e.g., "Doom-Scroller," "Casual Poster," "Aspiring Influencer") for targeted engagement strategies.
* **A/B Testing Simulation:** Studying the behavioral effects of platform changes on user engagement and retention.
* **Benchmarking:** Comparing synthetic behavioral patterns against real-world social media studies to validate product assumptions.
* **Education & Tutorials:** Serving as a framework for teaching correlation, regression, feature engineering, and high-performance handling of large datasets.

---

## Strategic Business Problems Addressed

### Pillar 1: Revenue and Growth
1. **Premium Subscription Propensity Model:** Utilized classification algorithms to identify drivers behind premium feature adoption.
2. **Ad-Targeting Optimization:** Segmented users based on lifestyle behaviors (exercise and diet) to improve predicted ad relevance.

### Pillar 2: Product Strategy and User Experience
3. **Feature Cannibalization Analysis:** Quantified the relationship between Reels consumption and traditional Feed engagement.

![Reels vs Feed Correlation]()
> **Strategic Insight:** The scatter plot demonstrates a strong positive correlation between Reels and Feed usage. This suggests that Reels acts as a "gateway" feature that increases overall platform stickiness rather than cannibalizing traditional Feed engagement.
<img width="993" height="525" alt="newplot (2)" src="https://github.com/user-attachments/assets/4d6a7885-9df3-44f9-927e-ad19870b9068" />

4. **User Persona Archetyping:** Implemented K-Means Clustering to categorize the user base into five distinct behavioral segments.

### Pillar 3: User Health and Retention
5. **Burnout Early Warning System:** Identified the specific usage threshold (minutes per day) at which perceived stress scores increase significantly.
6. **Sleep-Engagement Equilibrium:** Determined the optimal daily usage window that maximizes engagement without impacting user health.

![Sleep vs Usage Heatmap]()
> **Strategic Insight:** The density heatmap identifies a "Health Equilibrium" at 150–250 minutes of daily usage. Beyond the 300-minute mark, we observe a significant thinning of the 8-hour sleep cluster, providing a data-driven basis for time-limit notifications.
<img width="993" height="525" alt="newplot (1)" src="https://github.com/user-attachments/assets/50943a2c-5fdb-4a2e-88cc-597197d6be32" />

### Pillar 4: Operations and Security
7. **Security Friction Analysis:** Analyzed the impact of Two-Factor Authentication (2FA) on long-term user engagement and trust.
8. **Notification Sensitivity:** Evaluated how notification response rates influence average session lengths.
9. **Regional Behavioral Divergence:** Compared content preferences between urban and rural demographics for localized curation.

![Content Preference by Region]()
> **Strategic Insight:** Comparative analysis shows high uniformity in content preferences across urban and rural segments. This indicates that for this dataset, behavioral targeting (interests) is a more powerful driver of engagement than geographic location.
<img width="993" height="525" alt="newplot" src="https://github.com/user-attachments/assets/f3238a70-1ad5-4e07-928b-872181962291" />

10. **Happiness-Driven Growth:** Modeled the impact of non-digital habits on user happiness to support corporate social responsibility initiatives.


---

## Technical Stack
* **Data Processing:** Polars (Optimized for 1,000,000+ rows).
* **Machine Learning:** Scikit-Learn (Random Forest, K-Means Clustering, Linear Regression).
* **Visualization:** Plotly Express (Interactive statistical charting).
* **Environment:** Google Colab / Python 3.11+.

---

## Key Strategic Findings
* **The 120-Minute Threshold:** Data indicates a significant spike in perceived stress scores once daily usage exceeds 120 minutes.
* **Security as a Trust Driver:** Users with biometric or 2FA security enabled demonstrate higher platform loyalty scores compared to non-secured users.
* **Lifestyle Correlation:** Reading habits and physical exercise were found to be stronger predictors of self-reported happiness than absolute income level.

---

## Data Privacy & Ethics
* **100% Synthetic Data:** This project uses fully synthetic data generated through statistical distributions. No real user data was accessed, collected, or used in this analysis, making it perfectly safe for research and prototyping.

---

## Professional Statement
This project serves as a demonstration of technical proficiency in handling large-scale datasets and the ability to translate complex statistical outputs into actionable business strategies. It balances the need for revenue-focused growth with a rigorous commitment to user-centric product management.
