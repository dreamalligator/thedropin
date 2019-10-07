#!/usr/bin/env python

"""
update semver and tag for release.

perform ``chmod +x ./release.py`` to make executable.

usage:

    interactive mode:

        python release.py

        or

        ./release.py

    direct mode:

        python release.py 0.1.13

        or

        ./release.py 0.1.13

"""

from pelican_plugin_template.release import update_version_and_tag_for_release

if __name__ == '__main__':
    update_version_and_tag_for_release()
