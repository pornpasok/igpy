
import subprocess
import json
import sys
from pprint import pprint

# Usage: python3 ig.py hashtag
#print (sys.argv)

if len(sys.argv) < 2:
    print("Usage: python3 "+sys.argv[0]+" hashtag") 
    exit(0)

tag = sys.argv[1]
#tag = "sookyenfarm"

#cmd = "curl --cookie cookies_ig.txt -s https://www.instagram.com/explore/tags/"+tag+"/ |awk -F'window._sharedData = ' '{print $2}' | awk -F';</script>' '{print $1}'"
cmd = "curl -s https://www.instagram.com/explore/tags/"+tag+"/ |awk -F'window._sharedData = ' '{print $2}' | awk -F';</script>' '{print $1}'"
result = subprocess.getoutput(cmd).strip() # Hook JSON From Instargram

#print (result)

#with open('ig_print.json') as f:
#    data = json.load(f)
#pprint(data)

data = json.loads(result)

# Total Hashtag
total = data["entry_data"]["TagPage"][0]["graphql"]["hashtag"]["edge_hashtag_to_media"]["count"]

for i in range(total):
	#print(i)

	# IG URL
	display_url = data["entry_data"]["TagPage"][0]["graphql"]["hashtag"]["edge_hashtag_to_media"]["edges"][i]["node"]["display_url"]
	#display_url = display_url.split("?")[0]
	print(i, display_url)

	# IG Text
	print(data["entry_data"]["TagPage"][0]["graphql"]["hashtag"]["edge_hashtag_to_media"]["edges"][i]["node"]["edge_media_to_caption"]["edges"][0]["node"]["text"])

	# taken_at_timestamp
	print(data["entry_data"]["TagPage"][0]["graphql"]["hashtag"]["edge_hashtag_to_media"]["edges"][i]["node"]["taken_at_timestamp"])

	# shortcode
	code = data["entry_data"]["TagPage"][0]["graphql"]["hashtag"]["edge_hashtag_to_media"]["edges"][i]["node"]["shortcode"]
	print(data["entry_data"]["TagPage"][0]["graphql"]["hashtag"]["edge_hashtag_to_media"]["edges"][i]["node"]["shortcode"])

	# User Profile
	cmd_user = "curl -s https://www.instagram.com/p/"+code+"/ |awk -F'window._sharedData = ' '{print $2}' | awk -F';</script>' '{print $1}'"
	result_user = subprocess.getoutput(cmd_user).strip() # Hook JSON From Instargram User
	#print(result_user)

	data_user = json.loads(result_user)
	username = data_user['entry_data']['PostPage'][0]['graphql']['shortcode_media']['owner']['username']
	profile_pic_url = data_user['entry_data']['PostPage'][0]['graphql']['shortcode_media']['owner']['profile_pic_url']
	#profile_pic_url = display_url.split("?")[0]
	
	if data_user['entry_data']['PostPage'][0]['graphql']['shortcode_media']['location'] is None:
		location_name = ""
	else:
		location_name = data_user['entry_data']['PostPage'][0]['graphql']['shortcode_media']['location']['name']

	print(username+" : "+location_name+" : "+profile_pic_url)


		



