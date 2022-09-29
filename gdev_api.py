from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from typing import List


def unit_count_from_profile(driver, profile_url):
    driver.get(profile_url)
    badges_container = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "profile-badges-container")))

    badges: List[WebElement] = badges_container.find_elements(By.CLASS_NAME, "badge")
    unit_badge_counts = {"unit-1": 0, "unit-2": 0, "unit-3": 0, "unit-4": 0}
    for badge in badges:
        badge_url = badge.get_attribute("badge-url")
        badge_date = badge.find_element(By.CLASS_NAME, "badge-date").text

        # TODO update Eyl 2022
        if badge_url.startswith("https://developers.google.com/profile/badges/playlists/android/android-basics-compose") \
                and badge_date.endswith("Eyl 2022"):
            unit = badge_url[badge_url.find("unit"):badge_url.find("unit") + 6]
            unit_badge_counts[unit] = unit_badge_counts[unit] + 1

    # print(unit_badge_counts)

    completed_unit_count = 0
    for unit, count in unit_badge_counts.items():
        if count == 3:
            # print(unit + " completed!")
            completed_unit_count = completed_unit_count + 1

    return completed_unit_count
