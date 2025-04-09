## <remove all of the example text and notes in < > such as this one>

## Functional Requirements

1. User Registration – The system shall allow users to register by providing a username, email, and password.
2. User Login – The system shall authenticate users based on their credentials to allow access.
3. User Logout – The system shall allow logged-in users to securely log out.
4. Create Recipe – The system shall allow users to create and submit new recipes with ingredients and instructions.
5. Edit Recipe – The system shall allow users to edit their own submitted recipes.
6. Delete Recipe – The system shall allow users to delete their own submitted recipes.
7. View Recipe – The system shall allow all users to view any published recipe.
8. Search Recipe – The system shall allow users to search for recipes by keywords.
9. Rate Recipe – The system shall allow users to rate recipes on a scale (e.g., 1–5 stars).
10. Comment on Recipe – The system shall allow users to leave comments on recipe pages.
11. View User Profile – The system shall allow users to view their own profile including submitted recipes.
12. Edit User Profile – The system shall allow users to edit their display name, email, or password.
13. Save Recipe (Favorites) – The system shall allow users to save recipes to their favorites list.
14. View All Recipes – The system shall allow users to view a list of all publicly available recipes.
15. Filter Recipes – The system shall allow users to filter recipes by tags such as 'vegan', 'dessert', etc.

<using the syntax [](images/ui1.png) add images in a folder called images/ and place sketches of your webpages>

## Non-functional Requirements
1. The system shall load recipe pages in under 2 seconds
2. The system should support more than 100 users without performance issues

<each of the 14 requirements will have a use case associated with it>
## Use Cases <Add name of who will write (this specific requirement) and implement (in subsequent milestones) the use case below>

1. User Registration (Written and will be implemented by Eric)
- **Pre-condition:** Visitor is not logged in and has a valid email address.
- **Trigger:** Visitor clicks “Sign Up” on the website.
- **Primary Sequence:**
1. Visitor accesses the registration page and fills in username, email, and password.
2. Visitor submits the registration form.
3. System validates the data and creates a new user account.
4. System logs the user in or redirects them to the login page.
- **Primary Postconditions:** A new user account is created and stored in the system.
- **Alternate Sequence:**
1. Email already exists: System notifies user and suggests logging in.
2. Weak password: System asks for a stronger password.
3. Missing fields: System prompts user to complete all required inputs.
4. Server error: System shows failure message and retry option.

2. User Login (Written and will be implemented by Eric)
- **Pre-condition:** User has an existing account with valid email and password.
- **Trigger:** User clicks the “Login” button from the homepage or any restricted page.
- **Primary Sequence:**
1. User enters their email and password on the login form.
2. User submits the form.
3. System verifies the credentials.
4. If valid, system logs the user in and redirects to the dashboard.
- **Primary Postconditions:** User is authenticated and has access to protected features.
- **Alternate Sequence:**
1. Invalid email or password: System displays an error message.
2. Empty fields: System prompts user to fill in required inputs.
3. Account inactive: System informs user and provides help link.
4. Technical issue: System suggests retrying later.

3. User Logout (Written and will be implemented by Eric)
- **Pre-condition:** User is currently logged in.
- **Trigger:** User clicks the “Logout” button from the navigation bar or menu.
- **Primary Sequence:**
1. User clicks the logout action.
2. System processes the logout request.
3. System destroys the user session.
4. System redirects user to the homepage or login screen.
- **Primary Postconditions:** User is logged out and no longer has access to protected resources.
- **Alternate Sequence:**
1. Session already expired: User is redirected to the login page.
2. Logout fails: System displays an error message and retry option.

4. Create Recipe (Written and will be implemented by Eric)
- **Pre-condition:** User must be logged in.
- **Trigger:** User clicks the “Create Recipe” button or menu item.
- **Primary Sequence:**
1. User accesses the create recipe form.
2. User fills in title, description, ingredients, and instructions.
3. User submits the form.
4. System saves the recipe and redirects to the recipe detail page.
- **Primary Postconditions:** A new recipe is stored and visible under the user’s account.
- **Alternate Sequence:**
1. Missing fields: System prompts user to complete the form.
2. Invalid input: System highlights errors.
3. Session expired: User is redirected to login page.
4. System error: Recipe not saved, and user is asked to retry.

5. Edit Recipe (Written and will be implemented by Eric)
- **Pre-condition:** User is logged in and owns the recipe they want to edit.
- **Trigger:** User clicks the “Edit” button on one of their recipes.
- **Primary Sequence:**
1. User views their recipe and clicks “Edit.”
2. System shows a form pre-filled with the recipe’s details.
3. User updates fields and submits the form.
4. System validates and saves the changes, then redirects to updated recipe.
- **Primary Postconditions:** The recipe is updated in the system with the new details.
- **Alternate Sequence:**
1. User tries to edit a recipe they don’t own: Access is denied.
2. Invalid input: System highlights errors for correction.
3. Recipe deleted before submission: System shows error.
4. System issue: Changes not saved, and user is notified.

6..
7..
8..
9..
10..

11. Edit User Profile
- **Pre-condition:** 
- User must have an existing account
- User must be logged in
- **Trigger:** User selects edit my profile which asks them to update their display name, email, or password.
- **Primary Sequence:**
1. User opens up website
2. User navigates to button that says edit my profile
3. User enters name, email, and password they wish to update to
- **Primary Postconditions:** User’s display name, email, and password are successfully updated
- **Alternate Sequence:**
1. Database unable to retrieve user profile
2. User is not logged in in order to edit profile

12. Save Recipe (Favorites)
- **Pre-condition:** 
- User must have an existing account
- User must be logged in
- **Trigger:** User clicks on favorite recipe from the / endpoint
- **Primary Sequence:**
1. User opens up website by going to / endpoint
2. User clicks on favorite on the recipe they want to save
3. System verifies if user is logged in
4. System saves the recipes favorites to data base
- **Primary Postconditions:** Favorite recipes are successfully saved for the user
- **Alternate Sequence:**
1. User is not logged in
2. Database save error

13. View All Recipes
- **Pre-condition:** There must be a minimum of 1 recipe to view in order to view all recipes
- **Trigger:** User navigated to / endpoint to view all recipes
- **Primary Sequence:**
1. User navigates to website to the / endpoint
2. System queries the database to retrieve all recipes 
3. System displays all recipes  to the user
- **Primary Postconditions:** All recipes are successfully displayed 
- **Alternate Sequence:**
1. Database fails to retrieve all recipes
2. No recipes written to database when visiting / endpoint 

14. Filter Recipes
- **Pre-condition:** User must be on the recipe browsing page
- **Trigger:** User selects a filter or tag
- **Primary Sequence:**
1. User navigates to browsing section of website
2. User clicks or selects the tag
3. System will query recipes containing that specific tag
- **Primary Postconditions:** Filtered recipes are successfully displayed
- **Alternate Sequence:**
1. System does not find any recipe with the matching filter

15. View User Profile
- **Pre-condition:** 
- User must have an existing account  
- User must be logged in  
- **Trigger:** User selects view profile and recipes of user are displayed  
- **Primary Sequence:**
1. User opens up website
2. User navigates to profile he/she wants to view 
3. User selects view profile
4. System retrieves profile from database
5. System displays recipes created by user
- **Primary Postconditions:** User profile along with recipes are successfully displayed as output
- **Alternate Sequence:**
1. No wifi connection
2. No profile to view. Profile unavailable
