
"""
COMPLEX MUSICAL HARMONIES / SONG MUSICAL HARMONIES
import pygame
import numpy
import math

C Scale = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
* Step 1. Inputs: This program takes as input a series of notes, chords and durations, following the next format:
    note = [root_note, chord_letter, chord_scale, tension_existance, duration]
    where:  -> note represents an input list
            -> root_note represents the base note [C to B]
            -> chord letter represents the chord name [C to B]
            -> chord_scale represents the type of scale major or minor [M or m]
            -> tension existence represents the possible seventh character of the chord [0 or 7]
    Example 1: note = [C#, D, m, 0, 1] -> C# is the note we want to harmonize over the chord D minor for a whole measure.
    Example 2: note = [A, G, M, 7, 0.25] -> A is the note we want to harmonize over the chord G Major 7 for a quarter of a measure.
    Example 3: note = [G, D, m, 7, 0.5] -> G is the note we want to harmonize over the chord D minor 7 for half of a measure.
* Step 2. The harmonies will be generated with P_MUS_2_SimpleMusicalHarmonies.py program for all the root notes that are in resonance
with the chord they are played over. A new list will be created, containing all the harmonies for each root_note.
    Example 1:  notes = [[C, C, M, 0, 1], [E, C, M, 0, 1], [E, C, M, 7, 1], [A, F ,M, 0, 1]]
                harmonies = [E, G, A#, F] <- in this case, all root notes were in resonance so the harmonies were easy to deduce
    Example 2:  notes = [[C, C, M, 0, 1], [E, C, M, 0, 1], [D#, C, M, 0, 1], [A, F ,M, 0, 1]]
                harmonies = [E, G, 0, F] <- in this case, the third root note weren't in resonance so a 0 appeared in the harmony list
    This "0" will further inform the program that the work is not complete.
* Step 3.
It outputs a list in which each element is a sub list of two items: the root note and the harmony note.
"""

possible_notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
possible_chords = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
possible_scales = ["major", "minor"]
possible_tension = ["0", "7"]
possible_duration = ["1", "0.75", "0.5", "0.25"]
song_line = [] # Contains all information about the song
all_root_notes = [] # Contains all root notes
all_chords = []
all_scales = []
all_tensions = []
all_durations = []

while True:
    while True:
        note = input("Input the root note, chord, scale and tension sepparated by spaces: ")
        note = note.split()
        if note[0] in possible_chords and note[1] in possible_chords and note[2] in possible_scales and note[3] in possible_tension:
            song_line.append(note)
            break
        else:
            pass
    done = input("Write x if you have finished. Press enter to continue: ")
    if done == "x":
        break
    else:
        pass

for sublist in song_line:
    if len(sublist) > 0:
        root_note = sublist[0]
        all_root_notes.append(root_note)

for sublist in song_line:
    if len(sublist) > 0:
        chord = sublist[1]
        all_chords.append(chord)

for sublist in song_line:
    if len(sublist) > 0:
        scale = sublist[2]
        all_scales.append(scale)

for sublist in song_line:
    if len(sublist) > 0:
        tension = sublist[3]
        all_tensions.append(tension)

harmonies = []
# print(all_root_notes)
# print(all_chords)
# print(all_scales)
# print(all_tensions)
# print(all_durations)

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

    full_chord = [starting_note, second_note, third_note]
    return full_chord

def minor_chord(starting_note) ->list:
    scale = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

    if scale.index(starting_note) > 4:
        scale = scale + scale
        second_note = scale[scale.index(starting_note) + 3]
        third_note = scale[scale.index(starting_note) + 7]
    else:
        second_note = scale[scale.index(starting_note) + 3]
        third_note = scale[scale.index(starting_note) + 7]

    full_chord = [starting_note, second_note, third_note]
    return full_chord

def seven_major_chord(starting_note) -> list:
    scale = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    scale = scale + scale + scale
    second_note = scale[scale.index(starting_note) + 4]
    third_note = scale[scale.index(starting_note) + 7]
    fourth_note = scale[scale.index(starting_note) + 10]

    full_chord = [starting_note, second_note, third_note, fourth_note]
    return full_chord

def seven_minor_chord(starting_note) -> list:
    scale = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    scale = scale + scale + scale
    second_note = scale[scale.index(starting_note) + 3]
    third_note = scale[scale.index(starting_note) + 7]
    fourth_note = scale[scale.index(starting_note) + 10]

    full_chord = [starting_note, second_note, third_note, fourth_note]
    return full_chord


def one_note_harmony_simple_chords(scale_type:str, root_note:str, chord_letter:str ):
    if scale_type == "major":
        possible_chord = major_chord(chord_letter)
        major_or_minor = "major"
    elif scale_type == "minor":
        possible_chord = minor_chord(chord_letter)
        major_or_minor = "minor"

    if root_note in possible_chord:
        if possible_chord.index(root_note) == 0:
            harmony = possible_chord[possible_chord.index(root_note) + 1]
        elif possible_chord.index(root_note) == 1:
            harmony = possible_chord[possible_chord.index(root_note) + 1]
        elif possible_chord.index(root_note) == 2:
            harmony = possible_chord[possible_chord.index(root_note) - 2]
    else:
        harmony = "0"

    return harmony

def one_note_harmony_seven_chords(scale_type:str, root_note:str, chord_letter:str ) ->str:
    if scale_type == "major":
        possible_chord = seven_major_chord(chord_letter)
    elif scale_type == "minor":
        possible_chord = seven_minor_chord(chord_letter)

    if root_note in possible_chord:
        if possible_chord.index(root_note) in [0, 1, 2] :
            harmony = possible_chord[3]
        elif possible_chord.index(root_note) == 3:
            harmony = possible_chord[2]
    else:
        harmony = "0"

    return harmony

for i in range(len(all_root_notes)):
    if all_scales[i] == "major":
        if all_tensions[i] == "0":
            harmonies.append(one_note_harmony_simple_chords(all_scales[i], all_root_notes[i], all_chords[i]))
        elif all_tensions[i] == "7":
            harmonies.append(one_note_harmony_seven_chords(all_scales[i], all_root_notes[i], all_chords[i]))
    elif all_scales[i] == "minor":
        if all_tensions[i] == "0":
            harmonies.append(one_note_harmony_simple_chords(all_scales[i], all_root_notes[i], all_chords[i]))
        elif all_tensions[i] == "7":
            harmonies.append(one_note_harmony_seven_chords(all_scales[i], all_root_notes[i], all_chords[i]))

final_song = []

for i in range(len(all_root_notes)):
    note_and_harmony = all_root_notes[i] + "/" + harmonies[i]
    final_song.append(note_and_harmony)

final_song = " ".join(final_song)
print(f"The harmonies are: {final_song}")


frequencies = [261.63, 277.18, 293.66, 311.13, 329.63, 349.23, 369.99, 415.30, 440.00, 466.16, 493.88]


