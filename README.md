# Instagram Giveaways

### About

Tired of doing all the work to follow, like, and comment over and over when you see giveaway posts on Instagram? I want to help you make entering these giveaways autonomously. 

**What do I gain from this**: better my programming skills in Python and learn basics of Selenium Webdriver

**What you gain from this**: my program aims to enter 5 giveaways in the time it takes for you to enter one giveaway manually, significantly increasing your chances at winning something nice for yourself.

### Initial Phase

Current Progress when Insta.py is run: 
* **chromedriver.exe** will open Chrome and go to Instagram Login Page
* Login with user and pass inputted into **credentials.py**
* Go to the inputted giveaway link
* Follow the user and like the post

### Considerations

Since using the Selenium route, I have found it rather slow for an implementation to do all the steps. If I can not get the speed up faster, I will consider switching my strategy up to a mobile app emulation route.

### Next Steps

* Need to add an if statement to follow the user only if they are not already following.
* Need to add comments that take friend's accounts from **mentions.txt** 
