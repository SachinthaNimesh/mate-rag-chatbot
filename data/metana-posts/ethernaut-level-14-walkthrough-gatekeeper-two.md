



Ethernaut Level 14 Walkthrough: Gatekeeper Two - Metana






















































































 












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





 







Ethernaut Level 14 Walkthrough: Gatekeeper Two
==============================================

 



 * [Janos Barna](https://metana.io/blog/author/janos-barna/)
* [June 22, 2024](https://metana.io/blog/2024/06/22/)
* [Ethernaut Walkthrough](https://metana.io/blog/category/ethernaut-walkthrough/)














**Ethernaut challenges**, comparable to a Web3-themed hacking Capture The Flag (CTF) competition, offer a dynamic environment for diving into Ethereum and Solidity programming. Each level, including **Ethernaut Level 14**, introduces a distinct smart contract puzzle designed to test your abilities in pinpointing and exploiting flaws. This article provides a comprehensive **walkthrough for Ethernaut Level 14**, guiding you through the steps needed to solve the challenge and enhance your understanding of Ethereum security.


The `GatekeeperTwo` Contract
----------------------------


**The `GatekeeperTwo`** contract has a function called `enter` that sets an address as the “entrant” if three conditions (or “gates”) are met. Here is the code:



```
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract GatekeeperTwo {
    address public entrant;

    modifier gateOne() {
        require(msg.sender != tx.origin);
        _;
    }

    modifier gateTwo() {
        uint256 x;
        assembly {
            x := extcodesize(caller())
        }
        require(x == 0);
        _;
    }

    modifier gateThree(bytes8 _gateKey) {
        require(uint64(bytes8(keccak256(abi.encodePacked(msg.sender)))) ^ uint64(_gateKey) == type(uint64).max);
        _;
    }

    function enter(bytes8 _gateKey) public gateOne gateTwo gateThree(_gateKey) returns (bool) {
        entrant = tx.origin;
        return true;
    }
}
```

Gate 1: Understanding `msg.sender` and `tx.origin`
--------------------------------------------------


* `**msg.sender**`: This is the address that directly called the current function. It could be an externally owned account (EOA) or another contract.
* `**tx.origin**`: This is the address of the original external account that started the entire transaction.


To pass this gate, `msg.sender` must not be the same as `tx.origin`. This means the call to the `enter` function must come from another contract, not directly from an EOA. Here’s why:


* If you, as an EOA, call the `enter` function directly, `msg.sender` (your address) will be the same as `tx.origin` (your address).
* If another contract calls the `enter` function, `msg.sender` will be the address of that contract, while `tx.origin` will still be your address (the original initiator).


Gate 2: The Mystery of Code Size
--------------------------------


* `**extcodesize(address)**`: This function returns the size of the code at a given address.
* `**caller()**`: Returns the address of the caller.


For this gate, the code size of the caller must be zero. This is typically true for EOAs since they don’t have associated code, but since gate one requires a contract to call this function, how can a contract have a code size of zero?



![Illustration representing barriers for Ethernaut Level 14 GatekeeperTwo challenge walkthrough, part of the Ethernaut challenge series.](https://metana.io/wp-content/uploads/2024/06/BigLevel14.svg)
How a Contract Can Have Code Size Zero
--------------------------------------


When a contract is being deployed, it has two stages:


1. **Creation Bytecode**: This is the bytecode needed to create the contract and execute its constructor.
2. **Runtime Bytecode**: This is the actual code that runs the contract’s functions once deployed.


During the contract’s construction (before its constructor finishes executing), the contract’s runtime code isn’t yet stored on the blockchain. Therefore, its code size is zero during this period.


Gate 3: Bitwise XOR and Hashing
-------------------------------


* `**keccak256(abi.encodePacked(msg.sender))**`: Computes a Keccak-256 hash of the encoded `msg.sender`.
* `**bytes8(...)**`: Converts the hash to `bytes8`, taking the least significant 8 bytes.
* `**uint64(...)**`: Casts `bytes8` to a `uint64` integer.
* `**^**`**(Bitwise XOR)**: A binary operation where each bit of the output is the same as the corresponding bit in one operand if the bit in the other operand is 0, and it is different if the corresponding bit in the other operand is 1.


To pass this gate, the XOR of the hash of `msg.sender` (converted to `uint64`) and `_gateKey` must equal the maximum value for a `uint64` (which is `uint64(0) - 1` or `0xFFFFFFFFFFFFFFFF`).


Bitwise XOR Explained
---------------------


* **XOR Operation**: If the bits are the same, the result is `0`. If the bits are different, the result is `1`.


For example:


* `1010` XOR `0101` = `1111`
* `1111` XOR `1111` = `0000`


Given the XOR condition, `_gateKey` must be the bitwise complement of the hash of `msg.sender`.


Solution: Exploiting the Contract
---------------------------------


To solve the challenge, we need:


1. A contract to call the `enter` function (to pass gate one).
2. The call to be made during the contract’s construction (to pass gate two).
3. The correct `_gateKey` (to pass gate three).



```
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Gate2Attack {
    constructor(address _address) {
        bytes8 key = bytes8(uint64(bytes8(keccak256(abi.encodePacked(address(this))))) ^ (uint64(0) - 1));
        (bool success,) = _address.call(abi.encodeWithSignature('enter(bytes8)', key));
        require(success, "Call failed");
    }
}
```

Why This Contract Can Hack `GatekeeperTwo`
------------------------------------------


Now, let’s explain how this contract manages to pass each gate of the `GatekeeperTwo` contract.


### Gate 1: `msg.sender` vs `tx.origin`



```
modifier gateOne() {
    require(msg.sender != tx.origin);
    _;
}
```

* **Requirement**: `msg.sender` must not be equal to `tx.origin`.
* **How It Passes**: When the `Gate2Attack` contract calls the `enter` function, `msg.sender` is the address of the `Gate2Attack` contract, and `tx.origin` is the address of the user who deployed `Gate2Attack`. These two addresses are different, satisfying the requirement.


### Gate 2: Code Size of the Caller



```
modifier gateTwo() {
    uint256 x;
    assembly {
        x := extcodesize(caller())
    }
    require(x == 0);
    _;
}
```

* **Requirement**: The code size of the caller must be zero.
* **How It Passes**: The call to `enter` is made from the constructor of the `Gate2Attack` contract. During the execution of a contract’s constructor, its runtime code is not yet stored on the blockchain. Hence, the `extcodesize` of the contract is zero at this point, satisfying the requirement.


### Gate 3: Bitwise XOR and Hashing



```
modifier gateThree(bytes8 _gateKey) {
    require(uint64(bytes8(keccak256(abi.encodePacked(msg.sender)))) ^ uint64(_gateKey) == uint64(0) - 1);
    _;
}
```

* **Requirement**: The XOR of `uint64(bytes8(keccak256(abi.encodePacked(msg.sender))))` and `uint64(_gateKey)` must equal `uint64(0) - 1`.
* **How It Passes**:
* The `key` is calculated as follows:
* `keccak256(abi.encodePacked(address(this)))`: Hash the address of the `Gate2Attack` contract.
* `bytes8(...)`: Take the least significant 8 bytes of the hash.
* `uint64(...)`: Cast these bytes to a `uint64` integer.
* `^ (uint64(0) - 1)`: XOR with `uint64(0) - 1` to get the complement.
* This calculation ensures that the XOR condition in the gate is satisfied, allowing the key to pass the check.


Conclusion and Security Takeaways: Ethernaut Level 14
-----------------------------------------------------


**Avoid**`**tx.origin**`**for Authorization**:


* **Issue**: `tx.origin` can be easily manipulated by intermediate contracts.
* **Solution**: Use `msg.sender` for reliable access control


**Be Wary of Code Size Checks**:


* **Issue**: Contracts have zero code size during construction, bypassing `extcodesize` checks.
* **Solution**: Combine code size checks with other robust validation methods.


**Understand Bitwise Operations**:


* **Issue**: Bitwise operations like XOR can be reversed to deduce required inputs.
* **Solution**: Use secure, tested cryptographic methods and avoid easily reversible logic.


**Lifecycle Awareness**:


* **Issue**: Contracts behave differently during deployment, posing security risks.
* **Solution**: Design security mechanisms considering all stages of a contract’s lifecycle.


These insights underscore the importance of using well-established security practices and understanding the intricacies of smart contract behavior in Ethereum.



![faq](https://metana.io/wp-content/uploads/2024/05/Questions-bro-1.svg)
FAQs
----


**What is the Ethernaut Challenge?**


Ethernaut challenges are Web3-themed CTF competitions testing Ethereum and Solidity skills. Learn more.


**What is the goal of the GatekeeperTwo contract?**


Set an address as the “entrant” if three conditions (gates) are met. [Contract code](https://github.com/OpenZeppelin/ethernaut/blob/master/contracts/levels/GatekeeperTwo.sol).


**What are the three gate conditions?**


* **Gate One:** `msg.sender` ≠ `tx.origin`
* **Gate Two:** Caller’s code size = 0
* **Gate Three:** XOR of hash of `msg.sender` and gate key = max uint64


**Why is `msg.sender` different from `tx.origin` in Gate One?**


The call must come from a contract, not directly from an EOA.


**How does a contract have a code size of zero in Gate Two?**


During deployment, the contract’s runtime code isn’t yet stored on the blockchain.


**What is the role of the XOR operation in Gate Three?**


XOR of the hash of `msg.sender` and the gate key must equal the maximum uint64 value.


**How does the solution exploit GatekeeperTwo?**


* The `Gate2Attack` contract calls `enter` during its constructor:


* **Gate One:** `msg.sender` ≠ `tx.origin`
* **Gate Two:** Code size is zero during construction
* **Gate Three:** Key satisfies XOR condition


**Why avoid `tx.origin` for authorization?**


* It can be manipulated by intermediate contracts. Use `msg.sender`. More info.


**What are the security takeaways?**


* Avoid `tx.origin`
* Combine code size checks with other validations
* Use secure cryptographic methods
* Design for all contract stages


**How can I learn more about securing smart contracts?**


* Study best practices and participate in Ethernaut challenges.






![](https://metana.io/wp-content/uploads/2024/06/Ethernaut-Level-14-Walkthrough-Gatekeeper-Two.jpg) 





[PrevPreviousReentrancy Attack in Smart Contracts](https://metana.io/blog/reentrancy-attack-in-smart-contracts/) 




[NextImproper Input Validation in Smart ContractsNext](https://metana.io/blog/improper-input-validation-in-smart-contracts/) 







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




8 mins ago

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






