import random
import time

print("\nFLASH-SENDER v3.0")
print("Educational Blockchain Simulation Tool\n")

sender = input("Enter Sender Address: ")
receiver = input("Enter Receiver Address: ")

print("\nSelect Network")
print("1. Ethereum (ERC20)")
print("2. TRON (TRC20)")
print("3. BSC (BEP20)")
print("4. Polygon")

choice = input("\nChoose Option: ")

amount = input("Enter Amount: ")

networks = {
    "1": "Ethereum (ERC20)",
    "2": "TRON (TRC20)",
    "3": "BSC (BEP20)",
    "4": "Polygon"
}

network = networks.get(choice, "Unknown Network")

print("\nBroadcasting transaction...")
time.sleep(1)

print("Validating transaction...")
time.sleep(1)

tx_hash = "0x" + ''.join(
    random.choice("abcdef0123456789")
    for _ in range(64)
)

print("\n=== TRANSACTION RESULT ===\n")

print("Network:", network)
print("Sender:", sender)
print("Receiver:", receiver)
print("Amount:", amount)

print("\nTransaction Hash:")
print(tx_hash)

print("\nSTATUS: SUCCESS (SIMULATION ONLY)")

print("\nDISCLAIMER:")
print("This tool does NOT send real blockchain transactions.")
print("Educational use only.\n")
