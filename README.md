# Pentagrom - Visualizing all musical notes in a simple way

__Pentagrom__ and __Sistema Solfeo XXI__ was invented by Jaime Iglesias ([Linkedin](https://es.linkedin.com/in/jaimeiglesias/ "Linkedin Jaime Iglesias Álvaro-Gracia") and [Patent](https://patents.google.com/patent/ES2324268B2/en?assignee=jaime+iglesias&oq=jaime+iglesias)) the musician leading this project.  
Pentagrom allows visualizing all musical notes in an isomorphic, unequivocally, orderly and simple way, which exactly match the way notes are represented in a stave.  

Many papers and documents refer to music visualization as a hard problem to solve, ML algorithms are using some kind of piano roll or midi as the data source and are encoded/decoded piano-based, writing and reading music software has also some issues with mapping notes when using the piano as writing machine, and music has a steep learning rate. We think some of these issues could be solved using this system which gathers and represents information from a stave simpler and better than any other one.  

The PENTAGROM project was created using the new SISTEMA SOLFEO XXI musical theory and notation system based on an array of  
```[(7 rows x constant) x 3 columns] + key signature```  

<img width="344" alt="004" src="https://user-images.githubusercontent.com/1562701/220193613-18896c70-00c0-4397-a332-f274803309cd.png">  
You can add as many arrays (or parts thereof) as one wishes in order to increase the range to be able to represent any written note. 
This system also merges the two major theory systems, the "Traditional system" (Europe) and the "Movable Do system" (i.e. Berklee College of Music) helping anybody to visualize univocally any written note as in a stave, no matter the instrument.    

Nowadays AI is mature enough for bringing models that might allow exploring the whole potential of this system which, hopefully, could improve the ML algorithms, create a better UI and improve the way people understand, read, write, play, and visualize music.  

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

- 7 rows: corresponding to notes of the major scale.  
- constant: representing the number of octaves.  
- 3 columns: the central column contains the notes of the key
signature scale, while the side columns refer to the notes which are
half a tone up and down (normally sharps and flats).  
- Key signature: Enables one to tune the instrument in any key. The
musician can also add more key signatures in addition to the 14
existing ones. Thus giving rise to new music.  

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

