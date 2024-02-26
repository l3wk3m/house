"""
Here I will store all of the story text and choice prompts
in one dictionary.

The run.py program will call these in and prompt the player with
choices of what to do next in the story.
"""

story_description = {
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
        Option 1: "Will. My name is Will. Where am I?"
        Option 2: "Who are you? Where am I?"
**--------------------------------------------------------------------------**
                     """,
                "options": {
                    "option_1": "will",
                    "option_2": "where_am_I"
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