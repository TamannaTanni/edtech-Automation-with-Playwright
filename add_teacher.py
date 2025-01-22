def add_teacher(page, new_teacher_data):
    page.goto("https://3rd-eye-ed-mate-qa.mpower-social.com/batches?batchName=")

    page.wait_for_load_state("domcontentloaded")

    ## Navigate to user tab
    page.locator("(//button[@aria-label='theme-icon'])[5]").click()

    ## Navigate to teacher tab
    page.click("//a[@role='tab' and contains(., 'Teacher')]")

    ## Click Add new teacher
    page.locator("//button[normalize-space()='Add New Teacher']").click()

    ##-------------Step 1: User Information ---------------

    # Enter inputs
    last_name = "Rumman"
    page.fill("input[name='firstName']", "Teacher")
    page.locator("input[name='lastName']").fill(last_name)
    page.fill("input[name='contactNo']", "01122223333")
    page.fill("input[name='email']", "duce@bigolo.com")
    # Select the female radio button
    page.check("input[name='gender'][value='female']")
    page.fill("input[name='userName']", "rumman")
    page.fill("input[name='password']", "12345678")

    # Click the button with type="submit"
    page.click("button[type='submit']")
    # Click the button with visible text "Next"
    page.click("//button[normalize-space()='Next']")

    # Wait for the "Submit" button in the confirmation popup to appear
    page.wait_for_selector("//button[normalize-space()='Submit']")

    # Click the "Submit" button
    page.click("//button[normalize-space()='Submit']")

    # Wait for the confirmation dialog to appear
    page.wait_for_selector("//p[@id='alert-dialog-description']")

    # Get the message text
    message_text = page.text_content("//p[@id='alert-dialog-description']")

    # Validate the message
    assert "Teacher with details created successfully" in message_text, "Confirmation message validation failed"

    print("Confirmation message validated successfully!")

    #  Close the success message
    page.locator("//button[@aria-label='Close']").click()

    ##---------------Verify---------------------------

    # click search to verify it's added
    page.locator("//input[@type='text']").click()

    ## sendKeys to thhe search field
    page.locator("//input[@type='text']").fill("rumman1")

    # Wait for the search results to appear
    page.wait_for_selector("//h6[normalize-space()='Teacher Rumman1']", timeout=10000)

    # # Validate that the teacher appears in the search results
    search_result = page.locator("//h6[normalize-space()='Teacher Rumman1']").count()
    assert search_result > 0, "Teacher not found in the search results"
    print("Teacher validated in the list successfully!")

