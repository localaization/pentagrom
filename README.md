# Pentagrom - Music encoder and visualization tool

Focusing on the diatonic scale (which consists of the 7 primary notes
in Western music) without considering any sharps or flats, the list of
individual notes is as follows:
_A,B,C,D,E,F,G_

These are the fundamental note names. By adding sharps or flats (as determined 
by the key signature) and combining them with the octave number, we can represent 
any note in the Western musical system as a matrix of 7x3.
Note names are sorted bottom up, as they would appear in a staff (more about visualization later).
```
    | Flat  | Natural | Sharp |
-------------------------------
G   |   1   |    2   |   3    |
-------------------------------
F   |   4   |    5   |   X    | Ex. X -> F♯
-------------------------------
E   |   7   |    8   |   9    |
-------------------------------
D   |   10  |    X   |  12    | Ex. X -> D
-------------------------------
C   |   13  |   14   |  15    |
-------------------------------
B   |   16  |   17   |  18    |
-------------------------------
A   |   X   |   20   |  21    | Ex. X -> A♭
-------------------------------
```

# Vectorizing
Note Representation:
For any note in its natural, sharp, or flat form, we can set the corresponding element of the vector to 1, and all other elements to 0 (one hot).

For example, for the note F♯:
0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0

For example, for the note A♭:
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0

**Include Octaves**
Assuming we're dealing with common octaves in Western music (for example from C1 to C8), that's 8 different octaves. We can one-hot encode these, adding 8 elements to our vector, where each position corresponds to one of these octaves.

The updated vector length is now:
21(notes) + 8(octaves) = 29.

**Include Key Signatures**
Let's take the 7 main diatonic key signatures based on the natural major scales (C, D, E, F, G, A, B) and their relative minor keys. We can represent each of these major and minor keys with a one-hot encoded value (in this case if there are no flats or sharps as in C Major or A minor, all values will be 0. This is to be discussed)
That's 7(majorkeys) + 7(minorkeys) = 14 key different signatures.
The updated vector length is now: 
29(notes and octaves) + 14(keysignatures) = 43

# Vector Indexing (expanded)
0-20:    Note matrix as before
21-28:   Octaves (C1 to C8)
29-42:   Key signatures (C Major, C Minor, D Major, ... B Major, B Minor)

**Example**
For a note F♯ in the octave 4 and in the key of G Major:

The vector will have a 1 at index 5 (for the F♯ note), a 1 at index 24 (for the 4th octave), and a 1 at index 34 (for G Major). All other elements will be set to 0.
Example Vector for F♯4 in G Major:
...0,0,0,0,0,1,0...∣...0,0,0,0,1,0,0,0...∣...0,0,0,0,0,1,0...0

# How to deal with duration?
Idea: Expand the Vector with Bars of Varying Lengths.
We could define a duration mapping such as:
duration_mapping = {
    'whole': 4,
    'half': 2,
    'quarter': 1
}
which will be used in our (no longer) one hot vector. Taking the same example as before, if F♯ is a "half":              
...0,0,0,0,0,2,0...∣...0,0,0,0,1,0,0,0...∣...0,0,0,0,0,1,0...0


In summary, the model combines the mathematical understanding of music theory with interactive and feedback-based learning tools. This approach can significantly enhance the speed and depth of musical understanding. We think it could be potentially a better way to represent musical notes, for example better than MIDI values.


# Visualization

__Pentagrom__ and __Sistema Solfeo XXI__ was invented by Jaime Iglesias ([Linkedin](https://es.linkedin.com/in/jaimeiglesias/ "Linkedin Jaime Iglesias Álvaro-Gracia") and [Patent](https://patents.google.com/patent/ES2324268B2/en?assignee=jaime+iglesias&oq=jaime+iglesias)), the musician leading this project.  
Pentagrom allows visualizing all musical notes in an isomorphic, unequivocally, orderly and simple way, which exactly match the way notes are represented in a stave. As simple as it looks like, nobody came before with this "pattern".  

Many papers and documents refer to music transcription, translation and visualization as a hard problem to solve, ML algorithms are sometimes piano roll or midi based, and music has a steep learning rate. We think some of these issues could be solved using this system.

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
Discord: https://discord.gg/QurpyU2e  
Project [issues](https://github.com/users/localaization/projects/1)  

## Take a look at this Youtube video example, it will make things clear.
https://www.youtube.com/watch?v=NeP0kQ6tphI

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
Read the issues at https://github.com/users/localaization/projects/1


## This project was first started in 2008 and ended around 2015, we are recovering old information.
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
