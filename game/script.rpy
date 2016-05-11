# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
image bg savannah = "#c45693"

# Declare characters used by this game.
define e = Character('Eileen', color="#c8ffc8")


# The game starts here.
label start:
$ bl_game = False

scene bg savannah
with fade
"I was confronted with the choose do i help Raoos or continue to stand idly by?"

menu:

        "... I should help Raoos.":

            jump goodEnd

        "... I shouldn't get involved.":

            jump badEnd

label goodEnd:
"I did not know why i stood up for Raoos, but i knew i had to stop being a bystander"
"I was scared and did not want to bring any attention to myself It was as if a hand pushed into my chest and forced me to speak up and defend him."
"I wondered how can I stand up for him when I can't even stand up for myself and I allow people to treat me just as bad"   
"I did not understand why i cared but in actuality i cared deeply. My heart would not allow me to see injustice continue to happen in this manner. "
"When i went home that night and looked in the mirror, a funny thing appeared in my reflection that puzzled me, The prominent colored stripes  of crimson and orange, that marked my face, that connected me to my tribe and my clan, seemed to be fading"
return

label badEnd:
"I knew i had to stop being a bystander but"
"I was scared and did not want to bring any attention to myself"
"I wondered how can I stand up for him when I can't even stand up for myself and I allow people to treat me just as bad"
"So i left Raoos to his fate."
"When i went home that night and looked in the mirror, The prominent colored stripes  of crimson and orange, that marked my face, that connected me to my tribe and my clan, seemed to be Darking"

