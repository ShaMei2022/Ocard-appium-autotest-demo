Feature: Welcome
    A user can go home page

* @author : Conrad Zhang
* @since : 2024-01-16
* OpenApp - Go home page


    Scenario: Welcome - Open App - Error Number
    Given Open App
    When user see the Welcome
    Then user chose start using
    When user chose phone login
    When user input error number and see error message
    When user input success number and see success message
    Then user chose permissions
    Then user see home page
    When user slide banner
    Then user chose banner
    Then user back home page
    When user chose all select


    # Scenario: Welcome - Open App - Success Number
    # Given Open App
    # When user see the Welcome
    # Then user chose start using
    # When user chose phone login
    # When user input success number and see success message