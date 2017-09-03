#Objective: Retrieve the highest post of all NBA subreddits
#reddit.multireddit('samuraisam', 'programming').top('day')


import praw

reddit = praw.Reddit(client_id='7jkM23RwIf9oJw',
                     client_secret='TMtgItAKVYB8YaBlqzImRu3ICrc',
                     password='richard',
                     user_agent='testscript by /u/hellorichardpham',
                     username='hellorichardpham')

print(reddit.user.me())


# subreddit = reddit.multireddit('kings', 
# 	'warriors', 
# 	'chicagobulls', 
# 	'torontoraptors' ,
# 	'bostonceltics' ,
# 	'clevelandcavs' , 
# 	'nyknicks', 
# 	'nbaspurs')

subreddit = reddit.subreddit('kings').top('day', limit = 1)

# print(vars(subreddit))

for submission in subreddit:
	print(submission.title)

