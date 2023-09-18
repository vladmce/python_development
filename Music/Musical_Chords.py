"""
MUSICAL CHORDS
This program takes as input a root musical note and outputs four different chords that can be used with that root note.
-> MAJOR chords - create a happy, enjoyable vibe
-> MINOR chords - create a melancholic, nostalgic or even sad mood
-> MINOR or MAJOR SEVEN chords - create tension and are usually used in transition between two dominant chords
        'more on SEVEN chords on a special software soon to be developed'
"""

def starting_note_input():
    scale = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    scale_string = (" ".join(scale))
    print(f"\nThe possible notes are: {scale_string}")
    while True:
        starting_note = input("Chose the starting note of the chord: ")
        if starting_note in scale:
            break
        else:
            print(f"The available inputs are: {scale_string}")
    return starting_note
def major_chord(starting_note) -> str:
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

    chord = [starting_note, second_note, third_note, fourth_note]
    chord = " / ".join(chord)
    return chord

def minor_chord(starting_note) -> str:
    scale = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

    if scale.index(starting_note) > 4:
        scale = scale + scale
        second_note = scale[scale.index(starting_note) + 3]
        third_note = scale[scale.index(starting_note) + 7]
        fourth_note = starting_note
    else:
        second_note = scale[scale.index(starting_note) + 3]
        third_note = scale[scale.index(starting_note) + 7]
        fourth_note = starting_note

    chord = [starting_note, second_note, third_note, fourth_note]
    chord = " / ".join(chord)
    return chord

def seven_major_chord(starting_note) -> str:
    scale = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    scale = scale + scale + scale
    second_note = scale[scale.index(starting_note) + 4]
    third_note = scale[scale.index(starting_note) + 7]
    fourth_note = scale[scale.index(starting_note) + 10]

    chord = [starting_note, second_note, third_note, fourth_note]
    chord = " / ".join(chord)
    return chord

def seven_minor_chord(starting_note) -> str:
    scale = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    scale = scale + scale + scale
    second_note = scale[scale.index(starting_note) + 3]
    third_note = scale[scale.index(starting_note) + 7]
    fourth_note = scale[scale.index(starting_note) + 10]

    chord = [starting_note, second_note, third_note, fourth_note]
    chord = " / ".join(chord)
    return chord

def major_harmony(starting_note):
    scale = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    scale = scale + scale
    major_harmony_value = scale[scale.index(starting_note) + 4]
    return major_harmony_value

def minor_harmony(starting_note):
    scale = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    scale = scale + scale
    minor_harmony_value = scale[scale.index(starting_note) + 3]
    return minor_harmony_value

starting_note = starting_note_input()
print(f"\nThe major chord of {starting_note} is: {major_chord(starting_note)}. Use this to create a happy, enjoyable vibe.")
print(f"The minor chord of {starting_note} is: {minor_chord(starting_note)}. Use this to create a nostalgic or sad mood.")
print(f"The major seven chord of {starting_note} is: {seven_major_chord(starting_note)}. Use this to add tension to your song.")
print(f"The minor seven chord of {starting_note} is: {seven_minor_chord(starting_note)}. Use this to add tension to your song.")





