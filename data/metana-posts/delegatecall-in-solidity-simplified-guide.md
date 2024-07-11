



Delegatecall in Solidity: Simplified Guide - Metana






















































































 












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





 







Delegatecall in Solidity: Your Simplified Guide
===============================================

 



 * [Metana Editorial](https://metana.io/blog/author/editorial/)
* [May 28, 2024](https://metana.io/blog/2024/05/28/)
* [Blockchain](https://metana.io/blog/category/blockchain/), [Solidity](https://metana.io/blog/category/solidity/)














**`Delegatecall` is a powerful but intricate feature in Solidity that allows contracts to delegate execution to other contracts.** Understanding `delegatecalls` is crucial for building advanced smart contract functionalities like upgradeable contracts and proxy patterns. This article dives into the world of delegatecalls, exploring their inner workings, potential pitfalls, and best practices.


Understanding `delegatecall`
----------------------------


**`delegatecall` in Solidity** is a low-level function, that enables a contract (the Caller) to execute code from another contract (the Callee) but using the storage, sender, and value of the Caller. Essentially, `delegatecall` preserves the context of the Caller while running the logic of the Callee. This feature is particularly useful for creating upgradeable and modular smart contracts.


Practical Use Cases
-------------------


1. **Upgradeable Contracts**: One of the primary uses of `delegatecall` is to create upgradeable smart contracts. By separating the contract logic from the storage, developers can update the contract’s logic without altering its state. This is achieved by deploying a new contract with the updated logic and directing calls from the proxy contract (which holds the state) to this new logic contract using `delegatecall`.



1. **Modular Contract Systems**: `delegatecall` allows for modular contract design, where different functionalities are split into separate contracts. This modularity enhances the manageability and scalability of the system. Each module can be upgraded independently without affecting the overall system state.


Implementing `delegatecall` in Solidity
---------------------------------------


Here’s a basic example demonstrating how to use `delegatecall`:



```
solidityCopy code<code>pragma solidity ^0.8.0;

contract Callee {
    uint public num;

    function setNum(uint _num) public {
        num = _num;
    }
}

contract Caller {
    uint public num;
    address public calleeAddress;

    function setCalleeAddress(address _calleeAddress) public {
        calleeAddress = _calleeAddress;
    }

    function delegateSetNum(uint _num) public {
        (bool success, bytes memory data) = calleeAddress.delegatecall(
            abi.encodeWithSignature("setNum(uint256)", _num)
        );
        require(success, "delegatecall failed");
    }
}

```

In this example, the `Caller` contract uses `delegatecall` to invoke the `setNum` function from the `Callee` contract. However, the state changes (updating the `num` variable) occur within the `Caller` contract’s storage.


Detailed Example: Proxy Pattern
-------------------------------


A common pattern utilizing `delegatecall` is the proxy pattern. In this pattern, a proxy contract holds the storage and delegates function calls to an implementation contract. Here’s an example:



```
solidityCopy code<code>pragma solidity ^0.8.0;

// Implementation contract
contract Implementation {
    uint public x;
    address public owner;

    function setX(uint _x) public {
        x = _x;
    }
}

// Proxy contract
contract Proxy {
    address public implementation;
    address public owner;

    constructor(address _implementation) {
        implementation = _implementation;
        owner = msg.sender;
    }

    function setImplementation(address _implementation) public {
        require(msg.sender == owner, "Only owner can set implementation");
        implementation = _implementation;
    }

    fallback() external payable {
        (bool success, bytes memory data) = implementation.delegatecall(msg.data);
        require(success, "delegatecall failed");
    }
}

```

In this pattern, the `Proxy` contract can update its implementation by changing the `implementation` address, thereby enabling contract upgrades without changing the storage.


Key Considerations and Risks
----------------------------


* **Security Risks**: Improper use of `delegatecall` can lead to significant vulnerabilities, such as unexpected state changes or reentrancy attacks. Always validate the called function and handle the return values carefully. Ensure the called contract is trusted and verified to avoid security breaches.
* **Storage Layout**: Both the Caller and Callee contracts must share the same storage layout. Any mismatch can lead to unpredictable behavior or security vulnerabilities. Developers must carefully design and document the storage structure to prevent issues.
* **Gas Consumption**: Using `delegatecall` can be more gas-intensive than direct calls due to the additional overhead. Consider this factor when designing your contract architecture to optimize for efficiency.
* **Complexity**: `delegatecall` adds complexity to the contract logic. Thorough testing and auditing are essential to ensure the system works as intended and remains secure.



![delegate call in solidity](https://metana.io/wp-content/uploads/2024/05/chris-ried-ieic5Tq8YMk-unsplash-1.jpg)
Conclusion
----------


`delegatecall` is a potent tool in Solidity, offering flexibility for creating upgradeable and modular contracts. However, it requires a deep understanding and cautious implementation to avoid potential pitfalls. By mastering `delegatecall`, you can leverage its benefits while ensuring the security and efficiency of your smart contracts.



![faq](https://metana.io/wp-content/uploads/2024/05/Questions-bro-1.svg)
FAQs:
-----


**What is delegatecall in Solidity?**


* delegatecall is a low-level function in Solidity that allows a contract to execute code from another contract while maintaining its own context (storage, msg.sender, etc.).


**Why use delegatecall in Solidity?**


* delegatecall is used for code reuse and to enable upgradable contracts by delegating function calls to different contract versions.


**How does delegatecall differ from call in Solidity?**


* While call changes the context to the target contract, delegatecall keeps the context of the calling contract, allowing access to its storage and state.


**What are the risks associated with delegatecall?**


* delegatecall can introduce security vulnerabilities if the called contract has malicious code or if storage layouts are not aligned properly.


**How can you ensure delegatecall is secure?**


* Ensure that the called contract is trusted, carefully manage storage layouts, and perform thorough testing and auditing to mitigate security risks.


**Can delegatecall be used for contract upgrades?**


* Yes, delegatecall is often used in proxy patterns to enable contract upgrades by directing calls to new implementations while preserving state.


**What is the difference between staticcall and delegatecall?**


* staticcall is used to call functions without modifying state, while delegatecall allows for state modification within the caller’s context.


**What is a proxy contract in Solidity?**


* A proxy contract delegates calls to another contract (implementation) using delegatecall, enabling contract logic upgrades while keeping the same address.


**How do you test delegatecall functionality in Solidity?**


* Testing delegatecall involves writing unit tests to check the correct execution of functions, ensuring storage layout alignment, and verifying expected behavior.


**What is the significance of the fallback function in Solidity?**


* The fallback function is a default function that handles calls to non-existent functions in a contract, often used in conjunction with delegatecall for proxies.






![](https://metana.io/wp-content/uploads/2024/05/Delegatecall-in-Solidity-Simplified-Guide.jpg) 





[PrevPreviousWhat is Node.js? Explained Simply](https://metana.io/blog/what-is-node-js-explained-simply/) 




[NextHow to Launch a Web3 Project SuccessfullyNext](https://metana.io/blog/how-to-launch-a-web3-project-successfully/) 







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




10 mins ago

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






