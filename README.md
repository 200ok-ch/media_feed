                        _ _          __               _
     _ __ ___   ___  __| (_) __ _   / _| ___  ___  __| |
    | '_ ` _ \ / _ \/ _` | |/ _` | | |_ / _ \/ _ \/ _` |
    | | | | | |  __/ (_| | | (_| | |  _|  __/  __/ (_| |
    |_| |_| |_|\___|\__,_|_|\__,_| |_|  \___|\___|\__,_|

200ok media feed
================

The 200ok media feed is a podcast feed curated by the people at 200ok
and friends.


Prerequisites
-------------

The repo contains a bunch of ruby scripts (only depending on the ruby
standard library, so no need to install any gems) which might shell
out to external tools to facilitate generating a RSS feed based on
YAML data. Hence you need to have the following prerequisites in
place:

* ruby
* curl


Big Picture
-----------

### As a Curator

To add entries to the feed you will edit the YAML file `media.yml`
(either manually or with a provided script) and commit the changes to
the repo. This will trigger a pre commit hook, which will generate the
RSS feed in `feed.xml`.

### As a Consumer

The feed can be directly subscribed to on Github.(To quickly
subscribe from your phone scroll down for a QR code.)

### As a Commentator

As a commentator you may just edit or append to the field description
and add your personal comment.


Setup
-----

Clone the repo...

    git clone git@github.com:twohundredok/media_feed.git

After cloning the repo run setup to install the tracked pre commit
hook into your local repo

    cd media_feed
    ./setup.sh

Now you're all set.


Usage
-----

If you edit the file `media.yml` the pre commit hook will
regenerate the RSS feed in `feed.xml`.

You can edit the YAML file manually or use the provided sciprt `add`
to add a stub for a new entry.

Use `add` to add new entries to `media.yml`, e.g.

    ./add <url-to-media-file>

Then edit `media.yml` to complete missing details.

(Entries with the field `published` empty or missing are omitted when
generating the feed.)

The pre commit hook will update `feed.xml` automatically.

With the podcatcher of your choice subscribe to

    https://raw.githubusercontent.com/twohundredok/media_feed/master/feed.xml

![qrcode: subcribe to feed](https://raw.githubusercontent.com/twohundredok/media_feed/master/qrcode.png)


Under the hood
--------------

```
% tree
.
├── add                  - ruby script to add a new entry
├── annotations.org      - old index file, for reference only
├── build                - ruby script, which generates feed.xml from media.yml
├── feed.xml             - the rss feed
├── media_feed.png       - an image
├── media.yml            - the media index file in yaml
├── pre-commit           - git pre commit hook wrapper
├── qrcode.png           - the feed url to subscribe to as qr code
├── README.md            - this file
├── setup.sh             - setup shell script, to install (symlink) the git pre commit hook
└── template_rss.xml.erb - rss feed template file

0 directories, 11 files
```
