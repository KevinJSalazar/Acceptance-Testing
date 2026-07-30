Feature: List all products in the inventory
  As a user, I want to list all products in the inventory so that I can see what I have in stock.

  Scenario: List all products in the inventory
    Given the inventory contains products:
      | Product |
      | Coffee  |
      | Sugar   |
    When the user lists all products
    Then the output should contain:
      """
      Products:
      - Coffee
      - Sugar
      """
