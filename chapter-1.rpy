init python:
    #check game saves, we are the warrior after all
    def mod_check_saves(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "end":
            if persistent.ggwp_monika == 0:
                pass
            elif persistent.ggwp_monika == 2:
                renpy.jump("load_ga")
            elif persistent.ggwp_monika == 1:
                renpy.jump("load_g")

    #ya boy cant skip when monika dialogue shows up
    #seems more realistic actually
    #just monika
    def monika_showed_up(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "begin":
           config.keymap['dismiss'] = []
           renpy.display.behavior.clear_keymap_cache()
        elif event == "slow_done":
           config.keymap['dismiss'] = dismiss_keys
           renpy.display.behavior.clear_keymap_cache()

label intro_mod_2:
    $ delete_all_saves()
    $ persistent.deleted_saves = True
    $ gtext = glitchtext(48)
    stop music
    $ config.window_hide_transition = None
    scene black with trueblack
    pause 0.01
    scene bg residential_day
    with dissolve_scene_half
    $ config.window_hide_transition = Dissolve(.2)
    play music t2g
    queue music t2g2

    $ s_name = glitchtext(12)
    $ gtext = glitchtext(80)
    s "[gtext]"
    "I see an annoying girl running toward me from the distance, waving her arms in the air like she's totally oblivious to any attention she might draw to herself."
    "That girl is [s_name], my neighbor and good friend since we were children."
    "You know, the kind of friend you'd never see yourself making today, but it just kind of works out because you've known each other for so long?"
    "We used to walk to school together on days like this, but starting around high school she would oversleep more and more frequently, and I would get tired of waiting up."
    "But if she's going to chase after me like this, I almost feel better off running away."
    "However, I just sigh and idle in front of the crosswalk and let [s_name] catch up to me."

    show sayori glitch at t11 zorder 2
    python:
        currentpos = get_pos()
        startpos = currentpos - 0.3
        if startpos < 0: startpos = 0
        track = "<from " + str(startpos) + " to " + str(currentpos) + ">bgm/2.ogg"
        renpy.music.play(track, loop=True)
    pause 1.0
    $ gtext = glitchtext(48)
    s "{cps=60}[gtext]{/cps}{nw}"
    pause 1.0
    $ gtext = glitchtext(48)
    s "{cps=60}[gtext]{/cps}{nw}"
    show screen tear(8, offtimeMult=1, ontimeMult=10)
    pause 1.5
    hide screen tear
    window hide(None)
    window auto
    scene black with trueblack
    $ delete_all_saves()
    $ persistent.playthrough = 2
    #$ persistent.anticheat = renpy.random.randint(100000, 999999)
    #$ anticheat = persistent.anticheat

    scene bg residential_day
    with dissolve_scene_half
    play music t2
    jump intro_mod_2_2
    
label intro_mod_2_1:
    stop music fadeout 2.0
    scene bg residential_day
    with dissolve_scene_full
    play music t2
    jump intro_mod_2_2

default persistent.nice_try = 0

label intro_mod_2_2:
    $ persistent.ggwp_monika = 0
    $ delete_all_saves()
    #elif persistent.nice_try == 2:
        #$ renpy.call_screen("dialog", "Are you tired, [player]?", ok_action=Return())
        #$ renpy.call_screen("dialog", "I know it's hard to get over it.", ok_action=Return())
        #$ renpy.call_screen("dialog", "Look, I have an idea.", ok_action=Return())
        #$ renpy.call_screen("dialog", "After you see this messages, you\nshould save your game, then...", ok_action=Return())
        #$ renpy.call_screen("dialog", "When Monika shows up, load up\nyour save immediately!", ok_action=Return())
        #$ renpy.call_screen("dialog", "Then, you should good to go.", ok_action=Return())
        #$ renpy.call_screen("dialog", "Good luck beating this game!  ~Modder", ok_action=Return())
        #$ persistent.nice_try = 0
    "It's an ordinary school day, like any other."
    #just testing my stuff here
    #$ nani = m.display_args["callback"]
    #$ nani2 = narrator.display_args["callback"]
    #"[nani]   [nani2]"
    "Mornings are usually the worst, being surrounded by couples and friend groups walking to school together."
    "Meanwhile, I've always walked to school alone."
    $ currentpos = get_pos()
    stop music
    "..."
    $ narrator.display_args["callback"] = mod_check_saves
    "Alone...{w} I'm alone, huh?"
    "I feel like some kind of deja vu..."
    "I feel like I'm not supposed to be alone, right?"
    "Well...."
    $ s_name = glitchtext(12)
    menu:
        "What should I do at this point?"
        "Visit [s_name]'s house.":
            pass
        "Go to school.":
            jump intro_mod_2_3
    "Maybe I should check out my \"neighbor\" next door, since I'm very curious about what happened."
    "Wait, is it \"neighbor\" or \"neighbour\"?"
    "Whatever..."
    "Hope that I'll find something interesting."
    "Oh, I might want to save my game before continue."
    "If there's something wrong, I can load the game again, trying to play safe."
    jump its_time_boys
    
label intro_mod_2_3:
    $ audio.t2 = "<from " + str(currentpos) + " loop 4.499>bgm/2.ogg"
    play music t2
    "Well, going to school isn't really bad at all."
    "I always tell myself it's about time I meet some girls or something like that..."
    "But I have no motivation to join any clubs."
    "After all, I'm perfectly content just getting by on the average while spending my free time on games and anime."
    $ monika_seen = False
    jump chapter_mod_1
    
label its_time_boys:
    scene bg house
    with wipeleft_scene
    "This house..."
    "...looks familiar to me..."
    "I wonder why, though..."
    "I saw a name tag in front of the house."
    "Usually in Japan, the name or family name tag is present at the front gate to show the owner's name of his/her house."
    "But this one..."
    "It's gibberish to me."
    "I wonder why..."
    "If I could read it..."
    $ s_name = glitchtext(12)
    mc "[s_name]"
    "I couldn't read it..."
    "Then, I proceed myself to knock the door."
    mc "Hello? Is anyone there?"
    "The house looks empty to me, {w}the door is strangely unlocked... {w}I wonder why..."
    mc "I'm coming over... {w}{i}(in Japanese language){/i}{w}{i}(as i mutter quietly){/i}"
    
    scene black
    with dissolve_scene_half
    play music ghostmenu
    $ m.display_args["callback"] = slow_nodismiss
    m "{cps=*0.5}Hey, [player]!{/cps}{nw}"
    $ persistent.ggwp_monika = 1
    show screen tear(20, 0.1, 0.1, 0, 40)
    window hide(None)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.25
    stop sound
    hide screen tear
    window show(None)
    show bg glitch:
        yoffset 480 ytile 2
        linear 0.25 yoffset 0
        repeat
    show monika 2h at t11 zorder 2
    m "{cps=*0.5}What are you doing here?{/cps}"
    m 4i "{cps=*0.5}You shouldn't be here.{/cps}"
    m 1r "{cps=*0.5}Are you trying to cheat?{/cps}"
    m 5b "{cps=*0.5}Shame on you.{/cps}"
    m 5a "{cps=*0.5}You better not do that again, ok sweetheart?{/cps}"
    if persistent.nice_try == 0:
        $ renpy.call_screen("dialog", "Don't play with my heart~", ok_action=Return())
    $ persistent.nice_try = 1
    play music g1
    show sayori glitch at t11 zorder 2
    pause 0.5
    show screen tear(8, offtimeMult=1, ontimeMult=10)
    pause 1.5
    $ renpy.utter_restart()

label load_g:
    $ narrator.display_args["callback"] = None
    "Ah, what happened....?"
    "Just now..."
    "I saw..."
    "I saw her true form."
    "She was there all along."
    "She set up some kind of trap just to trick me?!"
    "I just couldn't stand this thing."
    "If that what she wants from me..."
    "Then I should get along? {w}Act normally like the game would be?"
    "I guess I have no choice but to move on..."
    "But you will pay for it!"
    "Just you wait, Moni-{nw}"
    $ monika_seen = True
    stop music
    scene black with trueblack
    pause 1.0
    $ audio.t2 = "<from " + str(currentpos) + " loop 4.499>bgm/2.ogg"
    play music t2
    jump chapter_mod_1

#choice flag
label chapter_mod_1a:
    "I knew it..."
    mc "Ah, before that..."
    mc "I need to pack up my things."
    mc "Also, I'm on duty today to clean out my classroom."
    "I am supposed to be on duty today by the way."
    mc "Can you wait outside a litte bit?"
    m 1c "???"
    "Monika looks at me."
    "I swallowed, not trying to spill my beans."
    m 5a "Okay, [player]. You just need to hurry up okay~?"
    mc "A-Ah, thanks."
    show monika at thide zorder 1
    hide monika
    
    $ poster_checked = False
    $ closet_checked = False
    "Okay, [player]... What should I do?"
    call i_do_1
    if closet_checked:
        pass
    elif poster_checked:
        call i_do_1
    return
    
label i_do_1:
    menu:
        "I guess I should..."
        "Do something violent":
            jump throw_chair
        "Check the closet":
            "I guess I should... {fast}check the classroom closet."
            call check_closet
            return
        "Check the poster" if not poster_checked:
            "I guess I should... {fast}check the poster at the wall, which is located at the back of the class."
            call check_poster
        "Nevermind...":
            "Ah, never mind..."
            "There's no point for me to to do something here."
            "After all, she is waiting for me."
            "I guess getting along is fine, as of now."
            "I can do something about this later on."
    return

label throw_chair:
    "Hmm..."
    "I thought of doing something crazy..."
    "Well, here goes nothing..."
    mc "May God save me.{nw}"
    $ style.say_dialogue = style.edited
    "LOAD ME{w=0.5}{nw}"
    $ style.say_dialogue = style.normal
    mc "May God save me.{fast}"
    "I grab one of the chair in my classroom."
    "Then... I throw the chair with my full power{nw}"
    #play sound throwchair
    "Then... I throw the chair with my full power{fast} at one of the classroom window{nw}"
    #play sound glassbreak
    scene black
    window hide(None)
    window auto
    pause 1.0
    $ persistent.ggwp_monika = 2
    play music ghostmenu
    show end
    with dissolve_scene_full
    pause 1.0
    "What?"
    "What am I seeing right now?"
    "Did I broke the game?"
    "What?!"
    pause 2.0
    "Huh..."
    pause 2.0
    "Well..."
    pause 2.0
    "What am I doing right now..."
    "I can't even go to main menu."
    "There must be another way!"
    pause 10.0
    "What happens if I quit this game?"
    "Will my memories stays intact after this?"
    "I'll guess we're about to find out."
    pause 30.0
    "I found something strange..."
    "What is this?"
    "Is that a switch?"
    "What if try to pull it?"
    $ consolehistory = []
    call updateconsole("renpy.utter_restart()", "Restarting...")
    pause 1.0
    "Oh."
    "Well, I guess that wor"
    stop music
    show screen tear(8, offtimeMult=1, ontimeMult=10)
    pause 1.5
    $ renpy.utter_restart()

label check_closet:
    "Just curious to see what's inside that closet."
    "I expect the content of that closet with classroom stuffs like books, files or markers."
    "But you'll never know what is actually inside it."
    scene bg closet
    with wipeleft_scene
    "Well, here goes nothing."
    "I proceed myself to open it."
    play sound closet_open
    mc "..."
    mc "I found markers."
    "Construction papers too.."
    "Wasn't Monika trying to find these stuff before?"
    #half chance isnt really half of a chance ~Monika
    $ half_chance = renpy.random.randomint(0, 2)
    if half_chance == 0:# or config.developer:
        mc "What's this?"
        "There's a lone volume of manga amidst a stack of various books on the side of one of the shelves."
        "Curious, I pull it out a volume of that box of manga."
        mc "Parfait Girls...? {w}Part one?"
        "Have I heard this manga before?"
        "My memory is a little bit hazy, so I don't know if I read it before."
        "I wonder why it was there in my classroom."
        "Was it there in the entire time?"
        mc "I guess I could keep it though..."
        "I put it inside my bag, just in case."
        "I kinda want to read it though in my spare time."
        "Well, about the markers and construction paper..."
        "I guess I could give them to Monika after all."
        $ persistent.parfait_girls = True
    else:
        "Well, I guess I could give them to Monika after all."
        $ persistent.parfait_girls = False
    play sound closet_close
    "I proceed to close the closet."
    m "[player], are you done already?"
    "I saw Monika, eagerly waiting for me outside."
    "I guess I have no choice."
    mc "Alright, I'm coming..."
    $ closet_checked = True
    return

label check_poster:
    "..."
    #half chance isnt really half of a chance ~Monika
    $ half_chance = renpy.random.randomint(0, 2)
    if half_chance == 0:# or config.developer:
        "I saw..."
        "A girl..."
        "In the poster."
        mc "Uh..."
        mc "What is this picture?"
        $ currentpos = getpos()
        stop music
        scene black
        pause 1.0
        scene s_hang
        pause 0.1
        show screen tear(20, 0.1, 0.1, 0, 40)
        window hide(None)
        play sound "sfx/s_kill_glitch1.ogg"
        pause 0.25
        stop sound
        hide screen tear
        window show(None)
        $ audio.t2 = "<from " + str(currentpos) + " loop 4.499>bgm/2.ogg"
        play music t2
        mc "What is this picture?{fast}"
        "My head started to feel dizzy again."
        "I wished I didn't saw that."
        stop music
        "I think... {w}I just wanted to go outside."
        "I need some air."
        scene bg corridor
        with wipeleft_scene
        show monika 1d at t11 zorder 2
        m "[player], what happened back there?"
        mc "Ugh.."
        mc "Uh..."
        mc "I..."
        show monika at lhide
        hide monika
        "I feel like I can't speak anymore."
        "I sit down at the corridor, against the wall."
        m "[player]..."
        show monika 1d at t11 zorder 2
        m "What just happened..."
        mc "I..."
        "I couldn't explained it to her, or else she might know my self-awareness."
        m 1h "[player]... {w}You saw it didn't you?"
        m "Ahaha~ Sorry you had to witness that thing."
        "What?"
        "I'm screwed..."
        m 5a "Don't do it ever again, ok sweetheart?~"
        "What did she just sa{nw}"
        $ persistent.ggwp_monika = 2
        show screen tear(8, offtimeMult=1, ontimeMult=10)
        pause 1.5
        $renpy.utter_restart()
    else:
        "Just a wall calendar."
        "Nothing interesting around here."
        "Maybe I should do something else?"
        "Well..."
        $ poster_checked = True
        return

#main chapter flag
label chapter_mod_1:
    #haha you cant save this game forever ~Monika
    $ delete_all_saves()
    $ persistent.ggwp_monika = 0
    scene bg class_day
    with wipeleft_scene
    "The school day is as ordinary as ever, and it's over before I know it."
    "After I pack up my things, I stare blankly at the wall, looking for an ounce of motivation."
    mc "Clubs..."
    "There really aren't any that interest me."
    "Besides, most of them would probably be way too demanding for me to want to deal with."
    "Except for one club that I recognise before..."
    $ currentpos = get_pos()
    stop music
    mc "What the hell is that?!{w=1.0}{nw}"
    "{cps=*1.5}The \"thing\" started to approach me.{/cps}{w=1.0}{nw}"
    "{cps=*1.5}I didn't recognise that distorted mess of entity.{/cps}{w=1.0}{nw}"
    "{cps=*1.5}It's getting closer and closer now...{/cps}{w=1.0}{nw}"
    "{cps=*1.5}Ah, what is happening to this world?!!?!{/cps}{w=0.5}{nw}"
    mc "{cps=*1.5}WHAT THE FU{/cps}{nw}"
    show monika g2 at t11 zorder 2
    $ style.say_dialogue = style.edited
    $ gtext = glitchtext(80)
    mc "{cps=*2.0}WHAT THE FU{fast}[gtext]{/cps}{nw}"
    window hide(None)
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.25
    stop sound
    hide screen tear
    hide monika
    window show(None)
    $ style.say_dialogue = style.normal
    
    $ m.display_args["callback"] = None
    $ audio.t2 = "<from " + str(currentpos) + " loop 4.499>bgm/2.ogg"
    play music t2
    $ m_name = "???"
    show monika 1a at t11 zorder 2
    m "...[player]?"
    m 1b "Oh my goodness, I totally didn't expect to see you here!"
    m 5 "It's been a while, right?"
    mc "Ah..."
    mc "Yeah, it has."
    if monika_seen:
        "Oh, yeah? After what I saw {i}just now???{/i}"
        "I literally want to die just by looking at her."
        "Having her smile at me so genuinely feels a little... {w}suspicious..."
    else:
        "Monika smiles sweetly."
        "We do know each other - well, we rarely talked, but we were in the same class last year."
        "Monika was probably the most popular girl in class - smart, beautiful, athletic."
        "Basically, completely out of my league."
        "So, having her smile at me so genuinely feels a little..."
    mc "What did you come in here for, anyway?"
    m 1a "Oh, I've just been looking for some supplies to use for my club."
    m 1d "Do you know if there's any construction paper in here?"
    m "Or markers?"
    if monika_seen:
        "I bet she didn't want look for them in the first place. Ugh, I hate this lady..."
    mc "I guess you could check the closet."
    mc "...You're in the debate club, right?"
    m 5 "Ahaha, about that..."
    m "I actually quit the debate club."
    mc "Really? You quit?"
    m "Yeah..."
    m 2e "To be honest, I can't stand all of the politics around the major clubs."
    m "It feels like nothing but arguing about the budget and publicity and how to prepare for events..."
    m "I'd much rather take something I personally enjoy and make something special out of it."
    mc "In that case, what club did you decide to join?"
    m 1b "Actually, I'm starting a new one!"
    m "A literature club!{nw}"
    show screen tear(20, 0.1, 0.1, 0, 40)
    window hide(None)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.25
    stop sound
    hide screen tear
    window show(None)
    m "A literature club!{fast}"
    window auto
    if monika_seen:
        "That scare the shit out of me."
    mc "Literature...?"
    if not monika_seen:
        "That sounds kind of...dull?"
    mc "How many members do you have so far?"
    m 5 "Um..."
    m "Ahaha..."
    m "It's kind of embarrassing, but there are only three of us so far."
    m "It's really hard to find new members for something that sounds so boring..."
    mc "Well, I can see that..."
    if monika_seen:
        "The fact that you had another member as well..."
    m 3d "But it's really not boring at all, you know!"
    m "Literature can be anything. Reading, writing, poetry..."
    m 3e "I mean, one of my members even keeps her manga collection in the clubroom..."
    "Have I heard this before? My head fuzzy a little bit lately..."
    mc "Wait...really?"
    m 2k "Yeah, it's funny, right?"
    m 2e "She always insists that manga is literature, too."
    m "I mean, she's not wrong, I guess..."
    m "And besides, a member's a member, right?"
    if not monika_seen:
        "...Did Monika say \"she\"?"
        "Hmm..."
    else:
        pause 1.0
    m 1a "Hey, [player]..."
    m "By any chance...are you still looking for a club to join?"
    mc "Ah--"
    mc "I mean, I guess so, but..."
    m "In that case..."
    m 5 "Is there any chance you could do me a big favor?"
    m "I won't ask you to join, but..."
    m "If you could at the very least visit my club, it would make me really happy."
    m "Please?"
    mc "Um..."
    if monika_seen:
        $ narrator.display_args["callback"] = mod_check_saves
        "Well, I guess I have no reason to refu-{nw}"
        "Wait, why did I say that?!"
        "I cant' just head over heels for her just yet."
        "I need a plan to take out on her."
        "I need to do something rather than playing along."
        "This game... there must be some kind of weak spot, an exploitation."
        "Ah, I might to save this game later..."
        "You know that something might happened in the future..."
        "If I could--{nw}"
        m 1g "[player]?"
        mc "Oh! Uh..."
    else:
        "Well, I guess I have no reason to refuse..."
        "Besides, how could I ever refuse someone like Monika?"
    mc "Sure, I guess I could check it out."
    m 1k "Aah, awesome!"
    m 1b "You're really sweet, [player], you know that?"
    mc "I-It's nothing, really..."
    if monika_seen:
        "I let my guard down."
        "God damn it!"
    m 1a "Shall we go, then?"
    m "I'll look for the materials another time - you're more important."
    if monika_seen:
        call chapter_mod_1a
    return
