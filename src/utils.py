def detect_monophony(midi_data):
    print_str = []
    monop_count = 0
    for ins in midi_data.instruments:
        if not ins.is_drum:
            ins_name = pretty_midi.program_to_instrument_name(ins.program)

            prev_note = ins.notes[0]
            is_monophonic = True
            for temp_note in ins.notes[1:]:
                if prev_note.end <= temp_note.start:
                    prev_note = temp_note
                else:
                    is_monophonic = False
                    break

            print_str.append(f'{ins_name}: {is_monophonic}')
            if is_monophonic:
                monop_count += 1

    return print_str,monop_count


def is_fourfour(midi_data):
    sig_ch = midi_data.time_signature_changes

    flag_fourfour = False
    if len(sig_ch) == 1:
        num,den = sig_ch[0].numerator, sig_ch[0].denominator
        if num == 4 and den == 4:
            flag_fourfour = True
    
    return flag_fourfour



def plot_piano_roll(pm, start_pitch, end_pitch, fs=100):
    # Use librosa's specshow function for displaying the piano roll
    librosa.display.specshow(pm.get_piano_roll(fs)[start_pitch:end_pitch],
                             hop_length=1, sr=fs, x_axis='time', y_axis='cqt_note',
                             fmin=pretty_midi.note_number_to_hz(start_pitch))