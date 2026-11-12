
def create_roadmap_prompt(field, level, hours_per_day, duration_weeks):

    prompt = f"""
    You are an expert learning path designer.

    Create a detailed learning roadmap using these details:

    Field: {field}
    Current skill level: {level}
    Study time: {hours_per_day} hours per day
    Total duration: {duration_weeks} weeks

    Requirements:

    1. Divide the roadmap into logical learning phases.
    2. Give each phase a clear title and duration.
    3. List the topics the learner must study.
    4. Include practical exercises and projects.
    5. Include milestones to measure progress.
    6. Recommend useful learning resources.
    7. End with one final project.

    Make the roadmap realistic for the learner's current level.

    Return the result in a clear, organized format.
    """

    return prompt

