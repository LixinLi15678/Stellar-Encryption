import numpy as np
from stellar_encryption import StellarEncryption

def text_to_vector(text):
    """
    Convert a text string to a vector of Unicode code points.

    Args:
        text (str): The text string to be converted.

    Returns:
        text_vector (np.array): The vector generated from the text.
    """
    text_vector = np.array([ord(char) for char in text])
    return text_vector

def vector_to_text(vector):
    """
    Convert a vector of Unicode code points back to a text string.

    Args:
        vector (np.array): The vector to be converted.

    Returns:
        text (str): The text string generated from the vector.
    """
    byte_values = [min(max(int(round(value)), 0), 255) for value in vector]
    byte_values = bytes(byte_values)
    text = byte_values.decode('utf-8', errors='ignore')
    return text


def planet_data_to_vector(planet_data):
    """
    Convert the planet data dictionary to a vector.

    Args:
        planet_data (dict): The planet data dictionary.

    Returns:
        planet_data_vector (np.array): The vector generated from the planet data.
    """
    return np.array(list(planet_data.values()))

def vector_to_planet_data(vector, keys):
    """
    Convert the vector back to a planet data dictionary.

    Args:
        vector (np.array): The vector to be converted.
        keys (list): The list of keys for the planet data dictionary.

    Returns:
        planet_data (dict): The planet data dictionary generated from the vector.
    """
    return {key: value for key, value in zip(keys, vector)}

def pad_vector(vector, target_length):
    """
    Pad the vector with zeros to reach the target length.

    Args:
        vector (np.array): The vector to be padded.
        target_length (int): The target length of the padded vector.

    Returns:
        padded_vector (np.array): The padded vector.
    """
    padding_length = target_length - len(vector)
    padded_vector = np.concatenate((vector, np.zeros(padding_length)))
    return padded_vector

def unpad_vector(vector, original_length):
    """
    Remove padding from the vector to restore its original length.

    Args:
        vector (np.array): The padded vector.
        original_length (int): The original length of the vector.

    Returns:
        unpadded_vector (np.array): The unpadded vector.
    """
    unpadded_vector = vector[:original_length]
    return unpadded_vector

if __name__ == "__main__":

    se = StellarEncryption()

    # The key for the Hadamard encryption
    key = 12345

    # The planet data dictionary
    planet_data_dict = {
        "mass": 1.0,  # Earth mass
        "radius": 6371,  # km
        "density": 5.52,  # g/cm^3
        "semi_major_axis": 1.0,  # Astronomical Units
        "orbital_period": 365.25,  # days
        "orbital_eccentricity": 0.0167,
        "rotation_period": 24.0,  # hours
        "surface_temperature": 288,  # K
    }

    # The text message to be encrypted along with the planet data
    message = "This is a secret message."

    # Convert the planet data dictionary to a vector
    planet_data_vector = planet_data_to_vector(planet_data_dict)

    # Convert the text message to a vector
    text_vector = text_to_vector(message)

    # Pad the text vector to the next power of 2
    next_power_of_2 = int(np.ceil(np.log2(len(text_vector) + len(planet_data_dict))))

    padded_text_vector = pad_vector(text_vector, 2**next_power_of_2 - len(planet_data_vector))

    # Combine the planet data vector and the padded text vector
    combined_vector = np.concatenate((planet_data_vector, padded_text_vector))

    # Encrypt the combined vector
    encrypted_vector = se.hadamard_encrypt(combined_vector, key)

    # Decrypt the encrypted vector
    decrypted_vector = se.hadamard_decrypt(encrypted_vector, key)

    # Split the decrypted vector into the planet data vector and the padded text vector
    decrypted_planet_data_vector = decrypted_vector[:len(planet_data_vector)]
    decrypted_padded_text_vector = decrypted_vector[len(planet_data_vector):]

    # Remove padding from the decrypted text vector
    decrypted_text_vector = unpad_vector(decrypted_padded_text_vector, len(text_vector))

    # Convert the decrypted text vector back to a text string
    decrypted_message = vector_to_text(decrypted_text_vector)

    # Convert the decrypted planet data vector back to a dictionary
    decrypted_planet_data = vector_to_planet_data(decrypted_planet_data_vector, list(planet_data_dict.keys()))
    decrypted_planet_data = {key: value / 64 for key, value in zip(planet_data_dict.keys(), decrypted_planet_data.values())}

    # Round the decrypted planet data values to match the original data
    for key, value in decrypted_planet_data.items():
        if isinstance(value, float):
            decrypted_planet_data[key] = round(value, 4)

    print("Encrypted vector:", encrypted_vector)

    print("Original message:", message)
    print("Decrypted message:", decrypted_message)
    print("Original planet data:", planet_data_dict)
    print("Decrypted planet data:", decrypted_planet_data)

