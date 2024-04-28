import time

def spin(duration):
    animation_frames = ['-', '\\', '|', '/']
    fps = 5
    total_frames = duration * fps

    for i in range(total_frames):
        print("\r" + animation_frames[i %
              len(animation_frames)], end="", flush=True)
        time.sleep(0.5 / fps)


def bar(total, length=50, speed=0.1):
    """
    Display a simple progress bar in the terminal.

    Parameters:
        total (int): Total number of iterations.
        length (int): Length of the progress bar in characters.
        speed (float): Speed of the progress bar animation (seconds per iteration).
    """
    for i in range(total + 1):
        progress = i / total
        bar_length = int(length * progress)
        bar = '█' * bar_length + '-' * (length - bar_length)
        print(f'\r[{bar}] {progress * 100:.2f}%', end='', flush=True)
        time.sleep(speed)

    print()
