



Modifying EVM Storage to Seed Token Balances in Testing - Metana



















































































 












Skip links* [Skip to primary navigation](#primary-nav)
* [Skip to content](#lqd-site-content)



 





 


 




Call us +1 415 416 0800 


















 [![Metana](https://metana.io/wp-content/uploads/2022/07/Metana-Logo.png)](https://metana.io/) 








* [Solidity BootcampHot 🔥](https://metana.io/web3-solidity-bootcamp-ethereum-blockchain/)
* [Bootcamps](#) 








###### Web3

 






### Web3 Solidity Bootcamp



Most Popular 🔥
The most advanced Solidity curriculum on the internet











### Full Stack Web3 Beginner Bootcamp



New ✨ | Beginner 👨‍💻
Starting off with web development and seamlessly integrating web3 development











### Web3 Rust Bootcamp



Become an expert Solana blockchain developer with one course!














###### Coding + Career Growth

 




 








### Software Engineering Bootcamp



Become a Software Engineer - Balance everyday life commitments & launch your coding career in as little as 16 weeks











### Metana's JobCamp™️



Learn to make a lasting first impressions, network effectively & search for jobs with confidence.















 ![](https://metana.io/wp-content/uploads/2023/10/Screenshot-2023-10-25-at-7.51.33 PM-300x61.png) 




 Rated
the Best

 





 Ranked as the industry's premier Web3 bootcamp with a stellar 4.8/5 star rating on Course Report.

 




[Read more reviews here](/reviews/)












[Still Unsure?](https://formless.ai/c/6bPi6ASGJ4ge)
* [Resources](#)
	+ [Reviews](https://metana.io/reviews/)
	+ [Metana’s Job Guarantee](https://metana.io/job-guarantee/)
	+ [Tuition](https://metana.io/tuition/)
	+ [Events](https://metana.io/events/)
* [Blog](https://metana.io/blog/)

 





[Apply now](https://metana.typeform.com/general)






















 







 [![Metana](https://metana.io/wp-content/uploads/2022/07/Metana-Logo.png)](https://metana.io/) 









Metana Bootcamps
----------------

 






* [Solidity BootcampHot 🔥](https://metana.io/web3-solidity-bootcamp-ethereum-blockchain/)
* [Full Stack Web3 Bootcamp](https://metana.io/web3-beginner-bootcamp/)
* [Rust Bootcamp](https://metana.io/web3-rust-bootcamp-solana-blockchain/)
* [Cybersecurity Bootcamp](https://metana.io/cybersecurity-bootcamp/)
* [AI & Machine Learning Bootcamp](https://metana.io/ai-machine-learning-bootcamp/)
* [Data Analytics Bootcamp](https://metana.io/data-analytics-bootcamp/)
* [Data Science Bootcamp](https://metana.io/data-science-bootcamp/)
* [Full Stack Bootcamp](https://metana.io/full-stack-software-engineer-bootcamp/)
* [Jobcamp](https://metana.io/jobcamp/)

 














Menu Items
----------

 






* [Blog](https://metana.io/blog/)
* [Metana’s Job Guarantee](https://metana.io/job-guarantee/)
* [Refer a Friend](https://metana.io/refer/)
* [Tuition](https://metana.io/tuition/)
* [Withdrawal and Refund Policy](https://metana.io/withdrawal-and-refund-policy/)

 









 








 [[email protected]](/cdn-cgi/l/email-protection)

 




 

[Facebook](https://www.facebook.com/metanahq) 


[Twitter](https://twitter.com/metanahq) 


[Linkedin](https://www.linkedin.com/school/metana/) 


























 [![Metana](https://metana.io/wp-content/uploads/2022/07/Metana-Logo.png)](https://metana.io/) 




[Apply now](https://metana.typeform.com/general)
























 
#### Table of Contents





 







Modifying EVM Storage to Seed Token Balances in Testing
=======================================================

 



 * [Mathieu Bertin](https://metana.io/blog/author/matt/)
* [February 19, 2024](https://metana.io/blog/2024/02/19/)
* [Web3.0](https://metana.io/blog/category/web3-0/)














[EVM (Ethereum Virtual Machine)](https://metana.io/blog/ethereum-virtual-machine-evm/) storage refers to the permanent storage space within the Ethereum blockchain where smart contract data is stored. Each [smart contract](https://metana.io/blog/what-is-a-smart-contract-understand-contracts-on-the-blockchain/) deployed on the Ethereum network has its own storage space, which contains everything related to maintaining the state of the contract, including variables, mappings, and other data structures.


The issues come from when your contract has additional logic you don’t necessarily want to trigger to complicate your testing. This can include minting limits, cooldowns, side-effects, interactions, etc. The easiest way I found to do this is to **modify the EVM storage** directly with a seeding function. Now, for this to come as second nature, you need to fully understand how EVM Storage works. If you already do and just want the code, then you can skip ahead to the hardhat.js section.


Understanding EVM Storage
-------------------------


![](https://miro.medium.com/v2/resize:fit:875/0*vBCKlPaHmcs6_Xg7)

Photo of some numbered storage by [Steve Johnson](https://unsplash.com/@steve_j?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com/?utm_source=medium&utm_medium=referral)


Imagine the [Ethereum Virtual Machine](https://metana.io/blog/ethereum-virtual-machine-evm/) (EVM) storage as a vast storage facility filled with countless numbered doors that **anyone**can look into in a regular environment **only the respective contracts can modify**. For this analogy to work you could picture that every account controls a bunch of these doors numbered from 0, 1, 2 and so on. Each door of every account represent the **slots** that can contain about **32 bytes** of [smart contract](https://metana.io/blog/what-is-a-smart-contract-understand-contracts-on-the-blockchain/) data.


Here’s an example smart contract showing you which slots get occupied by which variables:



```
asbtract contract ContainsData {
  uint256 private storedData; // occupies SLOT 0
}

contract StorageExample is ContainsBalances {
  address private owner; // occupies SLOT 1
  uint8 public mySmallerInt; // occupies SLOT 2
  uint8 public myOtherInt; // ALSO occupies SLOT 2
  mapping(address => uint256 balance /* 32 bytes */) private addressBalances; // Occupies SLOT 3, but how are its values stored?
  uint32 public moreData; // Occupies SLOT 4
  mapping(uint256 tokenId => mapping(address account => uint256 balance)) public tokenBalances // Occupies SLOT 5 but how do nested mappings work?
  {...}
}
```

Multiple things to note with the above example. First, you’ll see that storage slots first get assigned with the contracts we inherit from, which is the case with `storedData` taking up SLOT 0. Second, you can see that a single storage slot can house multiple smaller-sized variables into a single slot, as demonstrated by `mySmallerInt` and `myOtherInt` efficiently both occupying the same slot (SLOT 2). Third, we can see how dynamic data (SLOT 3) containing many balances each with 32bytes of data poses a challenge with our structure given that one slot is only 32 bytes and we have `moreData` (SLOT 4) following up closely afterwards.


Although we don’t cover arrays they actually follow a very similar structure: hashed keys. To compute the storage location of a mapped item you need to take the [**keccak256**](https://www.cryptopp.com/wiki/Keccak)hash of the **key (address)** and the the **storage slot (SLOT 3)** in which the `adressBalances` mapping sits. This will return a very large slot number like *161222445428101458212…4383975103811933265512* that will very very unlikely get overridden by any other objects.


Lastly, we need to talk about nested mappings and how they’re stored. Essentially, you apply the same concept to find the second mapping’s slot. Let’s take the nested mapping `mapping(uint256 tokenId => mapping(address account => uint256 balance)) public tokenBalances` (SLOT 5) as an example. If we remember the formula correctly being `keccak256(key, slot)`, then we can find the first mapping by hashing the `tokenId` and `5` to find the first location. Then, simply nest the formula*ad infinitum*to find as many nested mappings as we need. For our example, we can find the exact slot number with`keccak256(address, keccak256(tokenId, 5))`.


Hacking the Local EVM Storage with Hardhat.js
---------------------------------------------


![modify the evm storagemodifying evm storageevm storagemodify evm storagehow to modify evm storage for testing](https://miro.medium.com/v2/resize:fit:875/0*Qvkh-YwZbDXddn83)

Man about to get some work done by [Fotos](https://unsplash.com/@fotospk?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com/?utm_source=medium&utm_medium=referral)


So I mentioned that in a **regular** environment, only contracts can modify their own storage. Well, in a **testing** environment, you **control everything**. Hardhat.js gives you the tools to change every aspect you normally couldn’t on a live network.


To get started, let’s have hardhat scaffold our testing environment for us. The following command will guide you through exactly that. I assume you have **nodejs**installed but if not you can use [nvm for that](https://github.com/nvm-sh/nvm). Make sure you select **Create a Typescript project** in the interactive prompt because any other option is the wrong one.



```
npx hardhat init
```

We’ll also need to add OpenZeppelin and `@nomicfoundation/hardhat-toolbox`dependencies.



```
npm install --save-dev @openzeppelin/contracts @nomicfoundation/hardhat-toolbox
```

Next, we’ll write a very simple [ERC1155](https://docs.openzeppelin.com/contracts/3.x/erc1155) test contract with a that allows a user to mint a single NFT from collection 0–5 with a cooldown mechanic. It will also include a trade function to exchange tokens 2 and 3 to make a special token 6 that can’t be minted otherwise. We’ll test this method using our seeded balances.



```
// contracts/CoolDownMintable.sol

// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC1155/ERC1155.sol";

contract CoolDownMintableERC1155 is ERC1155 {
    error CooldownNotFinished();
    error InvalidTokenId(uint256 tokenId);

    uint256 public constant COOLDOWN_DURATION = 1 days;
    
    mapping(address => uint256) public lastMintTime;

    constructor() ERC1155("") {}

    modifier checkMintableToken(uint256 tokenId) {
        if (tokenId > 5) {
            revert InvalidTokenId(tokenId);
        }
        _;
    }

    // Minting function with cooldown
    function mint(uint256 tokenId) public checkMintableToken(tokenId) {
        if (block.timestamp < lastMintTime[msg.sender] + COOLDOWN_DURATION) {
            revert CooldownNotFinished();
        }

        // Update the last mint time for the sender
        lastMintTime[msg.sender] = block.timestamp;

        // Mint the token
        _mint(msg.sender, tokenId, 1, "");
    }

    // Function that allows us to trade tokens 3, 2 and 1 for 6
    function tradeIn() public {
        uint256[] memory tokenIds = new uint256[](3);
        tokenIds[0] = 1; // Token ID 1
        tokenIds[1] = 2; // Token ID 2
        tokenIds[2] = 3; // Token ID 3

        address[] memory users = new address[](3);
        users[0] = msg.sender; // User's address for Token ID 1
        users[1] = msg.sender; // User's address for Token ID 2
        users[2] = msg.sender; // User's address for Token ID 3

        uint256[] memory balances = balanceOfBatch(users, tokenIds);
        
        require(balances[0] >= 1, "Insufficient token 1 balance");
        require(balances[1] >= 2, "Insufficient token 2 balance");
        require(balances[2] >= 3, "Insufficient token 3 balance");

        _burn(msg.sender, 3, 3);
        _burn(msg.sender, 2, 2);
        _burn(msg.sender, 1, 1);

        _mint(msg.sender, 6, 1, "");
    }
}
```

Then, for all that typescript goodness, we’ll need to compile the interfaces for this contract for testing. This can be done with the `typechain` that our handy `hardhat-toolbox` came with. This can be done with the following command:



```
npx hardhat typechain
```

\*\*Note\*\* You might need to tweak the version in your `hardhat.config.ts` to use the solidity version that OpenZeppelin uses.


After this, you should notice a new folder pop-up: `/typechain-types`. Those contain those handy types we mentioned previously.


Next we’ll write a simple test outline in the `/test` folder.



```
// test/CooldownMintableERC1155.test.ts

import type { CoolDownMintableERC1155 } from "../typechain-types";

import { expect } from "chai";
import { ethers } from "hardhat";
import { loadFixture } from '@nomicfoundation/hardhat-toolbox/network-helpers'

async function deploy() {
  const cooldownFactory = await ethers.getContractFactory("CoolDownMintableERC1155");
  const token = (await cooldownFactory.deploy()) as CoolDownMintableERC1155;
  await token.waitForDeployment();
  const account = (await ethers.getSigners())[0]!;
  const amountOfTokens = 7;
  const tokenIds = Array.from({ length: amountOfTokens }, (_, index) => index.toString());

  async function getBalances () {
    const address = await account.getAddress();
    const accountIds = Array.from({ length: amountOfTokens }, () => address);
    return [...await token.balanceOfBatch(accountIds, tokenIds)];
  }

  return {
    token,
    account,
    getBalances
  };
}

describe("CoolDownMintableERC1155 Contract Tests", function () {
  it("Should be able to trade in NFTs accordingly", async () => {
    const { token, getBalances } = await loadFixture(deploy);

    // We'd love to seed the balances right here before testing
    // await seedBalances([3n, 3n, 3n, 3n, 0n, 0n, 0n])

    let balances = await getBalances();
    expect(balances).to.have.all.members([3n, 3n, 3n, 3n, 0n, 0n, 0n]);
    await token.tradeIn();
    balances = await getBalances();
    expect(balances).to.have.all.members([3n, 2n, 1n, 0n, 0n, 0n, 1n]);
  })
});
```

So, ideally we wouldn’t have to mint every NFT and modify the block times with `helpers.time.increase` just to test balances here. You should, however, use those utilities for testing the cooldown functionality. But, for this, we’d prefer something simpler to really laser-focus on test on a very specific functionality: the `tradeIn` function. This is a perfect use case for writing directly to EVM storage, in my opinion.


The EVM Storage Final Boss: Nested Mappings
-------------------------------------------


We’re now at the ultimate test to find out if you truly understand storage slots. If you’d like to try and implement your own function, you can go ahead and [clone my repository](https://github.com/Burtonium/hardhat-evm-hacking/tree/solve-yourself) and checkout the branch `solve-yourself` to give it a try. Come back here when you’re done.


Let’s go find our `_balances` mapping on the `ERC1155` contract. If you look at [line 23](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC1155/ERC1155.sol#L23) of OpenZeppelin’s implementation, you’ll find the following mapping at the very first slot:



```
abstract contract ERC1155 is Context, ERC165, IERC1155, IERC1155MetadataURI, IERC1155Errors {
    {...}

    mapping(uint256 id => mapping(address account => uint256)) private _balances;
    
    {...}
}
```

So how do you find the final balance object that we’re looking for in this case? Well, if we remember the formula correctly being `keccak256(key, slot)`, then we can simply nest the formula*ad infinitum*to find as many nested mappings as we need. For our example, we can find the slot number with`keccak256(address, keccak256(tokenId, 0))`. If we implement a helper function with this pseudocode in our test file to find the contract’s storage it should look like this:



```
function getSlot(contractAddress: string, tokenId: string, storageSlot = 0n) {
  const hash = ethers.keccak256(abiCoder.encode(['uint, uint'], [tokenId, storageSlot]));
  return ethers.keccak256(abiCoder.encode(['address', 'bytes32'], [contractAddress, hash]));
}
```

With this helper function, we’ll leverage `helpers.setStorageAt(address, storageSlot, newValue)` from [hardhat network helpers](https://hardhat.org/hardhat-network-helpers/docs/reference#setstorageat(address,-index,-value)) to modify the storage directly. Our `seedBalances` function should then look something like this:



```
async function seedBalances(contractAddr: string, userAddress: string, tokenBalances: [string, string][]): Promise<void> {
  await Promise.all(tokenBalances.map(async ([tokenId, balance]) => {
    const userNFTBalanceSlot = getSlot(userAddress, tokenId);
    await setStorageAt(
      contractAddr,
      userNFTBalanceSlot,
      abiCoder.encode(['uint'], [balance]),
    );
  }))
}
```

With this, we should be able to seed balances directly without having to go through minting. Here’s the final test file with the updated deploy function to add more functionality to our fixture:  




```
import type { CoolDownMintableERC1155 } from "../typechain-types";

import { expect } from "chai";
import { ethers } from "hardhat";
import { setStorageAt, loadFixture } from '@nomicfoundation/hardhat-toolbox/network-helpers'

const abiCoder = new ethers.AbiCoder();

function getSlot(contractAddress: string, tokenId: string, storageSlot = 0n) {
  const hash = ethers.keccak256(abiCoder.encode(['uint', 'uint'], [tokenId, storageSlot]));
  return ethers.keccak256(abiCoder.encode(['address', 'bytes32'], [contractAddress, hash]));
}

async function seedBalances(contractAddr: string, userAddress: string, tokenBalances: [string, string][]): Promise<void> {
  await Promise.all(tokenBalances.map(async ([tokenId, balance]) => {
    const userNFTBalanceSlot = getSlot(userAddress, tokenId);
    await setStorageAt(
      contractAddr,
      userNFTBalanceSlot,
      abiCoder.encode(['uint'], [balance]),
    );
  }))
}

async function deploy() {
  const cooldownFactory = await ethers.getContractFactory("CoolDownMintableERC1155");
  const token = (await cooldownFactory.deploy()) as CoolDownMintableERC1155;
  await token.waitForDeployment();
  const tokenAddress = await token.getAddress();
  const account = (await ethers.getSigners())[0]!;
  const amountOfTokens = 7;
  const tokenIds = Array.from({ length: amountOfTokens }, (_, index) => index.toString());

  async function getBalances () {
    const accountIds = Array.from({ length: amountOfTokens }, () => account.address);
    return [...await token.balanceOfBatch(accountIds, tokenIds)];
  }

  const balanceSeeder = (balances: (bigint | string)[]) => seedBalances(
    tokenAddress,
    account.address,
    tokenIds.map((id, idx) => [id, balances[idx]?.toString() ?? '0'] as [string, string])
  );

  return {
    token,
    account,
    getBalances,
    seedBalances: balanceSeeder
  };
}


describe("CoolDownMintableERC1155 Contract Tests", function () {
  it("Should be able to trade in NFTs accordingly", async () => {
    const { token, seedBalances, getBalances } = await loadFixture(deploy);

    await seedBalances([3n, 3n, 3n, 3n, 0n, 0n, 0n])
    
    let balances = await getBalances();

    expect(balances).to.have.all.members([3n, 3n, 3n, 3n, 0n, 0n, 0n]);
    await token.tradeIn();
    balances = await getBalances();
    expect(balances).to.have.all.members([3n, 2n, 1n, 0n, 0n, 0n, 1n]);
  })
});
```

If you run this test you should see that we’ve accomplished what we’ve set out to do:



![](https://miro.medium.com/v2/resize:fit:606/1*rVCfgSTz6R5bosw8L_WPJg.png)

What you should hopefully see in your terminal by now.


Any feedback would be appreciated be it here or on Github. You can find the entire repository here:  
<https://github.com/Burtonium/hardhat-evm-hacking>



![](https://metana.io/wp-content/uploads/2024/01/Questions-cuate-1024x1024.png)
FAQs
----


**What does modifying EVM storage for seeding token balances entail?**


* Modifying EVM storage to seed token balances involves directly manipulating blockchain state in a test environment to simulate specific scenarios for smart contract testing.


**Why is seeding token balances important in smart contract testing?**


* Seeding token balances is crucial for creating realistic testing environments, allowing developers to evaluate how contracts interact under various conditions and ensuring robustness.


**How can I modify EVM storage to seed token balances during testing?**


* Use testing frameworks like Hardhat or Truffle, which offer functionalities to interact with EVM storage directly, allowing you to set specific balances for addresses in your tests.


**What tools are available for modifying EVM storage in testing environments?**


* Tools such as Hardhat’s `hardhat_setStorageAt` or Ganache’s ability to fork blockchain states are commonly used for modifying EVM storage in testing environments.


**Are there risks associated with directly modifying EVM storage for testing?**


* While modifying EVM storage is safe in a testing environment, it’s important to ensure that tests still accurately reflect realistic scenarios and don’t rely on unrealistic state setups.


**What is the Ethereum Virtual Machine (EVM) and its role in [smart contracts](https://metana.io/blog/solidity-smart-contracts/)?**


* The Ethereum Virtual Machine (EVM) is the runtime environment for Ethereum smart contracts, executing contract code in a secure and isolated manner.


**How do smart contracts manage token balances?**


* Smart contracts manage token balances through internal data structures, typically mapping addresses to balance amounts, allowing for the tracking and updating of holdings.


**What is the significance of gas optimization in contract testing?**


* Gas optimization in testing helps identify areas where contract execution costs can be minimized, crucial for reducing transaction fees and improving contract efficiency.


**Can modifying EVM storage replicate real-world scenarios like airdrops in testing?**


* Yes, by seeding balances and setting specific storage states, developers can simulate real-world scenarios such as airdrops or large-scale token distributions in a controlled environment.


**What best practices should be followed when testing smart contracts?**


* Follow thorough testing practices including unit tests, integration tests, and using testnets. Also, consider security audits and peer reviews to ensure contract integrity and security.






![](https://metana.io/wp-content/uploads/2024/02/Modifying-EVM-Storage-to-Seed-Token-Balances-in-Testing.jpg) 





[PrevPreviousNFTs in Gaming: From Pixels to Profits](https://metana.io/blog/nfts-in-gaming-from-pixels-to-profits/) 




[NextSolidity Runtime Errors: A Beginner’s GuideNext](https://metana.io/blog/solidity-runtime-errors-a-beginners-guide/) 







#### Metana Guarantees  a Job 💼

 





#### Plus Risk Free 2-Week Refund Policy ✨

 




 You’re guaranteed a new job in web3—or you’ll get a full tuition refund. We also offer a hassle-free two-week refund policy. If you’re not satisfied with your purchase for any reason, you can request a refund, no questions asked.

 






Web3 Solidity Bootcamp
======================

 





 The most advanced Solidity curriculum on the internet!

 




* 4 Months
* Prior coding experience required
* 20h/ Week
* 1-on-1 mentorship
* Expert code reviews
* Coaching & career services






[View Program](/web3-solidity-bootcamp-ethereum-blockchain/)







Full Stack Web3 Beginner Bootcamp
=================================

 





 Learn foundational principles while gaining hands-on experience with Ethereum, DeFi, and Solidity.

 




* 7 Months
* Beginner - Zero to Hero
* 25h/ Week
* Your very own personal support tutor
* 1-on-1 mentorship
* Expert code reviews
* Coaching & career services






[View Program](/web3-beginner-bootcamp/)













You may also like
-----------------

 






![](https://metana.io/wp-content/uploads/2024/07/Protect-Yourself-from-Rug-Pulls-Tips-to-Avoid-Crypto-Scams-640x364.jpg)







### [Metana Editorial](https://metana.io/blog/author/editorial/)




14 mins ago

#### [Protect Yourself from Rug Pulls: Tips to Avoid Crypto Scams](https://metana.io/blog/protect-yourself-from-rug-pulls-tips-to-avoid-crypto-scams/)




The world of Web3 is brimming with promises of high returns and revolutionary projects, driving 


![](https://metana.io/wp-content/uploads/2024/07/ERC-Token-Standards-Your-Simplified-Guide-copy-640x364.jpg)







### [Metana Editorial](https://metana.io/blog/author/editorial/)




1 day ago

#### [Address Poisoning in Smart Contracts](https://metana.io/blog/address-poisoning-in-smart-contracts/)




Web3 thrives on user empowerment and the ease of sending and receiving cryptocurrency. However, a 
 







#### Metana Guarantees  a Job 💼

 





#### Plus Risk Free 2-Week Refund Policy

 




You’re guaranteed a new job in web3—or you’ll get a full tuition refund. We also offer a hassle-free two-week refund policy. If you’re not satisfied with your purchase for any reason, you can request a refund, no questions asked.

 






#### Web3 Solidity Bootcamp

 





 The most advanced Solidity curriculum on the internet

 




* 4 Months
* Prior coding experience required
* 20h/ Week
* 1-on-1 mentorship
* Expert code reviews
* Coaching & career services






[View Program](/web3-solidity-bootcamp-ethereum-blockchain/)







Full Stack Web3 Beginner Bootcamp
=================================

 





 Learn foundational principles while gaining hands-on experience with Ethereum, DeFi, and Solidity.

 




* 7 Months
* Beginner - Zero to Hero
* 25h/ Week
* Your very own personal support tutor
* 1-on-1 mentorship
* Expert code reviews
* Coaching & career services







 Learn foundational principles while gaining hands-on experience with Ethereum, DeFi, and Solidity.

 




[View Program](/web3-beginner-bootcamp/)







Events by Metana
================

 





 Dive into the exciting world of Web3 with us as we explore cutting-edge technical topics, provide valuable insights into the job market landscape, and offer guidance on securing lucrative positions in Web3. 

 




 





 







Do you have anything you want us to cover in our blog posts? What should we talk about next? We need your suggestions! 
 





Submit
















Start Your  Application
-----------------------

 






Secure your spot now. Spots are limited, and we accept qualified applicants on a first come, first served basis..




 






Email(Required)

Career Track(Required)


Web3



Data



Full Stack



Cyber

  








Δ










The application is free and takes just 3 minutes to complete.

 















##### What is included in the course?

 






### Expert-curated curriculum










### Weekly 1:1 video calls with your mentor










### Weekly group mentoring calls










### On-demand mentor support










### Portfolio reviews by Design hiring managers










### Resume & LinkedIn profile reviews










### Active online student community










### 1:1 and group career coaching calls










### Access to our employer network










### Job Guarantee




















 






###### Address

 





 44 Montgomery St,   

San Francisco, CA 94104, United States

 












Email 







Subscribe












###### Contact us

 





###### Call us directly

 





 (415) 416-0800

 





###### Mail us directly

 





 [[email protected]](/cdn-cgi/l/email-protection)

 









### Company

 




* [Home](/)
* [Blog](https://metana.io/blog/)
* [Jobs at Metana](/jobs/)
* [Bootcamp Application](https://metana.io/apply/)
* [Refer a friend](/refer/)
* [Student Perks](/perks/)
* [Testimonials](/reviews)
* [LMS login](https://app.metana.io/)
* [Open LMS login (Full Stack)](https://open.metana.io/)









### Bootcamp

 




* [Web3 Bootcamps](https://metana.io/web3-0-bootcamp/)
* [- Solidity Bootcamp](https://metana.io/web3-solidity-bootcamp-ethereum-blockchain/)
* [- Web3 Beginner Bootcamp](https://metana.io/web3-solidity-bootcamp-ethereum-blockchain/)
* [- Rust Bootcamp](https://metana.io/web3-rust-bootcamp-solana-blockchain/)
* [- ZK Bootcamp](/web3-zero-knowledge-bootcamp/)
* [Data + AI bootcamps](#)
* [- Data Analytics Bootcamp](/data-analytics-bootcamp/)
* [- Data Science Bootcamp](/data-science-bootcamp/)
* [- AI/ML Bootcamp](/ai-machine-learning-bootcamp/)
* [Software Engineering Bootcamp](/full-stack-software-engineer-bootcamp/)
* [Cybersecurity Bootcamp](/cybersecurity-bootcamp/)
* [Jobcamp](/jobcamp/)
* [Tuition](https://metana.io/tuition/)









### For businesses

 




* [Business](https://metana.io/business/)
* [- Hiring Partner](https://metana.io/business/hiring-partner/)
* [- Upskill Your Team](/business/upskill-your-team/)









### Legal

 




* [Licences](https://metana.io/licences/)
* [Metana's Job Guarantee](https://metana.io/job-guarantee/)
* [Withdrawal and Refund Policy](https://metana.io/withdrawal-and-refund-policy/)
* [Privacy Policy](/privacy-policy/)













[Still Unsure?](https://formless.ai/c/6bPi6ASGJ4ge)








[![](https://metana.io/wp-content/uploads/2022/07/Metana-Logo-Black-Full.png)](https://metana.io) 







 Disclaimer:
‍
Metana is involved in the Blockchain Education activities only. We are not dealing with any Crypto related stuff nor provide advice in the Crypto related field.

 

















 Metana is a pioneer in education and career transformation, specializing in today’s most in-demand skills. The leading source for training, staffing, and career transitions, we foster a flourishing community of professionals pursuing careers they love.
| © 2023 Edmore (private) limited

 








[Facebook](https://www.facebook.com/metanahq) 





[Linkedin](https://www.linkedin.com/school/metana/) 














































































Adding {{itemName}} to cart


Added {{itemName}} to cart













Loading...



×






