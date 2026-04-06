Feature: Test email operations
  As a user
  I want to open the tutamail page
  So that I can verify basic email client features

  Scenario: Open tutamail and log in
  Given the user opens the homepage
  When the user enters email and password
  And user clicks login
  Then user is logged in
  When the user clicks logout
  Then the user is logged out

  Scenario: Send email and verify that email was received
  Given user was logged in
  And emails were deleted
  When user sends email
  Then user received email
  When the user clicks logout
  Then the user is logged out

  Scenario: Send email with attachment and verify that email was received
  Given user was logged in
  And emails were deleted
  When user sends email with attachment
  Then user received email with attachment
  When the user clicks logout
  Then the user is logged out