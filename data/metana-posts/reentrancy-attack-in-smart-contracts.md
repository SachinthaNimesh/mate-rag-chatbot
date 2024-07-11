



Reentrancy Attack in Smart Contracts - Metana






















































































 












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





 







Reentrancy Attack in Smart Contracts
====================================

 



 * [Metana Editorial](https://metana.io/blog/author/editorial/)
* [June 21, 2024](https://metana.io/blog/2024/06/21/)
* [Smart Contracts](https://metana.io/blog/category/smart-contracts/), [Solidity](https://metana.io/blog/category/solidity/)














In a traditional transaction, one party sends funds to another in exchange for goods or services. This exchange typically follows a well-defined sequence of steps. However, in the realm of smart contracts, vulnerabilities can arise when this sequence is not properly enforced.


**This vulnerability, known as a reentrancy attack, allows a malicious actor to exploit a weakness in a smart contract’s code**. In this article, we’ll delve into the specifics of reentrancy attacks, exploring how they work, examining a real-world example, and discussing methods for prevention. We’ll also provide clear code examples to illustrate these concepts.


What is a Reentrancy Attack?
----------------------------


A reentrancy attack is a type of exploit that targets a vulnerability in smart contract functions involving external calls (like sending funds to another contract). This attack allows the malicious contract to repeatedly call the vulnerable function before it finishes executing, leading to multiple unauthorized executions of the function.


### How It Works


Here’s a step-by-step breakdown of how a reentrancy attack unfolds:


1. **Attacker Initiates:** An attacker sends money to a vulnerable smart contract function.
2. **The Bait is Set:** The function performs its intended action, like transferring some of the attacker’s funds to another address.
3. **The Malicious Call:** Before the function finishes, the attacker’s contract calls back into the original function again.
4. **Double Trouble:** The original function, unaware it’s being re-entered, repeats the steps, sending more funds to the attacker before finally updating its internal state.


This process can be repeated multiple times, draining the contract’s funds before it realizes something is wrong.


### Example of a Vulnerable Smart Contract


Let’s look at a simple example of a vulnerable smart contract in Solidity:



```
pragma solidity ^0.8.0;

contract VulnerableContract {
    mapping(address => uint) public balances;

    function deposit() public payable {
        balances[msg.sender] += msg.value;
    }

    function withdraw(uint _amount) public {
        require(balances[msg.sender] >= _amount, "Insufficient balance");

        // Transfer the requested amount to the caller
        (bool success, ) = msg.sender.call{value: _amount}("");
        require(success, "Transfer failed");

        // Update the balance only after transferring
        balances[msg.sender] -= _amount;
    }
}

```

In this contract, the `withdraw` function is vulnerable because it sends Ether to the caller before updating the balance.


The DAO Hack (2016)
-------------------


One of the most infamous reentrancy attacks involved a Decentralized Autonomous Organization (DAO) on the Ethereum blockchain. The DAO’s smart contract had a critical reentrancy bug. An attacker exploited this by calling the DAO’s contribution function, essentially tricking the contract into sending them Ether multiple times. This resulted in a loss of over 60 million USD worth of Ether!


### How the DAO Hack Worked


1. The attacker created a malicious contract and called the `withdraw` function of the DAO.
2. Before the DAO could update the balance, the attacker’s contract called back into the `withdraw` function again.
3. This reentrancy allowed the attacker to drain funds repeatedly until the contract was empty.



![Simplified illustration of a reentrancy attack in smart contracts, showing a smart contract with a recursive function call, an Ethereum logo, and a hacker symbol highlighting vulnerabilities in the code.](https://metana.io/wp-content/uploads/2024/06/DALL·E-2024-06-19-11.15.02-An-illustration-representing-a-reentrancy-attack-in-smart-contracts.-Simplify-the-image-by-focusing-on-a-smart-contract-with-a-recursive-function-call.jpg)
Preventing Reentrancy Attacks
-----------------------------


Thankfully, there are ways to prevent reentrancy attacks. Here are some popular methods:


1. **Checks-Effects-Interactions Pattern (CEI)** : This coding pattern ensures the contract updates its internal state (like recording a transfer) before making any external calls. By doing so, the contract can prevent reentrancy because the state is already updated when the external call is made.



```
pragma solidity ^0.8.0;

contract SecureContract {
    mapping(address => uint) public balances;

    function deposit() public payable {
        balances[msg.sender] += msg.value;
    }

    function withdraw(uint _amount) public {
        require(balances[msg.sender] >= _amount, "Insufficient balance");

        // Update the balance first
        balances[msg.sender] -= _amount;

        // Then transfer the requested amount
        (bool success, ) = msg.sender.call{value: _amount}("");
        require(success, "Transfer failed");
    }
}
```

In this version, the balance is updated before the transfer, preventing reentrancy.


2. **Reentrancy Guards** : Reentrancy guards are special functions that prevent a function from being re-entered by the same caller. One common way to implement this is by using a mutex, which locks the function during execution.



```
pragma solidity ^0.8.0;

contract SecureContractWithReentrancyGuard {
    mapping(address => uint) public balances;
    bool internal locked;

    modifier noReentrancy() {
        require(!locked, "No re-entrancy");
        locked = true;
        _;
        locked = false;
    }

    function deposit() public payable {
        balances[msg.sender] += msg.value;
    }

    function withdraw(uint _amount) public noReentrancy {
        require(balances[msg.sender] >= _amount, "Insufficient balance");

        // Update the balance first
        balances[msg.sender] -= _amount;

        // Then transfer the requested amount
        (bool success, ) = msg.sender.call{value: _amount}("");
        require(success, "Transfer failed");
    }
}
```

The `noReentrancy` modifier ensures that the function cannot be re-entered until it has finished executing.


3. Solidity Safe Math Solidity offers functions for safe arithmetic operations that prevent overflow errors, which attackers can sometimes leverage in reentrancy attacks. Using the SafeMath library can add an extra layer of security.



```
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract SecureContractWithSafeMath {
    using SafeMath for uint;
    mapping(address => uint) public balances;
    bool internal locked;

    modifier noReentrancy() {
        require(!locked, "No re-entrancy");
        locked = true;
        _;
        locked = false;
    }

    function deposit() public payable {
        balances[msg.sender] = balances[msg.sender].add(msg.value);
    }

    function withdraw(uint _amount) public noReentrancy {
        require(balances[msg.sender] >= _amount, "Insufficient balance");

        // Update the balance first
        balances[msg.sender] = balances[msg.sender].sub(_amount);

        // Then transfer the requested amount
        (bool success, ) = msg.sender.call{value: _amount}("");
        require(success, "Transfer failed");
    }
}
```

By using SafeMath, you ensure that your contract performs arithmetic operations safely.


Conclusion
----------


Reentrancy attacks are a serious threat to smart contracts, but they can be effectively mitigated with proper coding practices. By understanding how these attacks work and implementing preventive measures like the Checks-Effects-Interactions pattern, reentrancy guards, and Solidity’s SafeMath library, developers can build more secure smart contracts that safeguard user funds.



![faq](https://metana.io/wp-content/uploads/2024/05/Questions-bro-1.svg)
FAQs
----


**What is a reentrancy attack in smart contracts?**


* A reentrancy attack exploits a vulnerability in smart contracts, allowing an attacker to repeatedly call a function before previous executions complete, leading to unexpected behaviors and potential loss of funds.


**How can reentrancy attacks be prevented in smart contracts?**


* Reentrancy attacks can be prevented by using proper coding practices such as the “Checks-Effects-Interactions” pattern, reentrancy guards, and thorough contract audits.


**Why are reentrancy attacks a significant concern in DeFi?**


* DeFi platforms often handle large amounts of assets, making them prime targets for reentrancy attacks. Exploits can result in substantial financial losses and damage to the platform’s reputation.


**What are some famous examples of reentrancy attacks?**


* One of the most notable examples is the DAO hack in 2016, where attackers exploited a reentrancy vulnerability, leading to the loss of around $60 million worth of Ether.


**How does the “Checks-Effects-Interactions” pattern help prevent reentrancy attacks?**


* This pattern ensures that state changes (checks and effects) are made before any external interactions, reducing the risk of reentrancy attacks by updating the contract state before calling external contracts.


**Why is blockchain security important?**


* Blockchain security is crucial because it protects users’ assets, maintains trust in the system, and ensures the integrity of decentralized applications and services.


**What are some common vulnerabilities in smart contracts?**


* Common vulnerabilities include reentrancy, integer overflow/underflow, improper access control, and unchecked external calls.


**How can developers ensure their smart contracts are secure?**


* Developers can ensure security by following best practices, conducting regular audits, using formal verification methods, and staying updated with the latest security research and tools.


**What role do auditors play in blockchain security?**


* Auditors review and analyze smart contract code to identify vulnerabilities, provide recommendations for improvements, and help ensure that the contracts function as intended without security flaws.






![](https://metana.io/wp-content/uploads/2024/06/Reentrancy-Attack-in-Smart-Contracts.jpg) 





[PrevPreviousAccess Control in Solidity Smart Contracts](https://metana.io/blog/access-control-in-solidity-smart-contracts/) 




[NextEthernaut Level 14 Walkthrough: Gatekeeper TwoNext](https://metana.io/blog/ethernaut-level-14-walkthrough-gatekeeper-two/) 







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






