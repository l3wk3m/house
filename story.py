"""
Here I will store all of the story text and choice prompts
in one dictionary.

The run.py program will call these in and prompt the player with
choices of what to do next in the story.
"""

story_text = {
            "start": {
                "text": """
**--------------------------------------------------------------------------**

        You hear the sound of a ticking clock as you start to stir
        in your chair.

        Opening your eyes you see that you're seated opposite a man
        who looks oddly familiar. Uncannily familiar even. Like he
        could be a relative of yours who you haven't seen since you
        were a child. His name tag reads: "W. Navidson". Even the
        name is familiar to you.

        As he notices you wake he raises his eyebrows wordlessly.
        You don't know why you're here. The last thing you can 
        remember before now was...a bathroom? A pale green tiled
        wall..?

        "You gave us quite the scare!" Navidson pipes up after a
        few moments of silence.

        "Can you remember your name?"


**--------------------------------------------------------------------------**
        Option 1: Tell him your name.
        Option 2: Don't answer the question. Ask where you are instead.
**--------------------------------------------------------------------------**
                     """,
                "options": {
                    "option_1": "will",
                    "option_2": "where_am_i"
                }
            },
            "will": {
                        "text": """
**--------------------------------------------------------------------------**
        "Will. My name is Will. Where am I?"

        "Will!", Navidson booms back. "Well, it's nice to finally
        put a name to a face. Especially a face we've been rather
        worried about for a few hours now! Its our job to keep
        an eye on you for a bit, ask you a few questions, find
        out anything you can remember before passing out, make
        sure you're all healthy in the head - that sort of thing!"

        "Well, Will, is there anything you can recall from before
        you passed out?"

        You look around the room. There are two men in shirts and
        ties posted at either side of what seems to be the only 
        door in or out of here. Navidson himself wears a blue
        button-down shirt and navy slacks. The only feature on the
        walls, apart from the one door, looks like one of those
        reflective one-way windows they use in interrogation
        rooms in police stations in the movies. Except the shape
        of it is weird - its longer vertically than it is
        horizontally.

        You have an uneasy feeling as you take all of this in"



**--------------------------------------------------------------------------**
        Option 1: Tell Navidson you don't remember anything
        Option 2: Tell Navidson about the bathroom
**--------------------------------------------------------------------------**
                """,
                "options": {
                    "option_1": "dont_remember",
                    "option_2": "bathroom"
                }
            },
            "where_am_i": {
                        "text": """
**--------------------------------------------------------------------------**

        "Where am I?", you say cautiously. 
        
        "Ah, the cautious type." Navidson remarks with a half-grin 
        Its our job to keep an eye on you for a bit, ask you a few 
        questions, find out anything you can remember before passing 
        out, makesure you're all healthy in the head - that sort of 
        thing!"

        "Well, Will, is there anything you can recall from before
        you passed out?"

        You look around the room. There are two men in shirts and
        ties posted at either side of what seems to be the only 
        door in or out of here. Navidson himself wears a blue
        button-down shirt and navy slacks. The only feature on the
        walls, apart from the one door, looks like one of those
        reflective one-way windows they use in interrogation
        rooms in police stations in the movies. Except the shape
        of it is weird - its longer vertically than it is
        horizontally.

        You have an uneasy feeling as you take all of this in"



**--------------------------------------------------------------------------**
        Option 1: Tell Navidson you don't remember anything
        Option 2: Tell Navidson about the bathroom
**--------------------------------------------------------------------------**
                """,
                "options": {}
                "ending": "1"
            },
            "dont_remember": {
                        "text": """
**--------------------------------------------------------------------------**

        "I don't remember anything, sorry."

        Navidson looks at you, slightly unbelieving.

        "Nothing at all?", he presses you.

**--------------------------------------------------------------------------**
        Option 1: Insist you don't remember anything
        Option 2: Tell Navidson about the bathroom
**--------------------------------------------------------------------------**
                """,
                "options": {
                    "option_1": "still_dont_remember",
                    "option_2": "bathroom"
                }
            },
            "still_dont_remember": {
                        "text": """
**--------------------------------------------------------------------------**
        
        "No, nothing." You insist firmly.

        You look around the room. The small one-directional mirror
        draws your attention now more than ever.

        "Okay", sighs Navidson, resigned, "We just had to be sure!"

**--------------------------------------------------------------------------**
        Option 1: Ask if this is an interrogation
        Option 2: Tell Navidson about the bathroom
**--------------------------------------------------------------------------**
                """,
                "options": {
                    "option_1": "interrogation",
                    "option_2": "bathroom"
                }
            },
            "interrogation": {
                        "text": """
**--------------------------------------------------------------------------**
        
        "Am I being interrogated?" You ask.

        Navidson smiles, a tinge of regret flashing across his
        features.

        "No, you aren't being interrogated. Like I said before:
        we're only asking you these questions for the good of
        your health. You're free to leave at any time."

**--------------------------------------------------------------------------**
        Option 1: Ask to leave now
        Option 2: Tell Navidson about the bathroom
**--------------------------------------------------------------------------**
                """,
                "options": {
                    "option_1": "leave",
                    "option_2": "bathroom"
                }
            },
            "leave": {
                        "text": """
**--------------------------------------------------------------------------**
        
        "Well then I'd like to leave now." You say.

        Navidson smiles again and you seem to almost catch him rolling his eyes.

        "Your call!" He smiles.

        His smile is warm. In spite of how odd this all is, you can't help but
        feel a sense of trust towards him.

        He turns in his chair without standing and nods two the two men by the
        door. The two of them nod back, opening the door and walking out,
        leaving it ajar behind them.

        Navidson stays sitting, half turned towards the open door, as if
        waiting for something to happen. Then, suddenly, as if getting
        the que he was waiting for he sharply swivels his head back around to
        face you. He gets up suddenly moving swiftly across the room to where 
        you're seated, taking something from his pocket as he approaches. 
        He kneels beside you revealing a key he's holding out to you.

        "Okay, Will, this is it." he whispers. "Take the key, look in the
        mirror." he says, holding out the key.

        What do you do?

**--------------------------------------------------------------------------**
        Option 1: Take the key
        Option 2: Dash through the open door behind him
**--------------------------------------------------------------------------**
                """,
                "options": {
                    "option_1": "take_key",
                    "option_2": "dash"
                }
            },

        ***
        FORK!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        FORK!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        FORK!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        FORK!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        FORK!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        FORK!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        ***

        "dash": {
                        "text": """
**--------------------------------------------------------------------------**
        
        You push Navidson hard and make your dash for the door. You're
        not sure what's going on but hell if you're going to stick
        around to find out.

        Navidson falls easily out of your way from the crouched position
        he was in. Your path is clear and you make a dash for the open door.
        As you get close to the door, one of the men in shirts looks in the 
        door and sees you approaching. He sticks out his arms to block the
        door.

        You charge through the open door anyway colliding with the man and
        losing your footing. The two of you tumble to the ground. In moments,
        the second shirted man is also by you and your vision begins to swim.

        As you dip out of consciousness you think you hear Navidson shout
        out in protest for the men to stop in the other room. You lose
        consciousness.

                        ****

        You regain consciousness. It's hard to tell what happened to you
        but as you wake up you notice you're sitting in a private bathroom
        somewhere.

        You get to your feet and make your way to the door, its locked from
        the inside. You must have fainted in here earlier...but why?

        You feel fine, you think.

        You stand up and take a look in the mirror.

        Everything seems normal, but... You're not sure.

        It's as if something is out of place but you can't quite place what.

        You turn on the sink fosset and wash your hands before leaving - who
        knows how long you'd been lying on that floor.

        You unlock the door and walk out into what seems to be a hospital
        ward. Nurses and doctors zip by, the smell of the ward permeates 
        through to unpleasant memories you'd had of hospital visits when
        you were a child. You want to get out of here.

        How did nobody realise you'd been unconscious in a hospital
        bathroom for such a stretch of time. Actually, how long had it been?

        And why were you even visiting a hospital in the first place.

        The more you think about it, the more your brain seems to piece
        things together...but there's still a lingering feeling.

        Like you've missed something.

        It's probably not important.

        Wow, it sure is a nice day out.


        *** ENDING 1/4 *** 
        """
    },

        "take_key": {
                    "text": """
**--------------------------------------------------------------------------**
        
        You don't know why but...something in your gut tells you
        to trust this man. That you need to trust him.

        You take the key.

        Keeping silent, Navidson leans in closer to you and points to the
        wall behind him.

        He's pointing at the mini interrogation window you spotted earlier.

        You get up and aproach it, you need to find out where this is going.

        You look onto the shining surface that caught your eye earlier and
        something that you didn't fully notice earlier clicks for you.

        You can see the room around you reflected in this one-way window,
        the chairs you and Navidson were sitting on, Navidson himself
        watching intently from where he's still crouched down, but you
        aren't in the reflection...

        It's as if some light distortion happens around where you're
        standing.

        Bewildered, you look back to Navidson. He's slowly nodding.

        He gestures back to the reflective surface.

        You turn around to face the mirror again.

        

**--------------------------------------------------------------------------**
        Option 1: 
        Option 2: 
**--------------------------------------------------------------------------**
            """,
                "options": {
                    "option_1": "",
                    "option_2": ""
                }
        },  
}