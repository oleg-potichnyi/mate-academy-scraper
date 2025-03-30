import time
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec


def get_course_info(driver, wait, url) -> tuple:
    driver.get(url)
    time.sleep(2)

    course_description = wait.until(ec.presence_of_element_located((
        By.CSS_SELECTOR,
        "p.typography_textMain__oRJ69.SalarySection_aboutProfession__C6ftM"
    ))).text.strip()

    durations = driver.find_elements(
        By.CSS_SELECTOR,
        "div.TableFeedView_rowContent__Nih2n.typography_textH6__d230d.text-right"
    )
    full_time_duration = durations[6].text.strip()
    flexible_duration = durations[17].text.strip()

    module_count = len(driver.find_elements(
        By.CSS_SELECTOR, "p.CourseModulesList_topicName__7vxtk"
    ))

    topic_elements = driver.find_elements(
        By.CSS_SELECTOR,
        "p.CourseModulesList_topicsCount__H_fv3.typography_textMain__oRJ69"
    )
    topic_count = sum(
        int(re.search(r'\d+', el.get_attribute("innerText")).group())
        for el in topic_elements if re.search(r'\d+', el.get_attribute("innerText"))
    )

    course_types = [
        el.text.strip() for el in driver.find_elements(
            By.CSS_SELECTOR, "span.ButtonBody_buttonText__34ExO"
        )
    ]

    return (
        course_description,
        full_time_duration,
        flexible_duration,
        module_count,
        topic_count,
        course_types
    )
