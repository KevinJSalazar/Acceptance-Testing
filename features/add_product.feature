Feature: Add a product to the inventory
  As a user, I want to add products to the inventory so that I can keep track of my stock.

  Scenario: Add a product to the inventory
    Given the inventory is empty
    When the user adds a product "Coffee"
    Then the inventory should contain "Coffee"
