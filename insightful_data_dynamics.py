''' This module provides a reusable byline for Insightful Data Dynamics. Delivering Expert Analytics Solutions for Enhanced Business Growth '''

import math
import statistics

def main():
    # Company Profile
    company_name = "Insightful Data Dynamics"
    company_mission = "Empowering businesses with cutting-edge data insights"
    years_in_field = 3
    rate_per_hour = 62.99
    skills = ['Quick-learner', 'Problem-Solver', 'Enthusiastic', 'Open-Minded']
    has_masters_degree = False
    average_rating = 7.91
    max_rating = 8.7

    # Project Statistics
    ongoing_project_number = 5
    client_satisfaction_average = 4.7
    services_offered = ["Data Analysis", "Machine Learning Consulting", "Business      Intelligence Solutions"]
    client_feedback_scores = [4.8, 4.6, 4.9, 5.0, 4.7]

    # Formatted Strings for Non-String Variables
    ongoing_projects_string = f"Ongoing Projects: {ongoing_project_number}"
    client_satisfaction_string = f"Client Satisfaction Average: {client_satisfaction_average}"
    services_offered_string = f"Services Offered: {', '.join(services_offered)}"

    # Calculate Descriptive Statistics
    min_satisfaction = min(client_feedback_scores)
    max_satisfaction = max(client_feedback_scores)
    mean_satisfaction = statistics.mean(client_feedback_scores)
    median_satisfaction = statistics.median(client_feedback_scores)
    std_dev_satisfaction = statistics.stdev(client_feedback_scores)

    # Formatted Statistics String
    stats_string = f"""
    Descriptive Statistics for Client Feedback Scores:
      Smallest: {min_satisfaction}
      Largest: {max_satisfaction}
      Mean: {mean_satisfaction:.2f}
      Median: {median_satisfaction}
      Standard Deviation: {std_dev_satisfaction:.2f}
    """

    # Formatted Byline String
    byline = f"""
    {company_name}
    {company_mission}
    Rate Per Hour: ${rate_per_hour}
    Skills Include: {', '.join(skills)}
    Has Masters Degree: {has_masters_degree}
    Years in the Field: {years_in_field}
    Average Rating: {average_rating}
    Max Rating: {max_rating}
    {ongoing_projects_string}
    {client_satisfaction_string}
    {services_offered_string}
    {stats_string}
    """

    # Display the Byline
    print(byline)

if __name__ == '__main__':
    main()

