                        _ _          __               _
     _ __ ___   ___  __| (_) __ _   / _| ___  ___  __| |
    | '_ ` _ \ / _ \/ _` | |/ _` | | |_ / _ \/ _ \/ _` |
    | | | | | |  __/ (_| | | (_| | |  _|  __/  __/ (_| |
    |_| |_| |_|\___|\__,_|_|\__,_| |_|  \___|\___|\__,_|

200ok media feed
================

The 200ok media feed is a podcast feed curated by the people at 200ok
and friends.

Setup
-----

Run once after cloning the repo to setup pre commit hook

    ./setup.sh


Usage
-----

Edit `media.yml` to add items to the feed.

Entries with the field `published` empty or missing are omitted when
generating the feed.

The pre commit hook will update `feed.xml` automatically.

Subscribe to

    https://raw.githubusercontent.com/twohundredok/media_feed/master/feed.xml

![qrcode: subcribe to feed](https://raw.githubusercontent.com/twohundredok/media_feed/master/qrcode.png)
