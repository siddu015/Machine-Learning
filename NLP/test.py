import nltk

from nltk.book import *


raw = """
Hey there! I’ve been thinking a lot lately about all the amazing moments we’ve shared, and I just wanted to take a moment to appreciate how much you mean to me. Life gets so busy sometimes, and it’s easy to get caught up in the whirlwind of responsibilities and deadlines, but when I pause and reflect, I realize how fortunate I am to have someone like you in my life. Whether we’re chatting about our day, sharing a good laugh, or simply being there for each other during tough times, it all adds up to something really special.

You know, it’s funny how we sometimes take the little things for granted. Like those spontaneous conversations that somehow turn into deep, meaningful discussions, or those moments of silence that are so comfortable because we’re just in sync. I love that we can talk about anything, from the most random topics to the stuff that really matters. It’s rare to find that kind of connection, and I’m grateful for it every single day.

I’ve been thinking about some of our plans, too. Remember that trip we talked about? I’m really excited to make that happen. I think it’ll be an adventure we’ll both cherish for years to come. There’s so much to explore, and I can’t wait to experience it all with you. Whether it’s discovering a new place, trying out some local food, or just soaking in the scenery, I know it’ll be unforgettable.

And speaking of adventures, life itself is one big journey, isn’t it? We’ve had our ups and downs, but I wouldn’t trade any of it. Every challenge we’ve faced has only made us stronger, and every joy we’ve shared has made our bond even deeper. It’s comforting to know that no matter what comes our way, we’ll face it together. I really believe that we bring out the best in each other, and that’s something truly special.

I also want you to know how much I admire your resilience and positivity. You have this incredible ability to stay hopeful, even when things get tough, and it’s so inspiring. There have been times when I’ve felt overwhelmed, and just hearing your voice or getting a message from you has lifted my spirits. You have a way of making everything seem a little brighter, and I can’t tell you how much that means to me.

Sometimes I wonder if I say it enough, but I really do appreciate you. Not just for the big things, but for all the little things you do that make a difference in my life. Your kindness, your thoughtfulness, and your genuine care for the people around you are qualities I truly admire. It’s not every day that you meet someone who makes you feel seen, heard, and valued, and I feel so lucky to have found that in you.

So, here’s to us and to all the good times ahead. I’m looking forward to all the laughter, the memories, and even the challenges, because I know we’ll get through them together. You’re an incredible person, and I’m so glad we crossed paths. Let’s keep making the most of this journey, one day at a time, and never lose sight of the amazing connection we have. Thanks for being you, and for being such an important part of my life. Can’t wait to see what the future holds for us!
"""

tokens = nltk.word_tokenize(raw)
text = nltk.Text(tokens)
fd = FreqDist(text)
print(fd.most_common(10))
fd.plot()


