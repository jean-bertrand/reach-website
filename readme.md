# Reach Website
Landing pages and website for [Reach Vote app](https://github.com/ben-pr-p/reach-client).

# Installation

1.  Make sure you have [python](https://www.python.org/) installed
2.  If you don't have virtualenv installed, install it using `$ pip install virtualenv`
3.  Run `$ source venv/bin/activate`
4.  Install Flask library into this virtual environment `$ pip install flask`
5.  Install [Lektor](https://www.getlektor.com/docs/) static site management `$ pip install Lektor`


# Run
From the root directory run `$ lektor server` to start server

# Content
There are two ways to edit content on pages:
1. While the development server is running you can use the built-in admin interface. It can be accessed by clicking on the pencil symbol on a page or by manually navigating to `/admin/`

2. You can edit the content in the `/content` directory directly. Content files are in folders respective to each page. the `.contens.lr` file in `/content` root is content for the home page.

## Adding fields

If you want to define more specific content fiels to use in templates or components, you can define new fields in `/models`.

Fields defined in `.ini` model files will be visible and accessible when in Admin UI. More about data modeling for content [here](https://www.getlektor.com/docs/models/).

# Deployment
1.  From the root directory run `$ lektor build --output-path [PATH]`. Ideally path should be to a `dist` folder in the root directory.
2.  Run `$ Surge` from `dist` directory to domain: `reach-marketing.surge.sh`
