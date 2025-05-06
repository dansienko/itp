# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define h = Character(_("Holloway"), color="#7b8e96")
define w = Character(_("Wax"), color="#29a1e7")
define j = Character(_("Jed"), color="#2f25ea")
define r = Character(_("Reston"), color="#056821")
define n = Character(_(""), color="#ffffff")
define karen = Character(_("Karen"), color="#5aa102")
define fadein = Fade (0,0,5)
# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg begin

    

    # These display lines of dialogue.

    r "Come in, Holloway."

    h "I hear ya, loud and clear."

    r "Good. Likelihood is that radio contact will only hold for a few days. Check in as often as you can."

    h "Understood, we're going in. Over and out."

    define my_fade = Fade(5,5,0) 
    with my_fade

    scene bg room 
    n "Three nights have passed since you've begun this treacherous journey down the spiral staircase."
    n "You wonder why you ever came to this place, but you quickly remember your answer."
    show holloway neut
    n "You are Holloway Roberts, accomplished professional hunter and explorer. You were contacted by Billy Reston to lead this exploration."
    n "While you might not have normally answered Reston's call, after hearing about what is going on in the house on Ash Tree Lane you found yourself unable to refuse."
    n "Reports of a mysterious 'five and a half minute' hallway spawning out of thin air, alongside an entire world enclosed within a closet that did not exist when the owners first entered the house."
    n "This is what you have been waiting for. A true complete unknown. The ultimate adventure, your path to the history books."
    n "That's why you're here. And it's why you brought them."
    show jed neut at right 
    show wax neut at left
    n "Kirby 'Wax' Hook and Jed Leeder. Your faithful assistants. You took them along because you knew they could handle this."
    n "And if they handle it just as expected, they will go down in history alongside you."
    n "After entering the closet in the house on Ash Tree Lane, a house owned by Will Navidson, you found the stories to be true."
    n "There is nothing but black. Infinite black stretching into hallways and rooms and doorways but never anything more."
    n "Despite the report from Navidson that the walls are constantly shifting, there is one place within the House that seems to appear to all those who enter."
    n "You, to your great pleasure, have given this space a name."
    h "Welcome to the Great Hall."
    j "Woah... This is..."
    hide wax neut 
    show wax scared at left
    w "I feel sick. Something ain't right about this."
    h "There's a lot more, too. Shall we?"
    n "Holloway gestures towards a massive spiral staircase in the center of the Great Hall."
    n "Not without taking a second to revel in its uncanniness, and stare down into the murky depths of the staircase to which the bottom could not be seen, the group descends."
    with my_fade
    hide wax scared
    hide jed neut
    hide holloway neut

    label fourth_night:

    scene bg hallway
    with fadein

    n "Morning, if it can be called that, comes on the fourth day."

    n "There is no sun here. No real indication of time passing, except for what your bodies tell you."
    show wax scared at right
    show jed neut at center
    show holloway neut at left
    n "The group rests at the base of the staircase, weary and unsure. Wax fidgets with a flashlight. Jed watches you closely."

    w "Well now that we've made it to the bottom, I supposed we've done what we set out to do. There's just more... nothing down here."
    n "Wax swallows forcefully."
    w "How about we head back up?"
    menu:
        "Return to the surface":
            jump bad_ending
        "Continue exploring":
            jump continue_exploring


label bad_ending:

    h "Yes, I suppose we've done what we came to do. We'll save what we have left for the return trip."

    n "You half expect resistance — from the others, from the House itself — but nothing comes."

    n "Instead, it's easy. Remarkably easy."

    n "The ascent feels fast. The climb up the spiral staircase, which took hours to descend, takes minutes to climb."

    n "And then you're back. The door to the closet creaks open, revealing the house on Ash Tree Lane."

    n "The living room is still. Karen Green, long time partner to Navidson, is waiting."

    scene bg begin
    with fadein



    n "She says nothing at first. Then, her voice low and cutting..."

    karen "He’s going in next. Will. My Will. Because you didn’t go far enough."

    h "I-"

    karen "Because you quit."

    n "You try to speak, to defend yourself, but the words don’t come."

    n "This isn’t just an expedition. It never was. And now it’s someone else’s descent."

    n "And you may have sent him to his death."
    call screen bad_ending_screen
    # Bad ending label or screen could go here
    return

label continue_exploring:

    n "You push forward."

    n "The hallway narrows, then widens again. Always dark, always quiet... until it isn’t."

    n "A low growling noise rolls through the darkness like distant thunder."

    w "Did you hear that?"

    j "Yeah. It’s... behind us?"

    show holloway neut at center
    show jed mad at left
    n "But you — Holloway — feel something else. Excitement. The unknown is speaking."
    j "Don't you think you ought to be leaving trail markers more frequently, Holloway?"
    menu:
        "Agree with Jed":
            jump agree_with_jed
        "Brush it off and keep going":
            jump keep_going


label agree_with_jed:

    j "Holloway, you've stopped marking the trail... what's going on with you?"

    h "You're right... I... I don't know what came over me."

    n "You slow your pace. Is this place getting to you?"

    n "You feel your thoughts slipping, your sense of time and orientation unraveling."

    n "You remind yourself why you're here. History. Discovery. Legacy."

    n "But for a moment, you remember who you are."

    n "Still, there is only forward."

    jump reconverge_exploration

label keep_going:

    h "We’re wasting time. Can't you hear the sound? Could be anything. We have to keep going."

    n "You scowl and keep moving. Deeper."

    n "The walls close in again. You press a hand to one and pause."

    n "The surface feels damp, gritty, almost alive."

    n "You retrieve a small sample vial and scrape some of it in."

    n "Another piece of the puzzle."

    jump reconverge_exploration

label reconverge_exploration:

    n "The hallway is silent, almost expectant."

    n "You hold the sample vial tightly, staring at the wall."

    menu:
        "Leave the wall alone":
            jump discover_living_room
        "Break the wall open":
            jump break_the_wall



label discover_living_room:

    n "You decide against disturbing the wall."

    n "There’s a growing pressure behind your eyes. You ignore it."

    n "The group explores for a while longer."

    n "Then, impossibly, the hallway shifts... and there it is."

    scene bg begin
    with fade

    n "The living room."

    w "What the hell... we didn’t climb the stairs..."

    j "It looped. The House brought us back."

    n "You realize, too late, that you've lost your opportunity."

    call screen bad_ending_screen
    return


label break_the_wall:

    n "With the butt of your rifle, you slam the wall."
    scene bg crack1
    scene bg crack2
    n "Once. Twice. It cracks and gives way with a wet crunch, opening to blackness."
    scene bg hole
    show wax scared
    w "What are you doing?!"

    show jed scared at right
    j "That’s not exploration, that’s insanity!"

    n "You ignore them."
    scene bg hallway
    n "Later, as the growling returns, you load your rifle."


    show holloway neut at left
    h "It's close..."
    show wax scared at center
    w "Are you hearing yourself? Holloway, stop. The sound isn't moving. We have not gotten any closer."
    hide holloway neut
    show holloway mad at left
    h "You're distracting me, you coward."

    n "Your voice is sharp, filled with something they can’t understand."
    hide wax scared
    hide jed scared
    n "Your steps are faster now. Sloppier. Like a man chasing glory with a fever."
    show jed mad at right 
    j "We're not getting closer, Holloway. We’re going back."

    menu:
        "Follow Jed and Wax":
            jump good_ending
        "Keep going alone":
            jump holloway_alone


label good_ending:

    n "You stop."

    n "A war rages inside you — conquest, pride, legacy — but something else wins."

    n "Survival. Humanity."

    n "You turn around."

    n "The group makes it back, slowly, over several days."

    scene bg begin
    with fade

    n "In the months that follow, your findings are studied, respected... but the House remains untouched."

    n "You are the last to descend."

    show text "GOOD ENDING" at truecenter with dissolve
    pause 3

    return

label holloway_alone:

    n "You watch them walk away."
    hide jed mad
    n "Their lights fade. Their voices vanish."

    n "But the growling does not."

    n "You keep walking. Screaming. Hunting."

    h "COME ON! SHOW YOURSELF!"

    n "Then, at the end of a long hallway... movement."
    show bg monster
    n "You swear you see something at the end of the next hallway."
    n "You raise your rifle."

    menu:
        "Take the shot":
            jump shoot_monster
        "Don’t shoot":
            jump good_ending


label shoot_monster:



    n "The gunshot echoes endlessly. Smoke fills your nose."

    n "You rush forward, triumphant."

    scene jed dead
    with fade

    n "...and then you see Jed's body."

    n "Blood. Confusion. Horror."

    n "You fall to your knees."

    h "No. No no no..."

    n "If you go back, they’ll arrest you. Hate you."

    n "You run instead. Through halls, doors, voids. Forever hunted, and hunting."

    label holloway_true_ending:

    scene black
    with fade

    n "Time loses meaning."

    n "You wander. Eat what’s left in your pack. Then nothing."

    n "Your breath grows shallower. Lightless days. Lightless nights."

    n "And then... you begin to speak."

    h "The... corridors... they know me. They open and close when I ask."

    h "They showed me the way. The thing was there. I almost had it."

    h "Reston. They'll never believe him. He's not worthy of this place."

    n "Your voice echoes off nothing. Only the House listens."

    n "In the final recording, your voice is slurred, exhausted."

    h "...god, what is this place... the skin... is peelin' off the wall..."

    n "You rest against a corner. The rifle heavy in your hands."

    h "If I don’t do it, the House will..."

    pause 1

    n "A single gunshot rings out, echoes, and dies."
    n "The shadows grow and consume what is left of you."
    scene black with fade
    pause 2

    show text "TRUE ENDING" at truecenter with dissolve
    pause 3

    return
 

    return
screen bad_ending_screen:
    tag menu

    # Black background
    window:
        style "gm_root"
        background "#000000"

    # Centered "BAD ENDING" text
    frame:
        align (0.5, 0.4)
        xsize 800
        ysize 200
        background None

        text "BAD ENDING" size 60 color "#ff3333" xalign 0.5

    # Subtext
    frame:
        align (0.5, 0.55)
        xsize 1000
        background None

        text "You turned back. But the House was far from done." size 30 color "#aaaaaa" xalign 0.5

    # Return options
    frame:
        align (0.5, 0.75)
        has vbox

        textbutton "Return to Main Menu" action MainMenu(confirm=False)
        textbutton "Try Again" action Jump("fourth_night")