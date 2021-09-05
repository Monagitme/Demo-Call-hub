Feature: text broadcast campaign

    Background:
        Given user is on callhub home page

    Scenario: checking broadcast campaign
        When user login with "meenaageethu@gmail.com" and "meena123"
        Given user is on text broadcast page
        When user configure target panel with campaign "sample" phonebookname "Meena_Phonebook1" and "tester1"
        Then user will be on script panel
        When user configure script panel with message "Hi "
        Then user is on the settings panel
        When user configure settings panel with email "meenaageethu@gmail.com" and retries "1"
        Then user is on the preview panel
        When user preview the provided campaign name "sample" phonebook "Meena_Phonebook1" sender "tester1" message "Hi {first_name}" email "meenaageethu@gmail.com" and retries "01"
        Then user is on the schedule panel
        When user schedule campaign "Everyday" starts from "September 5,2021 19:30PM" till "September 6,2021 19:45PM" with daily operational hours set from "19:30" to "19:45"
        Then user able to see broadcast campaign statistics with provided "3","Meena_Phonebook1","Hi {first_name}" and "meenaageethu@gmail.com"

    Scenario Outline: Check login
         When user login with <Username> and <Password>

         Examples:
         | Username                | Password |
         | meenaageethu@gmail.com  | meena123 |
         | menaaaaaa@gmail.com     | meena    |