from flask import Flask, render_template, request

# C Major / A minor (no sharps or flats)
# G Major / E minor (1 sharp: F♯)
# D Major / B minor (2 sharps: F♯, C♯)
# A Major / F♯ minor (3 sharps: F♯, C♯, G♯)
# E Major / C♯ minor (4 sharps: F♯, C♯, G♯, D♯)
# B Major / G♯ minor (5 sharps: F♯, C♯, G♯, D♯, A♯)
# F♯ Major / D♯ minor (6 sharps: F♯, C♯, G♯, D♯, A♯, E♯)
# C♯ Major / A♯ minor (7 sharps: F♯, C♯, G♯, D♯, A♯, E♯, B♯)
# F Major / D minor (1 flat: B♭)
# B♭ Major / G minor (2 flats: B♭, E♭)
# E♭ Major / C minor (3 flats: B♭, E♭, A♭)
# A♭ Major / F minor (4 flats: B♭, E♭, A♭, D♭)
# D♭ Major / B♭ minor (5 flats: B♭, E♭, A♭, D♭, G♭)
# G♭ Major / E♭ minor (6 flats: B♭, E♭, A♭, D♭, G♭, C♭)
# C♭ Major / A♭ minor (7 flats: B♭, E♭, A♭, D♭, G♭, C♭, F♭)

app = Flask(__name__)

# Define a custom Jinja2 filter for enumeration
def jinja2_enumerate(iterable, start=0):
    return enumerate(iterable, start=start)

# Add the filter to Jinja2 environment
app.jinja_env.filters['enumerate'] = jinja2_enumerate

KEY_SIGNATURES = {
    'C Major': [
        ['B-', 'B', 'B#'],
        ['A-', 'A', 'A#'],
        ['G-', 'G', 'G#'],
        ['F-', 'F', 'F#'],
        ['E-', 'E', 'E#'],
        ['D-', 'D', 'D#'],
        ['C-', 'C', 'C#']
    ],
    'G Major': [ # G Major / E minor (1 sharp: F♯)
        ['B-', 'B', 'B#'],
        ['A-', 'A', 'A#'],
        ['G-', 'G', 'G#'],
        ['F', 'F#', 'F##'],
        ['E-', 'E', 'E#'],
        ['D-', 'D', 'D#'],
        ['C-', 'C', 'C#'],
    ],
    'D Major': [ # D Major / B minor (2 sharps: F♯, C♯)
        ['B-', 'B', 'B#'],
        ['A-', 'A', 'A#'],
        ['G-', 'G', 'G#'],
        ['F', 'F#', 'F##'],
        ['E-', 'E', 'E#'],
        ['D', 'D#', 'D##'],
        ['C-', 'C', 'C#'],
    ],
    'A Major': [ # A Major / F♯ minor (3 sharps: F♯, C♯, G♯)
        ['B-', 'B', 'B#'],
        ['A-', 'A', 'A#'],
        ['G', 'G#', 'G##'],
        ['F', 'F#', 'F##'],
        ['E-', 'E', 'E#'],
        ['D', 'D#', 'D##'],
        ['C-', 'C', 'C#'],

    ],
    'E Major': [ # E Major / C♯ minor (4 sharps: F♯, C♯, G♯, D♯)
        ['B-', 'B', 'B#'],
        ['A-', 'A', 'A#'],
        ['G', 'G#', 'G##'],
        ['F', 'F#', 'F##'],
        ['E-', 'E', 'E#'],
        ['D', 'D#', 'D##'],
        ['C', 'C#', 'C##'],
    ],
    'B Major': [ # B Major / G♯ minor (5 sharps: F♯, C♯, G♯, D♯, A♯
        ['B', 'B#', 'B##'],
        ['A', 'A#', 'A##'],
        ['G', 'G#', 'G##'],
        ['F', 'F#', 'F##'],
        ['E', 'E#', 'E##'],
        ['D', 'D#', 'D##'],
        ['C-', 'C', 'C#'],
    ],
    'F- Major': [ # F♯ Major / D♯ minor (6 sharps: F♯, C♯, G♯, D♯, A♯, E♯)
        ['B-', 'B', 'B#'],
        ['A', 'A#', 'A##'],
        ['G', 'G#', 'G##'],
        ['F', 'F#', 'F##'],
        ['E', 'E#', 'E##'],
        ['D', 'D#', 'D##'],
        ['C', 'C#', 'C##'],
    ],
    'C- Major': [ #		C♯ Major / A♯ minor (7 sharps: F♯, C♯, G♯, D♯, A♯, E♯, B♯)
        ['B', 'B#', 'B##'],
        ['A', 'A#', 'A##'],
        ['G', 'G#', 'G##'],
        ['F', 'F#', 'F##'],
        ['E', 'E#', 'E##'],
        ['D', 'D#', 'D##'],
        ['C', 'C#', 'C##'],
    ],
    'F Major': [ #		F Major / D minor (1 flat: B♭)
        ['B', 'B#', 'B##'],
        ['A', 'A#', 'A##'],
        ['G', 'G#', 'G##'],
        ['F', 'F#', 'F##'],
        ['E', 'E#', 'E##'],
        ['D', 'D#', 'D##'],
        ['C', 'C#', 'C##'],
    ],
    'B- Major': [ #		B♭ Major / G minor (2 flats: B♭, E♭)
        ['B--', 'B-', 'B'],
        ['A-', 'A', 'A#'],
        ['G-', 'G', 'G#'],
        ['F-', 'F', 'F#'],
        ['E--', 'E-', 'E'],
        ['D-', 'D', 'D#'],
        ['C-', 'C', 'C#'],
    ],
    'E- Major': [ #		E♭ Major / C minor (3 flats: B♭, E♭, A♭)
        ['B--', 'B-', 'B'],
        ['A--', 'A-', 'A'],
        ['G-', 'G', 'G#'],
        ['F-', 'F', 'F#'],
        ['E--', 'E-', 'E'],
        ['D-', 'D', 'D#'],
        ['C-', 'C', 'C#'],
    ],
    'A- Major': [ # 		A♭ Major / F minor (4 flats: B♭, E♭, A♭, D♭)
        ['B--', 'B-', 'B'],
        ['A--', 'A-', 'A'],
        ['G-', 'G', 'G#'],
        ['F--', 'F-', 'F'],
        ['E--', 'E-', 'E'],
        ['D-', 'D', 'D#'],
        ['C-', 'C', 'C#'],
    ],
    'D- Major': [ # 		D♭ Major / B♭ minor (5 flats: B♭, E♭, A♭, D♭, G♭)
        ['B--', 'B-', 'B'],
        ['A--', 'A-', 'A'],
        ['G--', 'G-', 'G'],
        ['F--', 'F-', 'F'],
        ['E--', 'E-', 'E'],
        ['D-', 'D', 'D#'],
        ['C-', 'C', 'C#'],
    ],
    'G- Major': [ # 		G♭ Major / E♭ minor (6 flats: B♭, E♭, A♭, D♭, G♭, C♭)
        ['B--', 'B-', 'B'],
        ['A--', 'A-', 'A'],
        ['G--', 'G-', 'G'],
        ['F--', 'F-', 'F'],
        ['E--', 'E-', 'E'],
        ['D--', 'D-', 'D'],
        ['C-', 'C', 'C#'],
    ],
    'C- Major': [ # 		C♭ Major / A♭ minor (7 flats: B♭, E♭, A♭, D♭, G♭, C♭, F♭)
        ['B--', 'B-', 'B'],
        ['A--', 'A-', 'A'],
        ['G--', 'G-', 'G'],
        ['F--', 'F-', 'F'],
        ['E--', 'E-', 'E'],
        ['D--', 'D-', 'D'],
        ['C--', 'C-', 'C'],
    ]
}

def build_matrix(note, key_signature='C Major'):
    matrix = KEY_SIGNATURES[key_signature]
    position = None
    note_position = None

    note = note.upper()

    for row_index, row in enumerate(matrix):
        if note in row:
            position = row_index
            note_position = row.index(note)
            break
    return matrix, position, note_position

@app.route('/', methods=['GET', 'POST'])
def index():
    key_signature = 'C Major'
    matrix = KEY_SIGNATURES[key_signature]
    position = None
    note_position = None
    custom_note = ''  # Initialize custom_note with an empty string

    if request.method == 'POST':
        custom_note = request.form.get('custom_note')
        key_signature = request.form.get('key_signature')
        matrix, position, note_position = build_matrix(custom_note, key_signature)

    return render_template(
        'index.html', 
        key_signature=key_signature, 
        matrix=matrix, 
        position=position,
        note_position=note_position,
        row_indices=range(len(matrix)),  # Pass row indices to the template
        key_signatures=KEY_SIGNATURES,
        custom_note=custom_note  # Pass the custom_note value to the template
    )

if __name__ == '__main__':
    app.run(debug=True)