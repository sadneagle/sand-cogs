import discord
from discord.ext import commands
from random import randint
from random import choice as randchoice
import re


class Alot:
    """Gives your server invite link to the alots and automatically 
    @mentions them whenever you say their names"""

    # TODO: put data into data file
    # turn on per channel
    

    def __init__(self,bot):
        self.bot = bot
        self.numAlotted = 0
        self.alotOfAvatar = "http://static.tvtropes.org/pmwiki/pub/images/alot2258.jpg"
        self.alotTags = {
            "cake":["cake"],
            "frosting":["cake"],
            "carb":["cake","cookies-love","cookies","cookies-eat","pizza-tin","beer","eat"],
            "pastry":["cake","cookies-eat"],
            "sugar":["cake","cookies-love","cookies","cookies-eat"],
            "sweet":["cake","cookies-love","cookies","cookies-eat"],
            "food":["cake","bacon","eat","cookies-love","cookies","cookies-eat","pizza-tin","spam","pizza","oatmeal"],
            "delicious":["cake","bacon","cookies","cookies-love","cookies-eat","pizza-tin","spam","pizza","oatmeal"],
            "tast":["cake","bacon","cookies-love","cookies-eat","pizza-tin","spam","oatmeal","eat"],
            "word":["words","fonts","comments","paper","code"],
            "letter":["words","fonts"],
            "font":["fonts"],
            "type":["fonts","comments"],
            "ink":["fonts","words","paper","paint"],
            "thought":["fonts","science","questions"],
            "think":["fonts","science","questions","care"],
            "post":["comments"],
            "comment":["comments"],
            "reply":["comments"],
            "reddit":["comments"],
            "thread":["comments","code-ROS"],
            "water":["snow","grief","beer","swim"],
            "wet":["swim"],
            "moist":["swim"],
            "blue":["cookies-love","beer","ice"],
            "green":["money-made","money","christmas-like-tree"],
            "chocolate":["cookies"],
            "white":["snow","mist","ice"],
            "red":["fire"],
            "orange":["fire"],
            "yellow":["fire"],
            "light":["christmas-like-tree"],
            "cookies":["cookies-love","cookies","cookies-eat"],
            "dough":["cookies","money","money-made"],
            "eat":["eat","cookies-eat"],
            "ate":["eat","cookies-eat"],
            "snack":["eat","cookies-eat","cookies-love","cookies","bacon","pizza"],
            "love":["love-you","care","like-more","cookies-love","pizza-tin","happiness","thanks"],
            "like":["like-more","love-you","care","cookies-love","christmas-like-tree","happiness","thanks"],
            "card":["heart-card"],
            "heart":["heart-card","love-you","care"],
            "science":["science"],
            "chemistry":["science"],
            "fur":["plush-left","paint","plush-right"],
            "fluff":["plush-left","plush-right"],
            "plush":["plush-right","plush-left"],
            "doll":["plush-right","plush-left"],
            "stuff":["plush-left","plush-right"],
            "nerve":["nerve"],
            "christ":["christmas-like"],
            "pizza":["pizza-tin","pizza"],
            "cheese":["pizza-tin","pizza"],
            "meat":["pizza-tin","bacon","spam","pizza"],
            "spam":["spam"],
            "patch":["patches","code-ROS"],
            "quite":["quite","gentleman"],
            "gentle":["gentleman","quite"],
            "fancy":["gentleman","oatmeal","quite"],
            "sir":["gentleman","oatmeal","quite"],
            "mr":["gentleman","oatmeal","quite"],
            "ros":["code-ROS"],
            "code":["code-ROS","patches","code"],
            "line":["code-ROS","words","code"],
            "question":["questions"],
            "ask":["questions"],
            "hero":["avengers"],
            "aveng":["avengers"],
            "costume":["avengers","oatmeal"],
            "cosplay":["avengers","oatmeal"],
            "people":["people"],
            "person":["people"],
            "leg":["people"],
            "pant":["people"],
            "hug":["love-you","care"],
            "paper":["paper","money-made","money"],
            "writ":["paper"],
            "essay":["paper"],
            "time":["time"],
            "late":["time","work"],
            "watch":["time"],
            "money":["money-made","money"],
            "cash":["money-made","money"],
            "buck":["money-made","money"],
            "dollar":["money-made","money"],
            "euro":["money-made","money"],
            "yen":["money-made","money"],
            "discord":["discord"],
            "monster":["discord","cookies-love","paint"],
            "creature":["discord","cookies-love","paint"],
            "mob":["discord","cookies-love"],
            "snow":["snow","ice"],
            "cold":["snow","mist","ice"],
            "ice":["snow","ice"],
            "froz":["snow","ice"],
            "freez":["snow","ice"],
            "paint":["paint","art"],
            "draw":["paint"],
            "art":["paint","art"],
            "christmas":["christmas-like-tree"],
            "xmas":["christmas-like-tree"],
            "tree":["christmas-like-tree"],
            "leave":["christmas-like-tree","straw"],
            "leaf":["christmas-like-tree","straw"],
            "santa":["christmas-like-tree"],
            "oatmeal":["oatmeal"],
            "comic":["oatmeal"],
            "cartoon":["oatmeal"],
            "manga":["oatmeal"],
            "anime":["oatmeal"],
            "happ":["happiness"],
            "smil":["happiness"],
            "joy":["happiness"],
            "thank":["thanks"],
            "grief":["grief","sad-i'm"],
            "sad":["grief","sad-i'm","work","sad"],
            "cry":["grief","sad-i'm"],
            "tear":["grief","sad-i'm","sad"],
            "work":["work"],
            "errand":["work"],
            "job":["work"],
            "busy":["work"],
            "busi":["work"],
            "yell":["yell","hear","charge"],
            "scream":["yell","hear","charge"],
            "loud":["yell","hear"],
            "talk":["yell","sad-i'm","hear"],
            "say":["yell","sad-i'm","hear"],
            "bacon":["bacon"],
            "pork":["bacon"],
            "grease":["bacon"],
            "oil":["bacon"],
            "care":["care","like-more","love-you"],
            "fire":["fire"],
            "hot":["fire"],
            "heat":["fire"],
            "cook":["fire","cookies-love","cookies","cookies-eat"],
            "burn":["fire"],
            "mist":["mist"],
            "air":["mist"],
            "fog":["mist"],
            "straw":["straw"],
            "hay":["straw"],
            "grass":["straw"],
            "beer":["beer"],
            "can":["beer"],
            "alcohol":["beer"],
            "drunk":["beer"],
            "booz":["beer"],
            "boose":["beer"],
            "drink":["beer"],
            "metal":["beer"],
            "charge":["charge"],
            "attack":["charge"],
            "hit":["charge"],
            "mad":["charge"],
            "see this":["sad"],
            "see that":["sad"],
            "see":["sad"],
            "hear":["hear"],
            "more":["like-more","danger-more"],
            "danger":["danger-more"],
            "scar":["danger-more"],
            "swim":["swim"],
            "better":["swim","better"],
            "alot":["alot"],
            "worse":["better"],
            "dark":["art"],
            "evil":["art"],
            "night":["art"],
            "egg":["eggs"],
            "dairy":["eggs"],
            "skate":["ice"],
            "hockey":["ice"],
            "that is":["that"],
            "that's":["that"],
            "this is":["that"]
            }
        self.alots = {
            "cake":"http://3.bp.blogspot.com/-n4Ew70HYS-0/T7BFQSwLmfI/AAAAAAAAAb0/KRxgEatkUgs/s1600/IMG_0689.JPG",
            "words":"https://foodandfocalpoints.files.wordpress.com/2012/02/alot-finished.jpg",
            "fonts":"http://api.ning.com/files/bP8OOwWYBe5qRip7KL46YbuFp5oncdysF*CHujgVWzRaenvvHhwphzdIf5Zit0ZzBOQTKiOzsrGR3Nc2*DO1Spbrgo*kfi*M/AllotWords.png",
            "comments":"http://i.imgur.com/P4YdE.png",
            "cookies-love":"http://i0.kym-cdn.com/photos/images/facebook/000/177/345/CookieMonster_ALOT.jpg",
            "cookies":"http://t00.deviantart.net/Cief8fYhSZQUh9ThGRZOSwsQJko=/300x200/filters:fixed_height(100,100):origin()/pre03/50a7/th/pre/i/2014/009/e/3/alot_of_cookies_by_thecanadianalligator-d71jqk0.png",
            "cookies-eat":"http://img02.deviantart.net/2d02/i/2012/009/a/4/i_eat_alot_of_cookies_by_muffindynasty-d4lw6lb.jpg",
            "heart-card":"http://imgfave-chat-herokuapp-com.global.ssl.fastly.net/image_cache/1411139814292536.png",
            "science":"https://s-media-cache-ak0.pinimg.com/236x/d8/f7/8f/d8f78f13cfd492df4215ebbd0449d997.jpg",
            "plush-left":"https://edit911.com/wp-content/uploads/2013/07/92d0950a87cf2564d2d4783785bd367c.jpg?cbf00e",
            "nerve":"https://b.thumbs.redditmedia.com/d0nfPJ4jE5JPIKgAtAGl5m4bYUJYc5gYAsOa2CC3qng.jpg",
            "christmas-like":"https://s-media-cache-ak0.pinimg.com/236x/34/8c/7e/348c7eb4c6b1b7c658ae6d25eb6b1cd0.jpg",
            "pizza-tin":"http://img.pandawhale.com/post-12967-My-friends-made-alot-of-pizza-oanS.jpeg",
            "spam":"http://mentalfloss.com/sites/default/legacy/blogs/wp-content/uploads/2011/02/550_alotspam.jpg",
            "patches":"http://i0.kym-cdn.com/photos/images/facebook/000/177/007/alot-of-patches.jpg",
            "gentleman":"http://cdn0.dailydot.com/cache/51/95/51950010b596348543008ad9019a2ae6.jpg",
            "code-ROS":"http://odestcj.net/wp-content/uploads/2012/02/ros_alot-300x168.png",
            "questions":"http://orig00.deviantart.net/68b1/f/2010/162/3/7/alot_of_questions_by_vineris.png",
            "avengers":"http://img06.deviantart.net/46d2/i/2012/152/7/8/alot_of_avengers_by_sophistikit-d51utvw.jpg",
            "people":"http://i.imgur.com/RYH9UdG.png",
            "love-you":"http://pre13.deviantart.net/62db/th/pre/f/2011/228/b/4/i_love_u_alot_by_sylvacoer-d46t4fh.jpg",
            "paper":"http://img03.deviantart.net/2079/i/2011/268/1/9/alot_of_paper_by_trueflyingsheep-d4avx5z.png",
            "time":"http://static2.fjcdn.com/thumbnails/comments/5025882+_fff5ab1d9cad77f97ced41e9c40d99c1.jpg",
            "discord":"http://s3.amazonaws.com/kym-assets/photos/images/newsfeed/000/176/370/rERSq.png?1316564220",
            "pizza":"http://static.fjcdn.com/pictures/Alot+of+pizza+been+a+fjer+for+a+while+but_484831_4827732.png",
            "money-made":"http://slimber.com/gallery/images2/8/84609/alot-of-cash.jpg",
            "snow":"http://i.imgur.com/7M4Xz.jpg",
            "money":"http://i.imgur.com/D0HkOzo.jpg",
            "paint":"http://img00.deviantart.net/3db7/i/2012/102/3/1/somewhat_realistic_alot_by_foxwolf333-d4vxkry.png",
            "christmas-like-tree":"http://img03.deviantart.net/f62e/i/2011/356/c/f/i_like_christmas_alot_by_alandra_noir-d4jvgsv.png",
            "oatmeal":"http://s3.amazonaws.com/theoatmeal-img/comics/oatmeal_day/alot.png",
            "plush-right":"http://media1.fdncms.com/chicago/imager/who-wants-to-own-alot/u/original/5189227/1323898246-alotmonster03.jpg",
            "code":"http://i.imgur.com/2fx07oA.png",
            "happiness":"http://archive.garron.us/img/2010/alot_of_happiness.png",
            "thanks":"http://i.imgur.com/2GlMqob.png",
            "grief":"http://oi55.tinypic.com/20ru0j9.jpg",
            "work":"http://i.imgur.com/Jw9HBLA.png",
            "yell":"https://pbs.twimg.com/profile_images/1771177754/alot_400x400.png",
            "bacon":"http://i.imgur.com/KLeYo.jpg",
            "original":"http://4.bp.blogspot.com/_D_Z-D2tzi14/S8TRIo4br3I/AAAAAAAACv4/Zh7_GcMlRKo/s1600/ALOT.png",
            "care":"http://3.bp.blogspot.com/_D_Z-D2tzi14/S8TTPQCPA6I/AAAAAAAACwA/ZHZH-Bi8OmI/s1600/ALOT2.png",
            "fire":"http://3.bp.blogspot.com/_D_Z-D2tzi14/S8TWUJ0APWI/AAAAAAAACwI/014KRxexoQ0/s1600/ALOT3.png",
            "mist":"http://3.bp.blogspot.com/_D_Z-D2tzi14/S8TWtWhXOfI/AAAAAAAACwQ/vCeUMPnMXno/s1600/ALOT9.png",
            "straw":"http://3.bp.blogspot.com/_D_Z-D2tzi14/S8TW0Y2bL_I/AAAAAAAACwY/MGdywFA2tbg/s1600/ALOT8.png",
            "beer":"http://1.bp.blogspot.com/_D_Z-D2tzi14/S8TZcKXqR-I/AAAAAAAACwg/F7AqxDrPjhg/s1600/ALOT13.png",
            "sad-i'm":"http://2.bp.blogspot.com/_D_Z-D2tzi14/S8Tdnn-NE0I/AAAAAAAACww/khYjZePN50Y/s1600/ALOT4.png",
            "sad":"http://orig06.deviantart.net/023c/f/2011/086/4/f/i_see_this_alot_by_pythosblaze-d3clwo8.png",
            "charge":"http://4.bp.blogspot.com/_D_Z-D2tzi14/S8TfVzrqKDI/AAAAAAAACw4/AaBFBmKK3SA/s1600/ALOT5.png",
            "hear":"http://2.bp.blogspot.com/_D_Z-D2tzi14/S8TiTtIFjpI/AAAAAAAACxQ/HXLdiZZ0goU/s1600/ALOT14.png",
            "like-more":"http://3.bp.blogspot.com/_D_Z-D2tzi14/S8TffVGLElI/AAAAAAAACxA/trH1ch0Y3tI/s1600/ALOT6.png",
            "danger-more":"http://1.bp.blogspot.com/_D_Z-D2tzi14/S8TflwXvTgI/AAAAAAAACxI/qgd1wYcTWV8/s1600/ALOT12.png",
            "swim":"http://1.bp.blogspot.com/_D_Z-D2tzi14/S8TpGRlt9eI/AAAAAAAACxY/qDqk63PhqGs/s1600/ALOT15.png",
            "alot":"http://2static.fjcdn.com/pictures/Obeying+the+great+leader+s+commands+big3+admin+big3+big2+asked+to+big2+big1+post+a_e5c0b4_5651409.jpg",
            "better":"http://i.imgur.com/m29Q9W4.png",
            "art":"http://36.media.tumblr.com/tumblr_m1ic2wseDN1qe6p9xo1_500.jpg",
            "eggs":"https://s-media-cache-ak0.pinimg.com/216x146/36/1e/67/361e67134e49476ca52cbdd292baff46.jpg",
            "quite":"http://i.imgur.com/nmHZXRT.png",
            "ice":"http://archive.garron.us/img/2010/alot_of_ice_skating.png",
            "eat":"https://s-media-cache-ak0.pinimg.com/236x/1e/dd/2f/1edd2ff3a4314571bc5a3bb6f01e3405.jpg",
            "that":"http://i.imgur.com/aPaDhiY.png"
            #That's alot : guy named That with an alot
            }
        self.keyRegex = re.compile("\\b"+"("+"|".join(self.alotTags.keys())+")")
        self.alotRegex = re.compile("\\balot\\b")

    @commands.command(pass_context=True)
    async def alot(self,ctx):
        """What's an alot?"""
        await self.bot.say("This is an alot: http://hyperboleandahalf.blogspot.com/2010/04/alot-is-better-than-you-at-everything.html")

    async def alot_of_checks(self, message):
        if message.author.id == self.bot.user.id:
            return

        lower = message.content.lower()
        if ' ' not in lower:
            return

        lowerm = re.sub(self.alotRegex,"",lower,1)
        if lowerm == lower:
            return

        matchedKeys = re.findall(self.keyRegex,lowerm)
        matchedTags = []
        print(matchedKeys)
        for k in matchedKeys:
            vals = self.alotTags[k]
            for tag in vals:
                if tag not in matchedTags:
                    matchedTags.append(tag)
        url = ""
        if matchedTags == []:
            url = randchoice(list(self.alots.values()))
        else:
            url = self.alots[randchoice(matchedTags)]
        await self.bot.send_message(message.channel,url)



def setup(bot):
    n = Alot(bot)
    bot.add_listener(n.alot_of_checks, "on_message")
    bot.add_cog(n)
