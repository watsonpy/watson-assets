Usage
=====

In order to take advantage of the webpack integration with Watson, you must have
webpack installed, and have already generated the built JS/CSS.

Make the following changes to your applications configuration:

::

    views = {
        'renderers': {
            'jinja2': {
                'config': {
                    'environment': {
                        'extensions': ['watson.assets.webpack.jinja2.webpack']
                    }
                }
            },
        }
    }

    # These are the standard defaults
    assets = {
        'webpack': {
            'stats_file': 'webpack-stats.json',  # the path to the stats file relative to the root of the application
            'bundle_dir': ''  # specify where the outputted files are located at the root of the served application, e.g. /static
        }
    }

Within your HTML templates you can then call to output the relevant HTML tags.

::

    {% webpack bundle='main', type='css' %}

`bundle` defaults to main, but this can be changed to whatever your webpack is outputting.
`type` allows you to output only the files that match the specific extension, which is useful for outputting JS before the </body>, but CSS in the <head>.
