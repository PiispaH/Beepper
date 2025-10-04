import subprocess


def beep(vol: float = 1.0) -> None:
    """Makes noise, non-blocking."""
    vol = max(0.1, min(2, vol))
    notes = [
        (440.0, 0.2),
        (554.365, 0.2),
        (659.255, 0.2),
        (880.0, 0.4),
        (659.255, 0.2),
        (880.0, 0.8),
    ]

    synth_sequence = " : ".join(
        f"synth {duration*0.7} square {freq}" for freq, duration in notes
    )

    subprocess.Popen(
        f"play -nq -t alsa {synth_sequence} vol {0.15 * vol}",
        shell=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
