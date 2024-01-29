Feature: Google search for the testing academy

  Scenario: search for the TTA on Google
    Given I am on the Google Home Page
    When I search for "TheTestingAcademy"
    Then I should see the "TheTestingAcademy" in the results

