



Ethernaut Level 15 Walkthrough: Naught Coin - Metana





















































































 












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





 







Ethernaut Level 15 Walkthrough: Naught Coin
===========================================

 



 * [Alexis Amoi](https://metana.io/blog/author/alexis-amoi/)
* [June 24, 2024](https://metana.io/blog/2024/06/24/)
* [Ethernaut Walkthrough](https://metana.io/blog/category/ethernaut-walkthrough/)














**Ethernaut Level 15, “Naught Coin,”** throws you headfirst into the world of ERC20 tokens and their potential vulnerabilities. This challenge presents a seemingly locked contract with a 10-year transfer lock on your own token balance. But fear not, intrepid hacker (for educational purposes only!), there’s a way to bypass this lock. Here’s a walkthrough on how to conquer Level 15 and the key takeaways you’ll gain.


Understanding the Challenge:
----------------------------


Upon entering Ethernaut Level 15, you’ll be presented with a deployed Naught Coin contract. This contract inherits the standard ERC20 functionality, allowing you to view your token balance but preventing any transfers due to the built-in timelock. The objective? Find a way to bypass the lock and transfer your tokens out of the contract.


![Ethernaut Level 15 Naught Coin Walkthrough - Solidity code and console output for solving the Ethernaut challenge. The image shows steps and commands used to tackle the Naught Coin challenge in the Ethernaut game.](https://metana.io/wp-content/uploads/2024/06/Screenshot-2024-06-17-at-9.57.38 PM-1.jpg)
The Exploit: Abusing Approvals
------------------------------


The key to cracking the Naught Coin vault lies in understanding the approve function within the ERC20 standard. This function allows users to grant permission to another address (called a spender) to transfer a specific amount of tokens on their behalf.


The vulnerability in this challenge stems from the way the Naught Coin contract interacts with the timelock. While the transfer function is restricted, the approvefunction doesn’t have the same limitations. This creates an opportunity for exploitation of the transferFrom  function.


The Walkthrough:
----------------


1. **Check Your Balance:** Use the console to create a new constant: player and to view your initial token balance in the Naught Coin contract:


![](https://metana.io/wp-content/uploads/2024/06/Screenshot-2024-06-17-at-10.44.09 PM-1024x227.png)
2. Copy the contract into Remix IDE and replace the import with this URL: <https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC20/ERC20.sol>


3. Compile the code and go to the deploy section, make sure to select Injected Provider – MetaMask as environment. Then copy the instance address in the “At address” field to deploy the contract at that address.



![](https://metana.io/wp-content/uploads/2024/06/Screenshot-2024-06-17-at-9.59.32 PM-1024x561.jpg)
4. Check the player function to see if it’s match your address and check the balance as well.



![](https://metana.io/wp-content/uploads/2024/06/Screenshot-2024-06-17-at-10.03.44 PM-1-1024x637.jpg)
5. **Approve Your Own Address:** Here comes the clever part. Use the approve function to grant your own address permission to transfer **your entire token balance**. In essence, you’re approving yourself to move your own tokens.



![](https://metana.io/wp-content/uploads/2024/06/Screenshot-2024-06-17-at-10.05.29 PM.jpg)
6. **Transfer Using** **transferFrom****:** Now, here’s the twist. Instead of using the transfer function (which is locked), leverage the transferFrom function. This function allows an approved spender (which is your address in this case) to transfer tokens **on behalf of the owner** (also your address).


Go to [etherscan](https://sepolia.etherscan.io/) find a random address and enter it in the “To” address in the transferFrom function. Then transfer the tokens to that address.



![](https://metana.io/wp-content/uploads/2024/06/Screenshot-2024-06-17-at-10.08.35 PM.jpg)
7. Check the your balance it should be reduced to 0



![](https://metana.io/wp-content/uploads/2024/06/Screenshot-2024-06-17-at-10.09.08 PM.png)
8. Finally submit the instance. Congratulations you passed this level



![](https://metana.io/wp-content/uploads/2024/06/Screenshot-2024-06-17-at-10.10.22 PM.jpg)
 By cleverly using transferFrom with your own address as both the spender and the owner, you can bypass the timelock and transfer your entire token balance out of the contract, effectively “draining” it.


Conclusion:
-----------


By exploiting the mismatch between the locked transfer function and the unrestricted approve function, you’ve successfully bypassed the timelock and transferred your tokens in the **Ethernaut Level 15 challenge**. **This walkthrough of the Ethernaut challenge highlights the importance of careful contract design and security audits within the DeFi space**. Approaching unfamiliar tokens, especially those with custom logic or odd functionalities, requires extra caution.



![faq](https://metana.io/wp-content/uploads/2024/05/Questions-bro-1.svg)
FAQs:
-----


**Is this a vulnerability in all ERC20 tokens?**


* No, not necessarily. This exploit relies on a specific design flaw in the Naught Coin contract. Well-written ERC20 contracts should have proper access control mechanisms to prevent such abuses.


**What are the takeaways from this challenge?**


* This challenge emphasizes the importance of understanding ERC20 token standards and potential vulnerabilities associated with approvals. It also highlights the need for thorough contract audits before deployment in DeFi.


**Can I get my tokens back after draining them?**


* Unfortunately, no. Once you transfer your tokens out, they’re gone from the Naught Coin contract. This is why it’s crucial to only use such exploits in educational settings and never on real contracts with your funds.


**Are there other ways to solve this challenge?**


* While the approve and transferFrom approach is a common solution, there might be alternative ways to exploit the contract’s logic depending on its specific implementation.


**What’s next on my Ethernaut journey?**


* Ethernaut offers a variety of challenges with increasing difficulty. Keep exploring to learn more about smart contract vulnerabilities and how to write secure code for the blockchain!







![](https://metana.io/wp-content/uploads/2024/06/Ethernaut-Level-15-Walkthrough-Naught-Coin.jpg) 





[PrevPreviousImproper Input Validation in Smart Contracts](https://metana.io/blog/improper-input-validation-in-smart-contracts/) 




[NextExcessive Function Restriction in Smart ContractsNext](https://metana.io/blog/excessive-function-restriction-in-smart-contracts/) 







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






