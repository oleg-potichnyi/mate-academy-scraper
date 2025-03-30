import json
from driver_module import init_driver
from scraper import get_course_info

course_urls = {
    "UI/UX designer": (
        "https://mate.academy/courses/ui-ux?source=profession_card"
    ),
    "Data analyst": (
        "https://mate.academy/courses/data-analytics?source=profession_card"
    ),
    "QA Manual": (
        "https://mate.academy/courses/qa?source=profession_card"
    ),
    "Python developer": (
        "https://mate.academy/courses/python?source=profession_card"
    ),
    "Frontend developer": (
        "https://mate.academy/courses/frontend?source=profession_card"
    ),
    "Fullstack developer": (
        "https://mate.academy/courses/fullstack?source=profession_card"
    ),
    "Digital marketing": (
        "https://mate.academy/courses/digital-marketing?source=profession_card"
    ),
    "DevOps engineer": (
        "https://mate.academy/courses/devops?source=profession_card"
    ),
    "Java developer": (
        "https://mate.academy/courses/java?source=profession_card"
    ),
    "Recruiter": (
        "https://mate.academy/courses/recruitment?source=profession_card"
    ),
    "QA Automation": (
        "https://mate.academy/courses/qa-automation?source=profession_card"
    )
}


def save_course_data() -> None:
    driver, wait = init_driver()
    course_data = []

    for idx, (name, url) in enumerate(course_urls.items()):
        (course_description, full_time_duration,
         flexible_duration, module_count,
         topic_count, course_types
         ) = get_course_info(driver, wait, url)

        if idx < 6:
            full_time_type = course_types[28]
            flexible_type = course_types[29]
        else:
            full_time_type = course_types[27]
            flexible_type = course_types[28]

        course_data.append({
            "Course name": name,
            "Short description": course_description,
            "Course type": {
                "full-time": full_time_type,
                "flex": flexible_type
            },
            "Number of Modules": module_count,
            "Number of Topics": topic_count,
            "Course Duration": {
                "full-time": full_time_duration,
                "flex": flexible_duration
            }
        })

    driver.quit()

    with open("courses_data.json", "w", encoding="utf-8") as json_file:
        json.dump(course_data, json_file, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    save_course_data()
