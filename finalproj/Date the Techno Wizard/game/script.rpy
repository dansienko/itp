# Declare characters
define my_fade = Fade(2, 2, 0)
define the_fade = Fade(10, 2, 0)
define af = renpy.audio.filter
image t happy = im.FactorScale("t happy.png", 0.5)
define t = Character("Techno Wizard")
define g = Character("George William")
define p = Character("Townsperson")
define n = Character("Narrator")

label start:

    scene bg startscreen

    menu:
        "Start Game":
            jump game_begin

label game_begin:
  
    scene bg start
    play music "start.mp3"

    n "You look upon the remarkably clear blue skies that characterize the Land of the Third Strain. You have finally made it."
    n "At a young age, you left your home in a merchant colony back East in order to see the world. You took your belongings and rode your trusty steed far and wide."
    n "After visiting many beautiful destinations worldwide, you intend to end your journey in the famous Land of the Third Strain."
    n "To your left, you see a large and intimidating castle. To the right, a bustling town, rich with music and dancing townspeople."

    menu:
        "Approach the Castle":
            jump gone_to_castle
        "Head to Town":
            jump gone_to_town
label gone_to_town:
    play music "town.mp3" fadeout 1.0
    scene bg lookingtown
    n "Upon arrival in town, you can see that everybody is in fact dancing. It also sounds like each home is blasting the same piece of music, a funky, hypnotic groove that seems to have a mesmerizing effect on the town."
    show p happy
    p "Hey there, stranger! I don't believe I've seen you around before. Where do you come from?"
    n "You tell your story."
    p "Wow, you must be awfully tired! I hope you find the rest you're looking for here in our town, but if I can be honest with you, nobody has been getting rest around here."

    menu:
        "Inquire Further":
            jump townsperson_speech
        "Head Back":
            jump game_begin
        "Head to the House on the Right":
            jump georgewilliam

label townsperson_speech:
    scene bg lookingtown
    show p happy
    p "Well, between you and me, nobody is happy with the leadership around here. That castle over there? The Techno Wizard lives there."
    p "Nobody knows much about him, other than the fact that he's super scary, and he cursed our town to dance all day! I mean, we love to dance, but this is excessive. It's been days, months, years, maybe."
    n "You pry for any more information regarding the Wizard."
    p "Legend has it he was once in love, and the loss of that love led him to the bitter grudge in which our curse is preserved. Maybe if he found someone new..."

    menu:
        "Inquire Further":
            jump townsperson_speech
        "Head Back":
            jump game_begin
        "Head to the House on the Right":
            jump georgewilliam

label georgewilliam:
    play music "gdubs.mp3" fadeout 1.0
    scene bg gwhut
    show g happy
    g "D... I... S... C... O... I can't forget the code..."
    n "You see a short man dressed in an astronaut's suit stewing over his notes."
    g "Hey, get outta here! And don't tell anyone what you saw."
    jump gone_to_town

label gone_to_castle:
    scene bg lookingcastle
    n "The Castle towers before you. It is made of beautiful carved stone. You wonder how long it has stood here."

    menu:
        "Turn Back":
            jump game_begin
        "Go In":
            jump entered_castle

label entered_castle:
    play music "castle.mp3" fadeout 1.0
    scene bg firstfloorcastle
    n "You enter the castle with a shaky step. To your right, a dark staircase heading who knows where. To your left, a painting with a small inscription."

    menu:
        "Examine the Painting":
            jump fine_dandy
        "Head Upstairs":
            jump castle_floortwo
        "Turn Back":
            jump gone_to_castle

label fine_dandy:
    play music "finendandy.mp3" fadeout 1.0
    scene bg firstfloorcastle
    n "The painting depicts two goblins, one quite large wearing dark red pants accented with a large golden D belt buckle, and the other small enough to be sitting on the back of the large goblin, wearing matching garb except for an F on his belt buckle."
    n "The inscription below reads, 'Fine and Dandy'"
    jump entered_castle

label castle_floortwo:
    play music "castle.mp3" fadein 1.0
    scene bg secondfloorcastle
    n "You reach the second floor, your heart pounding in your chest..."
    menu:
        "Examine the Painting":
            jump techno_lover
        "Go on the Balcony":
            jump balcony
        "Head Upstairs":
            jump twiz_encounter

label techno_lover:
    play music "start.mp3" fadeout 1.0
    scene bg secondfloorcastle
    n "The painting depicts an old man with a long, white beard..."
    n "The inscription below reads, 'Techno Wizard and ------'"
    jump castle_floortwo

label balcony:
    play music "town.mp3"
    scene bg viewoftheland
    n "From here, you can see the land that stretches East of the Castle..."
    jump castle_floortwo

label twiz_encounter:
    play music "twizencounter.mp3" fadeout 1.0
    scene bg twizdomain
    show t happy
    n "Before you stands the Techno Wizard himself."
    t "What?! What are you doing here!"
    t "Give me one good reason why I shouldn't send you to the dungeon immediately!"

    menu:
        "I'm here to talk!":
            jump secondphase
        "I'm in love with you!":
            jump gameoverone

label gameoverone:
    show t happy
    scene bg twizdomain
    t "You're full of it! You just met me! To the dungeon with you!"
    scene bg gameover
    hide t happy
    play music "castle.mp3" fadeout 1.0
    n "You've been sent to the dungeon."
    menu:
        "Start Game Over?":
            jump game_begin
        "Restart from Encounter":
            jump twiz_encounter

label secondphase:
    scene bg twizdomain
    show t happy
    t "Just to talk, huh?"
    menu:
        "Funkiest Moves":
            jump thirdphase
        "What's the Third Strain":
            jump gameovertwo
        "Juiciest Jams":
            jump thirdphase

label gameovertwo:
    scene bg twizdomain
    show t happy
    t "What are you, a cop? To the dungeon!"
    scene bg gameover
    hide t happy
    play music "castle.mp3" fadeout 1.0
    n "You've been sent to the dungeon."
    menu:
        "Start Game Over?":
            jump game_begin
        "Restart from Encounter":
            jump twiz_encounter

label thirdphase:
    scene bg twizdomain
    show t happy
    t "Ahh... I'm glad you asked!"
    menu:
        "If they love your song, why are you all alone?":
            jump fourthphase
        "The jam is funky, but you shouldn't force the town to dance all day!":
            jump gameoverthree

label gameoverthree:
    scene bg twizdomain
    show t happy
    t "Who are you to say what I should and should not do!"
    scene bg gameover
    hide t happy
    play music "castle" fadeout 1.0
    n "You've been sent to the dungeon."
    menu:
        "Start Game Over?":
            jump game_begin
        "Restart from Encounter":
            jump twiz_encounter

label fourthphase:
    scene bg twizdomain
    show t happy
    t "Well... They don't exactly love it."
    menu:
        "What did you do?":
            jump gameovertwo
        "Things don't have to be this way!":
            jump fifthphase

label fifthphase:
    play music "twizencounterspedup.mp3"
    scene bg twizdomain
    show t happy
    t "Well then how can they ever be?!"
    menu:
        "It's not too late.":
            jump sixthphase

label sixthphase:
    
    scene bg twizdomain
    show t happy
    t "How couldn't it be too late?!"
    menu:
        "Start dancing.":
            jump seventhphase

label seventhphase:
   
    scene bg twizdomain
    show t happy
    t "Are you..? Dancing? Of your own volition?"
    t "Would you maybe want to have a picnic with me?"
    menu:
        "Of course I would.":
            jump goodend
        "No way!":
            jump bad_ending

label bad_ending:
    
    scene bg twizdomain
    show t happy
    t "Wow, you worked my whole life story out of me just to reject my feelings? Out of my sight!"
    scene bg gameover
    hide t happy
    play music "castle.mp3" fadeout 1.0
    n "You've been sent to the dungeon."
    menu:
        "Start Game Over?":
            jump game_begin
        "Restart from Encounter":
            jump twiz_encounter

label goodend:
    scene bg twizdomain
    show t happy
    n "You join hands with the Techno Wizard as you each bust your funkiest move."
    with my_fade
    scene bg goodend
    hide t happy
    play music "start.mp3"
    n "Thanks for playing! Make sure to stream Techno Wizard by Jammwich out everywhere August 26th :)"
    return    
