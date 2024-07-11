



Ethernaut Level 7 Walkthrough: Force - Metana


















































































 












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





 







Ethernaut Level 7 Walkthrough: Force
====================================

 



 * [Jarrod Pyne](https://metana.io/blog/author/jarrod-pyne/)
* [May 8, 2024](https://metana.io/blog/2024/05/08/)
* [Ethernaut Walkthrough](https://metana.io/blog/category/ethernaut-walkthrough/)














Being relatively new to the Web3 space and having a keen interest in Security has naturally led to me participating the Ethernaut Challenge hosted by OpenZeppelin. For those unfamiliar with these challenges, each challenge revolves around exploiting common attack vectors seen in the Web3 space, with a particular focus on Solidity-based smart contracts. 


Since commencing these challenges, my understanding of smart contract vulnerabilities has increased exponentially. However, I am also conscious that these challenges are technically challenging and for those like me without a typical background in software engineering, further explanation of exploits are warranted. Without further ado, here is an explanation of the **Ethernaut level 7 titled ‘Force’.**


The Code
--------


OpenZeppelin has provided the following smart contract to be exploited:



```
// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

contract Force {/*

                   MEOW ?

         /\_/\   /

    ____/ o o \

  /~____  =ø= /

 (______)__m_m)

*/}
```

The Challenge Description
-------------------------


Accompanying the code above, the following description is also provided:  



*Some contracts will simply not take your money ¯\\_(*ツ*)\_/¯*


*The goal of this level is to make the balance of the contract greater than zero.*


*Things that might help:*


* *Fallback methods*
* *Sometimes the best way to attack a contract is with another contract.*


To simplify the above even further, the objective is to make this empty contract accept Ether, despite it having no functions. 


Where to start?
---------------


Let’s breakdown the contract itself first before we move onto OpenZeppelin’s hints. The Solidity version being used is ^0.8.0 and the contract is named Force. That’s it. Importantly, there are no functions contained in this contract. 


Okay now what? 


First, let’s breakdown OpenZeppelin’s hints at a Fallback method. 


Taken directly from [Solidity by Example](https://solidity-by-example.org/fallback/), `fallback` is a special function that is executed either when:


1. a function that does not exist is called; or
2. Ether is sent directly to a contract but `receive()` does not exist or `msg.data` is not empty.


At a very basic level, what does this mean for us? 


Let’s think back to our objective, we need to force this contract to take Ether. Are we going to be able to do that by calling a function that doesn’t exist in the Force contract, from a new contract we draft? No, this does not make logical sense. 


Turning to the second question, does a `receive()` function exist in the Force contract? No, which satisfies the second part of the second question. Now we must turn to whether we can we sent Ether directly to this contract considering this. 


Sending Ether to a contract without a `receive` function
--------------------------------------------------------


  
Whilst looking at the Solidity documentation, there are consistent warnings throughout about the utilisation of a ‘selfdestruct(address)’ function. The practical implication of this function is that it will destroy the contract that contains this function and send its balance to a contract specified in the address argument. 


This is very easy to do, and results in us creating a contract that looks like this:



```
// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

contract Boom {

    constructor (address payable target) payable {

        selfdestruct(target);

    }

}
```

Remix guide
-----------


 If you have the address of your Ethernaut challenge instance, be sure to copy this address into the address bar in remix, outlined here (please note this is for illustrative purposes only and your environment should be an Injected Provider):


![ethernaut level 7force walkthroughethernaut challenge](https://metana.io/wp-content/uploads/2024/05/image.png)
After retrieving the address of the Force contract, it should be entered into the Boom contract’s deploy address found here: 


![](https://metana.io/wp-content/uploads/2024/05/image-1.png)
Also note when deploying the Boom contract that the value parameter is greater than 0. This will ensure that the Force contract will have an Ether balance greater than 0, thus completing the challenge.


Concluding remarks
------------------


I hope the above has been helpful in outlining each step required when undertaking the Force Ethernaut challenge. By reading this guide you should be able to understand:


1. how a `fallback` function operates;
2. the implications of using a `selfdestruct` function in Solidity; and
3. how to practically deploy a contract using Remix.


*Ready for the next Ethernaut challenge? Click to check out the [previous ethernaut challenge](https://metana.io/blog/ethernaut-level-6-walkthrough-delegation/) and see what’s next in our series!*



![faq](https://metana.io/wp-content/uploads/2024/01/Questions-cuate-1024x1024.png)
FAQs
----


**What is Ethernaut Level 7: Force challenge about?**


* The challenge involves figuring out how to force Ether into a contract that doesn’t have a payable fallback function.


**How do you force ETH into a smart contract in Ethereum?**


* Use techniques like self-destruct from another contract that sends its balance, even if the recipient contract lacks payable functions. Please note, this involves extreme risk and users should proceed with caution when using self-destruct.


**What skills are essential to solve the Ethernaut challenges?**


* Understanding of Solidity, familiarity with Ethereum smart contract mechanics and, problem-solving skills in a blockchain context.


**Are there specific tools recommended for Ethernaut challenges?**


* Tools like Remix IDE for Solidity, MetaMask for interacting with Ethereum, and Etherscan for blockchain insights are recommended.


**Can I participate in Ethernaut challenges without any ETH?**


* Yes, you can use test networks like Sepolia or Holesky where test ETH is freely available and sufficient for learning and challenges.






![](https://metana.io/wp-content/uploads/2024/05/Ethernaut-Level-7-Walkthrough-Force-1.jpg) 





[PrevPreviousJavaScript Error Handling and Debugging Techniques](https://metana.io/blog/javascript-error-handling-and-debugging-techniques/) 




[NextAsynchronous JavaScript: Callbacks, Promises, and Async/AwaitNext](https://metana.io/blog/asynchronous-javascript-callbacks-promises-and-async-await/) 







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






