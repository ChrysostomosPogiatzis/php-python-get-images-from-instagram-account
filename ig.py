#!/usr/bin/env python3
import instaloader
import sys
import json
from instaloader import Profile, Post
sys.tracebacklimit=0
instance = instaloader.Instaloader()
if len(sys.argv) > 1:
    name = sys.argv[1]


profile = Profile.from_username(instance.context, username=name)
 
post_iterator = profile.get_posts()
i=0
a=[]
 
for post in post_iterator:
	if i >=9:
		break
	else:
        	#print(post.url)
        	
        	a.append(str(post)[6:-1])
        	i=i+1
print(json.dumps(a))
