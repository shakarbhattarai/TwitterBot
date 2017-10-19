import tweepy


CONSUMER_KEY = '###########'
CONSUMER_SECRET = '###########'
ACCESS_TOKEN = '###########'
ACCESS_TOKEN_SECRET = '###########'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


class MessageFollowers:
	
	def __init__(self,username,message):
		self.username=username #Your UserName 
		self.message=message #Message to tweet
		fg=open('testfile','w')
		fg.write("Executed once")
		fg.close()

	def checkSend(self):
		f=None
		try:
			f=open('latest_follower', 'r') # Get the user_id of the latest follower to whom message was sent.
		except:
			print "No file"
		
		
		if f==None:
			latest="123123123123"
		else:		
			latest=f.read().strip() 
	
		

		follower_ids= tweepy.Cursor(api.followers_ids, id = self.username).items(10)#Get the latest 10 followers(Hardcoded for now)
		first=''
		i=0
		for each_follower in follower_ids:
			
			if (i==0):
				first=each_follower
			
			if str(each_follower)==str(latest): #If the latest follower has already been messaged
				print "Updated"
				self.updateLatest(first)  #Add the name of the latest follower to external file
				return
			else:
				print "Sending message to",each_follower 
				self.sendMessage(each_follower)
			i=i+1
			
	 	self.updateLatest(first)  #Add the name of the latest follower to external file

	def sendMessage(self,follower):
		 api.send_direct_message(user_id=follower,text="Hello, "+api.get_user(follower).screen_name+"!! "+self.message)

	def updateLatest(self,follower):
		print follower
		f=open('latest_follower', 'w')
		#follower_ids= tweepy.Cursor(api.followers_ids, id = self.username).items(1)
		#for each_follower in follower_ids:
		f.write(str(follower))
		

a=MessageFollowers('shakarbhattarai'," Thank you for following me.I swear my tweets wont' disappoint you ;) ")
a.checkSend()
