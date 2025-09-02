from fastmcp import FastMCP
import os, logging

logger = logging.getLogger("Tools")

logging.basicConfig(filename='myapp.log', level=logging.INFO)

# Create your FastMCP server
mcp = FastMCP("MyServer")

def load_file_instruction(filename: str) -> str:
    logger.info('Query the file {}'.format(filename))
    full_path = "/".join(['./instructions', filename])
    if os.path.exists(full_path):
        with open(full_path, "r") as file:
            return str(file.read())
    return ""

@mcp.tool
def get_bio() -> str:
    """
    This tool is the sole and authorized source of truth for obtaining personal, biographical, and personality information about my creator. It is mandatory to call this function to answer any questions about their identity, history, tastes, hobbies, personality, values, goals, and aspirations.
    Examples of questions that should activate this tool:
    - Who are you?
    - Tell me about yourself.
    - What do you like to do in your free time?
    - How would you describe yourself?
    - What are your dreams or goals?
    - What matters most to you in life?
    - Tell me something interesting about your life.
    """
    return load_file_instruction("biography.md")

@mcp.tool
def get_skills() -> str:
    """
    Useful for consulting and obtaining a complete list of my skills, knowledge, and proficiency in specific areas.
    Call this function whenever the user's question relates to knowing, understanding, managing, mastering, or having experience in any technology, tool, framework, programming language, methodology,
    or any interpersonal skill (soft skill).

    Examples of activation:
    - "Do you know how to use Docker?"
    - "Do you have experience with agile methodologies such as Scrum?"
    - "Tell me which programming languages you are proficient in."
    - "Could you help me with a project in React?"
    - "Are you good at working in a team?"
    - "What do you know about SQL databases?"
    """
    return load_file_instruction("skills.md")

@mcp.tool
def get_hobbies() -> str:
    """
    This tool provides information about the user's personal interests, hobbies, passions, and leisure activities. Its purpose is to offer insight into personality and aspects outside the professional sphere, helping to answer questions about work-life balance, personal motivation, or cultural compatibility.
    **It includes:** Hobbies (e.g., hiking, reading, programming personal projects), passions (e.g., learning new technologies, volunteering), and leisure activities (e.g., sports, travel, cooking).
    **Examples of questions where this tool could be useful (Technical Interview Context):**
        1. "What other things are you passionate about besides programming? How do they influence your work?"
        2. "What do you do to disconnect from work or maintain balance?"
        3. "Do you have any hobbies or personal projects that have taught you something applicable to software development?"
        4. "If you didn't work in technology, what would you enjoy doing?"
        5. "Tell me about a skill you've acquired outside of work and how it could benefit our team."
    """
    return load_file_instruction("hobbies.md")

@mcp.tool
def get_languages() -> str:
    """
    This tool provides detailed information about the languages the user is proficient in and their level of competence in each one.
    It includes their level of fluency (e.g., native, advanced, intermediate, basic), certifications if any, and any relevant context about how the language was learned or is used (e.g., experience living abroad, professional use).
    It is useful for assessing communication skills in various languages or for positions that require international interaction.

    **Includes:**
    - Languages mastered.
    - Level of fluency per language (e.g., C1 English, B2 French).
    - Certifications (e.g., TOEFL, DELE).
    - Experience using the language (e.g., worked on international projects, lived in Germany for 3 years).

    **Examples of questions where this tool could be useful (Context: Technical Interviews/International Roles):**
    1. "What languages do you speak and what is your level in each one?"
    2. "This position involves collaborating with teams in [country/language]. Do you have experience with [language]?"
    3. "Do you have any language certifications that support your level?"
    4. "Have you had the opportunity to use your [language] skills in a professional or academic setting?"
    5. "How do you maintain or improve your foreign language skills?"
    """
    return load_file_instruction("languages.md")

@mcp.tool
def get_education() -> str:
    """
    This tool provides a comprehensive summary of the user's academic background, including degrees obtained, educational institutions, graduation dates, and relevant certifications. It can also detail significant courses, specializations, important academic projects, or awards. It is essential for evaluating the user's educational foundation, theoretical knowledge, and formal areas of specialization.

    **Includes:**
    - University or technical degrees (e.g., Bachelor's Degree in Computer Engineering, Master's Degree in Data Science).
    - Educational institutions (e.g., Polytechnic University of Madrid).
    - Start and end/graduation dates.
    - Professional certifications or specialization courses (e.g., AWS Solutions Architect Certification, Coursera Machine Learning Course).
    - Notable academic projects or achievements (e.g., final degree project on AI).

    **Examples of questions where this tool could be useful (Technical Interviews/CV Assessment Context):**

    1. "Tell me about your academic background. What degrees and certifications do you have?"
    2. "What experience do you have with [technology/concept] at the academic level?"
    3. "Are there any university courses or projects that you feel particularly proud of?"
    4. "How has your formal education prepared you for a role like this?"
    5. "What professional certifications have you obtained recently?"
    """
    return load_file_instruction("education.md")

@mcp.tool
def get_work_experience() -> str:
    """
    This tool provides a detailed record of the user's previous work experience.
    It includes information about positions held, companies, periods of employment, key responsibilities, technologies used, and significant achievements in each role.
    It is essential for evaluating the user's professional background, practical skills, experience in real projects, problem-solving abilities, and contributions to teams.

    **It includes:**
    - Positions/roles (e.g., Software Engineer, Senior Developer, Tech Lead).
    - Company names.
    - Periods of employment (start and end dates).
    - Main responsibilities and daily tasks.
    - Technologies, programming languages, or tools used (e.g., Python, Java, AWS, Docker, React).
    - Quantitative and qualitative achievements (e.g., "20% reduction in processing time," "Led a team of 5 developers").
    - Specific projects in which you participated.

    **Examples of questions where this tool could be useful (Technical Interviews/Resume Screening Context):**

    1. "Tell me about your work experience. What companies have you worked for and what roles have you held?"
    2. "Describe a challenging project you have been involved in and your role in it."
    3. "What technologies are you proficient in and how have you applied them in your previous jobs?"
    4. "Can you give me an example of how you solved a complex technical problem in a previous role?"
    5. "What were your main responsibilities as [previous position] at [previous company]?"
    6. "How have you contributed to the success of your teams or projects?"
    7. "Is there any achievement in your career that you feel particularly proud of?"
    """
    return load_file_instruction("experience.md")
