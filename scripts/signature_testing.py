import sys
from eth_account import Account
from eth_account.messages import encode_defunct
from web3.auto import w3
import secrets

# Create an Account
priv = secrets.token_hex(32)
# private_key = "0x" + priv
private_key = "eb6f697dc4de0679fd162be1e141e34902bd6adc834690775f1d2b5b22bebe3e"
acct = Account.from_key(private_key)


# Sign a Message with the Private Key
msg = "hello world"
message = encode_defunct(text=msg)
signed_message = w3.eth.account.sign_message(message, private_key=private_key)

message_hash = signed_message.messageHash.hex()

print("\nPrivate Key:", private_key)
print("\nAddress:", acct.address)
print("\nHashed_message:", message_hash)
print("\nSignature:", signed_message.signature.hex(), "\n")

signer_address = w3.eth.account.recoverHash(message_hash, signature=signed_message.signature)

print("Signer Address:", signer_address)