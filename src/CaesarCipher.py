class CasearCipher:
    ALPHABET_SIZE = 26
    CAPITAL_A_ASCII_CODE = 65

    def __init__(self, key: int = 0):
        self._key = key
        pass

    def crypt(self, cleartext: str):
        assert cleartext != '', "Cleartext should not be empty!"
        result = ""
        # transverse the plain text
        for i in range(len(cleartext)):
            char = cleartext[i]
            # Encrypt uppercase characters in plain text
            if char.isupper():
                result += chr((ord(char) + self._key - self.CAPITAL_A_ASCII_CODE) % self.ALPHABET_SIZE + self.CAPITAL_A_ASCII_CODE)
            # Encrypt lowercase characters in plain text
            else:
                result += char
        return result

    def pythonic_crypt(self, cleartext: str):
        assert cleartext != '', "Cleartext should not be empty!"
        return (
            ''.join(chr((ord(char) + self._key - self.CAPITAL_A_ASCII_CODE) % self.ALPHABET_SIZE + self.CAPITAL_A_ASCII_CODE)
                    if char.isupper() else char
                    for char in cleartext)
        )
