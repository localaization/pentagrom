# Pentagrom - A new music system, pitch space, encoder and visualization tool

Please take this writing with a grain of salt, since it is an ongoing project and we are taking notes here to sort them out later.

**Pentagrom** is a research project exploring the role of Machine Learning based on the work done back in 2008 by Jaime Iglesias ([Linkedin](https://es.linkedin.com/in/jaimeiglesias/ "Linkedin Jaime Iglesias Álvaro-Gracia") and [Patent](https://patents.google.com/patent/ES2324268B2/en?assignee=jaime+iglesias&oq=jaime+iglesias)), the musician leading this project.

Pentagrom allows visualizing all musical notes in an isomorphic, unequivocally, orderly and simple way, which exactly match the way notes are represented in a staff. As simple as it looks like, nobody came before with the idea behind it.  

Many papers and documents refer to music transcription, translation and visualization as a hard problem to solve, ML algorithms are sometimes piano roll or midi based, and music has a steep learning rate. We think some of these issues could be solved by combining this "system" and ML as well as simplyfing and improving some mathematical operations[^1] involving music theory and batch notes processing. Some domains that would be applicable might be, as an interface/controler where a note is self described as one position in a matrix, as a one-hot vector for embedings, as a way to represent a richer music vocabulary, CNN as filters and inputs, as a "music writer machine pretictor".

We believe that it could have great impact in education, where people will be able to learn, play, visualize and understand music in a better way.

[^1]: [note2vec](https://github.com/philhchen/note2vec/blob/master/naivemodel/note2vec.ipynb)

# The idea


Focusing on the diatonic scale (which consists of the 7 primary notes
in Western music) without considering any sharps or flats, the list of
individual notes is as follows:
_A,B,C,D,E,F,G_

These are the fundamental note names. By adding sharps or flats (as determined
by the key signature) and combining them with the octave number, we can represent univocally
any written note in the Western musical system as a matrix of 7x3, where the central column represents the
notes in the given key signature, and columns of both sides represent 1/2 tone up or down (usually 
sharps and flats).

Note names are sorted as they would appear in a staff (more about visualization later).

Here we have 3 examples of one note where "Middle C" is C4. For simplicity we are representing
all notes in the same matrix (4th octave in C Major) with the letter "X".

```
     | Flat  | Natural | Sharp |
-------------------------------
B4   |   1   |    2   |   3    |
-------------------------------
A4   |   X   |    5   |   6    | x -> A♭4 | y -> (2,1) | position 4
-------------------------------
G4   |   7   |    8   |   9    |
-------------------------------
F4   |   10  |   11   |   X    | x -> F♯4 | y -> (4,3) | position 12
-------------------------------
E4   |   13  |   14   |  15    |
-------------------------------
D4   |   16  |    X   |  18    | x -> D4  | y -> (6,2) | position 17
-------------------------------
C4   |   19   |   20   |  21   | 
-------------------------------
```
```
Representation of 9 notes in different key signatures

C Major:
Note C is plotted at a deviation of 0.
Note C# is plotted at a deviation of +0.5.
Note C♭ is plotted at a deviation of -0.5

For the key of G Major:
Note F is plotted at a deviation of -0.5 (since G Major has F#).
Note F# is plotted at a deviation of 0.
Note F♭ is plotted at a deviation of -0.5.

For the key of E-flat Major:
Note E is plotted at a deviation of +0.5 (since E-flat Major has E♭).
Note E♭ is plotted at a deviation of 0.
Note E♯ is plotted at a deviation of +0.5.
```
Note: Octaves are just random for the example.
![3D chart representation](https://github.com/localaization/pentagrom/blob/master/assets/3d-pentagrom-representation.jpg)
![Chord representation](https://github.com/localaization/pentagrom/blob/master/assets/3chords.png)



# Vectorizing
Given the note name, alteration (up to double flat and sharp), key signature and octave, all information can be compressed to a single number 
improving other systems such as MIDI since the number maps to a single and univocally note yet preserving all properties and style.
Example:
```
MIDI 61 -> C#4/Db4
Pentagrom 80 -> 21*4 -> C#4
Pentagrom 64 -> 16*4 -> Db4
```
## Note name
N as the note position where N ∈ {C, D, E, F, G, A, B} in this order, without alterations, octave neither key signature (default C major).

Note: We start from bottom up as in a staff.

N = {"C": 1, "D": 2, "E": 3, "F": 4, "G": 5, "A": 6, "B": 7}

Nv = [0,0,0,0,0,0,0]

Example: C4 -> [1, 0, 0, 0, 0, 0, 0]

## Note alteration
M = {"--":-2, "-":-1, "": 0, "#": 1, "##": 2} -> Before applying any key signature. We can compress this to a 3 values once the key signature has been applied:

M = {"-":-1, "": 0, "#": 1}

Example: C4# -> [0, 0, 1]

## Key signature
Let's take the 7 main diatonic key signatures based on the natural major scales (C, D, E, F, G, A, B) and their relative minor keys. We can represent each of these major and minor keys with a one-hot encoded value (in this case if there are no flats or sharps as in C Major or A minor, all values will be 0)
It will hold 15 posible values representing all key signatures. This will act as a "filter" positioning the note in the corresponding place in the "matrix", 
this way we handle up to double sharps and flats, aply the filter and have the note in our "matrix space".
```
Mkey = {
    "C major": [0, 0, 0, 0, 0, 0, 0],
    "G major": [0, 0, 0, 1, 0, 0, 0],
    "D major": [1, 0, 0, 1, 0, 0, 0],
    "A major": [1, 0, 0, 1, 1, 0, 0],
    "E major": [1, 1, 0, 1, 1, 0, 0],
    "B major": [1, 1, 0, 1, 1, 1, 0],
    "F# major": [1, 1, 1, 1, 1, 1, 0],
    "C# major": [1, 1, 1, 1, 1, 1, 1],
    "F major": [0, 0, 0, 0, 0, 0, -1],
    "Bb major": [0, 0, -1, 0, 0, 0, -1],
    "Eb major": [0, 0, -1, 0, 0, -1, -1],
    "Ab major": [0, -1, -1, 0, 0, -1, -1],
    "Db major": [0, 0, -1, -1, -1, -1, -1],
    "Gb major": [0, -1, -1, -1, -1, -1, -1],
    "Cb major": [-1, -1, -1, -1, -1, -1, -1]
}
```
Mkeyv = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

Example: 
F# G major -> Will be mapped to position 11 (within this key, the F# has the position of F) in our matrix, 
position 12 will hold F## (still in our matrix space).

N = [0, 0, 0, 1, 0, 0, 0]

M = [0, 0, 1]

Mkey = [0, 0, 0, 1, 0, 0, 0]

M will be transformed to:

[0, 0, 0, 1, 0, 0, 0]

So the complete information (Work in progress):
Position(i,j)

i = N[note_name]

j = base_notes * (M + Mkey + 2)

Mkey = - base_notes * ((base_notes + key_signature) -1)

We could be handeling more than one note at a time, for simplicity we are doing it for the given example.

base_notes = np.array([0, 0, 0, 1, 0, 0, 0])

M = np.array([0, 0, 0, 1, 0, 0, 0])

key_signature = np.array([0, 0, 0, 1, 0, 0, 0]) # D Mayor

We map the columns from 1 to 3 here, so the number 2 represents the central column and the index in the array represents the row.

Result = [0 0 0 2 0 0 0] -> (4,2)

## Include Octaves

Assuming we're dealing with common octaves in Western music (for example from C1 to C8), that's 8 different octaves. We can one-hot encode these, adding 8 elements to our vector, where each position corresponds to one of these octaves.

O = [0, 0, 0, 0, 0, 0, 0, 0]

# Vector Indexing (expanded)
```
N = [0, 0, 0, 0, 0, 0, 0]
M = [0, 0, 0]
Mkey = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
O = [0, 0, 0, 0, 0, 0, 0, 0]

Our one-hot vector could be:
[0, 0, 0, 0, 0, 0, 0] | [0, 0, 0] | [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] | [0, 0, 0, 0, 0, 0, 0, 0]
```
Bypassing octave and keystring will lead to a much compress format (but we might loose some crucial information about the musician style)

# How to deal with duration?

Idea: Expand the Vector with Bars of Varying Lengths.
We could define a duration mapping such as:

```
duration_mapping = {
    'whole': 4,
    'half': 2,
    'quarter': 1
}
```

which will be used in our (no longer) one hot vector. Taking the same example as before, if F♯ is a "half":

```
...0,0,0,0,0,2,0...∣...0,0,0,0,1,0,0,0...∣...0,0,0,0,0,1,0...0
```

In summary, the model combines the mathematical understanding of music theory with interactive and feedback-based learning tools. This approach can significantly enhance the speed and depth of musical understanding. We think it could be potentially a better way to represent musical notes, for example better than MIDI values.

# Code
We can represent a note as an integer value, a position in a 2D matrix (i, j), a position in a 3D matrix where x and y represent the 7x3 and z the octave. Note that common visualization would be to pile up the 7x3 matrix (as in a piano or piano roll), but piling them up in the z-axis can give as a perfect pattern and a way to process all notes at the same time.

Basic formulas using mostly lookup tables
```
def note_row(note_name):
    # TODO Check whether is better to use N.get(note_name) -> This return None
    # if value does not exist.
    i = N[note_name]
    return i

def note_column(note_name, alteration, keysig = "C major"):
    # TODO Handle exceptions (j < 1 | j > 2.)
    Mkeyvalue = Mkey[keysig][N[note_name]] - 1 
    j = M[alteration] + 2 + Mkeyvalue
    return j
```

Basic formulas using arrays (it can process several notes at a time)
```
We can batch processing all notes of a single octave at a time using arrays as we did in the example at the beggining of this document.
i = index of the note in the array + 1 (if 0 base index)
And "j" as in:

Mkey = - base_notes * ((base_notes + key_signature) -1)
j = base_notes * (M + Mkey + 2)
```

# Visualization


The PENTAGROM project was created using the new SISTEMA SOLFEO XXI musical theory and notation system based on an array of  
```[(7 rows x constant) x 3 columns] + key signature```  

<img width="344" alt="004" src="https://user-images.githubusercontent.com/1562701/220193613-18896c70-00c0-4397-a332-f274803309cd.png">  

- 7 rows: corresponding to notes of the major scale.
- constant: representing the number of octaves.
- 3 columns: the central column contains the notes of the key
signature scale, while the side columns refer to the notes which are
half a tone up and down (normally sharps and flats).
- Key signature: Enables one to tune the instrument in any key. The
musician can also add more key signatures in addition to the 14
existing ones. Thus giving rise to new music.  

You can add as many arrays (or parts thereof) as one wishes in order to increase the range to be able to represent any written note.
This system also merges the two major theory systems, the "Traditional system" (Europe) and the "Movable Do system" (i.e. Berklee College of Music) helping anybody to visualize univocally any written note as in a stave, also provides a mathematical representation which could improve some pitch translations and representations.

Nowadays AI is mature enough for bringing models that might allow exploring the whole potential of this system which, hopefully, could improve them, create a better UI through software and improve the way people understand, read, write, play, and visualize music.  

We would like to open source a model and potentially create a visualizing tool for everybody.  

**We have been granted with some funds and a lot of help from [Algovera.ai](https://app.algovera.ai/), we are creating a team and talking about it here:**  
Discord: <https://discord.gg/QurpyU2e>  
Project [issues](https://github.com/users/localaization/projects/1)  

## Take a look at this Youtube video example, it will make things clear
<https://www.youtube.com/watch?v=NeP0kQ6tphI>

## Patent

[<https://patents.google.com/patent/ES2324268B2/es?assignee=jaime+iglesias&oq=jaime+iglesias>](https://patents.google.com/patent/ES2324268B2/en?assignee=jaime+iglesias&oq=jaime+iglesias)

<img width="344" alt="pentagrom-presentation-000" src="https://user-images.githubusercontent.com/122649944/220181956-6a56ecad-04b9-4ad2-8e94-e9188135110a.png">

### Unifies both systems

<img width="344" alt="pentagrom-presentation-001" src="https://user-images.githubusercontent.com/122649944/220186883-d19e750f-b4e5-4a4c-8bf1-9e50e6c5e5ff.png">

<img width="344" alt="pentagrom-presentation-002" src="https://user-images.githubusercontent.com/122649944/220186959-6b6dfcc6-6868-4556-8b67-9e8f6fd459f8.png">

<img width="344" alt="pentagrom-presentation-003" src="https://user-images.githubusercontent.com/122649944/220186990-38a29bcf-dbbe-4de0-a2f2-9c702266c41b.png">

### Isomorphic

Key signature enables transposition  
<img width="344" alt="005" src="https://user-images.githubusercontent.com/1562701/220193566-1fe63fc1-7cda-4575-b6a4-133d422a5961.png">

<img width="344" alt="005" src="https://user-images.githubusercontent.com/122649944/220493127-c6c024f5-466f-4073-8fbd-968b69f9da70.png">

### Maps univocally any written note

<img width="271" alt="pentagrom-presentation-010" src="https://user-images.githubusercontent.com/122649944/220187552-a85d407d-e761-47f3-b8c2-18343aab9e0e.png">

## Docs

Take a look at the [/docs](https://github.com/localaization/pentagrom/tree/master/docs) folder in this repo for a summary presentation.

## Project Issues  

Read the issues at <https://github.com/users/localaization/projects/1>

## This project was first started in 2008 and ended around 2015, we are recovering old information

**Jaime** (the inventor) is not longer in possesion of the rrss, web domain and other media channels. We are starting to recover as much information as we can.

Trying to recover ownership - [Youtube channel](https://www.youtube.com/@pentagrom_es2489/videos)  
Trying to recover ownership - [Twiter](https://twitter.com/Pentagrom)  
Archived - [Website](https://web.archive.org/web/20140518132131/http://www.pentagrom.com/)  
Trying to recover ownership - [Pentagrom web](https://www.pentagrom.com)

## References (besides the patent links)  

- Redit - Piano roll VS. traditional notation ..? - [https://www.reddit.com/r/musictheory/comments/4p010u/piano_roll_vs_traditional_notation/](https://www.reddit.com/r/musictheory/comments/4p010u/piano_roll_vs_traditional_notation/)
- The Ehan Heing Blog - [https://www.ethanhein.com/wp/2011/visualizing-music/](https://www.ethanhein.com/wp/2011/visualizing-music/)
- Music Computing and Psychology Lab - [https://tomcollinsresearch.net/](https://tomcollinsresearch.net/)
- THE CHAMBER ENSEMBLE GENERATOR:LIMITLESS HIGH-QUALITY MIR DATA VIA GENERATIVE MODELING - [https://arxiv.org/pdf/2209.14458.pdf](https://arxiv.org/pdf/2209.14458.pdf)
- MIDI-DDSP: DETAILED CONTROL OF MUSICAL PERFORMANCE VIA HIERARCHICAL MODELING - [https://openreview.net/pdf](https://openreview.net/pdf)
- Discover Music - [https://discover-music.glitch.me/](https://discover-music.glitch.me/)
- Magenta - The Chamber Ensemble Generator and CocoChorales Dataset - [https://magenta.tensorflow.org/ceg-and-cocochorales](https://magenta.tensorflow.org/ceg-and-cocochorales)
- Magenta - The MAESTRO Dataset and Wave2Midi2Wave - [https://magenta.tensorflow.org/maestro-wave2midi2wave](https://magenta.tensorflow.org/maestro-wave2midi2wave)
- Magenta - MusicVAE: Creating a palette for musical scores with machine learning - [https://magenta.tensorflow.org/music-vae](https://magenta.tensorflow.org/music-vae)
- NSYNTH - [https://experiments.withgoogle.com/ai/sound-maker/view/](https://experiments.withgoogle.com/ai/sound-maker/view/)
- Modelling Symbolic Music: Beyond the Piano Roll - [https://arxiv.org/pdf/1606.01368.pdf](https://arxiv.org/pdf/1606.01368.pdf)
- Deep Learning for Music - [https://arxiv.org/pdf/1606.04930.pdf](https://arxiv.org/pdf/1606.04930.pdf)
- Deep Learning Techniques for Music Generation – A Survey - [https://arxiv.org/pdf/1709.01620.pdf](https://arxiv.org/pdf/1709.01620.pdf)
- This Time with Feeling: Learning Expressive Musical Performance - [https://arxiv.org/pdf/1808.03715v1.pdf](https://arxiv.org/pdf/1808.03715v1.pdf)
- Artificial neural networks based models for automatic performance of musical scores - [https://www.researchgate.net/publication/257810708_Artificial_neural_networks_based_models_for_automatic_performance_of_musical_scores](https://www.researchgate.net/publication/257810708_Artificial_neural_networks_based_models_for_automatic_performance_of_musical_scores)
- A NOTE ON THE EVALUATION OF GENERATIVE MODELS - [https://arxiv.org/pdf/1511.01844.pdf](https://arxiv.org/pdf/1511.01844.pdf)
- COUNTERPOINT BY CONVOLUTION - [https://arxiv.org/pdf/1903.07227.pdf](https://arxiv.org/pdf/1903.07227.pdf)
- MUSIC TRANSFORMER: GENERATING MUSIC WITH LONG-TERM STRUCTURE - [https://arxiv.org/pdf/1809.04281.pdf#page=10&zoom=100,110,540](https://arxiv.org/pdf/1809.04281.pdf#page=10&zoom=100,110,540)
- Glithch - [https://glitch.com/](https://glitch.com/)
- librosa: Audio and Music Signal Analysis in Python - [https://conference.scipy.org/proceedings/scipy2015/pdfs/brian_mcfee.pdf](https://conference.scipy.org/proceedings/scipy2015/pdfs/brian_mcfee.pdf)
- ONSETS AND FRAMES: DUAL-OBJECTIVE PIANO TRANSCRIPTION - [https://arxiv.org/pdf/1710.11153.pdf](https://arxiv.org/pdf/1710.11153.pdf)
- Encoding Musical Style with Transformer Autoencoders - [https://arxiv.org/pdf/1912.05537.pdf](https://arxiv.org/pdf/1912.05537.pdf)
- Visualizing Music Self-Attention - [https://openreview.net/pdf](https://openreview.net/pdf)
- Visualizing Music Transformer - [https://storage.googleapis.com/nips-workshop-visualization/index.html](https://storage.googleapis.com/nips-workshop-visualization/index.html)
- MuseMorphose: Full-Song and Fine-Grained Piano Music Style Transfer with One Transformer VAE - [https://arxiv.org/abs/2105.04090](https://arxiv.org/abs/2105.04090)
- ISMIR 2018 - Session A - [https://www.youtube.com/live/w-fsuRbAVuo?feature=share](https://www.youtube.com/live/w-fsuRbAVuo?feature=share)
- Humdrum - Basic Pitch Translations - [https://www.humdrum.org/guide/ch04/](https://www.humdrum.org/guide/ch04/)
- Humdrum - Searching for Patterns - [https://www.humdrum.org/guide/ch21/](https://www.humdrum.org/guide/ch21/)
- School of Physics Sydney, Australia - Note names, MIDI numbers and frequencies - [http://www.phys.unsw.edu.au/jw/notes.html](http://www.phys.unsw.edu.au/jw/notes.html)
- Digilent - Music Theory Basics - [https://learn.digilentinc.com/Documents/400](https://learn.digilentinc.com/Documents/400)
- Roger N. Sephard - Geometrical Approximations to the Structure of Musical Pitch - [http://psych.colorado.edu/~lharvey/P5665%20Prosem/P5665_2016/Class%20Material/Weekly_Readings/11%20(1982)%20Shepard%20PsychologicalReview.pdf](http://psych.colorado.edu/~lharvey/P5665%20Prosem/P5665_2016/Class%20Material/Weekly_Readings/11%20(1982)%20Shepard%20PsychologicalReview.pdf)
- Audiolabs Erlangen - Sheet Music Representations - [https://www.audiolabs-erlangen.de/resources/MIR/FMP/C1/C1S1_SheetMusic.html](https://www.audiolabs-erlangen.de/resources/MIR/FMP/C1/C1S1_SheetMusic.html)
