# Overview

Data Viz / Analysis of Google's Garden.  (well at least the part that didn't make it)

Multiple efforts documenting the death of a crop:

* [https://killedbygoogle.com/]() (my json src)
* [https://gcemetery.co/]()

# Process

Took [Google Charts simple example](https://developers.google.com/chart/interactive/docs/gallery/timeline#a-simple-example)
to create jinja template.

Modified [graveyard.json](graveyard.json) as I could not figure out how to pass an "anonymous" list to jinja.

`jinjajson` just pushes a "json.load" python data structure through a [jinja template](goograve2gchart_tline.j2)

`jinjajson goograve2gchart_tline.j2 graveyard.json > goograve.html` for the final result [goograve.html](https://kevbroch.github.io/goograve/)
