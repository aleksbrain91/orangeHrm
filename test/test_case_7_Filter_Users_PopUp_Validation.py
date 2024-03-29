# Test Case 7: Verify Employee Name Autocomplete Suggestion
# Test Name: Test_Employee_Name_Autocomplete
# Purpose: To verify that the autocomplete suggests names based on the entered value in the 'Employee Name' field.
# Steps:
# 1. Open the browser and navigate to the OrangeHRM URL.
# 2. Login to the application with valid credentials.
# 3. Navigate to the 'HR Administration' section from the left menu.
# 4. Click on the 'Filter Users' button.
# 5. Start typing a known employee name in the 'Employee Name' field.
# Expected Result:
# As the user types, an autocomplete dropdown should appear with employee name suggestions.

# -----------------------------------------------------------------------------------

# Test Case 7_1: Verify No Results Found Error Message
# Test Name: Test_Employee_Name_No_Results
# Purpose: To verify that an appropriate error message is shown when no employee names match the entered value.
# Steps:
# 1. Open the browser and navigate to the OrangeHRM URL.
# 2. Login to the application with valid credentials.
# 3. Navigate to the 'HR Administration' section from the left menu.
# 4. Click on the 'Filter Users' button.
# 5. Enter a non-existing employee name in the 'Employee Name' field.
# Expected Result:
# A message indicating 'no results found' should appear if no employee names match the entered value.

# -----------------------------------------------------------------------------------

# Test Case 7_2: Verify Dropdown Default Values
# Test Name: Test_Dropdown_Default_Values
# Purpose: To verify that the dropdowns in the 'Filter Users' pop-up are set to their default values upon opening.
# Steps:
# 1. Open the browser and navigate to the OrangeHRM URL.
# 2. Login to the application with valid credentials.
# 3. Navigate to the 'HR Administration' section from the left menu.
# 4. Click on the 'Filter Users' button.
# Expected Result:
# All dropdowns in the 'Filter Users' pop-up should display their default values.

# -----------------------------------------------------------------------------------

# Test Case 7_3: Verify Reset Button Functionality
# Test Name: Test_Reset_Button
# Purpose: To verify that the 'Reset' button clears all input fields and selections and closes the 'Filter Users' pop-up.
# Steps:
# 1. Open the browser and navigate to the OrangeHRM URL.
# 2. Login to the application with valid credentials.
# 3. Navigate to the 'HR Administration' section from the left menu.
# 4. Click on the 'Filter Users' button.
# 5. Change values in the input fields and dropdown selections.
# 6. Click on the 'Reset' button.
# 7. Reopen the 'Filter Users' pop-up by clicking on the 'Filter' button.
# Expected Result:
# The 'Filter Users' pop-up should close upon clicking the 'Reset' button and upon reopening, all input fields and dropdowns should be reset to their default selections.

# -----------------------------------------------------------------------------------

# Test Case 7_4: Verify Cancel Button Functionality
# Test Name: Test_Cancel_Button
# Purpose: To verify that the 'Cancel' button closes the 'Filter Users' pop-up without clearing selected values.
# Steps:
# 1. Open the browser and navigate to the OrangeHRM URL.
# 2. Login to the application with valid credentials.
# 3. Navigate to the 'HR Administration' section from the left menu.
# 4. Click on the 'Filter Users' button.
# 5. Change values in the input fields and dropdown selections.
# 6. Click on the 'Cancel' button.
# 7. Reopen the 'Filter Users' pop-up by clicking on the 'Filter' button.
# Expected Result:
# The 'Filter Users' pop-up should close upon clicking the 'Cancel' button and upon reopening, the previously selected values should be retained.
