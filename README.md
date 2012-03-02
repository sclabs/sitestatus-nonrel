sitestatus
===========

_Improved status page app built on django-nonrel for easy deployment to the Google App Engine._

Introduction
------------

sitestatus is an experimental web application that you can use to create a dynamic, self-updating status page for your domain or any arbitrary collection of sites you might want to track the status of.

Prerequisites
-------------

- [Python 2.x](http://python.org/)
- [Google App Engine SDK for Python](http://code.google.com/appengine/downloads.html#Google_App_Engine_SDK_for_Python)

Installation
------------

Make sure you have the prerequisites listed above installed. Next, [download the latest version of sitestatus](https://github.com/sclabs/sitestatus/zipball/master). Unzip the archive to any directory on your file system.

Alternatively, you can clone the git repository by executing

    git clone git://github.com/sclabs/sitestatus.git

Feel free to fork the repository and develop your own tweaks and features under the conditions of the license (see below).

Quick-Start (in Eight Easy Steps)
--------------------------------

1. Go to [appengine.google.com](http://appengine.google.com), log in with your Google Account, and follow the instructions to enable Google App Engine for your account (if you haven't done so already).
2. Create a new app, and remember your app's application identifier.
3. In `app.yaml`, replace `myapp` with the application identifier for your app.
4. In `settings.py`, change `SITE_TITLE` from 'My Awesome Status Page' to whatever you actually want to call your site.
5. Run `python manage.py deploy` and authenticate with your Google Account when prompted.
6. Run `python manage.py remote createsuperuser` to create a superuser for yourself.
7. Point your browser to <http://your_application_identifier.appspot.com/update/>
8. Change the example status entry from the Datastore Viewer in your application's Google App Engine dashboard to whatever site you want to track.

It's that simple! Point your browser to <http://your_application_identifier.appspot.com> to see your status page!

Notes
-----

### Update Types

sitestatus features four different ways to check the status of any given site, which you can change by modifying the `update_type` property of the site you want to change in the Datastore Viewer. These are:

1. `none` - This is the default update type, which causes the update mechanism to ignore this site and never update its status. Use this for custom statuses like "coming soon", etc.
2. `status` - This is probably the update type you will use most. It tells the update mechanism to send a request to the url in `update_url`. If the response has a status code of `200 OK`, the status will be updated to "online". Otherwise, it will be updated to "offline".
3. `title` - This update type looks at the title of the webpage at `update_url` and checks to see if it contains the string in `update_title`.
4. `content` - This update type looks at the entire content of the HTTP response returned by the site at `update_url` and checks to see if it contains the string in `update_content`.

Next Steps
----------

### Domain Setup

If you have a domain you'd like to host your webcomic on, you can add a domain to your app by going to the Application Settings page on your Google App Engine dashboard.

### Site Themes

The templates directory contains a bare-bones example template (`index.html`) that you should feel free to modify and style however you like. If you want to add CSS, Javascript, or other static files, remember to add the appropriate file or directory handlers in `app.yaml`.

### Need Help?

For more information visit <http://sitestatus.gilgi.org>. Direct all questions, comments, and bug reports to <sclabs@gilgi.org>.

License Information
-------------------

sitestatus-nonrel is released under the terms of the GNU General Public License, the full text of which is available in `GPL`. For details, please visit <http://www.gnu.org/licenses/gpl.html>.

Modules from the django-nonrel project are redistributed under the terms of the license found in `LICENSE`.