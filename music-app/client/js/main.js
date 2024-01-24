// Establish WebSocket connection
const socket = new WebSocket('ws://localhost:8080');
const notesContainer = document.getElementById('notes');
const notes = ['Bb', 'B', 'Bs', 'Ab', 'A', 'As', 'Gb', 'G', 'Gs', 'Fb', 'F', 'Fs', 'Eb', 'E', 'Es', 'Db', 'D', 'Ds', 'Cb', 'C', 'Cs'];

// Object to store audio objects for each note
const audioFiles = {};

// Preload audio files for each note
notes.forEach(note => {
    audioFiles[note] = new Audio(`audio/${note}.wav`);
});

// Create and display note circles
notes.forEach(note => {
    let circle = document.createElement('div');
    circle.classList.add('circle');
    circle.setAttribute('data-note', note);
    circle.textContent = note;
    circle.onclick = () => sendNote(note);
    notesContainer.appendChild(circle);
});

function sendNote(note) {
    if (socket.readyState === WebSocket.OPEN) {
        // console.log('Sending note:', note);
        socket.send(note);
        // Optionally play sound on sender's side
        playSound(note);
    } else {
        console.error("WebSocket is not open.");
    }
}

socket.onmessage = function(event) {
    // console.log('Note received:', event.data);
    playSound(event.data);
};

function playSound(note) {
    if (typeof note === 'object' && note instanceof Blob) {
        // Convert Blob to text
        note.text().then(textNote => {
            playNoteSound(textNote);
        });
    } else {
        // Directly play the note
        playNoteSound(note);
    }
}

// Function to play sound for a given note
function playNoteSound(note) {
    if (audioFiles[note]) {
        // Find the corresponding circle element
        const noteElement = document.querySelector(`.circle[data-note='${note}']`);
        noteElement.classList.add('active');

        audioFiles[note].currentTime = 0;
        audioFiles[note].play();

        // Remove the active class when the sound ends
        audioFiles[note].onended = () => {
            noteElement.classList.remove('active');
        };
    } else {
        console.error('Audio file for note not found:', note);
    }
}

