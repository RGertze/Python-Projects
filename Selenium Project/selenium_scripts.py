from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Path to the ChromeDriver
CHROMEDRIVER_PATH = 'C:/Users/USER 2020/Downloads/chromedriver-win64/chromedriver.exe'

# Moodle credentials and URL
MOODLE_URL = 'https://online.elearning-swakopca.edu.na/login/index.php'
USERNAME = 'Admin'
PASSWORD = 'admin1234'

# Start a new instance of Chrome browser
driver = webdriver.Chrome()

# Navigate to Moodle
driver.get(MOODLE_URL)

# Find the login elements and input credentials
username_elem = driver.find_element(By.ID, 'username')
password_elem = driver.find_element(By.ID, 'password')

username_elem.send_keys(USERNAME)
password_elem.send_keys(PASSWORD)
password_elem.send_keys(Keys.RETURN)

# Click on the "Categories" menu button
categories_button = driver.find_element(By.LINK_TEXT, 'Categories')
categories_button.click()

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

wait = WebDriverWait(driver, 10)
ela_maths_category = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'ELA, Maths')))
ela_maths_category.click()

# Navigate to the Mathematics: HS course
course_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Mathematics: HS')))
course_link.click()

# Wait for the page to load fully
wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

# Instead of searching for the 'Module 1 - Integer Exponents and Scientific Notation' using XPath, 
# we will now use PARTIAL_LINK_TEXT
try:
    module_section = wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, 'Module 1')))
    module_section.click()
except:
    print("Failed to find the module section. Please verify the partial link text or the page content.")
    driver.save_screenshot("module_section_error.png")

from selenium.webdriver.common.action_chains import ActionChains

# 1. Switch on editing.
editing_toggle = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@name="setmode"]')))
editing_toggle.click()

# 2. Scrolling is done automatically by Selenium when clicking elements.

# 3. Click on "Add an activity or resource"
add_activity_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Add an activity or resource')))
add_activity_button.click()

# 4. Add the Assignment Activity
# Note: For the assignment activity, link text might not work due to the nature of the element. I'll use an alternative method.
assignment_activity = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.modicon_assign')))
assignment_activity.click()

# 5. Give the assignment a name "Learning Journal"
assignment_name_input = wait.until(EC.element_to_be_clickable((By.ID, 'id_name')))
assignment_name_input.send_keys('Learning Journal')

# 6. Save the assignment
save_assignment_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@value="Save and return to course"]')))
save_assignment_button.click()

# 7. Navigate back into the module section (as done before).
# Assuming the module's link text is 'Module 1 - Integer Exponents and Scientific Notation'
module_section = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Module 1 - Integer Exponents and Scientific Notation')))
module_section.click()

# 8. (Scrolling)

# 9. Drag the Assignment to be under the "Lesson..." page
drag_source = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'i.edw-icon-Move')))
# Finding the target based on partial link text "Lesson"
target_location = driver.find_element(By.PARTIAL_LINK_TEXT, 'Lesson')
ActionChains(driver).drag_and_drop(drag_source, target_location).perform()

# 10. You can use a loop to repeat the process for each "Lesson..." page.
# Note: Adjust this section according to the number of lessons or use some loop logic based on the total lessons present.



