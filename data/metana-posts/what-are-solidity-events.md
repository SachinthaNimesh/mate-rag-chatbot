



What are Events in Solidity?
















































































 












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





 







What are Events in Solidity?
============================

 



 * [Metana Editorial](https://metana.io/blog/author/editorial/)
* [July 12, 2023](https://metana.io/blog/2023/07/12/)
* [Blockchain](https://metana.io/blog/category/blockchain/), [Smart Contracts](https://metana.io/blog/category/smart-contracts/)














**What are Solidity Events?**
-----------------------------


**Solidity events** are a way for **smart contracts** to communicate with each other and with external applications. They allow developers to track all significant actions and transactions in a contract, providing crucial information about the state and interaction of the contract. They can also be used to promote transparency and accountability in the blockchain ecosystem.


**The Beauty of Solidity Events**
---------------------------------


One of the most beautiful things about Solidity events is that they promote transparency and accountability in the blockchain ecosystem. Developers can emit events and declare events that anyone can access. This means that anyone can see what is happening in a contract, which helps to build trust with users.


**What is Solidity `emit`?**
----------------------------


In Solidity, `emit` is a keyword used to trigger events. These events are inheritable members of contracts. When you use `emit`, followed by the event name and its parameters, it logs the event to the blockchain. This means that the event is stored on the blockchain and can be accessed and listened to externally.


Here’s an example of how **Solidity emit** might be used in a smart contract:



```
pragma solidity ^0.8.0;

contract MyContract {
    event MyEvent(address indexed sender, uint256 value);

    function myFunction(uint256 _value) public {
        // Some logic
        emit MyEvent(msg.sender, _value);
    }
}

```


In this example, `MyEvent` is emitted every time `myFunction` is called, logging the sender’s address and the value passed to the function. External applications can listen to `MyEvent` to track these calls.


**What does Declaring or Emitting an event mean?**
--------------------------------------------------




| Declaring an event | Emitting an event |
| --- | --- |
| To declare an event, you use the event keyword, followed by the event name and input parameters. For example, the following code declares an event called Deposit: | To emit an event, you use the emit keyword, followed by the name of the event and the values of the input parameters. For example, the following code emits the Deposit event: |
| #Code snippet`event Deposit(address indexed _from, bytes32 indexed _id, uint _value);` | #Code snippet`emit Deposit(msg.sender, _id, msg.value);` |
| The indexed keyword tells Solidity to store the value of the parameter in the event log. The address type is used to represent an Ethereum address. The bytes32 type is used to represent a 32-byte value. The uint type is used to represent an unsigned integer. | The msg. sender variable refers to the address of the sender of the transaction that emitted the event. The \_id and \_value variables are the values of the input parameters to the Deposit event. |


**What are the various Solidity Event Types?**
----------------------------------------------


[Smart contracts can communicate](https://metana.io/blog/smart-contract-abi/) with one another and with external apps using solidity events. They give vital information about the status and interaction of the contract and enable developers to keep track of all major activities and transactions in a contract.


Solidity events come in two varieties: indexed events and non-indexed events.


* Indexed events are events that are indexed have parameter values that are stored in a form that makes them indexable. This implies that it is simple to run a query over the event log to retrieve all events of a specific category.
* Non-indexed events are events that are not easily indexable due to the manner the parameter values are stored are known as non-indexed events. This implies that it is difficult to search the event log for all events of a specific category.


Indexed events are generally used by developers since they make it simple to follow the occurrence of particular events. An indexed event, for instance, might be used to monitor the exchange of tokens between two accounts.


**Here is an example of an indexed event:**



* **Code snippet**



```
event Transfer(
    address indexed _from,
    address indexed _to,
    uint256 _value
);
```



In this example, the Transfer event has three input parameters:  `_from` , `_to`, and `_value`. The `indexed` keyword tells Solidity to store the value of the `_from` and `_to` parameters in a way that can be easily indexed. This means that you can easily query the event log to find all events of the Transfer type where the `_from` and `_to` parameters are equal to specific values.


![what are solidity events, smart contractssolidity emit](https://metana.io/wp-content/uploads/2023/08/nenad-novakovic-L2QB-rG5NM0-unsplash-1024x576.jpg)
**What are the differences between Functions and Events in Solidity?**
----------------------------------------------------------------------


Functions and events are two of the most important concepts in Solidity, the programming language used to create smart contracts. While they are both used to define the behavior of a [smart contract](https://metana.io/blog/what-is-a-smart-contract-understand-contracts-on-the-blockchain/), they serve different purposes.




| Functions | Events |
| --- | --- |
| Functions define the behavior of a smart contract. They are used to perform actions such as transferring tokens, creating new accounts, and storing data. Functions can be called by other contracts or by external applications. | Events serve as signals that indicate to external interfaces and dApps when a particular action has occurred within the contract. Events are emitted by functions, and they contain information about the action that was performed. Events can be listened to by other contracts or by external applications. |


**Here is an example to illustrate the difference between functions and events**:





```
contract Example {

    event Transfer(address indexed _from, address indexed _to, uint256 _value);

    function transfer(address to, uint256 value) public {
        // This is a function. It modifies the state of the contract by transferring tokens.
        emit Transfer(msg.sender, to, value);
    }
}
```




*In this example, the `transfer` function transfers tokens from the current address to the specified address. It also emits the `Transfer` event, which logs the transfer.*


*The main difference between functions and events is that functions modify the state of the contract, while events only log information about what has happened. Functions can also return a value, while events cannot.*


*In this example, the `transfer` function modifies the state of the contract by transferring tokens. The `Transfer` event simply logs the transfer, it does not modify the state of the contract.*



Here is a table summarizing the key differences between functions and events in Solidity:




| Feature | Function | Event |
| --- | --- | --- |
| Modifies state | Yes | No |
| Returns value | Can | Cannot |
| Logs information | No | Yes |



Differences between functions and events in Solidity


**What are applications of Solidity Events?**
---------------------------------------------


Solidity events are a versatile tool that can be used in a variety of ways in smart contract development. Depending on the project’s needs, events can be used to track state changes, trigger notifications, log data, and more. 


**Here are a few examples:**


* **Audit Trails:** Solidity events enable developers to create public audit trails of all contract interactions, making it possible to track the contract’s state and transactions.


* **Notification Systems:** Solidity events can trigger notifications to external interfaces or dApps, such as email or SMS alerts, letting them know when a certain activity has taken place within a contract.


* **Token Transfers:** Solidity developers often use events to track token transfers within contracts, a critical function for tracking ownership and flow.


* **Automated Testing:** Testing is an essential part of smart contract development. With events, developers can set up automated testing frameworks to verify their contracts’ correctness and maintainability.


**Why Should You Use Solidity Events In A Smart Contract?**
-----------------------------------------------------------


**Solidity events have many functional advantages over other means of contract communication:**


* **Transparency:** they promote transparency by publicly logging all contract interactions and transactions, which are easy to access and audit.


* **Efficiency:** they are lightweight ways of communicating between smart contracts and external interfaces or dApps. They reduce the number of unnecessary blockchain interactions required, which in turn increases efficiency.


* **Flexibility:** they allow developers to exchange data flexibly between smart contracts and external interfaces or dApps. They can include multiple input parameters and can occur at any point in contract execution.


To sum up, Solidity events are a flexible and effective mechanism that can be utilized to increase the effectiveness, accountability, and transparency of blockchain systems. There are numerous internet resources accessible if you’re interested in learning more about Solidity events. After gaining a foundational understanding, you can begin creating your own dApps and advancing the blockchain ecosystem.




![](https://metana.io/wp-content/uploads/2023/11/FAQs-cuate-1-1024x1024.png)

1. **What are Solidity events in ethers?**



> Solidity events in ethers are events that are emitted by smart contracts on the Ethereum blockchain. They can be used to track the state of the contract, such as when a token is transferred or a new account is created.


2. **What are events in Ethereum?**



> Events in Ethereum are similar to events in Solidity. They are emitted by smart contracts and can be used to track the state of the contract. However, events in Ethereum are also stored on the blockchain, which makes them accessible to anyone.


3. **What is the difference between function and event in Solidity?**



> The main difference between functions and events in Solidity is that functions modify the state of the contract, while events only log information about what has happened. Functions can also return a value, while events cannot.


4. **What are the parameters of Solidity event?**



> The parameters of a Solidity event are the values that are logged when the event is emitted. The parameters can be of any data type, including integers, floats, strings, and addresses.


5. **What is the size limit of Solidity event?**



> The size limit of a Solidity event is 320 bytes. This includes the name of the event, the parameters, and the data types of the parameters.


6. **What are data types in Solidity?**



> Data types in Solidity are used to define the type of data that can be stored in a variable. The main data types in Solidity are: 
> 
> 
> * Integers
> * Floats
> * Strings
> * Booleans
> * Addresses
> * Arrays
> * Structs
> * Mappings


7. **What are the 4 main data types?**



> The 4 main data types in Solidity are: 
> 
> 
> * Integers: Integers are numbers without decimals.
> * Floats: Floats are numbers with decimals.
> * Strings: Strings are sequences of characters.
> * Booleans: Booleans are values that can be either true or false.


8. **What are the 7 different data types?**



> The 7 different data types in Solidy are: 
> 
> 
> * Integers (int, uint)
> * Floats (float, double)
> * Strings (string)
> * Booleans (bool)
> * Addresses (address)
> * Arrays (array)
> * Structs (struct)
> * Mappings (mapping)


9. **What are the 3 main types of data?**



> The 3 main types of data are: 
> 
> 
> * Primitive data types: Primitive data types are the basic building blocks of data. They are integers, floats, strings, and booleans.
> * Structured data types: Structured data types are made up of primitive data types. They are arrays, structs, and mappings.
> * Reference data types: Reference data types are pointers to other data types. They are contracts and functions.


10. **What are the 5 main data types in databases?**



> The 5 main data types in databases are: 
> 
> 
> * Text: Text is a string of characters.
> * Numeric: Numeric is a number.
> * Boolean: Boolean is a value that can be either true or false.
> * Date: Date is a date and time.
> * Time: Time is a time.






![](https://metana.io/wp-content/uploads/2023/07/What-are-Events-in-Solidity.png) 





[PrevPreviousTestnet Ethereum: A Guide to Rinkeby, Goerli, and Sepolia](https://metana.io/blog/testnet-ethereum-a-guide-to-rinkeby-goerli-and-sepolia/) 




[NextSolidity: The Programming Language of Decentralized ApplicationsNext](https://metana.io/blog/solidity-the-programming-language-of-decentralized-applications/) 







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






