Feature: Update the quantity of a product
  As a user, I want to update the quantity of a product so that I can keep the stock accurate.

  Scenario: Update the quantity of a product
    Given the inventory contains products:
      | Product | Quantity |
      | Coffee  | 10       |
    When the user updates product "Coffee" to quantity "25"
    Then the inventory should show product "Coffee" with quantity "25"
