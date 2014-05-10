# [ANN][SCRYPT-N-R][MEG] Megcoin | No premine | Forked from bitcoin 0.9 | ASIC-resistant

# [Megcoin - Most Extravagent Goat Coin [MEG]](http://megcoin.com)

[img](http://i.imgur.com/0wcPCvq.png)

## About

Megcoin is a revolutionary new cryptocurrency designed first and foremost as a currency. It is positioned to become a major cryptocurrency for many reasons. It uses a short payout streak and a new algorithm to ensure ASICs will never be a problem, nor will multipools. Megcoin is forked from Bitcoin 0.9 to ensure that all of the recent Bitcoin wallet enhancements apply to this coin as well. It was provably not premined and is fully featured with multiple geographically-diverse DNS seed nodes to ensure extremely fast wallet synchronizations. For a limited time it is CPU only, until a GPU miner is ported.

## Rebrand and Reannouncement

Not enough time was spent before launch making a good logo and marketing. This is a rebrand and reannouncement of the coin with a fresh look and better marketing strategy to correct that. All coins already mined are unchanged. This is only a new look and strategy with additional team members.

## Specifications:

* Launched May 3rd, 2014
* PoW Algo: Scrypt-8-4 (scrypt-n-r)
* Premine: 0%
* Total: infinite (20K final block reward)
* Block time: one minute
* Reward halved: every 200,000 blocks
* Rewards mature: 120 blocks (~2 hours)
* Difficulty adjustment: Every block, digishield
* Wallet forked from Bitcoin 0.9

## Reward schedule:

* 1–200,000: 500K Megcoin 
* 200,001–400,000: 250K Megcoin
* 400,001–600,000: 125K Megcoin
* 600,001–800,000: 62500 Megcoin
* 800,001–1,000,000: 31,250 Megcoin
* 1,000,000+: 20,000 Megcoin

## Scrypt-N-R

Megcoin's algorithm uses a new algorithm I've dubbed scrypt-N-R. Typically, `scrypt` means scrypt with N=1024, R=1, P=1. This algorithm changes R for more granular tuning of memory usage. Currently, there is only the wallet miner and cpuminer(minerd) ported to the new algorithm. The memory usage of scrypt-8-4 is only 4Kbytes, compared to normal scrypt where it is 128Kbytes. 

Scrypt-R-N should be easily ported to GPUs and FPGAs. However, ASICs are not practical to make for Megcoin because of the short "payout streak" period of about 1.5 years. If ASICs were produced for the algorithm, it would be near the end of big rewards and when mining is needed more for network stability than for coin generation. 

## Digishield

This uses the Digishield difficulty algorithm which has been proven stable by Dogecoin and Digicoin. Although multipools shouldn't be a worry with the unique algorithm parameters, digishield has been proven to handle large hashrate changes very well to ensure the network is never stuck with slow blocks or vulnerable to a timewarp attack.

## Forked from Bitcoin 0.9

Because it was forked form Bitcoin 0.9, Megcoin's wallet includes the many advancements that Bitcoin 0.9 has:

* A faster graphical user interface (supporting Qt5 as well)
* Fixes for transaction malleability
* Services broken up into megcoind, megcoin-cli, and megcoin-qt
* Many more features which can be seen in the bitcoin 0.9 [changelog](https://bitcoin.org/bin/0.9.0/README.txt)

## Downloads

* [Windows (32bit)](http://earlz.net/static/megcoin1.0win32.zip)
* Mac OSX wallet coming soon
* Linux wallet coming soon 

The source code is available on [github](https://github.com/Megcoin/megcoin) for self-compilation

## Community and Resources

* [reddit](http://www.reddit.com/r/megcoin)
* #megcoin on IRC
* [website](http://megcoin.com)


## Block explorers

* http://cryptexplorer.com/chain/Megcoin
* http://megchain.earlz.net:8080

## Mining

* [cpuminer](https://bitbucket.org/earlz/megcpuminer) [64bit Windows build](http://earlz.net/static/megcpuminer_win64.zip)
* The wallet supports mining by using `setgenerate true -1`

## Pools

* http://coins.rapidhash.net
* http://megpool.mooo.com
* http://megpoolzws.com


## Nodes

There are multiple geographically-diverse DNS seeds built in to the wallet for fast syncing. However, if you have a reliable node, report it to me and I'll add it to this list in case those servers get overloaded. No addnode arguments should be required right now.

## Exchanges

* [Bittrex](http://bittrex.com) coming very soon

## Bounties

* AMD GPU Miner -- 40 Million MEG (bounty address: [MSGoyrBfXad1Pv8Jqc3t74a2yBsDoDbE1G](http://cryptexplorer.com/address/MSGoyrBfXad1Pv8Jqc3t74a2yBsDoDbE1G)
* Nvidia GPU Miner -- 3 Million MEG
* Faucet -- 2 Million MEG

## Testnet

Also, if you would like to test services or mining with Megcoin, I have testnet nodes running so syncing should be trivial