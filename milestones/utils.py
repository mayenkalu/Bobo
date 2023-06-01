# milestones/utils.py
def generate_progress_report(logged_milestones, age_in_months):
    milestone_list = [milestone.description for milestone in logged_milestones]
    report = f"At {age_in_months} months, the baby has achieved the following milestones: \n"
    for milestone in milestone_list:
        report += f"- {milestone} \n"
    if not milestone_list:
        report += "No milestones have been logged for this month yet. Please log your current baby's achieved milestones to get a summary of her progress."
    return report
