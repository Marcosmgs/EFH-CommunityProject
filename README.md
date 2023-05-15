# EFH - Eating From Home

![Am I Responsive]

EFH - Eating From Home is a web application built with Django that aims to help individuals working from home save time and eat healthier by providing meals inspirations in a platform where you can create and manage your own recipes just like a granny's book.

In a work-from-home environment, finding time to prepare healthy meals can be challenging. EFH web application addresses this by empowering users to take control of their diet and make healthier eating choices. By using My Recipe Book, you can save time, stay organized, descover new ideas and much more.

- - -

## CONTENTS (summary)

- - -

## User Experience (UX)

An user for EFH app would likely be an adult professional working from home, looking to save time and make healthier food choices, maintaining a healthy lifestyle while working. 
Our main visitor will be people who want to optimize their time and prioritize their well-being.

### User Stories - Epics
**Site Administration**
- As a Site Admin I can approve or disapprove comments so that I can moderate comments
- As a Site Admin I can create, read, update and delete recipes so that I can manage my community content 
- As a Site Admin I can create draft recipes so that I can finish writing the content later

**User Interaction**
- As a Site User I can view the number of likes on each recipe so that I can see which is the most popular
- As a Site User I can like or unlike a recipe so that I can interact with the content
- As a Site User I can leave comments on a recipe so that I can get involved in a conversation

**User Profile**
- As a Site User I can register an account so that I can interact with the community and manage my own recipes

**Recipe Management**
- As a Site User I can create, read, update and delete my recipes so that I can manage my content
- As a Site User I can view a paginated list of recipes so that easily select a recipe to view
- As a Site User I can click on a recipe so that I can read the full recipe

**User Stories not implemented**

The user Storie bellow were removed from the project due time was running short. The intentions are  to implement it in the future.
- As a Site User I can publish my recipes so that I can share my own recipes
- As a Site Admin I can approve or disapprove recipes so that I can moderate the content

### Design
With a minimalist and user-friendly interface, we have carefully crafted the design to ensure user can effortlessly navigate through the application and focus on what matters most: preparing a delicious and healthy lunch.

**-COLOUR SCHEME**

Color theme from Adobe Color

![Color Scheme Image](Docs/Readme_images/colour_palet.png)
 Carefully chosen a soothing color palette that complements our mission of making your lunchtime routine a stress-free and pleasant experience.
 There are strong contrast between background colors and text throughout our web application, ensuring maximum readability and usability for all users.
 
**-TYPOGRAPHY**
 
Google Fonts was used to import the chosen fonts below for use in the application.

CSS rules to specify families

font-family: 'Open Sans', sans-serif;

![Font Open Sans](Docs/Readme_images/font_open_san.png)

font-family: 'Oswald', sans-serif;

![Font Oswald](Docs/Readme_images/font_oswald.png)
        
**-IMAGERY**

All imagery used within the site has been chosen from [pexel](https://www.pexels.com) taken by the photographers bellow:

Photos by: 

- [Jess Ho](https://www.pexels.com/@jess-ho-51667983/)
- [Kaju](https://www.pexels.com/@kaju-102944731/)
- [Nicola Barts](https://www.pexels.com/@nicola-barts/)

The rest of the imagery will be uploaded by users for their individual recipes.

**-WIREFRAMES**

<details>
<summary>Landing Page</summary>

 ![Landing Page Frame](Docs/Readme_images/landing_page_wireframe.png))

</details>

<details>
<summary>My Book Page</summary>

 ![My Book Frame](Docs/Readme_images/my_book_wireframe.png)

</details>

<details>
<summary>Add Recipe Page</summary>

 ![Add Recipe Frame](Docs/Readme_images/add_recipe_wireframe.png)

</details>

## Agile Methodology

Github project was used to manage the development process of this project using an agile approach. 
Find the link to the Github project [here](https://github.com/users/Marcosmgs/projects/3/views/1) 

The  EFH Community User Stories is documented within the Github project. A Github issue was created for each user stories and allocated to the Project. 
The user stories were moved accordingly the application was been built.  

## Data Model

The views in this project have been organized into classes, following the OOP paradigm. 
Each class represents a specific action or behavior, allowing for clear and modular code structure.

To facilitate user interaction a comment feature was implemented using the Comment model. 
Each comment is associated with a particular recipe through a foreign key relationship to ensures that a comment can only be linked to one recipe.

[Django AllAuth](https://django-allauth.readthedocs.io/en/latest/) was used for user authentication. 
This powerful authentication system provides a seamless and secure user login and registration process, enhancing the overall user experience.

To enable users to create their own recipes, a Recipe model has been implemented. 
The author of each recipe is represented by a foreign key reference to the User model, ensuring that each recipe is associated with a single author.

Additionally a like model have implemented to allow users to express their appreciation for recipes in the inspiration section.

The diagram below details the database schema.

![ER Diagram Image](Docs/Readme_images/er_model_diagram.png)

Entity relationship diagram was created using [Lucid Chart](https://www.lucidchart.com/) shows the schemas for each of the models and how they are related.

## Credits

Code
* Code Institute for the Walkthrough Projects
* Tutorial on Hello [Django project](https://github.com/Code-Institute-Solutions/Django3blog) from Code Institute.
* Code Institute for the CI Python Linter used throughout the project at every stage of the building.
*  [AutoSlugField](https://django-extensions.readthedocs.io/en/latest/field_extensions.html)
* [StackOverflow ](https://stackoverflow.com/)

Content
* Recipes were taken from [BBC Good Food](https://www.bbcgoodfood.com/)

Media
* Code Institute for the README.md file tutorial.
* Code Institute for the project template CI Template
* Imagery on this site were taken from [Pexels](https://www.pexels.com/)

