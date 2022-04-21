<h1>Testing</h1>

# Code Validation

### HTML5
[W3C HTML Validator](https://validator.w3.org/#validate_by_input) Passed all tests, minus the Jinja errors.
![HTML Validator](static/images/validation/html-test.png)

### CSS3 
[W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) No Errors
![CSS Validator](static/images/validation/css-test.png)

### JS
[JSHint](https://www.jshint.com/) No Errors

![Javascript Validator](static/images/validation/javascript-test.png)

### Python
[PEP8 Online](http://pep8online.com/) No Errors
![HTML Validator](static/images/validation/python-test.png)

# Features and Functionality

### Security Testing

- Website was tested on multiple devices.
- Tested to ensure unregistered users can't access user profiles.
- Tested to ensure edit/delete functions only available to users who created the recipe.
- Error messages display when an error occurs on site.

### Responsiveness

-	The responsiveness of this site was tested using an Apple MacBook Pro, an Ipad 2, an Iphone X, an Iphone XR, a Samsung notepad and a Windows laptop.

# User Stories

## User Story Testing

### New Users

All navigation and interaction works properly.
    
- Nav features were tested on multiple devices as they display differently depending on screen size. I also checked scroll and swiping features on certain elements to ensure they translated well to mobile devices.

Responsive on all devices.

- All pages were viewed to ensure everything renders in an acceptable way. Breakpoints all work as expected.

Homepage button.

- Tested homepage button to ensure it took new users to the register page, this changes to the view profile page when logged in. I tested this for multiple users to ensure it was rendered properly.

Navbar.

- Tested nav links in the same way as above. As a new unregistered user the "Profile" and "Log Out" options should not be available. This worked in all my tests.

Add a recipe.

- New users should not be able to add a recipe, this was checked.

Edit/Delete recipe.

- Buttons to edit/delete recipes should not be available to unregistered users, the page was sent to multiple people to check that they could not do this.

View/search recipes.

- Unregistered users should have the same ability to view and search all recipes on the website as someone with an account. This worked in all my testing.

Register for account.

- Form validation works correctly ensuring the user entered a valid email. Once created the password is properly hashed and the details are stored on the database. The user receives a visual prompt and is sent to their profile page.

### Logged in user

View Profile and own recipes.

- Checked with multiple users. Flash messages display username and access the recipes created by the user for easy access to delete/edit.

View Profile and own recipes.

- Checked with multiple users. Flash message displays username and displays the recipes created by the user for easy access to delete/edit.

Edit and Delete.

- Checked to ensure only the recipes created by the logged in user can be modified. 
- Edit function works correctly on all fields, data already stored populates the input fields. 
- As noted below the "Ingredient" and "Steps" fields caused issues with deleting themselves, this is now fixed. 
- Delete function works correctly and removes the recipe from all pages of the website. 

Logout.

- User is able to logout and is no longer able to add/alter recipes.

# Bugs and Fixes

## Edit Recipe issue

Due to the .update() function no longer working in the newer Pymongo versions, I had a lot of issues with .update_one(). My arrays would delete themselves if the user updated another recipe field. For instance, if you wanted to change the cook time, when the update button was clicked all the steps and ingredients were deleted.

I spent a lot of time trying to solve this issue. It turns out I left the {{loop.index}} in the input name which was causing the name to change on each loop. It was not the .update_one() method as I thought.

## iPhone footer spacing

I found that on an iphone x the contact info on the footer did not display properly. This did not appear in Chrome device emulation.

![iPhone footer spacing](static/images/iphone-footer-spacing-bug.PNG)

This was fixed by altering grid values on smaller screens.

## Card Images

I had an odd issue that had my recipe cards not breaking evenly and leaving empty gaps.

This was fixed by forcing my img heights to be the same. Materialize grids can have issues with images of different sizes.

## .webP format on older Apple devices

During my testing process I found a confusing bug, nn older apple devices none of my images were loading, however on my iPhone X they worked fine.

![Edit Review form](static/images/safari-webp-bug.PNG)

I eventually found out that older versions of Safari do not support the webP file format. To fix this all I had to do was revert back to a .jpg format. Although this dropped my performance score on lighthouse testing I felt it was the best thing to do.

## User Story Testing

* "I want to view some recipes without creating an account"

  * A user is able to view all recipes without needing to register.

    
* "I want to upload my recipe and have my name credited"

  * A logged in user can upload their recipe from the profile page. The full recipe page auto loads the username of the creator.

    
* " I made a mistake and want to edit my recipe"

  * The recipe creator can edit a single field in the recipe without having to input the whole thing.

    

* "I want to be delete a recipe I no longer want online"

  * The recipe creator can delete their own recipe on the full recipe page.

    

* "I want to be search for a specific recipe"

  * A user can use the search bar in the recipes page to find specific results.

    
## Lighthouse Testing

- As mentioned above, I chose to revert to .jpg images to ensure compatibility. My largest file is a background image in my .css folder. I was not able to find a way to create a dual image system that checked compatibility. This slightly lowered my score, however my pages were still nearly all green in all of my testing.

#### Desktop 

![Lighthouse Desktop Test 1](static/images/lighthouse-testing/lighthouse-test-1.png)

#### Mobile 

![Lighthouse Mobile Test 1](static/images/lighthouse-testing/lighthouse-test-2.png)


## General Testing

* All internal page links work.

* External link works properly and opens on new tab.

* Pages/buttons hide/show as expected.

* All flash messages display correctly.

* Error pages display correctly on invalid input.

* 404 and 500 error pages show properly.



