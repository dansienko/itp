# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define t = Character("Techno Wizard")
define g = Character("George William")
define p = Character ("Townsperson")
define n = Character ("Narrator")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg startscreen

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    menu:
        "Start Game":
            jump game_begin
label game_begin:
    scene bg start
    n "You look upon the remarkable clear blue skies that characterize the Land of the Third Strain. You have finally made it."
    n "At a young age, you left your home in a merchant colony back East in order to see the world. You took your belongings and rode your trusty steed far and wide."
    n "After visiting many beautiful destinations worldwide, you intend to end your journey in the famous Land of the Third Strain."
    n "To your left, you see a large and intimidating castle. To the right, a bustling town, rich with music and dancing townspeople."
    menu:
        "Approach the Castle":
            jump gone_to_castle
        "Head to Town":
            jump gone_to_town
label gone_to_town:
    scene bg lookingtown
    n "Upon arrival in town, you can see that everybody is in fact dancing. It also sounds like each home is blasting the same piece of music, a funky, hypnotic groove that seems to have a mezmerizing effect on the town."
    show p 
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
    show p
    p "Well, between you and I, nobody is happy with the leadership around here. That castle over there? The Techno Wizard lives there."
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
    scene bg gwhut
    return

