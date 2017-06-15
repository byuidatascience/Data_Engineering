#!/usr/bin/env python

import sys
import json

for line in sys.stdin:
    tcid = json.loads(line)
    entities = tcid.get("entities")
    if entities:
        for hashtag in entities.get("hashtags", []):
            print('{}\t{}'.format(hashtag.get("text"), 1))
