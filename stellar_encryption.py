import numpy as np
import scipy.linalg

class StellarEncryption:

    def __init__(self):
        # Initialize any necessary variables or data structures
        pass
    
    @staticmethod
    def planet_data_to_vector(planet_data: dict) -> np.array:
        """
        Convert planet data to a vector.

        Args:
            planet_data (dict): A dictionary containing planet data.

        Returns:
            data_vector (np.array): The vector generated from the planet data.
        """
        data_list = list(planet_data.values())
        data_vector = np.array(data_list)

        return data_vector

    @staticmethod
    def hadamard_encrypt(data_vector: np.array, encryption_key: np.array) -> np.array:
        """
        Encrypt the data vector using Hadamard matrix and the encryption key.

        Args:
            data_vector (np.array): The vector to be encrypted.
            encryption_key (np.array): The key to use for encryption.

        Returns:
            encrypted_vector (np.array): The encrypted vector.
        """
        hadamard_matrix = scipy.linalg.hadamard(len(data_vector))
        encrypted_vector = np.dot(hadamard_matrix, data_vector) + encryption_key

        return encrypted_vector

    @staticmethod
    def hadamard_decrypt(encrypted_vector: np.array, decryption_key: np.array) -> np.array:
        """
        Decrypt the encrypted vector using Hadamard matrix and the decryption key.

        Args:
            encrypted_vector (np.array): The encrypted vector to be decrypted.
            decryption_key (np.array): The key to use for decryption.

        Returns:
            decrypted_vector (np.array): The decrypted vector.
        """
        hadamard_matrix = scipy.linalg.hadamard(len(encrypted_vector))
        decrypted_vector = np.dot(hadamard_matrix, encrypted_vector - decryption_key)

        return decrypted_vector



"""
Below is the test code for the StellarEncryption class.
Please see and run the code in main.py
"""

def text_to_vector(text: str) -> np.array:
    """
    Convert a text string to a vector of normalized Unicode code points.

    Args:
        text (str): The text string to be converted.

    Returns:
        text_vector (np.array): The vector generated from the text.
    """
    text_vector = np.array([ord(char) / 1114112 for char in text])
    return text_vector

def vector_to_text(vector: np.array) -> str:
    """
    Convert a vector of normalized Unicode code points back to a text string.

    Args:
        vector (np.array): The vector to be converted.

    Returns:
        text (str): The text string generated from the vector.
    """
    text = ''.join([chr(int(round(value * 1114112))) for value in vector])
    return text

def pad_to_power_of_two(vector: np.array) -> np.array:
    """
    Pad a vector with zeros to make its length a power of 2.

    Args:
        vector (np.array): The vector to be padded.

    Returns:
        padded_vector (np.array): The padded vector.
    """
    target_length = int(2 ** np.ceil(np.log2(len(vector))))
    padded_vector = np.pad(vector, (0, target_length - len(vector)))
    return padded_vector

# Example usage
if __name__ == "__main__":
    stellar_encryption = StellarEncryption()

    planet_data = {
        "mass": 1.0,  # Earth mass
        "radius": 6371,  # km
        "density": 5.52,  # g/cm^3
        "semi_major_axis": 1.0,  # Astronomical Units
        "orbital_period": 365.25,  # days
        "orbital_eccentricity": 0.0167,
        "rotation_period": 24.0,  # hours
        "surface_temperature": 288,  # K
    }

    # Convert planet_data to a vector
    data_vector = stellar_encryption.planet_data_to_vector(planet_data)
    print(f"Data vector: {data_vector}")

    message = "Hello, world!"
    text_vector = text_to_vector(message)
    combined_vector = np.concatenate((data_vector, text_vector))
    padded_vector = pad_to_power_of_two(combined_vector)
    print(f"Combined vector: {combined_vector}")

    # Generate encryption and decryption keys
    key = np.random.random(len(padded_vector))

    # Encrypt the data vector
    encrypted_vector = stellar_encryption.hadamard_encrypt(padded_vector, key)
    print(f"Encrypted vector: {encrypted_vector}")

    # Decrypt the encrypted vector
    decrypted_vector = stellar_encryption.hadamard_decrypt(encrypted_vector, key)
    print(f"Decrypted vector: {decrypted_vector}")

    # Remove padding from the decrypted vector
    decrypted_vector = decrypted_vector[:len(combined_vector)]

    # Separate the decrypted vector back into planet data and text
    decrypted_data_vector = decrypted_vector[:len(data_vector)]
    decrypted_text_vector = decrypted_vector[len(data_vector):]

    decrypted_message = vector_to_text(decrypted_text_vector)
    print(f"Decrypted message: {decrypted_message}")