import ast
from datetime import datetime

def create_batch(page, new_batch_data):
    # Navigate to batch page
    page.goto("https://3rd-eye-ed-mate-qa.mpower-social.com/batches?batchName=")

    page.wait_for_load_state("domcontentloaded")

    # wait for appear all batch list
    page.wait_for_selector("//button[normalize-space()='Add New Batch']", timeout=10000)

    # Code to create a batch...

    ##Click add new batch
    page.locator("//button[normalize-space()='Add New Batch']").click()

    #### Part 1: Batch Information ###################

    ## Give batch name
    # page.locator("//input[@name='name']").fill(input("Enter your batch name: "))

    # batch_name = input("Please enter the value for 'name': ")
    batch_name = new_batch_data["batch_name"]
    page.locator("//input[@name='name']").fill(batch_name)

    # Click the Room input field to open the dropdown
    page.locator("//div[@role='presentation']//div[2]//div[1]//div[1]//div[1]//div[1]//button[1]").click()

    # Wait for the dropdown options to appear
    page.wait_for_selector("//li[@role='option']", timeout=5000)

    # Now select the room value from the dropdown
    page.locator(f"//li[@role='option' and .//h6[text()='{new_batch_data["room"]}']]").click()
    # page.locator(f"//li[contains(@class, 'MuiAutocomplete-option') and @data-option-index='{int(input("Please enter class; index start from 'zerro': "))}']").click()


    ##  Click Teacher
    page.locator("//div[.='Teacher (Optional)']").click()

    # Wait for the dropdown options to appear
    page.wait_for_selector("//li[@role='option']", timeout=5000)

    # Now select the Teacher
    page.locator(f"//li[@role='option' and .//h6[text()='{new_batch_data["teacher_name"]}']]").click()

    # Now click grade
    page.locator("//div[.='Grade']").click()

    # Wait for the dropdown options to appear
    page.wait_for_selector("//li[@role='option']", timeout=5000)

    # Now select O-level
    page.locator(f"//li[normalize-space()='{new_batch_data["grade"]}']").click()
    # page.locator(
    #     f"//li[@role='option' and @data-option-index='{int(input("Please enter grade; index start from 'zerro': "))}']").click()

    ## Now click curriculumn
    page.locator("//div[.='Curriculum']").click()

    ## WAit por list to appear
    page.wait_for_selector("//li[@role='option']", timeout=5000)

    ## Select curriculumn as Cambridge
    page.locator(f"//li[normalize-space()='{new_batch_data["curriculum"]}']").click()
    # page.locator(
    #     f"//li[@role='option' and @data-option-index='{int(input("Please enter curriculum; index start from 'zerro': "))}']").click()

    ## Click Syllabus
    page.locator("//div[.='Syllabus']").click()

    ## WAit for list to appear
    page.wait_for_selector("//li[@role='option']", timeout=5000)

    ## Select Syllabus
    page.locator(f"//li[normalize-space()= '{new_batch_data["syllabus"]}']").click()
    # page.locator(
    #     f"//li[@role='option' and @data-option-index='{int(input("Please enter syllabus; index start from 'zerro': "))}']").click()

    ## Click Course
    page.locator("//div[.='Courses']").click()

    ## WAit for list to appear
    page.wait_for_selector("//li[@role='option']", timeout=5000)

    ## Select Course
    page.locator(f"//li[normalize-space()= '{new_batch_data["course"]}']").click()
    # page.locator(
    #     f"//li[@role='option' and @data-option-index='{int(input("Please enter course; index start from 'zerro': "))}']").click()

    # ## Select payment frequency
    # page.locator("//input[@value='ff68ccf9-e895-4b54-a4f7-c9c14e4813bf']").click()
    #
    # ## Select price
    # page.locator("//input[@name='price']").fill(int(input("Please enter the payment amount:  ")))

    ##Select next button
    page.locator("(//button[normalize-space()='Next'])[1]").click()

    ########## --------- Move to Step 2 ------------

    #### Part 2: Batch Timing ###################

    # ##Click start date calender button
    # page.locator("(//button[@aria-label='Choose date'])[1]").click()
    #
    #  # Get today's date

    # today = datetime.now().strftime("%d")  # Get day as a two-digit number (e.g., '21')
    #
    # # Remove leading zero if your calendar uses single-digit days for the first 9 days
    # if today.startswith("0"):
    #     today = today[1:]
    #
    # # Locate today's date on the calendar and click it
    # page.locator(f"//button[normalize-space()='{today}']").click()

    ##Click start date calender button
    page.locator("label:has-text('Start Date') ~ div input[placeholder='DD/MM/YYYY']").fill(new_batch_data["batch_start_date"])


    ## Click End Date
    page.locator("label:has-text('End Date') ~ div input[placeholder='DD/MM/YYYY']").fill(new_batch_data["batch_end_date"])
    page.wait_for_timeout(1000)

    ## Click date
    # page.locator("//button[normalize-space()='30']").click()

    ## Select schedule day
    # days_to_select = ["Mon", "Wed"]
    # selected_days_input = input("Enter the days separated by commas (e.g., Sun, Mon, Tue): ")
    # Get the value from the CSV (e.g., ["Sat, Sun"])
    selected_days = new_batch_data["selected_days"]

    days_to_select = [day.strip() for day in selected_days.split(",")]

    # Print the list for confirmation (optional)
    print("Days to select:", days_to_select)

    # Iterate through the list and use it in the locator
    for day in days_to_select:
        # Assuming 'page' is your initialized playwright page object
        page.locator(f"input[name='{day}']").check()

    ## Same schedule for different days
    page.locator("//span//input[@name = 'saveCard']").click()

    # Click the "Hour" input field under the "Start Time" section
    page.locator("h6:has-text('Start Time') ~ div div:has(label:has-text('Hour')) [role='combobox']").click()

    # Select the hour "05" from the dropdown
    page.locator(f"ul[role='listbox'] li[data-value='{new_batch_data["start_time_hour_value"]}']").click()

    ## Click minute input field for start time
    page.locator("h6:has-text('Start Time') ~ div div:has(label:has-text('Minute')) [role='combobox']").click()

    ## wait for list to appear
    page.wait_for_selector("//li[@role='option']", timeout=5000)

    ## Select minute as 20
    page.locator(f"li[data-value='{new_batch_data["start_time_minute_value"]}']").click()

    ## Click am/pm value for start time
    page.locator("h6:has-text('Start Time') ~ div div:has(label:has-text('AM/PM')) [aria-haspopup='listbox']").click()

    ##wait for appear list
    page.wait_for_selector("//li[@role='option']", timeout=5000)

    ##Select PM
    page.locator(f"//li[normalize-space()= '{new_batch_data["start_time_AM/PM_value"].upper()}']").click()

    # Click the "Hour" input field under the "End Time" section
    page.locator("h6:has-text('End Time') ~ div div:has(label:has-text('Hour')) [role='combobox']").click()

    # Select the hour "06" from the dropdown
    page.locator(f"ul[role='listbox'] li[data-value='{new_batch_data["end_time_hour_value"]}']").click()

    ## Click minute input field for End time
    page.locator("h6:has-text('End Time') ~ div div:has(label:has-text('Minute')) [role='combobox']").click()

    ## wait for list to appear
    page.wait_for_selector("//li[@role='option']", timeout=5000)

    ## Select minute as 20
    page.locator(f"li[data-value='{new_batch_data["end_time_minute_value"]}']").click()

    ## Click am/pm value for End time
    page.locator("h6:has-text('End Time') ~ div div:has(label:has-text('AM/PM')) [aria-haspopup='listbox']").click()

    ##wait for appear list
    page.wait_for_selector("//li[@role='option']", timeout=5000)

    ##Select PM
    page.locator(f"//li[normalize-space()= '{new_batch_data["end_time_AM/PM_value"].upper()}']").click()

    ## Scroll to last
    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")

    ## Click Next
    page.locator("//button[normalize-space()='Next']").click()

    ## Navigate to the preview page

    ## Click submit
    page.locator("//button[normalize-space()='Submit']").click()

    ## Assert success message
    page.wait_for_selector("//div[@role='status']")

    ## Click to batch list
    # page.locator("(//button[@aria-label='theme-icon'])[3]").click()

    # # wait for appear all batch list
    page.wait_for_selector("//button[normalize-space()='Add New Batch']", timeout=10000)

    # click search to verify it's added
    page.locator("//input[@placeholder='Search Batch Name']").click()

    ## sendKeys to thhe search field
    page.locator("//input[@placeholder='Search Batch Name']").fill(batch_name)

    # Wait for the search results to appear
    page.wait_for_selector(f"//a[normalize-space()='{batch_name}']", timeout=10000)

    # Validate that the Batch appears in the search results
    search_result = page.locator(f"//a[normalize-space()='{batch_name}']").count()
    assert search_result > 0, "Batch not found in the search results"
    print("Batch validated in the list successfully!")

    return batch_name








