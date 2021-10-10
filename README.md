# Halo Pizza

# Project overview
This app serves to provide a space where users can log in to share their pizza recipes, view other users' submitted recipes, and edit recipes they have submitted. The site requires users to log in to submit and edit recipes, and features authentication to securely facilitate this.

## User stories
### A visitor to the site will want to:
1. Browse pizza recipes and ideas.
2. Upload their own recipes for others to see.
3. Edit their submitted recipes.
4. Delete their submitted recipes.
5. Register with the site to submit recipes.
6. View recipes without having to register for the site or log in.

### A site owner will want to:
1. Create themed collections of recipes.
2. Edit recipe collections.
3. Delete recipe collections.
4. Review the details of user-submitted recipes so as to determine their place in collections.
5. Promote their own or selected users' recipes.

---

# Deployment
 Here I'll explain how to deploy/how I deployed the website to GitHub and how to run it locally. 

## Deploying a static project to GitHub pages:
 1. You'll need a GitHub account, if you don't already have one. Head to their site https://github.com and you'll see the sign-up links straightaway on the home page. Google Chrome is the recommended browser for GitHub.
 2. Once you're signed-up, this'll be your landing page.
 3. Click on the user icon in the top right corner of the screen. This opens a dropdown menu. Click "Your repositories."
 4. You'll then see a list of your repositories.
 5. In the list of repositories, click the repository you want - in this case, Halo Pizza.
 6. Then, from the bar along the top (not the nav bar - lower, under the repo name) click Settings.
 7. On the Settings page, click "Pages" from the left-hand menu.
 8. In the Pages options, before you've deployed, your "Branch" under "Source" will have a default value of none. Click this, then set it to Main or Master depending on the version you're using. Mine, having been already deployed, says Master and yours will too when deployed, but ignore that discrepancy for now.
 9. Click Save.
 10. The page will refresh, and you'll see it change to say "Your site is ready to be deployed at "https://username.github.io/repository-name/"
 11. Be aware this deployed site will take a few minutes to deploy, usually about ten. Be patient and don't click while it's building as that can slow it down.
 12. Click the link to make sure it works after a suitable wait. Et voila, you've deployed the site!

### Forking the repository for your own use
This creates a copy of the repository for editing or viewing without affecting my (original) version. If you want to do it, do this:
1. You'll need a GitHub account. Go to https://github.com to make one.
2. Locate the repository (this one). At the top right of the page, beneath my pink and white avatar, you'll see the Fork button. Click it.
3. This should add a version for you to use in your own repository. Have fun with it!

### Cloning the repository
Another way of getting your own local version to work on is to clone the repository. Below are the steps.
1. You'll need a GitHub account. Go to https://github.com to make one.
2. Locate the repository (this one).
3. Click Code, the button just to the left of the green GitPod button.
4. Click HTTPS to make sure you're in it, then copy the link you see there.
6. Head into GitPod or your IDE of choice, and open up the terminal.
5. Switch your working directory to the location you want to the cloned directory created.
6. Then you want to type "git clone https://github.com/James-VT/MS3_Halo_Pizza", the same URL as before.
7. Hit Enter. You're good to go!

## Deploying to Heroku:
Heroku allows us to host Python projects, instead of merely static sites which are all GitHub allows.
### Create your Heroku app
1. Make an account with Heroku, if you don't already have one, here: https://www.heroku.com/
2. After setting your password and/or logging in, you'll find yourself looking at the Heroku dashboard.
3. You can click your chosen development language for some helpful tips and tutorials about how to use it with Heroku, if that'd help you.
4. From the dashboard, click "Create new app."
5. Enter a name for your app. It must be unique, and contain only letters, numbers and hyphens.
6. Choose a region. In our case, Europe.
7. Click "Create app."
8. Return to your development environment and type, in the terminal "npm install -g heroku"
9. npm is an abbreviation of "Node Package Manager" and "-g" tells the console that this will be a global installation.
10. You can now log in to heroku via the CLI at any time by typing heroku login -i and entering your credentials.
11. You can now click "Open app" on your app's page on heroku to confirm that your app is up and running. Congratulations!

### Connect your Git repository to Heroku
1. Head back to your app's page on the Heroku dashboard.
2. Click settings.
3. Grab the Heroku git URL
4. In the console, type "git remote add [your choice of name here; I went with heroku] [your Heroku git url here]".
5. To make sure this has worked, you can then type "git remote -v" to view what should now be both your git remotes and your heroku ones.

### Create your "requirements.txt" file
1. Heroku uses this to detect which language we're using, and our dependencies.
2. The way to create the requirements.txt file is to type, in the console: pip3 freeze --local > requirements.txt
3. Wait for Heroku to install what it needs. After this, it will now be deployed to Heroku, but if you try to open it there now, you'll see an error. There's one more thing to do.

### Create your Heroku "Procfile"
1. A Procfile is a specific file Heroku needs in order to know how to run our project.
2. To create it, redirect an echo command by typing "echo web: python run.py > Procfile". The capital P is crucial.
3. git add this, commit it, and finally git push it.
4. Well done!

### Set up your env.py file for your environment variables.
1. Make sure you create a .gitignore file if you haven't already, and add the file you'll use for your environment variables into it.
2. The convention for the file holding your environment variables is env.py
3. In env.py, you can place your IP, PORT, any secret keys etc.
4. Crucially, you can also set up the links between your project and MongoDB here as well, by adding the key-value pairs to connect to your Mongo database. Make sure you've installed flask-pymongo and dnspython to allow your Flask application to work with MongoDB.

### Enter your environment variables into Heroku's config vars.
1. On your project's Heroku page, go to settings and scroll down to "config vars"
2. Here you can add the information in your env.py file to your Heroku project. The reason you need to do this is that your env.py file, which is listed in your .gitignore, is not pushed to Heroku or GitHub. As such, Heroku does not have access to the information contained within it, which is vital to the running of the project.
3. Add those environment variables in config vars as key-value pairs.
4. You should now be able to open your project via the "Open app" button.

---
