



Ethernaut Level 4 Walkthrough: Telephone - Metana


















































































 












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





 







Ethernaut Level 4 Walkthrough: Telephone
========================================

 



 * [Sven Daneel](https://metana.io/blog/author/sven-daneel/)
* [May 1, 2024](https://metana.io/blog/2024/05/01/)
* [Ethernaut Walkthrough](https://metana.io/blog/category/ethernaut-walkthrough/)















This [Web3](https://metana.io/web3-beginner-bootcamp/)/Solidity-based wargame is akin to a hacking Capture The Flag (CTF) challenge, where each level presents a smart contract puzzle waiting to be ‘hacked’. It’s an immersive and interactive way to learn about Ethereum and Solidity programming. **Let’s take a look at the Ethernaut Level 4 Walkthrough: Telephone**


![ethernaut level 4 walkthrough telephone](https://metana.io/wp-content/uploads/2024/04/image-5.png)
Telephone: Owning Up to the Deceptiveness of tx.origin
------------------------------------------------------


In the intriguing world of Ethereum smart contracts, security is paramount. Today, we’ll delve into Challenge 4: Telephone, a clever puzzle that exposes a vulnerability in how contracts identify message originators. By the end, we’ll not only conquer the challenge but gain valuable insights into the intricacies of `tx.origin` and `msg.sender`.


### The Challenge’s Call


Challenge 4 presents a seemingly straightforward objective: claim ownership of a pre-deployed smart contract. But there’s a catch! Directly calling the contract’s `changeOwner` function won’t grant ownership. This compels us to think outside the box and exploit a clever trick.


### Unveiling the Contract’s Secrets


The first step is to understand the contract’s logic. We need to dissect how it verifies ownership claims. Here, the key lies in differentiating between two crucial variables:


* `tx.origin`: This represents the original initiator of the transaction, the user’s wallet address.
* `msg.sender`: This signifies the address directly calling the function, which could be another contract.


### The Art of Deception


The vulnerability lies in the fact that a contract can’t directly determine `tx.origin`. Here’s where the magic happens:


1. We craft a new smart contract, let’s call it `Impersonator`.
2. `Impersonator` mirrors the `changeOwner` function from the Telephone contract.
3. The twist: When called, `Impersonator`‘s `changeOwner` function relays the call to the Telephone contract’s `changeOwner`, but with a crucial twist.


### The Grand Illusion


Instead of directly calling Telephone’s `changeOwner`, `Impersonator` acts as a middleman. This seemingly insignificant step alters how the Telephone contract perceives the message origin. Because `Impersonator` calls Telephone’s `changeOwner`, `msg.sender` becomes `Impersonator`‘s address, while `tx.origin` remains our user wallet.


The Telephone contract, lacking the ability to see `tx.origin`, gets deceived. It believes `Impersonator` is claiming ownership, while in reality, the transaction originated from our wallet, making us the true owner.


### Beyond the Challenge


Challenge 4 sheds light on the potential pitfalls of relying solely on `msg.sender` for authorization. It emphasizes the importance of considering `tx.origin` when necessary to prevent ownership manipulation or other vulnerabilities.


### The Road Ahead


The Ethernaut challenges provide a fantastic platform to explore the intricacies of smart contract security. Each challenge unveils new concepts and challenges our understanding of Solidity. As we venture further, stay tuned for more explorations into the captivating realm of Ethereum smart contracts!


This blog post explores Challenge 4, highlighting the significance of understanding `tx.origin` and `msg.sender` for robust smart contract design. By exploiting the limitations of message origin identification, we not only conquered the challenge but gained valuable security insights.


Ready for the next Ethernaut challenge? Click to check out the [previous ethernaut challenge](https://metana.io/blog/ethernaut-level-3-walkthrough-coin-flip/) and see what’s [next](https://metana.io/blog/ethernaut-level-4-walkthrough-telephone) in our series!



![faq](https://metana.io/wp-content/uploads/2024/01/Questions-cuate-1024x1024.png)
FAQs
----


**What is the Ethernaut Level 4: Telephone challenge?**


* The challenge involves interacting with a smart contract to change ownership by exploiting specific conditions in its code.


**How do you solve the Ethernaut Level 4: Telephone challenge?**


* Solve it by using another contract to call the target contract’s function, thereby bypassing the direct call restriction.


**What skills are needed to complete Ethernaut Level 4?**


* A basic understanding of Ethereum, Solidity, and how smart contracts operate is essential.


**What tools are required for the Ethernaut challenges?**


* Tools like Remix IDE, Metamask, and a solid understanding of Ethereum’s test networks are necessary.


**What is the importance of the Telephone challenge in learning Ethereum?**


* It teaches about function visibility, contract interaction, and security considerations in smart contract development.







![](https://metana.io/wp-content/uploads/2024/04/Ethernaut-Level-4-Walkthrough-Telephone.jpg) 





[PrevPreviousThe Rise of Layer 2 Solutions](https://metana.io/blog/the-rise-of-layer-2-solutions/) 




[NextDAO Treasury ManagementNext](https://metana.io/blog/dao-treasury-management/) 







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






