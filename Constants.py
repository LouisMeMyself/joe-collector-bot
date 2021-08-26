import json

# SubGraph links
JOE_EXCHANGE_SG_URL = "https://api.thegraph.com/subgraphs/name/traderjoe-xyz/exchange"
JOE_BAR_SG_URL = "https://api.thegraph.com/subgraphs/name/traderjoe-xyz/bar"

# address for web3
JOEMAKER_ADDRESS = "0x861726BFE27931A4E22a7277bDe6cb8432b65856"
JOEFACTORY_ADDRESS = "0x9Ad6C38BE94206cA50bb0d90783181662f0Cfa10"
JOEMASTERCHEFV2_ADDRESS = "0xd6a4F121CA35509aF06A0Be99093d08462f53052"

# ABI for web3
with open("utils/joemakerabi.json", "r") as f:
    JOETOKEN_ABI = json.load(f)

with open("utils/joefactoryabi.json", "r") as f:
    JOEFACTORY_ABI = json.load(f)

with open("utils/joemasterchefv2abi.json", "r") as f:
    JOEMASTERCHEFV2_ABI = json.load(f)

with open("utils/joepairabi.json", "r") as f:
    JOEPAIR_ABI = json.load(f)
