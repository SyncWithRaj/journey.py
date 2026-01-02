import arrow

brewing_time = arrow.utcnow()
brewing_time.to("Europe/Rome")

#Collection in python (Google it)

from collections import namedtuple
chaiProfile = namedtuple("chaiProfile", ["flavor", "aroma"])

