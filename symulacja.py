import numpy as np

def generate_random_discrete_signal():
    """
    Generuje losowy sygnał dyskretny przez określoną liczbę sekund.

    Parametry:
        - duration (float): Czas trwania sygnału w sekundach.
        - sampling_rate (int): Częstotliwość próbkowania sygnału.
        - num_samples (int): Liczba próbek sygnału.

    Zwraca:
        - ndarray: Wygenerowany sygnał dyskretny.

        
    """
    duration = 15 # Czas trwania sygnału w sekundach
    sampling_rate = 44100 # Częstotliwość próbkowania w Hz
    num_samples = int(duration * sampling_rate)
    signal = np.random.rand(num_samples) # Generowanie losowych wartości od 0 do 1
    return signal

