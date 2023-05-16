# EFH - Project app Testing

## Content

## Manual Testing

### Navigation
| Test  | Action | Expected Results  | Pass/Fail |
| ------------- | ------------- | ------------- | ------------- |
| Home link  | Click on the Home link in the navigation bar  | The page should navigate to the home page  | Pass  |
| MyBook link (when the user is authenticated) | Click on the MyBook link in the navigation bar  | The page should navigate to the users book page  | Pass  |
| AddRecipe link (when the user is authenticated)  | Click on the AddRecipe link in the navigation bar  | The page should navigate to the add recipe page  | Pass  |
| Logout link (when the user is authenticated)  | Click on the Logout link in the navigation bar  | The user should be logged out and redirected to the logout page  | Pass  |
| Register link (when the user is not authenticated)  | Click on the Register link in the navigation bar  | The page should navigate to the registration page  | Pass  |
| Login link (when the user is not authenticated)  | Click on the Login link in the navigation bar  | The page should navigate to the login page  | Pass  |

### Index Page
| Test  | Action | Expected Results  | Pass/Fail |
| ------------- | ------------- | ------------- | ------------- |
| Welcome Message  | Open the index page  | Welcome to Eating From Home!! along with the description should be displayed.  | Pass  |
| Reasons to Join Us  | Open the index page  | Four cards should be displayed with titles and descriptions  | Pass  |
| Inspiration Corner  | Open the index page  | A list of recipe cards should be displayed. Each card should contain an image(placeholder or a recipe featured image) author name, recipe title, excerpt, creation date and the number of likes.| Pass  |
| Pagination List  | If the recipe list has more than the default number of entries per page  | Pagination links should be displayed at the bottom, allowing navigation to previous and next pages  | Pass  |
| Pagination Single  | If the recipe list has fewer entries than the default number  | No pagination links should be displayed  | Pass  |
| Title Recipe Details Link  | Click on a recipe card title  | The page should navigate to the detailed view of the clicked recipe  | Pass  |

### My Book Page(when the user is authenticated) 
| Test  | Action | Expected Results  | Pass/Fail |
| ------------- | ------------- | ------------- | ------------- |
| Add Recipe Button  | Click on the Add Recipe button  | The user should be redirected to the add recipe page  | Pass  |
| Recipe List  | Open the my book page  | A list of recipe cards should display, each card contain an image(placeholder or featured image) author name, recipe title, options to edit and delete the recipe, and the creation date  | Pass  |
| Pagination List  | If the user book has more than the default number of entries per page  | Pagination links should be displayed at the bottom, allowing navigation to previous and next pages  | Pass  |
| Pagination Single  | If user book list has fewer entries than the default number  | No pagination links should be displayed  | Pass  |
| Recipe details link  | Click on a recipe cards title   | The page should navigate to the detailed view of the clicked recipe  | Pass  |
| Edit Recipe Button  | Click on the Edit button of a recipe card  | The user should be redirected to the edit recipe page for the selected recipe  | Pass  |
| Delete Recipe Button  | Click on the Delete button of a recipe card  | The user should be prompted to confirm the deletion of the recipe  | Pass  |

### Recipe Details Page
| Test  | Action | Expected Results  | Pass/Fail |
| ------------- | ------------- | ------------- | ------------- |
| Display Recipe Details  | Open the recipe details page  | All the recipe details are correctly displayed on the page  | Pass  |
| Recipe Description  | Open the recipe details page  | The recipe description is correctly displayed on the page  | Pass  |
| Display Ingredients  | Open the recipe details page  | The recipe ingredients are correctly displayed on the page  | Pass  |
| Display Method  | Open the recipe details page  | The recipe method is correctly displayed on the page  | Pass  |
| Display Comments  | Open the recipe details page that has comments  | All comments are correctly displayed with the commenter's name, comment content, and creation date  | Pass  |
| Submit Comment  | If authenticated, leave a comment using the comment form  | The comment is displayed in the comments section, awaiting approval  | Pass  |
| Like Button Functionality  | If authenticated, click the like button  | The like count increases, and the button reflects the users action liked or unliked  | Pass  |
| Image Display  | Open the recipe details page | The placeholder image or featured image is correctly displayed on the page  | Pass  |
| Proper Formatting and Styling  | Open the recipe details page on different devices with varying screen sizes  | The page layout, formatting, and styling are consistent and responsive on different devices  | Pass  |

### User Recipe Details Page(when the user is authenticated) 
| Test  | Action | Expected Results  | Pass/Fail |
| ------------- | ------------- | ------------- | ------------- |
| Display Recipe Details  | Open users recipe details page  | All the recipe details are correctly displayed on the page  | Pass  |
| Recipe Description  | Open users recipe details page  | The recipe description is correctly displayed on the page  | Pass  |
| Display Ingredients  | Open users recipe details page  | The recipe ingredients are correctly displayed on the page  | Pass  |
| Display Method  | Open users recipe details page  | The recipe method is correctly displayed on the page  | Pass  |
| Image Display  | Open users recipe details page  | The placeholder image or featured image is correctly displayed on the page  | Pass  |

### Add Recipe Page(when the user is authenticated) 
| Test  | Action | Expected Results  | Pass/Fail |
| ------------- | ------------- | ------------- | ------------- |
| Form Rendering  | Open Add Recipe page  | The form should be rendered correctly with all the specified fields  | Pass  |
| Submiting Form  | Fill in and Submit the Add Recipe Form  | Redirects User to My Book and return message that the form data is successfully submitted  | Pass  |
| Field Validation  | Submit the form without filling in any of the required fields  | Redirect to field or error messages are displayed for required field that was left empty  | Pass  |
| File Upload  | Select a file for the featured image field  | The selected file for the featured image field is uploaded successfully  | Pass  |

### Edit Recipe(when the user is authenticated) 
| Test  | Action | Expected Results  | Pass/Fail |
| ------------- | ------------- | ------------- | ------------- |
| Display Update Recipe Form  | Open the page to Update Recipe form  | The Update Recipe form is displayed correctly with all the required fields pre populated with the info already saved.  | Pass  |
| Updating Form  | Fill in and Update the Update Recipe Form  | Redirects User to My Book and return message that the form data is successfully updated  | Pass  |
| Field Validation  | Update the form without filling in any of the required fields  | Redirect to field or error messages are displayed for required field that was left empty  | Pass  |
| File Upload Update  | Select a file for the featured image field  | The selected file for the featured image field is uploaded successfully  | Pass  |

### Delete Recipe(when the user is authenticated) 
| Test  | Action | Expected Results  | Pass/Fail |
| ------------- | ------------- | ------------- | ------------- |
| Delete Button  | Click  | Recipe is removed from users book page  | Pass  |
| Delete Button  | Click  | Success message appears to user saying that the recipe has been successfully deleted  | Content  |
| Delete Button  | Click  | The page should navigate to the my book page   | Pass  |
| Cancel Button  | Click  | The page should navigate to the my book page  | Pass  |

### Django All Auth Pages
| Test  | Action | Expected Results  | Pass/Fail |
| ------------- | ------------- | ------------- | ------------- |
| Sign Up  |  |  |  |
| Log in link  | Click  | Redirect to login page  | Pass  |
| Username field  | Leave empty  | On submit: form won't submit  | Pass  |
| Username field  | Leave empty  | Error message displays  | Pass  |
| Username field  | Insert correct format  | On submit: form submit  | Pass  |
| Username field  | Insert duplicate username  | On submit: form won't submit  | Pass  |
| Username field  | Insert duplicate username  | Error message displays  | Pass  |
| Email field  | Insert incorrect format  | On submit: form won't submit  | Pass  |
| Email field  | Insert incorrect format  | Error message displays  | Pass  |
| Email field  | Insert correct format  | On submit: form submit  | Pass  |
| Email field  | Leave empty  | On submit: form submit  | Pass  |
| Email field  | Insert duplicate email  | On submit: form won't submit  | Pass  |
| Email field  | Insert duplicate email  | Error message displays  | Pass  |
| Password field  | Insert incorrect format  | On submit: form won't submit  | Pass  |
| Password field  | Insert incorrect format  | Error message displays  | Pass  |
| Password field  | Passwords don't match  | On submit: form won't submit  | Pass  |
| Password field  | Passwords don't match  | Error message displays  | Pass  |
| Password field  | Insert correct format  | 	On submit: form submit  | Pass  |
| Sign Up button (form valid)  | Click  | Form submit  | Pass  |
| Sign Up button (form valid)  | Click  | Redirect to home page  | Pass  |
| Sign Up button (form valid)  | Click  | Success message confirming login appears  | Pass  |
| Sign Up button (form valid)  | Click  | Success message fades after 3 seconds  | Pass  |
| Log in  |  |  |  |
| Sign up link  | Click  | 	Redirect to sign up page  | Pass  |
| Username field  | Leave empty  | On submit: form won't submit  | Pass  |
| Username field  | Leave empty  | 	Error message displays  | Pass  |
| Username field  | Insert wrong username  | On submit: form won't submit  | Pass  |
| Username field  | Insert wrong username  | Error message displays  | Pass  |
| Password field  | Leave empty  | On submit: form won't submit  | Pass  |
| Password field  | Leave empty  | Error message displays  | Pass  |
| Password field  | Insert wrong password  | On submit: form won't submit  | Pass  |
| Password field  | Insert wrong password  | Error message displays  | Pass  |
| Login button (form valid)  | Click  | Form submit  | Pass  |
| Login button (form valid)  | Click  | Redirect to home page  | Pass  |
| Login button (form valid)  | Click  | Success message confirming login appears  | Pass  |
| Login button (form valid)  | Click  | Success message fades after 3 seconds  | Pass  |
| Log Out Confirmation  |  |  |  |
| Logout button  | Click  | Content  | Content  |

## Admin panel
* The Recipe, Comment are successfully registered in the admin panel.

* Admins have full access to CRUD functionality for all recipes and comments in the admin panel.

* Admins also have full moderation over the comments, comments can also be approved or deleted.

* Django Allauth works successfully and the admins can change users permissions.

## Browser Testing
* The Website was tested on Google Chrome, Firefox, Safari browsers with no issues noted.

## Bugs

### Fixed Bugs
Django User Form not uploading featured image. No error was showing, looking into stackoverflow I have found this [information](https://stackoverflow.com/questions/29171077/imagefield-not-saving-images-in-modelform-django-python) which was very helpful to fix the issue.

Herokuapp URL page not displaying on am I responsive frames. Error showing in the mock screens was **recipes-for-me-herokuapp.com refused to connect** this [link](https://code-institute-room.slack.com/archives/C026PTF46F5/p1669748686922019?thread_ts=1669744943.768489&cid=C026PTF46F5) was very helpful to fix the issue.

### Unfixed Bugs
No Unfixed Bugs left behind ;)

## Code Validation

### W3C HTML VALIDATION
All html pages have been run through the [W3C HTML Validator](https://validator.w3.org/) and the below results were returned.

**- index.html**
* Erros = None.
* Warnings = None.
![index html test](Docs/Readme_images/testing/home_page_test_html.png)

**- my_book.html**
* Erros = None.
* Warnings = None.
![my book html test](Docs/Readme_images/testing/my_book_test_html.png)

**- addrecipe.html**
* Erros = None.
* Warnings = None.
* ![addrecipe html test](Docs/Readme_images/testing/added_recipe_test_html.png)

**- edit.html**
* Erros = None.
* Warnings = None.
![edit html test](Docs/Readme_images/testing/edit_recipe_test-html.png)

**- recipe_details.html**
* Erros = None.
* Warnings = None.
![page recipe html test](Docs/Readme_images/testing/page_recipe_test_html.png)

**- single.html**
* Erros = None.
* Warnings = None.
* ![user recipe html test](Docs/Readme_images/testing/user_recipe_details_html.png)

**- login.html**
* Erros = None.
* Warnings = None.
* ![login html test](Docs/Readme_images/testing/sign_in_test_html.png)

**- signup.html**
* Erros = None.
* Warnings = None.
* ![signup html test](Docs/Readme_images/testing/sign_up_test_html.png)

## Jigsaw CSS VALIDATION
No errors or warnings are returned when passing the styles.css through the [Jigsaw CSS Validator](https://jigsaw.w3.org/css-validator/).

* ![css testing image](Docs/Readme_images/testing/css_validator_test_results.png)

## JSHint JavaScript VALIDATION
All the sripts used in EFH have been run through the [JSHint Javascript Validator](https://jshint.com/) and they return no errors.

* ![jshint java testing](Docs/Readme_images/testing/jshint_test_result.png)

## CI Python Linter Python VALIDATION 
All the main Python files were run through the [CI Python Linter Validator](https://pep8ci.herokuapp.com/) with no errors returned.

**- forms.py**
* Erros = None.
* ![test forms.py](Docs/Readme_images/testing/forms_test_python.png)

**- models.py**
* Erros = None.
* ![test models.py](Docs/Readme_images/testing/models_test_python.png)

**- urls.py**
* Erros = None.
* ![test urls.py](Docs/Readme_images/testing/ursl_test_python.png)

**- views.py**
* Erros = None.
* ![test views.py](Docs/Readme_images/testing/views_test_python.png)

## LIGHTHOUSE REPORTS
EFH app home page have been tested for Performance, Accessibility, Best Practices and SEO using [Lighthouse Chrome Developer Tool](https://developer.chrome.com/docs/lighthouse/overview/).
The lighthouse scores look very good overall, with some things that could be improved. A future implementation would be to convert all images to the webp format.

**- Home Page**
* Performance = 72
* Accessibility = 98
* Best Practices = 100
* SEO = 100
* ![lighthouse test](Docs/Readme_images/testing/lighthouse_test_homepage.png)
