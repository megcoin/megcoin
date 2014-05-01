# [ANN][SCRYPT-N-R][MEG] Megcoin | No premine | Forked from bitcoin 0.9 | New scrypt-N-R PoW | Digishield

# [Megcoin - Get Megged [MEG]](http://megcoin.com)

[img]()

## Specifications:

* PoW Algo: Scrypt-8-4 (scrypt-n-r)
* Premine: 0%.  
* Total: infinite (20K final block reward)
* Block time: one minute
* Reward halved: every 200,000 blocks
* Reward ripen: 120 blocks (~2 hours)
* Difficulty adjustment: Every block, digishield
* Wallet forked from Dogecoin 1.7/Bitcoin 0.9

## Reward schedule:

* 1–200,000: 500K Megcoin 
* 200,001–400,000: 250K Megcoin
* 400,001–600,000: 125K Megcoin
* 600,001–800,000: 62500 Megcoin
* 800,001–1,000,000: 31,250 Megcoin
* 1,000,000+: 20,000 Megcoin

## Scrypt-N-R

Megcoin's algorithm uses a new algorithm I've dubbed scrypt-N-R. Typically, `scrypt` means scrypt with N=1024, R=1, P=1. This algorithm changes R for more granular tuning of memory usage. Currently, there is only the wallet miner and cpuminer(minerd) ported to the new algorithm. The memory usage of scrypt-8-4 is only 4Kbytes, compared to normal scrypt where it is 128Kbytes. This means that GPUs and FPGAs will have a large advantage once they are ported to the algorithm. However, ASICs are not practical to make for Megcoin because of the short "primary mining" period of about 1.5 years. If ASICs were produced for the algorithm, it would be near the end of big rewards and when mining is needed more for network stability than for coin generation. 

## Digishield

This uses the Digishield difficulty algorithm which has been proven stable by Dogecoin. Although multipools shouldn't be a worry with the unique algorithm parameters, digishield has been proven to handle large hashrate changes very well. 

## Forked from Dogecoin 1.7/Bitcoin 0.9

Because it was forked from Dogecoin 1.7, which is forked from Bitcoin 0.9, Megcoin's wallet includes the many advancements that Bitcoin 0.9 has:

* A faster graphical user interface (supporting Qt5 as well)
* Fixes for transaction malleability
* Services broken up into megcoind, megcoin-cli, and megcoin-qt
* Many more features which can be seen in the bitcoin 0.9 [changelog](https://bitcoin.org/bin/0.9.0/README.txt)

## Downloads

* [Windows (32bit)](http://megcoin.com/wallet1.7/windows)
* [Arch Linux(pkgbuild)](http://megcoin.com/wallet1.7/ff)
* [Mac OSX](http://megcoin.com/wallet1.7/windows)

The source code is available on [github](https://github.com/Megcoin/megcoin)

## Resources

* [reddit](http://www.reddit.com/r/megcoin)
* [website](http://megcoin.com)

## Block explorers

* [megchain.earlz.net](http://megchain.earlz.net)

## Mining

* [cpuminer](https://bitbucket.org/earlz/megcpuminer)
* The wallet supports mining by using `setgenerate true -1`

This should be very easily (and effeciently) mined by GPUs and even FPGAs due to it's low 4Kbyte memory requirement. I do not have the knowledge to port a GPU miner though, so this is why I've only ported cpuminer.

## Pools

* [megpool.earlz.net](http://megpool.earlz.net)

**Note:** megpool.earlz.net is only for bootstrapping the coin and allowing easy initial mining. To encourage pool diversity, it has a schedule:

* Day 1-2: 0% fees
* day 3-5: 2% fees
* day 6-7: 5% fees
* day 8-13: 8% fees
* day  14+: 10% fees 

After day 14, the fees will remain very high until megpool.earlz.net is less than 30% of the network hashrate. 
Setting up a pool is very easy with NOMP (if you're not afraid of prerelease software). NOMP has out of the box support for Megcoin and is very easy to setup. 

The first pool to be setup and reported to me will be rewarded with 1M MEG.

## Nodes

I've tried to ensure there are plenty of servers for the initial rush of wallet syncs including nodes in the US, Europe, and China. However if you have a reliable node, report it to me and I'll add it to this list in case those servers get overloaded or are later scaled down for cost reasons. 

## Exchanges

None yet, but soon! 
