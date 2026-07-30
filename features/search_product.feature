Feature: Search for a product in the inventory
  As a user, I want to search for a product so that I can quickly find items in my inventory.

  Scenario: Search for a product by name
    Given the inventory contains products:
      | Product  |
      | Coffee   |
      | Sugar    |
      | Milk     |
    When the user searches for "Coffee"
    Then the search results should contain "Coffee"
    And the search results should not contain "Sugar"
