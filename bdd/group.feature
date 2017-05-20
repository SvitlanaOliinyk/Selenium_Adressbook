Feature: Group feature
  Description

  Scenario Outline: Add new group
    Given a group list
    Given a group with <name>, <header>, <footer>
    When I add a new group to the list
    Then a new group list is equal to the old list with the old group

    Examples:


    | name     | header | footer |
    | uyg guyg | hj     | kjnj   |
    | 876yg    | 67hj   |        |
    |    шро   |   пми  | роти   |