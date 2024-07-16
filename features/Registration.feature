Feature: Verifying Registration Functionality
    Background:
        Given User is on Registration Page

    @smoke
    Scenario Outline: User Register with username that doesn't exists in repository
    When User enter username <username>
    And User enters email_id <email_id>
    And User enters password <password>
    And User pick bod <bod>
    And User choose Gender <gender>
    And User choose <country> as country
    And User choose <state> as state
    And User choose <city> as city
    And User enters <zipcode> zip code
    And User check the terms and condition
    And User clicks on Sign Up Button
    
    Then User should be registered successfully
    Examples:
        |username|email_id|password| gender | bod | country | state | city | zipcode |
        |orakksa|adadasd1123@yopmail.com|1234qwer| Male | 29/12/1945 | Indonesia | Serang | Cilegon | 42412 |


    