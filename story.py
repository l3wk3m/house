from colorama import Fore


# Here I will store all of the story text and choice prompts
# in one dictionary.

# The format is that each key has a node name, e.g. "start" for the first node
# and an associated value that is itself another dictionary with the keys of
# "text" and "options".

# When the user makes their choice, input to the console, the run.py program
# will record the choice and load up the next node, outputting the value
# associated with that node's "text" key to the terminal, prompting the
# user with their next choices.

# This structure was suggested by my mentor and I used gayatrig19's structure
# for the dictionaries https://github.com/gayatrig19/the-quest-adventures-game/
# which I added to with elements such as prompts that would update the Player
# class's property of whether or not they have acquired a key for a specific
# ending, which is checked against as a win condition for one of the endings


story_text = {
    "start": {
        "text": f"""
- - - - - - - - - - - - ------------------------------- - - - - - - - - - - - -

        You hear the sound of a ticking clock as you start to stir
        in your chair.

        Opening your eyes you see that you're seated opposite a man
        who looks oddly familiar. Uncannily familiar even. Like he
        could be a relative of yours who you haven't seen since you
        were a child. His name tag reads: {Fore.RED}"W. Navidson"{Fore.WHITE}. Even the
        name is familiar to you.

        As he notices you wake he raises his eyebrows wordlessly.
        You don't know why you're here. The last thing you can
        remember before now was...a bathroom? A pale green tiled
        wall..?

        {Fore.RED}"You gave us quite the scare!"{Fore.WHITE} Navidson pipes up after a
        few moments of silence.

        {Fore.RED}"Can you remember your name?"{Fore.WHITE}


- - - - - - - - - - - - ------------------------------- - - - - - - - - - - - -
        Option 1: Tell him your name.
        Option 2: Don't answer the question. Ask where you are instead.
- - - - - - - - - - - - ------------------------------- - - - - - - - - - - - -
                     """,
        "options": {"option_1": "will", "option_2": "where_am_i"},
    },
    "will": {
        "text": f"""
- - - - - - - - - - - - ------------------------------- - - - - - - - - - - - -
        {Fore.GREEN}"Will. My name is Will. Where am I?"{Fore.WHITE}

        {Fore.RED}"Will!"{Fore.WHITE}, Navidson booms back. "Well, it's nice to finally
        put a name to a face. Especially a face we've been rather
        worried about for a few hours now! Its our job to keep
        an eye on you for a bit, ask you a few questions, find
        out anything you can remember before passing out, make
        sure you're all healthy in the head - that sort of thing!"{Fore.WHITE}

        {Fore.RED}"Well, Will, is there anything you can recall from before
        you passed out?"{Fore.WHITE}

        You look around the room. There are two men in shirts and
        ties posted at either side of what seems to be the only
        door in or out of here. The only feature on the
        walls, apart from the one door, looks like one of those
        reflective one-way windows they use in interrogation
        rooms in police stations in the movies. Except the shape
        of it is weird - its longer vertically than it is
        horizontally.

        You have an uneasy feeling as you take all of this in.



- - - - - - - - - - - - ------------------------------- - - - - - - - - - - - -
        Option 1: Tell Navidson you don't remember anything
        Option 2: Tell Navidson about the bathroom
- - - - - - - - - - - - ------------------------------- - - - - - - - - - - - -
                """,
        "options": {"option_1": "dont_remember", "option_2": "bathroom"},
    },
    "where_am_i": {
        "text": f"""
- - - - - - - - - - - - ------------------------------- - - - - - - - - - - - -

        {Fore.GREEN}"Where am I?"{Fore.WHITE}, you say cautiously.

        {Fore.RED}"Ah, the cautious type."{Fore.WHITE} Navidson remarks with a half-grin
        {Fore.RED}"Its our job to keep an eye on you for a bit, ask you a few
        questions, find out anything you can remember before passing
        out, makesure you're all healthy in the head - that sort of
        thing!"{Fore.WHITE}

        {Fore.RED}"Well, Will, is there anything you can recall from before
        you passed out?"{Fore.WHITE}

        You look around the room. There are two men in shirts and
        ties posted at either side of what seems to be the only
        door in or out of here. Navidson himself wears a blue
        button-down shirt and navy slacks. The only feature on the
        walls, apart from the one door, looks like one of those
        reflective one-way windows they use in interrogation
        rooms in police stations in the movies. Except the shape
        of it is weird - its longer vertically than it is
        horizontally.

        You have an uneasy feeling as you take all of this in.



- - - - - - - - - - - - ------------------------------- - - - - - - - - - - - -
        Option 1: Tell Navidson you don't remember anything
        Option 2: Tell Navidson about the bathroom
- - - - - - - - - - - - ------------------------------- - - - - - - - - - - - -
                """,
        "options": {},
        "ending": "1",
    },
    "dont_remember": {
        "text": f"""
- - - - - - - - - - - - ------------------------------- - - - - - - - - - - - -

        {Fore.GREEN}"I don't remember anything, sorry."{Fore.WHITE}

        Navidson looks at you, slightly unbelieving.

        {Fore.RED}"Nothing at all?"{Fore.WHITE}, he presses you.

- - - - - - - - - - - - ------------------------------- - - - - - - - - - - - -
        Option 1: Insist you don't remember anything
        Option 2: Tell Navidson about the bathroom
- - - - - - - - - - - - ------------------------------- - - - - - - - - - - - -
                """,
        "options": {"option_1": "still_dont_remember", "option_2": "bathroom"},
    },
    "still_dont_remember": {
        "text": f"""
- - - - - - - - - - - - ------------------------------- - - - - - - - - - - - -

        {Fore.GREEN}"No, nothing."{Fore.WHITE} You insist firmly.

        You look around the room. The small one-directional mirror
        draws your attention now more than ever.

        {Fore.RED}"Okay"{Fore.WHITE}, sighs Navidson, resigned, {Fore.RED}"We just had to be sure!"{Fore.WHITE}

- - - - - - - - - - - - ------------------------------- - - - - - - - - - - - -
        Option 1: Ask if this is an interrogation
        Option 2: Tell Navidson about the bathroom
- - - - - - - - - - - - ------------------------------- - - - - - - - - - - - -
                """,
        "options": {"option_1": "interrogation", "option_2": "bathroom"},
    },
    "interrogation": {
        "text": f"""
- - - - - - - - - - - - ------------------------------- - - - - - - - - - - - -

        {Fore.GREEN}"Am I being interrogated?"{Fore.WHITE} you ask.

        Navidson smiles, a tinge of regret flashing across his
        features.

        {Fore.RED}"No, you aren't being interrogated. Like I said before:
        we're only asking you these questions for the good of
        your health. You're free to leave at any time."{Fore.WHITE}

- - - - - - - - - - - - ------------------------------- - - - - - - - - - - - -
        Option 1: Ask to leave now
        Option 2: Tell Navidson about the bathroom
- - - - - - - - - - - - ------------------------------- - - - - - - - - - - - -
                """,
        "options": {"option_1": "leave", "option_2": "bathroom"},
    },
    "bathroom": {
        "text": f"""
- - - - - - - - - - - - ------------------------------- - - - - - - - - - - - -

        {Fore.GREEN}"There was...I think I remember...being in a bathroom?"{Fore.WHITE}

        He turns in his chair without standing and nods two the two men by the
        door. The two of them nod back, opening the door and walking out,
        leaving it ajar behind them.

        There's a tension in the air now and you can't decide if honesty
        is really the best policy right now.

        Navidson stays sitting, half turned towards the open door, as if
        waiting for something to happen. Then, suddenly, as if getting
        the que he was waiting for he sharply swivels his head back around to
        face you. He gets up suddenly moving swiftly across the room to where
        you're seated, taking something from his pocket as he approaches.
        He kneels beside you revealing a key he's holding out to you.

        {Fore.RED}"Okay, Will, this is it."{Fore.WHITE} he whispers. {Fore.RED}"Take the key, look in the
        mirror."{Fore.WHITE} he says, holding out the key.

        What do you do?

- - - - - - - - - - - - ------------------------------- - - - - - - - - - - - -
        Option 1: Take the key
        Option 2: Ignore Navidson, lean into your memory. Try remember more.
- - - - - - - - - - - - ------------------------------- - - - - - - - - - - - -
                """,
        "options": {"option_1": "take_key", "option_2": "ignore"},
    },

# This is the choice where the user will end up back in the house 
# WITHOUT the key, guaranteeing ending 4

    "ignore": {
        "text": f"""
- - - - - - - - - - - - ------------------------------- - - - - - - - - - - - -

        You ignore Navidson. You ignore the key.

        You instead lean into your memories. What is this bathroom you can't
        get out of your head?

        You look around and spot that one-way mirror again. But it looks
        different now.

        You get up and aproach it and as you do it seems to change? Its no
        longer a rectangular window, but a mirror. A bathroom mirror. 

        Bewildered, you look back to Navidson. There's nobody there.

        You turn around to face the mirror again and in the reflection...

        It's Mr. Navidson. You. Will Navidson.

        You haven't been trasported to this dingey bathroom, its more like..
        Like you never left the bathroom to begin with. You have to get out
        of here.

        What do you do?

- - - - - - - - - - - - ------------------------------- - - - - - - - - - - - -
        Option 1: Head for the door
        Option 2: Check the room
- - - - - - - - - - - - ------------------------------- - - - - - - - - - - - -
                """,
        "options": {"option_1": "door", "option_2": "check_bathroom"},
        "key": "acquired",
    },
    "leave": {
        "text": f"""
- - - - - - - - - - - - ------------------------------- - - - - - - - - - - - -

        {Fore.GREEN}"Well then I'd like to leave now."{Fore.WHITE} You say.

        Navidson smiles again and you seem to almost catch him rolling
        his eyes.

        {Fore.RED}"Your call!"{Fore.WHITE} He smiles.

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

        {Fore.RED}"Okay, Will, this is it."{Fore.WHITE} he whispers. {Fore.RED}"Take the key, look in the
        mirror."{Fore.WHITE} he says, holding out the key.

        What do you do?

- - - - - - - - - - - - ------------------------------- - - - - - - - - - - - -
        Option 1: Take the key
        Option 2: Dash through the open door behind him
- - - - - - - - - - - - ------------------------------- - - - - - - - - - - - -
                """,
        "options": {"option_1": "take_key", "option_2": "dash"},
    },
    "dash": {
        "text": f"""
- - - - - - - - - - - - ------------------------------- - - - - - - - - - - - -

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

- - - - - - - - - - - - ------------------------------- - - - - - - - - - - - -
        """,
        "options": {},
        "ending": "1",
    },
    "take_key": {
        "text": f"""
- - - - - - - - - - - - ------------------------------- - - - - - - - - - - - -

        You don't know why but...something in your gut tells you
        to trust this man. That you need to trust him.

        You take the key.

        Keeping silent, Navidson leans in closer to you and points to the
        wall behind him.

        He's pointing at the mini interrogation window you spotted earlier.

        You get up and aproach it and as you do it seems to change? Its no
        longer a rectangular window, but a mirror. A bathroom mirror.

        Bewildered, you look back to Navidson. There's nobody there.

        You turn around to face the mirror again and in the reflection...

        It's Mr. Navidson. You. Will Navidson.

        You haven't been trasported to this dingey bathroom, its more like..
        Like you never left the bathroom to begin with. You have to get out
        of here.

        What do you do?

- - - - - - - - - - - - ------------------------------- - - - - - - - - - - - -
        Option 1: Head for the door
        Option 2: Check the room
- - - - - - - - - - - - ------------------------------- - - - - - - - - - - - -
            """,
        "options": {"option_1": "door", "option_2": "check_bathroom"},
        "key": "acquired",
    },
    "door": {
        "text": f"""
- - - - - - - - - - - - ------------------------------- - - - - - - - - - - - -

        You find yourself in a long corridor that disappears off into
        darkness in either direction. But from one direction you can hear...

        Is that...a growling? Like a low thunderous rumble, some sinister
        noise radiates from one end of the hallway.

        Where do you go?

- - - - - - - - - - - - ------------------------------- - - - - - - - - - - - -
        Option 1: Towards the growling
        Option 2: Away from the growling
- - - - - - - - - - - - ------------------------------- - - - - - - - - - - - -
            """,
        "options": {"option_1": "towards", "option_2": "away"},
    },
    "away": {
        "text": f"""
- - - - - - - - - - - - ------------------------------- - - - - - - - - - - - -

        You know what's good for you. Turning away from the growling
        you make down the hallway of the {Fore.BLUE}house{Fore.WHITE}. A place you once upon a
        time recognised as your home, now a hellscape of unexplainable
        endless hallways.

        You run as fast as you can away from the low growling behind you
        but it doesn't seem to get any quiter. As if its keeping pace
        with you.

        All of a sudden, the seemingly infintely long hallway seems to
        terminate in a room. You recognise this room, its your old
        living room. You {Fore.BLUE}house{Fore.WHITE} seems such the distant memory now. But
        you know that door in front of you. The front door. The door out.

        You sprint across the living room.

        All that's on your mind right now is escape.

        You reach the door, what do you do now?

- - - - - - - - - - - - ------------------------------- - - - - - - - - - - - -
        Option 1: Try the door
        Option 2: Use the key
- - - - - - - - - - - - ------------------------------- - - - - - - - - - - - -
            """,
        "options": {"option_1": "open_door", "option_2": "unlock_door"},
    },
    "towards": {
        "text": f"""
- - - - - - - - - - - - ------------------------------- - - - - - - - - - - - -

        Either path down the hallway seems infinitely treacherous.
        Infinitely long. You're not sure if its madness getting the
        better of you, but what even constitutes a 'good' or a 'bad'
        choice any more. Its madness in every direction.

        You walk down the hall towards the growling.

        Its getting louder. And louder. Until gently on your face you
        can feel...something breathing.

        Before you can think what to do next you hear an ear shatteringly
        loud noise and...

- - - - - - - - - - - - ------------------------------- - - - - - - - - - - - -

        █▀▀ ▄▀█ █▀▄▀█ █▀▀   █▀█ █░█ █▀▀ █▀█
        █▄█ █▀█ █░▀░█ ██▄   █▄█ ▀▄▀ ██▄ █▀▄

- - - - - - - - - - - - ------------------------------- - - - - - - - - - - - -
            """,
        "options": {},
        "ending": "2",
    },
    "check_bathroom": {
        "text": f"""
- - - - - - - - - - - - ------------------------------- - - - - - - - - - - - -

        You find yourself coming to in this grimey, tiled-wall
        bathroom.

        Except you're beginning to realise you were never anywhere else.

        Behind you is a door out of the bathroom. Before moving towards
        it you take one last look in the mirror. In the reflection you can
        see a key resting on the sink in front of it. But when you look
        down at the sink in front of the mirror, there's no key where
        the reflection shows there to be.

        What do you do?

- - - - - - - - - - - - ------------------------------- - - - - - - - - - - - -
        Option 1: Head for the door
        Option 2: Check the room
- - - - - - - - - - - - ------------------------------- - - - - - - - - - - - -
            """,
        "options": {"option_1": "door", "option_2": "check_bathroom"},
    },
    "unlock_door": {
        "text": f"""
- - - - - - - - - - - - ------------------------------- - - - - - - - - - - - -

        You try the key in the keyhole. It turns.

        Without taking a beat to look back at the source of the sound
        behind you, you push your way out through the door, the sunlight
        piercing your eyes for the first time in what feels like days.

- - - - - - - - - - - - ------------------------------- - - - - - - - - - - - -
            """,
        "options": {},
        "lock": "try",
        "ending": "3",
    },
    "open_door": {
        "text": f"""
- - - - - - - - - - - - ------------------------------- - - - - - - - - - - - -

        You try open the door, but it's locked!

        The growling sound behind you grows louder...

        What do you do?

- - - - - - - - - - - - ------------------------------- - - - - - - - - - - - -
            """,
        "options": {"option_1": "open_door", "option_2": "wait"},
    },
    "wait": {
        "text": f"""
- - - - - - - - - - - - ------------------------------- - - - - - - - - - - - -

        You've resigned yourself to your fate.

        The door is locked and you have no key.

        All you can do now is...wait...

        Wait for the inevitable.

- - - - - - - - - - - - ------------------------------- - - - - - - - - - - - -

        █▀▀ ▄▀█ █▀▄▀█ █▀▀   █▀█ █░█ █▀▀ █▀█
        █▄█ █▀█ █░▀░█ ██▄   █▄█ ▀▄▀ ██▄ █▀▄

- - - - - - - - - - - - ------------------------------- - - - - - - - - - - - -

            """,
        "options": {},
        "ending": "4",
    },
}
