



Understanding Solidity Global Variables: Types and Uses - Metana




















































































 












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





 







Understanding Solidity Global Variables: Types and Uses
=======================================================

 



 * [Ali Kanso](https://metana.io/blog/author/aii-kanso/)
* [November 7, 2023](https://metana.io/blog/2023/11/07/)
* [Smart Contracts](https://metana.io/blog/category/smart-contracts/)














Solidity is a popular programming language for writing smart contracts on the Ethereum blockchain. In **Solidity, global variables** play a crucial role in the functioning of smart contracts. These variables provide important information about the state and context of the blockchain, making it possible to create complex, decentralized applications. In this article, we will explore Solidity global variables, their different types, and their various uses.


What are Solidity Global Variables?
-----------------------------------


Global variables in Solidity are predefined variables that hold information about the current state of the Ethereum blockchain and the execution context of a [smart contract](https://metana.io/blog/what-is-a-smart-contract-understand-contracts-on-the-blockchain/). These variables are accessible from any part of a contract and are often used to access blockchain-specific data or manipulate the contract’s state. Understanding the types and uses of these global variables is essential for [writing efficient and secure smart contracts.](https://metana.io/blog/solidity-smart-contracts/)


The main variables we will be covering are: **`block`**, **`msg`**, and **`tx`**.


![solidity global variablessolidity variables](https://metana.io/wp-content/uploads/2023/11/pexels-markus-spiske-4439901-1024x683.jpg)
Block
-----


The **`block`** is where the *block*—chain got its name. The blockchain works by creating new blocks and chaining them together linearly. Anytime a new block is created, it carries a set of transactions with it, those being invocations to smart contract functions. Those same functions can have access to their current carrier block, which grants them access to its information.


A block’s information includes details about its number in the blockchain, its mining difficulty, and a bunch of other stuff. The main attribute that we need to focus on however, is the **`block timestamp`.**


The timestamp of a block indicates when this block has been mined. This is very important because it allows us to keep records of when a transaction has occurred. We can use those records to restrict interaction with a contract for a certain amount of time, or reward certain users based on timely dependent interactions with the contract.




```
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

contract GlobalVariables {
    uint256 constant MIN_TIME_BETWEEN_INTERACTIONS = 15 minutes;
    uint256 lastInteraction;

    function doSomeStuff() external {
        require(
            block.timestamp - lastInteraction > MIN_TIME_BETWEEN_INTERACTIONS,
            "Not enough time has passed since last interaction"
        );
        lastInteraction = block.timestamp;
        // do some stuff
    }
}

```


*Hint: The `block.timesamp` is represented in seconds according to the UNIX timestamp. Solidity offers a set of numeric types such as minutes, hours, days… which are also represented in seconds (eg. 2 hours = 2 \* 60 minutes \* 60 seconds = 7200 seconds). These types are built into Solidity to ease time based comparisons such as the one in the example.*


Msg
---


Similar to how a **`block`** carries information about its attributes in the blockchain, a **`msg`** carries information about a contract function call.


A **`msg`** also has a few attributes, the most common of which are the `**sender**` and **`value`**.


The sender of a msg, as the name suggest, is the person or contract calling the function. The value on the other hand, contrary to what its name suggests, is not about the inputs being given to the function. The value is actually the amount of WEi sent to the contract, which is a currency in the Ethereum ecosystem that can be [converted to Ether.](https://eth-converter.com/)


We can use the msg sender to keep track of certain users or contracts and their interactions with ours. And we can use the msg value to handle payments in our contract.




```
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

contract GlobalVariables {
    uint256 constant MIN_DONATION = 0.01 ether;
    uint256 constant MAX_DONATION = 100 ether;
    mapping(address => uint256) public donations;

    function donate() external payable {
        require(
            msg.value >= MIN_DONATION,
            "Donation must be at least 0.01 ether"
        );
        require(msg.value <= MAX_DONATION, "Donation can be at most 100 ether");
        donations[msg.sender] += msg.value;

        // do some stuff
    }
}
```


*Hint: Similar to time based units, Solidity offers currency based units to ease currency based computations.*


Tx
--


The word **`tx`** is a shorthand for the word transaction. You might be wondering what is the difference between a **`msg`** and a **`tx`** then. While the **`msg`** carries data about the function call, the **`tx`** carries data about the entire transaction chain. The only properties exposed by **`tx`** are **`gasprice`** and **`origin`**.


To give an example: if a user calls contract A, which in turn calls contract B, the msg sender in contract B would be contract A, while the tx origin would be the user themselves.


The **`tx`** is rarely a variable that you would use, and it’s generally a good practice to avoid it.




```
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

contract GlobalVariables {
    mapping(address => uint256) public donations;

    //* good
    function donate() external payable {
        donations[msg.sender] += msg.value;

        // do some stuff
    }

    //! bad
    function donateFromOrigin() external payable {
        donations[tx.origin] += msg.value;

        // do some stuff
    }
}

```


For a deeper understanding of how these global variables are effectively utilized within Solidity’s control structures, explore our comprehensive guide on [control structures](https://metana.io/blog/solidity-control-structures/) in Solidity.


All global variables
--------------------


For a full list of Solidity global variables, you can reference the table below:




| Name | Returns |
| --- | --- |
| blockhash(uint blockNumber) | Hash of the given block – only works for 256 most recent, excluding current, blocks |
| block.coinbase | Current block miner’s address |
| block.difficulty | Current block difficulty |
| block.gaslimit | Current block gas limit |
| block.number | Current block number |
| block.timestamp | Current block timestamp as seconds since UNIX epoch |
| gasleft() | Remaining gas |
| msg.data | Complete calldata |
| msg.sender | Sender of the message (current caller) |
| msg.sig | First four bytes of the calldata (function identifier) |
| msg.value | Number of wei sent with the message |
| now | Current block timestamp |
| tx.gasprice | Gas price of the transaction |
| tx.origin | Sender of the transaction |



Full list of global variables


You can also find a more in depth explanation for every variable and its usage in the official [Solidity documentation](https://docs.soliditylang.org/en/v0.8.17/units-and-global-variables.html).


Don’t miss out our previous articles on [Solidity Variables](https://metana.io/blog/solidity-variables-types-and-uses/) and [Solidity Functions](https://metana.io/blog/solidity-functions-types-and-use-cases/)!




![Frequently Asked Questions](https://metana.io/wp-content/uploads/2023/10/FAQs-cuate-1024x1024.png)
1. What is a global variable in Solidity?


* Global variables are special variables available in Solidity that provide information about the blockchain or the transaction itself. They can be used to retrieve data about the current block, transaction, or contract execution.


2. Can I get the miner’s address of the current block?


* Yes, you can access the miner’s address of the current block using `block.coinbase`.


3. How can I access the current block difficulty?


* The current block difficulty can be accessed via `block.difficulty`.


4. How to get the remaining gas in Solidity?


* You can get the remaining gas using the `gasleft()` function.


5. What does `msg.sender` indicate in Solidity?


* `msg.sender` is a global variable that denotes the address of the caller of the current function.


6. How can we check the number of wei sent with a message?


* The number of wei sent with the current message can be verified via `msg.value.`


7. Can I get the timestamp of the current block?


* Yes, the timestamp of the current block can be obtained using `block.timestamp` or `now`.


8. What is the purpose of `msg.data` in Solidity?


* `msg.data` contains the complete calldata, which is the data passed in the call to the function in the contract.


9. What is `tx.origin` in Solidity?


* `tx.origin` refers to the original entity that initiated the transaction. It could be different from `msg.sender` in case contracts are calling each other.


10. How to get the gas price of the transaction?


* The gas price of the transaction can be retrieved using `tx.gasprice`.






![Understanding Solidity Global Variables: Types and Uses](https://metana.io/wp-content/uploads/2023/11/2737.jpg) 





[PrevPreviousUnderstanding Solidity Functions: Types and Use Cases](https://metana.io/blog/solidity-functions-types-and-use-cases/) 




[NextUnderstanding Solidity Methods: How They Differ from FunctionsNext](https://metana.io/blog/solidity-methods-solidity-functions/) 







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




16 mins ago

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






