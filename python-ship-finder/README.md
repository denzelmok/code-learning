# My Ship Tracking Adventure

Recently I ordered a package that was to be delivered by ship, and unfortunately the tracking information they provided was rather lacking in detail, containing only information up to the point where it departed the sorting facility to be boarded for shipping. Hence, I decided upon myself to track down where and when exactly the ship would arrive.

My first instinct was to obviously google search for any website and data that provided the location of ships.

![alt text](https://github.com/denzelmok/python-projects/blob/main/python-ship-finder/images/search.png)

I was happy to find that this was working pretty well, getting the information about ***all*** the ships that they had information on.
*Look at those colours.*

![alt text](https://github.com/denzelmok/python-projects/blob/main/python-ship-finder/images/map.png)

Now the one thing I found in common with these websites and was also the biggest obstruction to my quest, was the ~~annoying~~ business-sustaining paywall they had setup if you wanted to gain access to their detailed information.

Fortunately there was this one amazing site who although did not have all the records available, they had 10 days of Port arrival and departure data available, and I instantly knew this was the one, the one site where I could uncover which ship my package was to be boarded on.

Aaaaand here we are. ***702*** records with ***36*** pages of information, great.

![alt text](https://github.com/denzelmok/python-projects/blob/main/python-ship-finder/images/data.png)

My initial plan was, why not go through each vessel page by page? I know the vessel I'm looking for will probably be a cargo ship, so thats less work needed.

Away we go, clicking out ship after ship to find the one ship that would arrive in my country. *Ooooooh tabs.*

![alt text](https://github.com/denzelmok/python-projects/blob/main/python-ship-finder/images/tabs.png)

After a couple of pages of clicking away, developing arthritis and questioning the meaning of life, I thought to myself, didn't I learn to code so I could automate this stuff?

***Whooooosh!***

As if by magic, a Python script appeared before me, and I was *shocked* to find that:

![alt text](https://github.com/denzelmok/python-projects/blob/main/python-ship-finder/images/result.png)

***There were no cargo ships heading towards Australia!*** :sob:

Now this could mean a couple of things, either:
- the data did not go further back enough, as it has been quite a few days since my package has left their facility
- the package has not yet boarded a ship
- the ship might be heading to other destinations before arriving at Australia
- the package might be on the bulk carrier? *unlikely*
- ~~theres a bug in my script~~ **certainly not**

So, what do I do now that I've hit a dead end to my quest? Guess I'll just sitback and patiently wait for it to arrive like everyone else.
*For now that is* :smiling_imp:
