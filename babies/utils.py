def generate_progress_report(logged_milestones, age_in_months):
    report = f"At {age_in_months} months old, "
    if logged_milestones:
        milestones = ", ".join([milestone.description for milestone in logged_milestones])
        report += f"the baby has achieved the following milestones: {milestones}."
    else:
        report += "the baby has not achieved any milestones yet."
    return report
