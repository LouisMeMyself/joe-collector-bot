from web3 import Web3
import getpass
import Constants

# web3
w3 = Web3(Web3.HTTPProvider("https://api.avax.network/ext/bc/C/rpc"))
if not w3.isConnected():
    print("Error web3 can't connect")

# account
private_key = getpass.getpass(prompt="Paste your private key here: ", stream=None)
acct = w3.eth.account.privateKeyToAccount(private_key)

# contracts
joeMaker = w3.eth.contract(address=Constants.JOEMAKER_ADDRESS, abi=Constants.JOETOKEN_ABI)
joeFactory = w3.eth.contract(address=Constants.JOEFACTORY_ADDRESS, abi=Constants.JOEFACTORY_ABI)
joeMasterChefV2 = w3.eth.contract(address=Constants.JOEMASTERCHEFV2_ADDRESS, abi=Constants.JOEMASTERCHEFV2_ABI)


def exec_contract(acct_, nonce_, func_):
    """
    call contract transactional function func
    """
    construct_txn = func_.buildTransaction({'from': acct_.address, 'nonce': nonce_})
    signed = acct_.signTransaction(construct_txn)
    tx_hash = w3.eth.sendRawTransaction(signed.rawTransaction)
    return tx_hash.hex()


# blacklist
blacklist = ("0x6e7f5c0b9f4432716bdd0a77a3601291b9d9e985", "0x440aBbf18c54b2782A4917b80a1746d3A2c2Cce1")

# constants
# npairs = int(joeFactory.functions.allPairsLength().call())
npairs = int(joeMasterChefV2.functions.poolLength().call())

print('Iterating throughout the {} pairs.'.format(npairs))
token0s = []
token1s = []
for i in range(npairs):

    # address = joeFactory.functions.allPairs(i).call()
    # joePairN = w3.eth.contract(address=address, abi=Constants.JOEPAIR_ABI)
    # if joePairN.functions.balanceOf(Constants.JOEMAKER_ADDRESS).call() == 0:
    #     continue

    address, rewards, _, _, _ = joeMasterChefV2.functions.poolInfo(i).call()
    joePairN = w3.eth.contract(address=address, abi=Constants.JOEPAIR_ABI)
    if joePairN.functions.balanceOf(Constants.JOEMAKER_ADDRESS).call() == 0 or rewards == 0:
        continue

    token0 = joePairN.functions.token0().call()
    token1 = joePairN.functions.token1().call()
    if token0 in blacklist or token1 in blacklist:
        continue
    token0s.append(token0)
    token1s.append(token1)

print("Found {} pairs for JoeMaker".format(len(token0s)))
# call transactional method
nonce = w3.eth.getTransactionCount(acct.address)
from_block_number = w3.eth.blockNumber
contract_func = joeMaker.functions.convertMultiple(token0s, token1s)
print(contract_func)
print('Invoke convertMultiple()')
tx_hash = exec_contract(acct, nonce, contract_func)
print('tx_hash={} waiting for receipt..'.format(tx_hash))
tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash, timeout=120)
print("Receipt accepted. gasUsed={gasUsed} blockNumber={blockNumber}".format(**tx_receipt))
