# Megcoin Core [MEG]
==========================

![Megcoin](http://i.imgur.com/TqxAuAN.png)

## What is Megcoin?
Megcoin is a cryptocurrency like Bitcoin, although it does not use SHA256 as its proof of work (POW). Taking development cues from Tenebrix, Litecoin, and Dogecoin, Megcoin currently employs a unique variant of scrypt.

http://megcoin.com/

## License
Megcoin is released under the terms of the MIT license. See [COPYING](COPYING)
for more information or see http://opensource.org/licenses/MIT.

## Development and contributions 
Development is ongoing and the development team as well as other volunteers can freely work in their own trees and submit pull requests when features or bug fixes are ready.

## Proof Of Work
Megcoin uses scrypt as it's proof of work, with a unique N parameter of `123`. To mine it, you must ensure that your miner is capable of mining scrypt-n where the `n` is 123, NOT 2^123. This value was chosen for uniqueness. In this way, even if scrypt-n ASICs came out, they'd be unlikely to support non-power of 2 values of N, so this provides ASIC resistance without using experimental or unfamiliar algorithms. This low value also means that GPUs should be easier to mine with and it should be practical to build FPGAs for this algorithm.

## Wallet
Unlike most altcoin wallets forked from litecoin etc, this has been built by forking from dogecoin-1.7. dogecoin-1.7 is basically a rebase on top of bitcoin 0.9. So, all of the nifty features in bitcoin 0.9 are also in this wallet, including the "core" and cli functionality changes.

## Difficulty
Difficulty is adjusted each block by the digishield algorithm. This algorithm has been proven to be stable by dogecoin and digitalcoin and allows for extremely fast difficulty adjustments, at the cost of slightly more block time fluctuation

## Frequently Asked Questions

### How much meg can exist?
Approximately two and a half years after release there will be about 193,750,000,000 coins.
Each subsequent block will grant 20,000 coins to encourage miners to continue to secure the network and make up for lost wallets on hard drives/phones/lost encryption passwords/etc.

### How to get megged? 
Megcoin uses a simplified variant of the scrypt key derivation function as its proof of work with a target time of one minute per block and difficulty readjustment after every block. The block rewards are fixed and halve every 200,000 blocks. Starting with the 1,000,000th block, a permanent reward of 20,000 Megcoin per block will be paid. 

The current block reward schedule:
1–200,000: 500K Megcoin 

200,001–400,000: 250K Megcoin

400,001–600,000: 125K Megcoin

600,001–800,000: 62500 Megcoin

800,001–1,000,000: 31,250 Megcoin

1,000,000+: 20,000 Megcoin


### Building megcoin-qt

    sudo apt-get install build-essential \
                         libssl-dev \
                         libdb5.1++-dev \
                         libboost-all-dev \
                         libqrencode-dev \
                         libminiupnpc-dev

    ./autogen.sh
    ./configure --with-gui=qt4
    make USE_UPNP=1 USE_IPV6=1 USE_QRCODE=1

### Ports
RPC 22888
P2P 22889


