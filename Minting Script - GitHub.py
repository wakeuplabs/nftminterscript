import requests

api_url = "https://api-minter.wakeuplabs.link/custom/mint"
api_key = "8122c487-EasterEgg-4a28-b4d6-32fc24ee62p4" #Replace with your API Key

headers = {
    "apikey": api_key
}

addresses = ["0xExample1", "0xExample2", "0x000000000000000000000000000000000000dEaD"] #Replace with the Recipient's address

payload = {
    "contractId": "648p3eb09c01e2cab99a",  # Replace with your contract ID
    "dynamicMetadata": False,
    "metadata": {
        "name": "Optimism Workshop Series 1: Certificado de particiación", # Replace with name of the nft
        "description": "Este Certificado que corre sobre la Blockchain de Optimism verifica que el usuario Owner de la address en la cual fue minteado participó al menos 1 vez del Workshop online dictado por WakeUp Labs, L2 Español y OP Español. Felcitaciones", # Replace with your description
        "image": "https://copper-total-fly-652.mypinata.cloud/ipfs/QmT6EN54yZxRf4MUaYXuipFEeHzdDMF29dd8Lfbcoqp6m5" # Replace with your Image URL
    }
}

def mint_nft(address):
    payload["mintToAddress"] = address

    response = requests.post(api_url, json=payload, headers=headers)

    if response.status_code == 200:
        data = response.json()
        # Handle the response data as needed
        print(f"Minting successful for address: {address}")
    else:
        print(f"Failed to mint for address: {address}")
        print(f"Response status code: {response.status_code}")
        print(f"Response body: {response.text}")

# Loop through addresses and mint NFT for each address
index = 0
while index < len(addresses):
    mint_nft(addresses[index])
    index += 1