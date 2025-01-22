from datetime import datetime


def add_student(page, new_admin_data):
    page.goto("https://3rd-eye-ed-mate-qa.mpower-social.com/batches?batchName=")

    page.wait_for_load_state("domcontentloaded")
    

    ## Navigate to students tab
    page.locator("(//button[@aria-label='theme-icon'])[5]").click()

    page.click("//a[@role='tab' and contains(., 'Student')]")

    ## Click Add new student
    page.locator("//button[normalize-space()='Add New Student']").click()

    ## Send values at firstname field
    page.locator("//input[@name='firstName']").fill("Naim")
 
    ## Send values at lastname field
    page.locator("//input[@name='lastName']").fill("Khan")

    ## Send values for contact number
    page.locator("//input[@name='contactNo']").fill("01122330001")

    ## Send value email field
    page.locator("//input[@name='email']").fill("asd001@gmail.com")

    # ## Select date 
    # page.locator("//button[@aria-label='Choose date']").click()
    # today = datetime.now().strftime("%d")  # Get day as a two-digit number (e.g., '21')

    # # Remove leading zero if your calendar uses single-digit days for the first 9 days
    # if today.startswith("0"):
    #     today = today[1:]

    # page.locator(f"//button[normalize-space()='{today}']").click()

    # Clear the input field first
    date_input = page.locator("label:has-text('Date of Birth') ~ div input[placeholder='DD/MM/YYYY']")
    date_input.fill("")  # Clears the field

    # Type the full date
    date_input.type("10/10/2000")    

    ## Select blood group dropdown
    page.locator("//div[.='Blood Group']").click()

    ## wait fpr list
    page.wait_for_selector("//li[@role='option']", timeout=1000)

    ## Select blood group
    page.locator("//li[normalize-space()= 'O (+ve)']").click()

    ##Select Division
    page.locator("//div[.='Division']").click()

    ## wait for list
    page.wait_for_selector("//li[@role='option']", timeout=1000)

    ## Select division
    page.locator("//li[normalize-space()= 'DHAKA']").click()

    ## Select district
    page.locator("//div[.='District']").click()

    ## Select district
    page.locator("//li[normalize-space()= 'DHAKA']").click()

    ## Give address
    page.locator("//textarea[@name='address']").fill("346/6, Lake Circus")

    ## Open school dropdown
    page.locator("//div[.='School']").click()
 
    ## wait for list
    page.wait_for_selector("//li[@role='option']", timeout=1000)

    ## Give school
    page.locator("//li[normalize-space()= 'Aga Khan Academy']").click()

    ## Click gender
    page.locator("//input[@value='female']").click()

    ## Give username
    page.locator("//input[@name='userName']").fill("edmojo111")

    ## Give password
    page.fill("//input[@name='password']", "12345678")

    ##Scroll down

    page.evaluate('''
                const container = document.querySelector(".MuiPaper-root");
                if (container) {
                    container.scrollTo(0, container.scrollHeight);
                }
            ''')

    ## Click Next button
    page.wait_for_timeout(1000)
    page.locator("//button[normalize-space()='Next']").click()
    

    ##--------------Step 2 --------------------------

    ## Select guardian first Name
    page.locator("//input[@name='guardian[0].relationId.firstName']").fill("Mojo")

    ## Select guardian last name
    page.locator("//input[@name='guardian[0].relationId.lastName']").fill("Ramify")

    ## Select guardian contact no
    page.locator("//input[@name='guardian[0].relationId.contactNo']").fill("01122330001")

    ##Select guardian email
    page.locator("//input[@name='guardian[0].relationId.email']").fill("edmojof101@acex.com")

    ## Select relation with student
    page.locator("//div[.='Relation with student']").click()

    ## wait for list
    page.wait_for_selector("//li[@role='option']", timeout=1000)

    ## Select father
    page.locator("//li[normalize-space()= 'Father']").click()

    ## Select primary guardian
    page.locator("//input[@name='saveCard']").click()

    ## Select username
    page.locator("//input[@name='guardian[0].relationId.userName']").fill("edmojof112")

    ## Select password
    page.locator("//input[@name='password']").fill("12345678")

    ## Scroll to last
    page.evaluate('''
                    const container = document.querySelector(".MuiPaper-root");
                    if (container) {
                        container.scrollTo(0, container.scrollHeight);
                    }
                ''')

    ## Click next
    page.wait_for_timeout(1000)
    page.locator("//button[normalize-space()='Next']").click()
    

    ##-------------Step 3---------------

    ## Click next from batch enrollment
    page.locator("//button[normalize-space()='Next']").click()

    ##--------------------Step 4 ---------------------

    ## Review and submit
    page.wait_for_timeout(1000)
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
    page.wait_for_timeout(1000)
    page.locator("//button[@aria-label='Close']").click()

    





