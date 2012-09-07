apps-extension-doc-updates
==========================

Scripts to check for apps and extension doc updates. 
The ultimate goal is to create a file which lists the latest changes
to each apps and extension api, hopefully cleaned up a bit so only content of interest
is saved to the file, and in a way that is somewhat readable.

<h3>api-page.py</h3>
This script writes the 'Index of /trunk/src/chrome/common/extensions/api (filtered by revision downward)
to a file called apiPage.html. The latest changes made to each app and extension is displayed on this page.