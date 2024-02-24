**What is the phase spectrum?**

We know that the fourier transform provides the frequency domain information about the signal. The phase spectrum provides the individual phases of each individual frequency component in the frequency domain representation. To gain a better understanding, let's visualize it in a few plots.

Let's start by visualizing the amplitude (of frequency) and phase spectrum of a simple cosine wave.

> **Note**: All of the function definitions can be found at the bottom of this page.

```python
plot_spectrums(
    frequencies = [1], # frequency in hertz
    amplitudes = [1], 
    phases = [0] # phase shifts in radians
)
```

<img src = "https://github.com/Mayukhdeb/notes/assets/53133634/fa1bae29-939a-4c33-8e6d-399bd33cbab5" width = "100%">

Now in order to obtain a sine wave, we can just shift the phase (forward or backward) by 90 degrees (pi/2 radians).

```python
plot_spectrums(
    frequencies = [1], # frequency in hertz
    amplitudes = [1], 
    phases = [np.pi/2] # phase shifts in radians
)
```

<img src = "https://github.com/Mayukhdeb/notes/assets/53133634/13630e70-3952-4a6d-b356-43f722ff1ce8" width = "100%">

Now let's add one more wave to the mix:

```python
plot_spectrums(
    frequencies = [1, 3], # frequency in hertz
    amplitudes = [1, 0.5], 
    phases = [np.pi/2, 0] # phase shifts in radians
)
```

<img src = "https://github.com/Mayukhdeb/notes/assets/53133634/d1a6af26-74c6-4f13-ac29-b97c3ac727cd" width = "100%">

Watch what happens when we change the phase of only the newly added wave.

```python
animate_spectrums(
    frequencies = [1, 3]  # Frequencies in Hertz
    amplitudes = [1, 0.5],  # Amplitudes
    initial_phases = [np.pi/2, 0],  # Initial phase shifts in radians 
    cycles=2, 
    fps=30, 
    duration=8
)
```

<video width="100%" controls>
  <source src="https://github.com/Mayukhdeb/notes/assets/53133634/acde28d3-50f5-4a6a-9fc4-0e811e1acd6c" type="video/mp4">
</video>

In order to gain a better intuition, let's also see what happens when we vary the amplitude of the new wave.

```python
animate_amplitude_variation(
    frequencies = [1, 3],  # Frequencies in Hertz
    initial_amplitudes = [1, 0.5],  # Initial Amplitude
    phases = [np.pi/2, 0],  # Phase shifts in radians
    cycles=2, 
    fps=30, 
    duration=10
)
```

<video width="100%" controls>
  <source src="https://github.com/Mayukhdeb/notes/assets/53133634/20f9a16e-6485-4fc1-a737-325530186066" type="video/mp4">
</video>

This is my conclusion:

1. The amplitude spectrum controls the intensity of each wave.
2. The phase spectrum controls the offset of each wave along the time dimension.

# Source code

```python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation
import numpy as np
import matplotlib.pyplot as plt

def plot_spectrums(frequencies, amplitudes, phases):
    """
    Plot the amplitude spectrum, phase spectrum, and reconstructed signal
    from the given frequencies, amplitudes, and phase spectrum.
    """
    # Ensure inputs are numpy arrays for easier math operations
    frequencies = np.array(frequencies)
    amplitudes = np.array(amplitudes)
    phases = np.array(phases)

    # Number of sample points for reconstruction
    N = 500
    # Time vector for reconstruction
    t = np.linspace(0, 2*np.pi, N)

    # Reconstruct signal from its Fourier components
    signal = np.zeros(N)
    for i in range(len(frequencies)):
        signal += amplitudes[i] * np.cos(frequencies[i] * t + phases[i])

    # Plotting
    fig, axs = plt.subplots(3, 1, figsize=(10, 8))

    # Amplitude Spectrum
    axs[0].stem(frequencies, amplitudes, basefmt=" ", use_line_collection=True)
    axs[0].set_title('Amplitude Spectrum')
    axs[0].set_xlabel('Frequency (Hz)')
    axs[0].set_ylabel('Amplitude')
    axs[0].grid(True)

    # Phase Spectrum
    axs[1].stem(frequencies, phases, basefmt=" ", use_line_collection=True)
    axs[1].set_title('Phase Spectrum')
    axs[1].set_xlabel('Frequency (Hz)')
    axs[1].set_ylabel('Phase (radians)')
    axs[1].grid(True)

    # Reconstructed Signal
    axs[2].plot(t, signal)
    axs[2].set_title('Reconstructed Signal from Amplitude and Phase Spectrums')
    axs[2].set_xlabel('Time')
    axs[2].set_ylabel('Signal Amplitude')
    axs[2].grid(True)
    plt.tight_layout()
    plt.show()

# Adjusted function for animation
def animate_spectrums(frequencies, amplitudes, initial_phases, cycles=1, fps=30, duration=10):
    """
    Create an animation varying the second phase from 0 to 2*pi radians and back.
    
    Parameters:
        frequencies (array-like): Frequency components.
        amplitudes (array-like): Amplitude of each frequency component.
        initial_phases (array-like): Initial phase (in radians) of each frequency component.
        cycles (int): Number of cycles of phase variation.
        fps (int): Frames per second in the animation.
        duration (int): Duration of the animation in seconds.
    """
    fig, axs = plt.subplots(3, 1, figsize=(10, 8))
    
    # Total frames for the animation
    frames = fps * duration
    
    def update(frame):
        # Clear previous plots
        for ax in axs:
            ax.clear()
        
        # Calculate current phase for the second component
        t = (frame % (frames // (2 * cycles))) / (frames // (2 * cycles))
        phase_shift = 2 * np.pi * t
        if frame >= frames // 2:
            phase_shift = 2 * np.pi - phase_shift
        phases = initial_phases.copy()
        phases[1] += phase_shift
        
        # Reconstruct signal with updated phase
        signal = np.zeros(500)
        t = np.linspace(0, 2*np.pi, 500)
        for i in range(len(frequencies)):
            signal += amplitudes[i] * np.cos(frequencies[i] * t + phases[i])
        
        # Update plots
        axs[0].stem(frequencies, amplitudes, basefmt=" ", use_line_collection=True)
        axs[1].stem(frequencies, phases, basefmt=" ", use_line_collection=True)
        axs[2].plot(t, signal)
        
        # Set titles and labels
        axs[0].set_title('Amplitude Spectrum')
        axs[0].set_xlabel('Frequency (Hz)')
        axs[0].set_ylabel('Amplitude')
        axs[0].grid()
        
        axs[1].set_title('Phase Spectrum')
        axs[1].set_xlabel('Frequency (Hz)')
        axs[1].set_ylabel('Phase (radians)')
        axs[1].set_ylim(0, 2 * np.pi*1.05)
        axs[1].grid()
        
        axs[2].set_title('Reconstructed Signal')
        axs[2].set_xlabel('Time')
        axs[2].set_ylabel('Signal Amplitude')
        axs[2].grid()
        axs[2].set_ylim(-2, 2)
        
        plt.tight_layout()

    anim = FuncAnimation(fig, update, frames=np.arange(0, frames), blit=False)
    
    # Save animation
    FFwriter = animation.FFMpegWriter(fps=fps, codec='libx264', extra_args=['-preset', 'veryslow', '-qp', '0'])
    anim.save('phase_animation.mp4', writer=FFwriter)

def animate_amplitude_variation(frequencies, initial_amplitudes, phases, cycles=1, fps=30, duration=10):
    """
    Create an animation varying the amplitude of the second frequency component.
    
    Parameters:
        frequencies (array-like): Frequency components.
        initial_amplitudes (array-like): Initial amplitude of each frequency component.
        phases (array-like): Phase (in radians) of each frequency component.
        cycles (int): Number of cycles of amplitude variation.
        fps (int): Frames per second in the animation.
        duration (int): Duration of the animation in seconds.
    """
    fig, axs = plt.subplots(3, 1, figsize=(10, 8))
    
    # Total frames for the animation
    frames = fps * duration
    
    def update(frame):
        # Clear previous plots
        for ax in axs:
            ax.clear()
        
        # Calculate current amplitude for the second component
        t = (frame % (frames // (2 * cycles))) / (frames // (2 * cycles))
        amplitude_modulation = np.abs(np.sin(np.pi * t))
        amplitudes = initial_amplitudes.copy()
        amplitudes[1] *= amplitude_modulation
        
        # Reconstruct signal with updated amplitude
        signal = np.zeros(500)
        t = np.linspace(0, 2*np.pi, 500)
        for i in range(len(frequencies)):
            signal += amplitudes[i] * np.cos(frequencies[i] * t + phases[i])
        
        # Update plots
        axs[0].stem(frequencies, amplitudes, basefmt=" ", use_line_collection=True)
        axs[1].stem(frequencies, phases, basefmt=" ", use_line_collection=True)
        axs[2].plot(t, signal)
        
        # Set titles and labels
        axs[0].set_title('Amplitude Spectrum')
        axs[0].set_xlabel('Frequency (Hz)')
        axs[0].set_ylabel('Amplitude')
        axs[0].grid()
        
        axs[1].set_title('Phase Spectrum')
        axs[1].set_xlabel('Frequency (Hz)')
        axs[1].set_ylabel('Phase (radians)')
        axs[1].set_ylim(0, 2 * np.pi*1.05)
        axs[1].grid()
        
        axs[2].set_title('Reconstructed Signal')
        axs[2].set_xlabel('Time')
        axs[2].set_ylabel('Signal Amplitude')
        axs[2].grid()
        axs[2].set_ylim(-2, 2)
        
        plt.tight_layout()

    anim = FuncAnimation(fig, update, frames=np.arange(0, frames), blit=False)
    
    # Save animation
    FFwriter = animation.FFMpegWriter(fps=fps, codec='libx264', extra_args=['-preset', 'veryslow', '-qp', '0'])
    anim.save('amplitude_variation_animation.mp4', writer=FFwriter)
```