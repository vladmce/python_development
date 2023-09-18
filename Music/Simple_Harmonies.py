"""
SIMPLE MUSICAL HARMONIES
This program takes as input a note and a chord over which that note is plays.
It outputs the range of harmonies that can be added over that note in order to sound pleasing around the chord.
"""
def input_chord():
    scale = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    scale_string = (" ".join(scale))
    print(f"\nThe possible chords are: {scale_string}")
    while True:
        chord_letter = input("Chose the chord: ")
        if chord_letter in scale:
            break
        else:
            print(f"The available inputs are: {scale_string}")
    return chord_letter

def input_scale_type():
    major_or_minor = ["M", "m"]
    print(f"\nChose M for Major scale or m for minor scale: ")
    while True:
        scale_type = input("Chose the scale: ")
        if scale_type in major_or_minor:
            break
        else:
            print(f"Invalid input. M for Major scale or m for minor scale.")
    return scale_type

def input_tension_existance():
    tension_posibilities = ["7", "0"]
    print(f"\nChose 7 for seven chord or 0 for a simple chord: ")
    while True:
        tension_existance = input("Chose the scale: ")
        if tension_existance in tension_posibilities:
            break
        else:
            print(f"Invalid input. 7 for seven chord or 0 for a simple chord.")
    return tension_existance

def input_root_note():
    scale = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    scale_string = (" ".join(scale))
    print(f"\nThe possible notes are: {scale_string}")
    while True:
        root_note = input("Chose the root note: ")
        if root_note in scale:
            break
        else:
            print(f"The available inputs are: {scale_string}")
    return root_note

def major_chord(starting_note) ->list:
    scale = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    if scale.index(starting_note) > 4:
        scale = scale + scale
        second_note = scale[scale.index(starting_note) + 4]
        third_note = scale[scale.index(starting_note) + 7]
        fourth_note = starting_note
    else:
        second_note = scale[scale.index(starting_note) + 4]
        third_note = scale[scale.index(starting_note) + 7]
        fourth_note = starting_note

    chord = [starting_note, second_note, third_note]
    return chord

def minor_chord(starting_note) ->list:
    scale = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

    if scale.index(starting_note) > 4:
        scale = scale + scale
        second_note = scale[scale.index(starting_note) + 3]
        third_note = scale[scale.index(starting_note) + 7]
    else:
        second_note = scale[scale.index(starting_note) + 3]
        third_note = scale[scale.index(starting_note) + 7]

    chord = [starting_note, second_note, third_note]
    return chord

def seven_major_chord(starting_note) -> list:
    scale = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    scale = scale + scale + scale
    second_note = scale[scale.index(starting_note) + 4]
    third_note = scale[scale.index(starting_note) + 7]
    fourth_note = scale[scale.index(starting_note) + 10]

    chord = [starting_note, second_note, third_note, fourth_note]
    return chord

def seven_minor_chord(starting_note) -> list:
    scale = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    scale = scale + scale + scale
    second_note = scale[scale.index(starting_note) + 3]
    third_note = scale[scale.index(starting_note) + 7]
    fourth_note = scale[scale.index(starting_note) + 10]

    chord = [starting_note, second_note, third_note, fourth_note]
    return chord

chord_letter = input_chord()
scale_type = input_scale_type()
tension_existance = input_tension_existance()
root_note = input_root_note()

def one_note_harmony_simple_chords(scale_type:str, root_note:str, chord_letter:str ) ->list:
    harmony = []
    if scale_type == "M":
        possible_chord = major_chord(chord_letter)
        major_or_minor = "major"
    elif scale_type == "m":
        possible_chord = minor_chord(chord_letter)
        major_or_minor = "minor"

    if root_note in possible_chord:
        if possible_chord.index(root_note) == 0:
            harmony = f"Harmony 1: The upper {major_or_minor} third -> {possible_chord[possible_chord.index(root_note) + 1]} from any " \
                      f"octave.\n" + f"Harmony 2: The upper perfect fifth -> {possible_chord[possible_chord.index(root_note) + 2]} from " \
                      f"any octave.\n" + f"Harmony 3: Octave resonance -> {possible_chord[possible_chord.index(root_note)]} from " \
                      f"an upper or a lower octave."
        elif possible_chord.index(root_note) == 1:
            harmony = f"Harmony 1: The lower {major_or_minor} third -> {possible_chord[possible_chord.index(root_note) - 1]} from any " \
                      f"octave.\n" + f"Harmony 2: The upper {major_or_minor} third -> {possible_chord[possible_chord.index(root_note) + 1]} from " \
                      f"any octave.\n" + f"Harmony 3: Octave resonance -> {possible_chord[possible_chord.index(root_note)]} from " \
                      f"an upper or a lower octave."
        elif possible_chord.index(root_note) == 2:
            harmony = f"Harmony 1: The lower perfect fifth -> {possible_chord[possible_chord.index(root_note) - 2]} from any " \
                      f"octave.\n" + f"Harmony 2: The lower {major_or_minor} third -> {possible_chord[possible_chord.index(root_note) - 1]} from " \
                      f"any octave.\n" + f"Harmony 3: Octave resonance -> {possible_chord[possible_chord.index(root_note)]} from " \
                      f"an upper or a lower octave."
    else:
        harmony = f"Unfortunately, it is impossible to create a strong harmony for the note {root_note} inside the chord {chord_letter} {major_or_minor} as " \
                  f"they are not in resonance with eachother. \nIn order to obtain a good harmony in this case, more context is required."

    return harmony

def one_note_harmony_seven_chords(scale_type:str, root_note:str, chord_letter:str ) ->str:
    if scale_type == "M":
        possible_chord = seven_major_chord(chord_letter)
        major_or_minor = "major"
    elif scale_type == "m":
        possible_chord = seven_minor_chord(chord_letter)
        major_or_minor = "minor"

    if root_note in possible_chord:
        if possible_chord.index(root_note) == 0:
            harmony = f"Harmony 1: The upper {major_or_minor} third -> {possible_chord[possible_chord.index(root_note) + 1]} from any " \
                      f"octave.\n" + f"Harmony 2: The upper perfect fifth -> {possible_chord[possible_chord.index(root_note) + 2]} from " \
                      f"any octave.\n" + f"Harmony 3: The upper chord dominant seventh -> {possible_chord[possible_chord.index(root_note) + 3]} from " \
                      f"any octave.\n" + f"Harmony 4: Octave resonance -> {possible_chord[possible_chord.index(root_note)]} from " \
                      f"an upper or a lower octave."
        elif possible_chord.index(root_note) == 1:
            harmony = f"Harmony 1: The lower {major_or_minor} third -> {possible_chord[possible_chord.index(root_note) - 1]} from any " \
                      f"octave.\n" + f"Harmony 2: The upper third -> {possible_chord[possible_chord.index(root_note) + 1]} from " \
                      f"any octave.\n" + f"Harmony 3: The upper chord dominant seventh -> {possible_chord[possible_chord.index(root_note) + 2]} from " \
                      f"any octave.\n" + f"Harmony 4: Octave resonance -> {possible_chord[possible_chord.index(root_note)]} from " \
                      f"an upper or a lower octave."
        elif possible_chord.index(root_note) == 2:
            harmony = f"Harmony 1: The lower {major_or_minor} third -> {possible_chord[possible_chord.index(root_note) - 1]} from any " \
                      f"octave.\n" + f"Harmony 2: The lower perfect fifth -> {possible_chord[possible_chord.index(root_note) - 2]} from " \
                      f"any octave.\n" + f"Harmony 3: The upper chord dominant seventh -> {possible_chord[possible_chord.index(root_note) + 1]} from " \
                      f"any octave.\n" + f"Harmony 4: Octave resonance -> {possible_chord[possible_chord.index(root_note)]} from " \
                      f"an upper or a lower octave."
        elif possible_chord.index(root_note) == 3:
            harmony = f"Harmony 1: The lower {major_or_minor} third -> {possible_chord[possible_chord.index(root_note) - 1]} from any " \
                      f"octave.\n" + f"Harmony 2: The lower perfect fifth -> {possible_chord[possible_chord.index(root_note) - 2]} from " \
                      f"any octave.\n" + f"Harmony 3: The lower chord dominant seventh -> {possible_chord[possible_chord.index(root_note) - 3]} from " \
                      f"any octave.\n" + f"Harmony 4: Octave resonance -> {possible_chord[possible_chord.index(root_note)]} from " \
                      f"an upper or a lower octave."
    else:
        harmony = f"Unfortunately, it is impossible to create a strong harmony for the note {root_note} inside the chord {chord_letter} {major_or_minor} as " \
                  f"they are not in resonance with eachother. \nIn order to obtain a good harmony in this case, more context is required."

    return harmony


if scale_type == "M":
    if tension_existance == "0":
        harmony = one_note_harmony_simple_chords(scale_type, root_note, chord_letter)
        print(f"\n{harmony}")
    elif tension_existance == "7":
        harmony = one_note_harmony_seven_chords(scale_type, root_note, chord_letter)
        print(f"\n{harmony}")
elif scale_type == "m":
    if tension_existance == "0":
        harmony = one_note_harmony_simple_chords(scale_type, root_note, chord_letter)
        print(f"\n{harmony}")
    elif tension_existance == "7":
        harmony = one_note_harmony_seven_chords(scale_type, root_note, chord_letter)
        print(f"\n{harmony}")

