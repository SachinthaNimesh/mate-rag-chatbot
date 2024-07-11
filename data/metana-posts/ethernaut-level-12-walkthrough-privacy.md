



Ethernaut Level 12 Walkthrough: Privacy - Metana





















































































 












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





 







Ethernaut Level 12 Walkthrough: Privacy
=======================================

 



 * [Alexis Amoi](https://metana.io/blog/author/alexis-amoi/)
* [June 12, 2024](https://metana.io/blog/2024/06/12/)
* [Ethernaut Walkthrough](https://metana.io/blog/category/ethernaut-walkthrough/)














**Ethernaut Level 12** titled “**Privacy**” challenges the concept of “private” data on the blockchain. In this level, you’ll encounter a locked contract, and your objective is to unlock it. The key, however, isn’t so private after all! It lies in the way the [Ethereum Virtual Machine](https://metana.io/blog/ethereum-virtual-machine-evm/) (EVM) stores data. **This walkthrough will guide you through the process.**


Understanding Storage Slots
---------------------------


Imagine a shoebox with compartments. The EVM stores variables similarly, allocating 32 bytes (256 bits) to each compartment called a storage slot. The EVM is space-efficient; smaller variables like booleans (1 byte) or uint8s (1 byte) can share a slot with other variables as long as the total size doesn’t exceed 32 bytes. This level serves as a valuable lesson in understanding how the EVM stores data.


Analyze the Contract
--------------------


First, take a look at the `Privacy.sol` contract. You’ll notice a variable named `data` declared as a `bytes32` array. There’s also a function called `unlock` that takes a `bytes16` argument as input.



![Ethernaut Privacy level console walkthrough with tips and contract code](https://metana.io/wp-content/uploads/2024/06/Screenshot-2024-06-07-at-1.27.27 PM-1-1024x552.png)
EVM Storage Shenanigans
-----------------------


The EVM packs variables efficiently to save storage space. Smaller variables like `locked` (bool) and `denomination` (uint8) share the same storage slot as the first element of the `data` array (`data[0]`).



![](https://metana.io/wp-content/uploads/2024/06/Screenshot-2024-06-12-at-11.09.41 AM-1024x509.png)
Unlocking the Secret
--------------------


To unlock the contract, we need the value stored in `data[2]`. That value is located at slot 5. However, the EVM stores it as `bytes32`. We need to cast it to `bytes16` to match the `unlock` function’s input.


Here’s a step-by-step guide to unlocking the contract:


1. **Use the terminal in the console:**
2. Get the Hex string of the `data[2]` at slot 5: `await web3.eth.getStorageAt(contract.address, 5)`. This will give us a string of `bytes32`. We want to convert it to `bytes16`.
3. Put that hex string in a constant: `const b32 = '0x5d6655fba48ea25651c1cad326e3a62ded205cb4464b71e0cf64951ecfe605d2'`.
4. Find the length: `b32.length` (This will return 66).
5. Convert it to `bytes16` (half the length, excluding `0x`): `const b16 = b32.slice(0, 34)`.
6. Use that value to call the `unlock` function: `contract.unlock('0x5d6655fba48ea25651c1cad326e3a62d')`.



![Ethernaut Level 12 Privacy contract unlock steps with MetaMask confirmation](https://metana.io/wp-content/uploads/2024/06/Screenshot-2024-06-07-at-1.53.42 PM-1024x645.png)
7. Check the status of the `locked` boolean to see if it changed to `false`: `await contract.locked()`.
8. Finally, you can submit the instance. Congrats on completing this level!



![Ethernaut challenge 12 Privacy walkthrough showing successful contract unlock steps and completion message](https://metana.io/wp-content/uploads/2024/06/Screenshot-2024-06-07-at-1.56.12 PM.png)
Conclusion: Ethernaut level 12 (Privacy)
----------------------------------------


This challenge highlights that nothing on the blockchain is truly private, not even data declared with the `private` keyword. The [EVM’s storage](https://metana.io/blog/modifying-evm-storage-to-seed-token-balances-in-testing/) layout can reveal information you might think is hidden. So, when building [smart contracts](https://metana.io/blog/what-is-a-smart-contract-understand-contracts-on-the-blockchain/), be mindful of how data is stored and accessed. Rely on encryption or other secure mechanisms for truly sensitive information.


**Bonus Tip:** Security best practices involve keeping user data off-chain whenever possible. Consider using decentralized storage solutions for sensitive information that doesn’t require constant on-chain interaction.



![faq](https://metana.io/wp-content/uploads/2024/05/Questions-bro-1.svg)
FAQs:
-----


1. **Can this exploit be used to steal funds from real contracts?**


No, directly exploiting storage packing like this wouldn’t be effective for stealing funds from real contracts. This technique relies on specific contract vulnerabilities and wouldn’t work universally.


2. **What are some best practices to avoid similar vulnerabilities?**


When writing smart contracts, be mindful of storage slot packing. Avoid storing sensitive data directly on-chain, and consider using encryption or alternative storage solutions for truly private information.


3. **Is there another way to solve this challenge without the Truffle console?**


Yes, it’s possible to solve this challenge using other tools or platforms that allow interaction with deployed contracts and storage slots.


4. **What if I don’t know the storage slot locations beforehand?**


Analyzing the contract code and understanding Solidity variable sizes can help you predict storage slot usage. Alternatively, some tools offer functionalities to explore storage slots on deployed contracts.


5. **What are the limitations of the “private” keyword in Solidity?**


The `private` keyword in Solidity only affects code visibility within the contract itself. It doesn’t guarantee data privacy on the blockchain due to the EVM’s storage layout and potential for analysis.






![](https://metana.io/wp-content/uploads/2024/06/Ethernaut-Level-12-Walkthrough-Privacy_.jpg) 





[PrevPreviousTop Languages for dApp Development: Beginner Guide](https://metana.io/blog/top-languages-for-dapp-development-beginner-guide/) 




[NextJavaScript Array Splice() MethodNext](https://metana.io/blog/javascript-array-splice-method/) 







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






