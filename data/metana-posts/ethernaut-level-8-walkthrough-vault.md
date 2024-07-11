



Ethernaut Level 8 Walkthrough: Vault - Metana






















































































 












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





 







Ethernaut Level 8 Walkthrough: Vault
====================================

 



 * [Rupam Roychoudhury](https://metana.io/blog/author/rupam-roychoudhury/)
* [May 19, 2024](https://metana.io/blog/2024/05/19/)
* [Ethernaut Walkthrough](https://metana.io/blog/category/ethernaut-walkthrough/)














Ethernaut challenges, akin to a hacking Capture The Flag (CTF) for Web3 enthusiasts, provide an immersive platform to explore Ethereum and Solidity programming. Each challenge presents a unique smart contract puzzle, testing your skills in identifying and exploiting vulnerabilities.


As a full-stack software engineer venturing into the world of blockchain technology, Ethernaut challenges serve as stepping stones to understand [smart contract](https://metana.io/blog/solidity-smart-contracts/) vulnerabilities. With each challenge, we gain deeper insights into blockchain security, enhancing our capabilities in decentralized application development. In this blog we will be unveiling the **Ethernaut Level 8** where we unravel the mysteries of Solidity smart contracts and master the art of bypassing security locks.


Decoding the Vault Contract
---------------------------


Explore the inner workings of the `Vault` contract, designed with a clever locking mechanism:



```
// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

contract Vault {

    bool public locked;

    bytes32 private password;

    constructor(bytes32 _password) {

        locked = true;

        password = _password;

    }

    function unlock(bytes32 _password) public {

        if (password == _password) {

            locked = false;

        }

    }

}
```

Unveiling the secrets
---------------------


* `locked`: Indicates whether the vault is locked (`true`) or unlocked (`false`).
* `password`: Privately stores the password as a `bytes32` hash.


The `constructor` initializes the vault with the specified password and locks it initially.


The `unlock` function checks if the provided password matches the stored `password` to unlock the vault.


Understanding the Vulnerability
-------------------------------


The vulnerability in this smart contract lies in the storage of sensitive information (password) directly on the blockchain. In the decentralized and transparent nature of blockchain, all data stored on the blockchain is visible to anyone. This means that even though the password is stored as a private variable (private bytes32 password), its value can still be retrieved and manipulated through various techniques.


Why is Blockchain Transparent?
------------------------------


Blockchain’s transparency stems from its fundamental design principles. Blockchain operates on a distributed ledger where every transaction is recorded and verified by multiple nodes in the network. This transparency ensures immutability and trust but also means that data stored on the blockchain, including smart contract state variables, is accessible and auditable by anyone.


Cracking the Vault: Techniques Revealed
---------------------------------------


Uncover strategic techniques to deal with the Ethernaut Challenge 8:


### Approach 1: Leveraging Blockchain Explorer


**Transaction Analysis**


Analyze blockchain transactions associated with the `Vault` contract.


**State Change Identification**


Identify transactions altering the contract state, particularly changes to the `password` variable.


**Retrieve Password Hash**


Extract the hashed password value from relevant transactions to unlock the vault.


### Approach 2: Harnessing Ethereum Developer Console


**Deploy New Contract Instance**


Click on the new instance button in ethernaut challenge page.


**Access Developer Console**


Press F12 in the keyboard to open the developer console


**Retrieve Password Hash**


Execute command `await web3.eth.getStorageAt(contract.address, 1)` to retrieve the stored password hash. Basically this command is retrieving the value from storage slot 2 as the password variable is stored in the 2nd storage slot. To understand more about storage slot in blockchain check this [link](https://medium.com/@ozorawachie/solidity-storage-layout-and-slots-a-comprehensive-guide-2cee71817ed8%23:~:text=Storage%2520is%2520divided%2520into%2520slots,using%2520a%2520key-value%2520pair.).


**Unlock the Vault**


Utilize the retrieved password hash to call the `unlock` function and gain access to the vault.


Accessing and Submitting the Solution
-------------------------------------


Once you have retrieved the password copy the contract code and create a new contract **Vault** in Remix IDE.


Compile the code then use the “At Address” feature to deploy the contract at the specified address retrieved from the Ethernaut browser console.



![ethernaut level 8 vault walkthrough](https://metana.io/wp-content/uploads/2024/05/image-2.png)
Call the unlock function of the deployed contract instance using the retrieved password hash.


After successfully unlocking the vault, submit the instance on Ethernaut platform to complete the challenge.


Conclusion: Ethernaut Level 8
-----------------------------


Ethernaut Challenge 8 provides invaluable lessons in smart contract vulnerabilities, emphasizing the importance of robust security practices in blockchain development.Unlock the vault responsibly and continue your journey towards mastering blockchain security!


*Ready for the next Ethernaut challenge? Click to check out the [previous ethernaut challenge](https://metana.io/blog/ethernaut-level-7-walkthrough-force/) and see what’s next in our series!*



![faq](https://metana.io/wp-content/uploads/2024/05/Questions-bro-1.svg)
FAQs
----


**What is the vulnerability in Ethernaut Challenge 8?**


* Ethernaut Challenge 8 exposes the risk of storing sensitive data (like passwords) directly in smart contract state variables, which can be exploited through blockchain analysis.


**How can developers mitigate risks associated with smart contract vulnerabilities?**


* Developers should avoid storing sensitive information directly in contract state and utilize encryption techniques for protection.


**What skills are essential for tackling Ethernaut challenges?**


* Solidity proficiency, Ethereum smart contract understanding, and strategic problem-solving abilities in a blockchain context.


**Which tools are recommended for Ethernaut challenges?**


* Use Remix IDE for Solidity development, MetaMask for Ethereum interactions, and Etherscan for blockchain insights.


**Can participants engage in Ethernaut challenges without using real ETH?**


* Yes, explore test networks like Sepolia or Holesky, where test ETH is available for learning and challenges.






![Ethernaut-Level-8-Walkthrough-Vault](https://metana.io/wp-content/uploads/2024/05/Ethernaut-Level-8-Walkthrough-Vault.jpg) 





[PrevPreviousLow Level Call vs High Level Call in Solidity [Simplified]](https://metana.io/blog/low-level-call-vs-high-level-call-in-solidity/) 




[NextEthernaut Level 9 Walkthrough: KingNext](https://metana.io/blog/ethernaut-level-9-walkthrough-king/) 







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






