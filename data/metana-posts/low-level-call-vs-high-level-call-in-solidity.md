



Low Level Call vs High Level Call in Solidity - Metana



















































































 












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





 







Low Level Call vs High Level Call in Solidity [Simplified]
==========================================================

 



 * [Metana Editorial](https://metana.io/blog/author/editorial/)
* [May 17, 2024](https://metana.io/blog/2024/05/17/)
* [Blockchain](https://metana.io/blog/category/blockchain/), [Solidity](https://metana.io/blog/category/solidity/)














In Solidity, contracts can interact with other contracts in two main ways: through **high level calls** using the contract’s interface or **low level calls** using methods like `call`, `delegatecall`, and `staticcall`. Though both approaches use the CALL opcode at the Ethereum Virtual Machine (EVM) level, their handling and behavior in Solidity differ significantly.


Understanding High Level and Low Level Calls
--------------------------------------------


### High Level Calls:


High-level calls in Solidity are made using the contract’s interface. This method is user-friendly and includes automatic error handling. For example:



```
contractInstance.someFunction();

```

When this call is made, Solidity generates the appropriate bytecode to handle success and failure cases, ensuring that any errors in the called function result in a revert of the transaction.


### Low Level Calls:


Low-level calls provide more control but require explicit handling of errors. They are made using methods like `call`:



```
(bool success, bytes memory data) = targetAddress.call(abi.encodeWithSignature("someFunction()"));

```

This method returns a boolean indicating the success of the call and any returned data, but it does not automatically revert on failure.



![low level call vs high level call](https://metana.io/wp-content/uploads/2024/05/Pair-programming-rafiki.svg)
Detailed Comparison
-------------------


**Behavior on Failure**: When a high-level call fails, Solidity automatically reverts the transaction, bubbling up the error. This behavior simplifies error handling for developers:



```
contractInstance.someFunction(); // This will revert if someFunction fails

```

In contrast, a low-level call requires manual checking of the success value:



```
(bool success, ) = targetAddress.call(abi.encodeWithSignature("someFunction()"));<br>require(success, "Call failed");
```

If the low-level call fails, the `success` value will be `false`, and the transaction will continue unless explicitly handled.


**Calling Non-Existent Contracts**: High-level calls check if the target address contains a contract before executing the call. If the address does not contain code (checked via the `EXTCODESIZE` opcode), the call will revert:



```
interface IContract {
    function someFunction() external;
}

IContract(targetAddress).someFunction(); // Reverts if targetAddress has no contract

```

Low-level calls, however, do not perform this check and will return `false` if the address has no contract:



```
(bool success, ) = targetAddress.call(abi.encodeWithSignature("someFunction()"));
require(success, "Call to non-existent contract failed");

```

Practical Example
-----------------


Here’s a practical comparison of high-level and low-level calls within a Solidity contract:


**High-Level Call Example**:



```
pragma solidity ^0.8.0;

contract HighLevelCaller {
    function callFunction(address _target) public {
        ITarget(_target).targetFunction(); // Reverts if targetFunction fails
    }
}

interface ITarget {
    function targetFunction() external;
}

```

**Low-Level Call Example**:



```
pragma solidity ^0.8.0;

contract LowLevelCaller {
    function callFunction(address _target) public {
        (bool success, ) = _target.call(abi.encodeWithSignature("targetFunction()"));
        require(success, "Low-level call failed");
    }
}

```

### Key Takeaways


1. **Ease of Use vs. Control**: High-level calls offer ease of use and built-in safety, making them ideal for standard interactions. Low-level calls provide greater control and flexibility, useful for advanced scenarios requiring manual handling of call results.
2. **Error Handling**: High-level calls automatically revert on failure, simplifying error management. Low-level calls require explicit success checks and error handling.
3. **Contract Existence Check**: High-level calls check for the existence of the contract at the target address, reverting if none is found. Low-level calls do not perform this check, requiring manual verification if necessary.


By understanding the differences between high-level and low-level calls, Solidity developers can choose the appropriate method for their specific use cases, balancing ease of use with the need for control and flexibility.



![faq](https://metana.io/wp-content/uploads/2024/05/Questions-bro-1.svg)
FAQs
----


**What is a low level call in Solidity?**


* A low level call in Solidity refers to using functions like `call`, `delegatecall`, `staticcall`, or `callcode` to interact with other contracts. These are more flexible but riskier.


**What is a high level call in Solidity?**


* A high level call uses Solidity’s function calls to interact with other contracts, which are safer and easier to use than low-level calls.


**When should I use low-level calls in Solidity?**


* Low-level calls should be used when you need more control over the call process or when interacting with contracts that don’t expose an ABI.


**What are the risks of using low-level calls in Solidity?**


* Low-level calls can fail silently, making them vulnerable to security issues such as reentrancy attacks if not handled correctly.


**How can I make low-level calls safer in Solidity?**


* To make low-level calls safer, always check the return value, use appropriate security patterns, and consider using high-level calls when possible.


**Why are high-level calls preferred in Solidity development?**


* High-level calls are preferred because they are simpler to use, provide better error handling, and integrate seamlessly with Solidity’s type system.


**What are common use cases for high-level calls in Solidity?**


* High-level calls are commonly used for standard contract interactions, such as transferring tokens or interacting with DeFi protocols.


**Can I combine high-level and low-level calls in a Solidity contract?**


* Yes, combining both types of calls can be useful. High-level calls offer simplicity, while low-level calls provide flexibility when needed.


**What are some best practices for using calls in Solidity?**


* Best practices include favoring high-level calls, handling all call returns, implementing checks-effects-interactions patterns, and avoiding unnecessary complexity.


**How do high-level calls handle errors in Solidity?**


* High-level calls automatically revert on failure, providing built-in error handling which simplifies debugging and improves contract reliability.






![](https://metana.io/wp-content/uploads/2024/05/Low-Level-Call-vs-High-Level-Call-in-Solidity.jpg) 





[PrevPreviousMetana Grads Share Their Journey to Success in Web3](https://metana.io/blog/metana-grads-share-their-journey-to-success-in-web3/) 




[NextEthernaut Level 8 Walkthrough: VaultNext](https://metana.io/blog/ethernaut-level-8-walkthrough-vault/) 







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






