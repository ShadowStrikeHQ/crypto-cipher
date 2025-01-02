## Crypto-Cipher

Crypto-Cipher is a text encryption and decryption tool designed for basic cryptographic operations. It offers a streamlined interface and robust security features.

### Installation

```
pip install crypto-cipher
```

### Usage

```
python -m crypto-cipher [-h] [-e ENCRYPTION_KEY] [-d DECRYPTION_KEY] [-t TEXT_TO_ENCRYPT | -f FILE_WITH_TEXT] [-o OUTPUT_FILE_PATH]
```

### Examples

**Encryption:**

```
python -m crypto-cipher -e my_encryption_key -t "Hello, world!" -o encrypted_text.txt
```

**Decryption:**

```
python -m crypto-cipher -d my_decryption_key -f encrypted_text.txt -o decrypted_text.txt
```

### Security Warnings

* Keep your encryption keys confidential.
* Ensure the security of the communication channel while exchanging keys.
* Consider using additional security measures such as encryption in transit and at rest.

### License

Copyright (c) CY83R-3X71NC710N

Crypto-Cipher is licensed under the GNU General Public License v3.0.