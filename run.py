"""
Welcome the player to the game.
Tell them this is a survival horror text based adventure game.
Ask them if they'd like to try escape...HOUSE (in ascii art)
y/n/how to play
"""

"""
How to play:
You will be walked through your memories by Mr. N
As you recall what happened you will be prompted with choices of what you chose (past tense)
to do next.
You will be prompted with a sanity meter from the first question you're asked
and immediately lose some sanity.
Reaching below zero sanity will cause a GAME OVER state.
The game has four endings.
(There are collectibles along the way)
(100% clear means finding the "true" ending and getting every collectible)
"""

"""
Describe the interrogation room that they find themselves in
Describe the man asking them questions
He asks what the last thing you remember is...
As you think back you mention a bathroom
He pushed you, saying you were found in a long hallway
You immediately take sanity damage
But as you reach into your memory you do remember something
about a hallway
"""

"""
Choice 1:
You remember a hallway that didn't seem to end
Worse than that, you remember finding this hallway
In your own house.

He prompts you to continue.

Do you:

1. Continue to explore your memories?
2. Ask him where you are right now?

Exploring you memories will cause you to lose sanity, but will uncover more of what really happened.
Asking him where you are now will restore sanity, though his answer won't match up to your memories.
"""

"""
This creates the first branching path:

You can continue down the line of questioning your interrogator,
gaining sanity all while you do.
This will grant you ending 1:

"The bureau helps you fill in the story, your sanity recovers as they do and 
you come to the conclusion (despite what was written in the beginning of the game) 
that you never passed out in your house and were found, 
you voluntarily walked to the bureau’s offices to report something strange about your house. 
They reassure you there was nothing strange 
about what you experienced. Maybe you just need a good night’s sleep. Maybe you do. 
You leave the bureau with a full bar of sanity but as a player 
you will get the feeling that something isn’t right."

You can choose to break from this path at any choice as you go along
but the later you break from the path the more sanity you lose.
"""