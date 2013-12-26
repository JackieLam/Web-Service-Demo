# -*- coding: utf-8 -*-
import pymongo

paper_info={
    "title":"Spoiler alert: Bill Gates did not get you, because he got me.",
    "detail":"Dec. 18, 2013 by NY1227, 139 comments , From: thisisbillgates | Secret Santa 2013",
    "content":"<p>I want to start by giving a HUGE THANK YOU to Mr. Bill Gates for an amazing gift and secret santa experience. Bill- you ROCK (can I call you Bill?! I feel like we're friends now!). I am so very, very grateful for the amazing and thoughtful gift you have picked for me! Not only is the gift PERFECT from anyone, but I am sincerely very appreciative that you took the time to find something so fitting for me. I asked for a return address to send a thank you card to whomever my \"Santa\" was. I see that you did not provide one so I hope this serves as a proper thank you. Regardless, I'd still love to send a personal thank you if you want to give me your mailing address!!</p><p>I did not realize my santa was Mr. Bill Gates himself until very far into this. Here's my \"journey\" of discovery, sorry for the length but I thought many might be interested.</p><p>My information got pulled about 3 days after elf matching was done. My santa had not messaged me, but I knew I was super thorough and have a pretty good posting history so I wasn't too worried that my santa would stiff me. Finally, I received a shipped notification to my email on Monday- I was SO SO SO excited but even more excited when I realized A) my gift was being OVERNIGHTED and B) it was 7 pounds- OMG!</p><p>Of course life is life and I wasn't able to get to the gift until this evening (Wednesday night). I decided to document my journey, starting with the box. The first thing I noticed was a stuffed animal. I didn't know I gave off the stuffed animal vibe, but I excitedly added him to my collection of teddy bears and other delightful friendly creatures. Next, I found the card. Next, I found the card. To me, from Bill. This still had not clicked, by the way, that it was Bill Gates.</p><p>I thought Bill sounded like a friendly fellow. In fact, I had this whole image of this poor guy named Bill trying to navigate my wishlist full of makeup, nailpolish, glittery things to buy me. Quite frankly I felt bad for this \"Bill\" since I'm a self identified pain in the ass to shop for. I finally opened the card and realized that \"Bill\" (I use quotes, because like I said, I still didn't realize that this was THE Bill) had donated to a charity on my behalf.</p><p>The charity was/is Heifner International. I took a break from my present to research the charity a bit, and now the stuffed animal cow made sense. I was so excited, the cause seemed really worthy and amazing, and it is the season of giving. By the way, the charity \"gives families in need the right tools- such as animals, seeds, clean water, safe stoves or a chance for girls to go to school.\" The last part was/is my favorite, since my master's degree is in education and I am SO into educational benefits for all. It makes me so happy that he was able to donate to a charity on my behalf that helped people with both needs and educational benefits. Nailed it, Bill!</p><p>By the way, in case anyone was being nosy it does not say how much he donated to my behalf, but I can only imagine it was QUITE a bit.</p><p>But I digress, back to the gift. Still not realizing who was gifting me, I quickly opened the bulk and weight of the gift, which was an amazing and beautiful travel book, \"Journeys of a lifetime.\" I went on and on in my likes and dislikes for my love of travel and seeing the world, and I cannot WAIT to read this. Not only that, but I love pictures and reading up on new places. This gift was perfect! I quickly flipped through it, missing the inscription, message and signature from Bill on the first page, and headed to the final part of my gift.</p><p>Once again, To me, From Bill. I opened this and it's a man holding a sign. Oh....</p><p>wait.</p><p>holy shit.</p><p>time out.</p><p>and then it finally hit me. All the presents I just tore open, the charity, then everything-- was from Bill GATES. I quickly went back to the book to see a really nice message and note from Bill wishing me a Merry Christmas and a Happy Birthday (not pictured, because I really want to keep one part of this gift to myself) my jaw hit the EVER LOVING FLOOR. I went back to all the other gifts completely shocked. Then I paused for a minute and thought, what if this is someone screwing with me. Well of course Mr. Bill Gates already thought of this and took a picture of himself with my stuffed animal and a sign and then sent me the stuffed animal and sign.</p><p>My god. Never in my entire life did I imagine, ever, ever, ever that Bill would get me. I am SO SO thankful for the time, thought and energy he put into my gift, and especially thankful for him over nighting it :)</p><p>I feel SO shocked and excited that not only did I receive a gift from Bill, but it was perfectly and EXACTLY tuned into my interests. My gosh, what a rush!! I cannot express how much I really loved reading about a new charity. By the way everyone, you should go donate too! http://www.heifer.org/</p><p>Thank you so much Bill for a fantastic and thoughtful gift. I'd really love to send a thank you card to you, but if not, I hope this post and message suffices. Thank you so much!!!!!! I will think of you every time I read my book, which will find a nice home on my coffee table once I'm done reading it.</p><p>10/10 would receive gift from Bill Gates again</p><p>ps: Sorry for the apple ipad on my wishlist, that was really awkward.</p><p>EDIT: I just got home to see this exploded on the news. To everyone requesting interviews with me, I appreciate the thought but I'm not really looking to exploit this into publicity. I've described my gift, my reactions, and my feelings as best as I can through my post and comments. There is really nothing left for me to say, except privately to Bill (I really hope I can call him that), which I have attempted to do. Merry Christmas!</p>",
    "comment":[
    {"name":"talula79",
     "time":"Dec. 18, 2013",
     "content":"How cool is that? I asked him to pay off my student loans if he got me. I guess that is a no go now. ;-)"},
    {"name":"ltrem",
     "time":"Dec. 18, 2013",
     "content":"holy wow!!"},
    {"name":"mrefish",
     "time":"Dec. 18, 2013",
     "content":"Thank you for sharing your experience! It was a fun read :)"},
    {"name":"Semebay",
     "time":"Dec. 18, 2013",
     "content":"I laughed really hard at that. Those are wonderful gifts, and you are an awesome receiver! Very entertaining experience :)"},
    {"name":"Acaelia",
     "time":"Dec. 18, 2013",
     "content":"That is amazing! The picture alone is worth it!!"}
    ]
}

def importData():
    infoDB.remove()
    infoDB.insert(paper_info)

def valid():
    for info in infoDB.find():
        print info

conn=pymongo.Connection("localhost",27017)
db=conn["paperDB"]
infoDB=db.infoDB
importData()
valid()
