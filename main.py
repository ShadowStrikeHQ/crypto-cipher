import argparse
import logging
from cryptography.fernet import Fernet

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def setup_argparse():
    """
    Setup command line argument parsing.
    """
    parser = argparse.ArgumentParser(
        description="Text encryption and decryption tool using Fernet symmetric encryption."
    )
    parser.add_argument(
        "operation", choices=["encrypt", "decrypt", "generate-key"],
        help="Operation to perform: encrypt, decrypt, or generate-key."
    )
    parser.add_argument(
        "--key", help="Encryption/Decryption key (required for encrypt/decrypt)."
    )
    parser.add_argument(
        "--text", help="Text to encrypt or decrypt (required for encrypt/decrypt)."
    )
    return parser

def main():
    """
    Main function to handle encryption, decryption, and key generation.
    """
    parser = setup_argparse()
    args = parser.parse_args()

    try:
        if args.operation == "generate-key":
            # Generate a new key
            key = Fernet.generate_key()
            logging.info("Generated encryption key: %s", key.decode())
            print(key.decode())

        elif args.operation == "encrypt":
            if not args.key or not args.text:
                raise ValueError("Both --key and --text are required for encryption.")
            fernet = Fernet(args.key.encode())
            encrypted_text = fernet.encrypt(args.text.encode()).decode()
            logging.info("Encryption successful.")
            print(encrypted_text)

        elif args.operation == "decrypt":
            if not args.key or not args.text:
                raise ValueError("Both --key and --text are required for decryption.")
            fernet = Fernet(args.key.encode())
            decrypted_text = fernet.decrypt(args.text.encode()).decode()
            logging.info("Decryption successful.")
            print(decrypted_text)

        else:
            logging.error("Invalid operation. Use encrypt, decrypt, or generate-key.")
            parser.print_help()

    except Exception as e:
        logging.error("An error occurred: %s", str(e))
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()