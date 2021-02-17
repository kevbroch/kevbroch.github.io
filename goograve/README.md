# Google Graveyard

Data Viz / Analysis of Google's Garden.  (well at least the part that didn't make it)

Multiple efforts documenting the death of a crop:

* [https://killedbygoogle.com/](https://killedbygoogle.com/) (my json src)
* [https://gcemetery.co/](https://gcemetery.co/)

## Process

Took [Google Charts simple example](https://developers.google.com/chart/interactive/docs/gallery/timeline#a-simple-example)
to create jinja template.

Jinja template and reading JSON from URL all embedded in single script: [gen_goograve_timeline.py](gen_goograve_timeline.py)

Run `python3 gen_goograve_timeline.py > goograve.html` and the final result is here: [goograve.html](https://kevbroch.github.io/goograve/)
