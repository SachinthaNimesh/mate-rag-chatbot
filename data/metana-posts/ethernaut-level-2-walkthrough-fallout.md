



Ethernaut Level 2 Walkthrough: Fallout - Metana



















































































 












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





 







Ethernaut Level 2 Walkthrough: Fallout
======================================

 



 * [Marko Jauregui](https://metana.io/blog/author/marko-jauregui/)
* [March 21, 2024](https://metana.io/blog/2024/03/21/)
* [Ethernaut Walkthrough](https://metana.io/blog/category/ethernaut-walkthrough/)















**The Ethernaut Level 2 offers a fascinating glimpse into the vulnerabilities that can arise from seemingly minor oversights in smart contract development.** This article takes you through the challenge, revealing the misstep in the contract’s construction and guiding you through the process of exploiting it. Furthermore, we explore the evolution of constructors in Solidity, providing a comprehensive understanding of how this aspect of Solidity has matured and how it impacts smart contract security and development.


The Fallout Challenge: A Case Study in Smart Contract Vulnerability
-------------------------------------------------------------------


At the heart of the Ethernaut Challenge 2 is a smart contract named Fallout, which contains a critical flaw due to an incorrectly named constructor function. This vulnerability stems from a period in Solidity’s history when constructors were defined by naming a function after the contract. This method led to potential risks, especially if the contract was renamed without updating the constructor function’s name, thereby leaving the function open to being called by anyone.



```
// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

import 'openzeppelin-contracts-06/math/SafeMath.sol';

contract Fallout {

  using SafeMath for uint256;
  mapping (address => uint) allocations;
  address payable public owner;


  /* constructor */
  function Fal1out() public payable {
    owner = msg.sender;
    allocations[owner] = msg.value;
  }

  modifier onlyOwner {
	        require(
	            msg.sender == owner,
	            "caller is not the owner"
	        );
	        _;
	    }

  function allocate() public payable {
    allocations[msg.sender] = allocations[msg.sender].add(msg.value);
  }

  function sendAllocation(address payable allocator) public {
    require(allocations[allocator] > 0);
    allocator.transfer(allocations[allocator]);
  }

  function collectAllocations() public onlyOwner {
    msg.sender.transfer(address(this).balance);
  }

  function allocatorBalance(address allocator) public view returns (uint) {
    return allocations[allocator];
  }
}
```

### Exploiting the Misnamed Constructor


The challenge revolves around the fact that the Fal1out function, intended as the constructor, was misnamed. This oversight allowed any user to call this function, claim ownership of the contract, and expose a significant security vulnerability. The solution involves interacting with the contract to call this misnamed function, demonstrating a critical lesson in the importance of precise syntax and naming conventions in smart contract development.


The Evolution of Constructors in Solidity
-----------------------------------------


The journey of constructors in Solidity from version-specific functions to the adoption of the constructor keyword reflects the language’s evolution toward enhanced safety, readability, and developer experience.


### Early Versions (Before 0.4.22)


Originally, Solidity utilized a naming convention for constructors that required the function to share the name with the contract. This approach, while straightforward, introduced a vulnerability to renaming errors—a concern highlighted by our exploration of the Ethernaut Challenge 2.



```
// Example of an old-style constructor
contract MyContract {
    uint public value;

    function MyContract(uint _value) public {
        value = _value;
    }
}
```

### Introduction of the constructor Keyword (0.4.22 and Later)


The introduction of the constructor keyword in Solidity 0.4.22 marked a significant leap forward, eliminating the risk associated with contract renaming and enhancing code clarity.



```
// Example with the `constructor` keyword
contract MyContract {
    uint public value;

    constructor(uint _value) public {
        value = _value;
    }
}
```

### Current Best Practices


Today, the best practice involves using the constructor keyword without visibility specifiers, a testament to Solidity’s ongoing development aimed at improving security and developer experience.



```
// Current best practice example
contract MyContract {
    uint public value;

    constructor(uint _value) {
        value = _value;
    }
}
```

Implementing the Solution to the Challenge
------------------------------------------


Understanding the historical context and evolution of constructors in Solidity enhances our appreciation for the solution to the Ethernaut Challenge 2. By exploiting the misnamed constructor vulnerability, we not only navigate the challenge but also engage with a practical example of how Solidity’s development has sought to mitigate such risks.


### Steps to Claim Ownership


1. Identifying the misnamed constructor (Fal1out).
2. Interacting with the contract to call this function. Setting the owner to be the `msg.sender`
3. Verifying ownership transfer through automated testing and interaction scripts, or also through the Ethernaut broswer console.


This approach, while specific to the challenge, offers broader lessons in smart contract security, attention to detail, and the importance of staying updated with Solidity’s best practices.


Conclusion: Lessons Beyond the Challenge
----------------------------------------


**The Ethernaut Challenge 2**, set against the backdrop of Solidity’s evolution, provides a rich learning experience that extends beyond the specifics of the challenge. It emphasizes the importance of understanding the fundamentals of [smart contract](https://metana.io/blog/what-is-a-smart-contract-understand-contracts-on-the-blockchain/) development, the implications of language updates, and the continuous need for diligence and best practices in the blockchain development space. As Solidity and the Ethereum ecosystem evolve, staying informed and engaged with these developments remains crucial for developers aspiring to build secure, efficient, and reliable smart contracts.


If you are curious about the Fallback Challenge, don’t worry! we got your back. Go checkout our article about the Ethernaut Challenge 1 [here](https://metana.io/blog/first-ethernaut-challenge-fallback/).


Ready for the next Ethernaut challenge? Click to see what’s [next](https://metana.io/blog/ethernaut-level-3-walkthrough-coin-flip/) in our series!


![faqethernaut level 2ethernaut challenge 2falloutwalkthrough](https://metana.io/wp-content/uploads/2024/01/Questions-cuate-1024x1024.png)
FAQs:
-----


**What is the Ethernaut Challenge 2 about?**


* The Ethernaut Challenge 2, known as “Fallout,” is a [smart contract](https://metana.io/blog/solidity-smart-contracts/) puzzle that involves exploiting a vulnerability due to an incorrectly named constructor function. Participants are tasked with claiming ownership of the contract by calling this misnamed function.


**Why does the misnamed constructor in the Fallout contract pose a vulnerability?**


* In Solidity, constructors are meant to be called once upon contract deployment to initialize the contract’s state. The Fallout contract’s constructor was incorrectly named, making it a regular function callable by anyone. This allows an attacker to claim ownership of the contract by calling the misnamed function.


**How did Solidity’s approach to constructors evolve over time?**


* Initially, Solidity used a naming convention for constructors where the constructor function had the same name as the contract. This changed with Solidity 0.4.22, which introduced the `constructor` keyword, making contract initialization clearer and less prone to errors related to contract renaming.


**What are the current best practices for defining constructors in Solidity?**


* As of the latest Solidity versions, the best practice is to use the `constructor` keyword without visibility specifiers. This approach is more secure and intuitive, eliminating the risks associated with the old naming convention and making the code more readable.


**Can constructors have visibility specifiers in Solidity?**


* Initially, constructors could have visibility specifiers like `public` or `internal`. However, with the introduction of the `constructor` keyword and subsequent Solidity versions, setting visibility for constructors became unnecessary and is now disallowed. Constructors are implicitly internal and are called only once upon contract creation.


**Why is understanding the evolution of Solidity important for developers?**


* Keeping up with Solidity’s evolution helps developers write safer, more efficient, and up-to-date code. Understanding changes, such as the transition to the `constructor` keyword, allows developers to avoid common pitfalls and vulnerabilities in smart contract development.






![](https://metana.io/wp-content/uploads/2024/03/Ethernaut-Level-2-Walkthrough-Fallout.gif) 





[PrevPreviousWeb2 vs. Web3: What’s the Difference? [The Breakthrough]](https://metana.io/blog/web2-vs-web3-whats-the-difference-the-breakthrough/) 




[NextBest Practices for Smart Contract Testing & how toNext](https://metana.io/blog/best-practices-for-smart-contract-testing-how-to/) 







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




13 mins ago

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






