



Require, Assert, and Revert: Solidity Error Handling Methods - Metana

















































































 












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





 







Require, Assert, and Revert: Solidity Error Handling Methods
============================================================

 



 * [Metana Editorial](https://metana.io/blog/author/editorial/)
* [May 16, 2023](https://metana.io/blog/2023/05/16/)
* [Blockchain](https://metana.io/blog/category/blockchain/)














How Error Handling is Handled in Solidity Code?
-----------------------------------------------


**Solidity,** an object-oriented programming language used for implementing smart contracts on Ethereum and other blockchains, provides several functions to address potential errors during compile time and runtime. While syntax errors can be caught at compile time, runtime errors can be challenging to detect and often occur during contract execution. Examples of runtime errors include divide-by-zero, array-out-of-index, and so forth.


Solidity uses state-reverting exceptions to handle errors, effectively ensuring atomicity. When a smart contract call terminates with an error, all state changes made to variables, balances, and other aspects are reverted, all the way up the chain of contract calls. This error handling mechanism enables developers to interact directly with other contracts by declaring an interface.


It’s essential to note that Ethereum transactions are atomic, meaning they are either fully completed or have no effect on the state and are entirely reversed. Overall, Solidity provides a robust error handling mechanism that enables [smart contract](https://metana.io/blog/solidity-smart-contracts/) developers to write code that is reliable, efficient, and error-free.



![solidity error handling](https://metana.io/wp-content/uploads/2023/08/elisa-ventur-bmJAXAz6ads-unsplash-1024x683.jpg)

The 3 Main Solidity Error Handling Functions
--------------------------------------------


Earlier versions of Solidity utilized a single throw statement for error handling, but this method proved suboptimal for gas efficiency and required additional test functions to check values and throw errors. To address this issue, Solidity version 4.10 introduced three special [functions](https://metana.io/blog/solidity-functions-types-and-use-cases/) – **assert, require, and revert** – as new error handling constructs. With the throw statement made absolute, developers can now more effectively manage errors and optimize gas usage in their code.



### The Require Function in Solidity



The **require** function plays a pivotal role in developing secure and reliable Solidity contracts. By employing the require function effectively, you can validate inputs, enforce conditions, and enhance the overall integrity of your contract’s logic. This article will provide valuable insights on how to utilize the require function in your Solidity contracts to ensure robustness and mitigate potential vulnerabilities


Here’s an example:



```
function transfer(address recipient, uint amount) public {

    require(amount > 0, "Amount must be greater than 0");

    balances[msg.sender] -= amount;

    balances[recipient] += amount;}
```


In this example, the transfer function ensures that the amount being transferred is greater than zero before executing the rest of the function code. If the amount is not greater than zero, the function throws an exception and reverts the transaction.



### The Assert Function in Solidity



The **assert** function is used to check for internal errors in the contract code. It takes a boolean expression as its argument and throws an exception and reverts the transaction if the expression evaluates to false. However, unlike the require function, the assert function should only be used to check for internal errors in the contract code that should never occur. Here’s an example:



```
function withdraw(uint amount) public {

    assert(balances[msg.sender] >= amount);

    balances[msg.sender] -= amount;

    payable(msg.sender).transfer(amount);

}
```


In this example, the withdraw function checks if the user’s balance is greater than or equal to the withdrawal amount. If it’s not, the function throws an exception and reverts the transaction. However, since this should never occur if the contract code is working correctly, the assert function is used instead of the require function.



### The Revert Function in Solidity



The **revert** function is similar to the require function in that it’s used to revert a transaction if a condition is not met. However, the revert function provides more flexibility in error handling and allows you to provide a reason string to explain why the transaction was reverted. Here’s an example:



```
function withdraw(uint amount) public {

    require(balances[msg.sender] >= amount, "Insufficient balance");

    balances[msg.sender] -= amount;

    if (!msg.sender.send(amount)) {

        revert("Failed to send funds");

    }

}
```


In this example, the buyTokens function checks if there are enough tokens available for purchase before executing the rest of the function code. If there are not enough tokens, the function reverts the transaction and provides a reason string to explain why it was reverted.


To solve the EVM execution reverted error check our recent article [here](https://metana.io/blog/evm-execution-reverted-errors/).



Conclusion
----------



To sum up these functions, the require function should be used to validate user input or contract state before executing the rest of the contract code. The assert function should be used to check for internal errors in the contract code that should never occur. The revert function should be used to revert a transaction if a condition is not met and provides more flexibility in error handling. By understanding when to use these functions in your Solidity contracts, you can write safer and more secure [smart contracts](https://metana.io/blog/what-is-a-smart-contract-understand-contracts-on-the-blockchain/) on the Ethereum blockchain



![Frequently asked questions](https://metana.io/wp-content/uploads/2023/11/FAQs-cuate-1-1024x1024.png)
1. **What is the difference between require and assert and revert in Solidity?**


 The main difference is the behavior when the condition fails. require and revert revert the entire transaction and undo all changes, while assert is used for internal errors and will always revert the transaction.


2. **What are the error handling methods in Solidity?**


Solidity provides three error handling methods: require, assert, and revert. These methods are used to validate conditions and handle exceptions in smart contracts.


3. **What is the difference between require and assert in Solidity?**


The difference lies in the behavior when the condition fails. require and assert both check conditions, but require is used for input validation and will revert the transaction, while assert is used for internal errors and will always revert the transaction.


4. **What is the revert function in Solidity?**


revert is a function in Solidity that is used to revert the entire transaction and undo all changes made so far. It is commonly used for error handling and to revert the state back to its original state.


5. **Why use require instead of assert?**


Use require when you want to check for input validation and ensure that certain conditions are met before proceeding with the execution of the contract. If the condition fails, require will revert the transaction and undo all changes, providing a safer way to handle errors.


6. **Why do we use the require method?**


The require method is used to validate conditions in smart contracts. It allows you to check for certain conditions and revert the transaction if the conditions are not met. This helps ensure that the contract functions correctly and prevents unwanted behavior.


7. **Which is better assert or verify?**


In Solidity, assert is used for internal errors that should never occur, while require is used for input validation and to check conditions that should always be true. It is generally recommended to use require for most cases as it provides a safer way to handle errors and prevents unwanted behavior.


8. **When shouldn’t you use the assert statement?**


The assert statement should not be used for input validation or checking conditions that might be false in certain cases. It is meant to be used for internal errors that should never occur. For input validation, it is recommended to use the require statement instead.


9. **Does assert raise an error?**


Yes, when the condition provided to the assert statement evaluates to false, it will raise an error and revert the entire transaction.


10. **What happens if assert fails?**


If an assert statement fails, there has likely been an internal programming issue. All modifications made during the course of the transaction are undone, and the contract’s execution is instantly suspended. This is done to safeguard the integrity of the contract’s state and to stop any additional unexpected activity.


11**. What does require do in Solidity?**


The require keyword is used in Solidity to ensure that certain conditions are met before proceeding with the execution of a function.  
  
If the condition specified in the require statement is true, the function will continue to execute. However, if the condition is false, the function will stop executing and revert any changes made to the state of the contract. Reverting means that any state changes made during the execution of the function (such as changes to variables or storage) will be undone, and the contract will return to its previous state.



12**. What is require vs assert in Solidity?**


Require checks if inputs and conditions are valid, while assert checks if the code itself is behaving as expected, and throws an error if something unexpected or out of place happens.



13. **Why use require instead of assert?**


It’s important to use require when validating user input or external dependencies (such as whether a user’s balance is sufficient), and assert to validate internal conditions that should never fail. By using both of these keywords where appropriate, [Solidity developers](https://metana.io/blog/solidity-developer-salary/) can create more robust and secure contracts that are less prone to error.






![](https://metana.io/wp-content/uploads/2023/05/Require-Assert-and-Revert-Solidity-Error-Handling-Methods.png) 





[PrevPrevious5 Best Web3 Solidity Courses To Get Started On Development](https://metana.io/blog/web3-solidity-courses/) 




[NextSmart Contract ABI: What is it?Next](https://metana.io/blog/smart-contract-abi/) 







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




18 mins ago

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






