def add_admin(page):

    page.goto("https://3rd-eye-ed-mate-qa.mpower-social.com/batches?batchName=")

    page.wait_for_load_state("domcontentloaded")

    ## Navigate to user tab
    page.locator("(//button[@aria-label='theme-icon'])[5]").click()

    ## Confirm Admin tab
    page.click("//a[@role='tab' and contains(., 'Admin')]")

    ## Click Add new student
    page.locator("//button[normalize-space()='Add New Admin Officer']").click()

    ##-------------Step 1: User Information ---------------

    ## Send values at firstname field
    page.locator("//input[@name='firstName']").fill("3rd")

    ## Send values at lastname field
    page.locator("//input[@name='lastName']").fill("Admin")

    ## Send values for contact number
    page.locator("//input[@name='contactNo']").fill("01100000001")

    ## Send value email field
    page.locator("//input[@name='email']").fill("3rd@admin.com")

    ## Click gender
    page.locator("//input[@value='female']").click()

    ## Give username
    page.locator("//input[@name='userName']").fill("3rdAdmin")

    ## Give password
    page.fill("//input[@name='password']", "P@ssw0rd")

    ##Scroll down
    page.evaluate('''
                    const container = document.querySelector(".MuiPaper-root");
                    if (container) {
                        container.scrollTo(0, container.scrollHeight);
                    }
                ''')

    ## Click Next button
    page.wait_for_timeout(5000)
    page.locator("//button[normalize-space()='Next']").click()

    ##-------------Step 2: Review---------------
    ## Review and submit
    page.wait_for_timeout(5000)
    page.locator("//button[normalize-space()='Submit']").click()
    page.wait_for_timeout(10000)

    ##Get the message
    message_text = page.text_content("//p[@id='alert-dialog-description']")

    print("########################################")

    print(message_text)

    # Validate the message
    assert "Student with details created successfully" in message_text, "Confirmation message validation failed"

    print("Confirmation message validated successfully!")

    ##  Close the success message
    page.wait_for_timeout(5000)
    page.locator("//button[@aria-label='Close']").click()
