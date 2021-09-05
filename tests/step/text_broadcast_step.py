import pytest
import datetime
from pytest_bdd import scenario, given, then, when, parsers
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

# home url
call_hub_url = 'https://callhub.io/'

# locator
login_btn_xpath = ".//div[@class='et_pb_text_inner']//a[text()='Log in']"
username_id = "id_user"
password_id = "id_password"
homepage_xpath = ".//h1[contains(text(),'Create a Campaign')]"
phonebook_icon_class_name = "phonebook-icon"
phonebook_page_xpath = ".//h1[contains(text(),'Phonebooks')]"
create_btn_xpath = ".//section[1]/div[5]//div[2]/div[2]/div[1]/div[2]//a[1]"
text_broadcast_campaign_xpath = ".//h3[contains(text(),'Text Broadcast campaign')]"
campaign_name_xpath = "//div[@class='input-group undefined']/input[1]"
phonebooks_field_xpath = "//div[@class='phonebook css-2b097c-container']//div[@class=' css-1hwfws3']"
automatic_rent_number_xpath = "//input[@value='automaticallyRentedNumber']"
sender_radiobtn_xpath = "//input[@value='senderName']"
sender_name_xpath = "//input[@placeholder='Set sender name']"
personalise_tag_icon_xpath = "//span[contains(text(),'Personalise')]"
first_name_tag_xpath = "//span[contains(text(),'First name')]"
email_address_xpath = "//input[@placeholder='Enter email address']"
max_retries_xpath = "//input[@placeholder='How many']"
campaign_title_xpath = "//th[contains(text(),'Name')]//parent::tr/td"
phonebook_name_element_xpath = "//ul[@class='summary-phonebooklist']/li[1]/span"
sender_name_preview_xpath = "//th[contains(text(),'Number/Shortcode')]//parent::tr/td"
retries_xpath = "//th[contains(text(),'Max retries')]//parent::tr/td"
message_element_xpath = "//th[contains(text(),'Broadcast')]//parent::tr//following-sibling::td/div"
email_element_xpath = "//th[contains(text(),'Send replies to')]//parent::tr/td[1]"
start_date_element_xpath = "//div[@class='start-date']//div[@class='react-datepicker__input-container']/input[1]"
finish_date_element_xpath = "//div[@class='finish-date']//input[1]"
text_broadcast_result_page_xpath = "//div[@class='campaign-card']//span[2]"
daily_start_time_xpath = "//div[@class='daily-start-time']//div[@class='react-datepicker__input-container']"
daily_end_time_xpath = "//div[@class='daily-start-end']//div[@class='react-datepicker__input-container']"


# text_broadcast_result_page_path = "//span[contains(text(),'Text Broadcast Campaign')]"

@scenario('../features/text_broadcast.feature', 'checking broadcast campaign')
def test_something():
    pass



@scenario('../features/text_broadcast.feature', 'Check login')
def test_outline():
    pass



@pytest.fixture
def browser():
    # b = webdriver.Chrome(executable_path="d://Users//Admin//Downloads//chromedriver_win32//chromedriver.exe")
    b = webdriver.Firefox(executable_path="d://Users//Admin//Downloads//geckodriver-v0.29.1-win64//geckodriver.exe")
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    time.sleep(15)
    b.maximize_window()
    b.implicitly_wait(10)
    yield b
    b.quit()


# browser will open the call hub url
@given('user is on callhub home page')
def open_page(browser):
    browser.get(call_hub_url)


# user will login with valid username and password and check home page id displayed or not
@when(parsers.parse('user login with "{Username}" and "{Password}"'))
@when('user login with <Username> and <Password>')
def login(browser, Username, Password):
    try:
        login_btn = browser.find_element(By.XPATH, login_btn_xpath).click()
        username = browser.find_element(By.ID, username_id).send_keys(Username)
        next_btn = browser.find_element_by_id('change-btn-text').click()
        show_tick_icon = browser.find_element_by_id('show_tick').is_displayed()
        password = browser.find_element(By.ID, password_id).send_keys(Password)
        sign_in_btn = browser.find_element_by_id('change-btn-text').click()
        home_page = browser.find_element(By.XPATH, homepage_xpath).is_displayed()
        assert home_page is True
    except NoSuchElementException:
        browser.save_screenshot('../screenshots/login_fail_1.png')


# user is on phonebook page by clicking phonebooks icon
@given('user is on phonebooks page')
def phonebooks_page(browser):
    phonebook_icon = browser.find_element(By.CLASS_NAME, phonebook_icon_class_name).click()
    phonebook_page = browser.find_element(By.XPATH, phonebook_page_xpath).is_displayed()
    assert phonebook_page is True


# user is on text broadcast page by clicking create button from callhub dashboard
@given('user is on text broadcast page')
def campaign_page(browser):
    create_btn = browser.find_element(By.XPATH, create_btn_xpath).click()
    text_broadcast_campaign_page = browser.find_element(By.XPATH, text_broadcast_campaign_xpath).is_displayed()
    assert text_broadcast_campaign_page is True


@pytest.fixture()
# user will configure target panel with required details
@when(parsers.parse(
    'user configure target panel with campaign "{name}" phonebookname "{select_phonebooks_name}" and "{sendername}"'))
def configure_target_panel(browser, name, select_phonebooks_name, sendername):
    campaign_name = browser.find_element(By.XPATH, campaign_name_xpath).send_keys(name)
    phonebooks_field = browser.find_element(By.XPATH, phonebooks_field_xpath).click()
    # element = browser.find_element_by_id('react-select-2-option-0').click()
    element = browser.find_element_by_xpath(
        "//div[@class=' css-11unzgr']/div[contains(text(),'" + select_phonebooks_name + "')]").click()
    sender_radio_btn = browser.find_element(By.XPATH, sender_radiobtn_xpath).click()
    status = browser.find_element(By.XPATH, sender_radiobtn_xpath).is_selected()
    sender = browser.find_element(By.XPATH, sender_name_xpath).send_keys(sendername)
    next_btn = browser.find_element_by_class_name('primary-button').click()
    assert status is True


# once target configuration is done by clicking next user will be on script panel
@then('user will be on script panel')
def check_script_panel(browser):
    # next_btn = browser.find_element_by_class_name('primary-button').click()
    script_panel_check = browser.find_element_by_xpath("//h6[contains(text(),'Script')]").is_displayed()
    assert script_panel_check is True


# user will configure script panel with text message
@when(parsers.parse('user configure script panel with message "{text_message}"'))
def configure_script_panel(browser, text_message):
    message_text_field = browser.find_element_by_id('message-textarea').send_keys(text_message)
    personalise_tag_icon = browser.find_element(By.XPATH, personalise_tag_icon_xpath).click()
    first_name_tag = browser.find_element(By.XPATH, first_name_tag_xpath).click()
    next_btn = browser.find_element_by_class_name('primary-button').click()


# once script panel is configured successfully by clicking next user will be on settings page
@then('user is on the settings panel')
def check_settings_panel(browser):
    settings_panel_check = browser.find_element_by_xpath("//h6[contains(text(),'Notifications')]").is_displayed()
    assert settings_panel_check is True


# user will configure settings panel with required data
@when(parsers.parse('user configure settings panel with email "{email_id}" and retries "{count}"'))
def configure_settings_panel(browser, email_id, count):
    # test = email_id
    email_address = browser.find_element(By.XPATH, email_address_xpath).send_keys(email_id)
    max_retries = browser.find_element(By.XPATH, max_retries_xpath).send_keys(count)
    next_btn = browser.find_element_by_class_name('primary-button').click()


# once settings panel is configured successful will check user is on preview panel
@then('user is on the preview panel')
def check_preview_panel(browser):
    preview_panel_check = browser.find_element_by_xpath("//h3[contains(text(),'Preview')]").is_displayed()
    assert preview_panel_check is True


# user will preview the provided data in preview panel
@when(parsers.parse('user preview the provided campaign name "{campaign_title}" phonebook "{phonebook_name}" sender "{sender_name}" message "{message_text}" email "{email_detail}" and retries "{retry_count}"'))

def verify_preview_panel(browser, campaign_title, phonebook_name, sender_name, message_text, email_detail, retry_count):
    result = ''
    campaign_name_element = browser.find_element_by_xpath(campaign_title_xpath)
    campaign_name_element_text = campaign_name_element.text
    phonebook_name_element = browser.find_element_by_xpath(phonebook_name_element_xpath)
    phonebook_name_element_text = phonebook_name_element.text
    sender_name_element = browser.find_element_by_xpath(sender_name_preview_xpath)
    sender_name_element_text = sender_name_element.text
    message_element = browser.find_element_by_xpath(message_element_xpath)
    message_element_text = message_element.text
    email_element = browser.find_element_by_xpath(email_element_xpath)
    email_element_text = email_element.text
    retries_element = browser.find_element_by_xpath(retries_xpath)
    retries_element_text = retries_element.text
    if campaign_name_element_text == campaign_title:
        if phonebook_name_element_text == phonebook_name:
            if sender_name_element_text == sender_name:
                if message_element_text == message_text:
                    if email_element_text == email_detail:
                        if retries_element_text == retry_count:
                            result = True

    next_btn = browser.find_element_by_class_name('primary-button').click()
    assert result is True


# user is on schedule panel
@then('user is on the schedule panel')
def check_schedule_panel(browser):
    schedule_panel_check = browser.find_element_by_xpath("//h6[contains(text(),'Schedule')]").is_displayed()
    assert schedule_panel_check is True


# user will schedule the campaign
@when(parsers.parse(
    'user schedule campaign "{days}" starts from "{start_date}" till "{finish_date}" with daily operational hours set from "{start_time}" to "{end_time}"'))
def schedule_campaign(browser, days, start_date, finish_date, start_time, end_time):
    start_date_element = browser.find_element(By.XPATH, start_date_element_xpath)
    start_date_element.click()
    start_date_element.clear()
    start_date_element.send_keys(start_date)
    finish_date_element = browser.find_element(By.XPATH, finish_date_element_xpath)
    finish_date_element.click()
    finish_date_element.clear()
    finish_date_element.send_keys(finish_date)
    daily_start_time = browser.find_element(By.XPATH, daily_start_time_xpath).click()
    select_start_time = browser.find_element_by_xpath("//li[contains(text(),'" + start_time + "')]").click()
    daily_end_time = browser.find_element(By.XPATH, daily_end_time_xpath).click()
    select_end_time = browser.find_element_by_xpath("//li[contains(text(),'" + end_time + "')]").click()
    timezone_switch = browser.find_element_by_class_name('switch').click()
    campaign_timezone_radio_btn = browser.find_element(By.XPATH, "//input[@value='campaign_timezone']").click()
    runs_drop_down = browser.find_element_by_class_name("css-1hwfws3").click()
    campaign_runs_day = browser.find_element_by_xpath("//div[contains(text(),'" + days + "')]").click()
    finish_btn = browser.find_element_by_class_name('primary-button').click()
    text_broadcast_result_page = browser.find_element(By.XPATH, text_broadcast_result_page_xpath)
    if text_broadcast_result_page.text == "Text Broadcast Campaign":
        result = True
    assert result is True


# user should able to see the successfully completed toast
@then(parsers.parse(
    'user able to see broadcast campaign statistics with provided "{count},"{phonebook}","{message}" and "{email}"'))
def campaign_statistic_page(browser, count, phonebook, message, email, start_time, name, sendername, start_date, finish_date):
    global completed
    flag = 0
    summary_tab = browser.find_element_by_xpath("//ul[@class='campaign-overview-tab']/li[2]").click()
    browser.find_element_by_xpath("//span[contains(text(),'" + phonebook + "')]").is_displayed()
    browser.find_element_by_xpath("//span[contains(text(),'" + message + "')]").is_displayed()
    browser.find_element_by_xpath("//td[contains(text(),'" + email + "')]").is_displayed()
    summary_name = browser.find_element_by_xpath(campaign_title_xpath)
    summary_name_text = summary_name.text
    summary_outgoing_number = browser.find_element_by_xpath("//th[contains(text(),'Outgoing number')]//parent::tr/td")
    summary_outgoing_number_text = summary_outgoing_number.text
    summary_schedule = browser.find_element_by_xpath("//th[contains(text(),'Schedule')]//parent::tr/td")
    summary_schedule_text = summary_schedule.text
    summary_phonebook = browser.find_element_by_xpath("//th[contains(text(),'Phonebook')]//parent::tr/td")
    summary_phonebook_text = summary_phonebook.text
    summary_message = browser.find_element_by_xpath("//th[contains(text(),'BROADCAST MESSAGE')]//parent::tr/td//span")
    summary_message_text = summary_message.text
    summary_mail = browser.find_element_by_xpath(email_element_xpath)
    summary_mail_text = summary_mail.text
    if summary_name_text == name:
        if summary_outgoing_number_text == sendername:
            if summary_phonebook_text == phonebook:
                if summary_mail_text == email:
                    result = True
    assert result is True
    start_campaign_btn = browser.find_element_by_xpath("//span[contains(text(),'Start')]").click()
    overview_tab = browser.find_element_by_xpath("//span[contains(text(),'Overview')]").click()
    pending = browser.find_element_by_xpath("//div[@class='row justify-content-center']/div[2]/div[contains(text(),'3')]").is_displayed()
    e = datetime.datetime.now()
    current_time = e.strftime("%I:%M %p")
    exact_time = ''
    if current_time[-2:] == "AM" and current_time[:2] == "12":
        exact_time = "00" + current_time[:-2]
    elif current_time[-2:] == "AM":
        exact_time = current_time[:-2]
    elif current_time[-2:] == "PM" and current_time[:2] == "12":
        exact_time = current_time[:-2]
    else:
        exact_time = str(int(current_time[:2]) + 12) + current_time[2:5]
    if pending is True:
        if exact_time > start_time:
            flag = 1
            while True:
                try:
                    completed = browser.find_element_by_xpath("//div[@class='row justify-content-center']/div[1]/div[contains(text(),'3')]")
                except:
                    browser.refresh()
                else:
                    completed = browser.find_element_by_xpath("//div[@class='row justify-content-center']/div[1]/div[contains(text(),'3')]").is_displayed()
                    break
            assert completed is True
        else:
            flag = 0

    assert flag == 1, 'scheduled time is not a current time'
