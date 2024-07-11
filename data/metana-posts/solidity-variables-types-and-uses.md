



Solidity Variables: Types and Uses - Metana

















































































 












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





 







Solidity Variables: Types and Uses
==================================

 



 * [Ali Kanso](https://metana.io/blog/author/aii-kanso/)
* [October 20, 2023](https://metana.io/blog/2023/10/20/)
* [Blockchain](https://metana.io/blog/category/blockchain/), [Smart Contracts](https://metana.io/blog/category/smart-contracts/)














Solidity is the most popular programming language for developing smart contracts on Ethereum. And just like in any programming language, [**Solidity**](https://metana.io/blog/solidity-the-programming-language-of-decentralized-applications/) **variables** play a crucial role in defining the state and behavior of these smart contracts. They enable developers to store and manipulate data, making it essential to have a comprehensive understanding of the various variable types and their uses in Solidity.


What are Solidity Variables?
----------------------------


In Solidity, a variable is a container for storing data. These variables can represent a wide range of data types, from simple numbers to complex structures. **Solidity variables** are crucial for defining the state of a contract and are used to store values that are manipulated during the contract’s execution.


Solidity supports both value types and reference types, each with its specific use cases and behavior. Let’s delve into these types and explore their uses.


What are the Data Types?
------------------------


In the majority of programming languages, you’ll find two types of data, those that have a value, and those that hold a reference.


Value types are basic data types that store their data directly. They are copied when assigned to another variable or passed as function arguments. The primary value types in Solidity include:


* **uint:** Unsigned integer types. These types are used to represent a positive integer or natural number. The keyword uint is a shorthand for uint256 which is a number that can range between 0 and 2256-1 . Other uint types include uint8, uint16, uint40…
* **int:** Signed integer types. Similar to unsigned integers but these are normal integers that can be positive or negative.
* **bool:** Boolean values that are used to declare whether a variable is true or false.
* **address:** This is a type unique to Ethereum and Solidity. It’s used to store the addresses of users or other contracts.
* **enum:** User-defined types for creating a set of named constants.
* **bytes and bytes32:** Eventually all the other types are stored in the form of bytes. Bytes themselves are used to store data that is not represented by those other types.



```
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

contract Variables {
    // value types
    uint256 positiveNumber;
    int256 positiveOrNegativeNumber;
    bool trueOrFalse;
    address userOrContractAddress;
    bytes32 someData;
}
```


Reference types store a reference to the data, which means that they don’t hold a value themselves but rather hold a pointer to a certain location in memory or storage that can have many values. They are used because values such as text words and item lists don’t have a definite size and so cannot be accessed directly like numbers or Booleans. The primary reference types in Solidity include:


* **strings:** A collection of one or more characters. Any text from “Hello!” to “123” to “?” is considered a string.
* **arrays:** A collection of data of the same type, like uint[] or bool[];
* **mappings:** Key-value stores where data is organized in a mapping from keys to values.
* **structs:** User-defined data structures that can contain a combination of different data types.



```
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

contract Variables {
    // value types
    uint256 positiveNumber;
    int256 positiveOrNegativeNumber;
    bool trueOrFalse;
    address userOrContractAddress;
    bytes32 someData;
    enum Colors {
        Red,
        Green,
        Blue
    }

    // reference types
    string text;
    bytes data;
    uint256[] positiveNumbersList;
    address[] userOrContractAddressesList;
    mapping(address => uint256) addressToPositiveNumber;
    mapping(address => uint256[]) addressToPositiveNumbersList;
    mapping(address => mapping(address => bool)) addressToAddressToTrueOrFalse;
    struct User {
        uint256 positiveNumber;
        address userOrContractAddress;
    }
}

```


Solidity Variables: Visibility
------------------------------


Variables can be declared with different visibility modifiers, such as **public**, **private**, **internal**, which determine who can access the variable. Let’s take a look at **Solidity public variables**, private variables and internal variables.


* **Public** variables, as their name suggests, are accessible by everyone including the contract itself.
* **Private** variables on the other hand, are ones that can only be read by the contract itself.
* **Internal** variables are a special case that can be used by contracts that inherit our contract. We will go in depth about contract inheritance in a separate article so stay tuned.



```
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

contract Variables {
    uint256 public notSecretNumber;
    uint256 private secretNumber;
    uint256 internal internalNumber;
    // when you don't specify a visibility, it defaults to public
    uint256 number; // same as "public uint256 number";
}

contract VariablesClone is Variables {
    // we can access notSecretNumber
    // we can access internalNumber
    // we can not access secretNumber

    function accessNumbers() public {
        notSecretNumber = 1;
        internalNumber = 2;
        // secretNumber = 3; // this will fail
    }
}

```


It must be clarified that once a Solidity contract is live on the blockchain, anyone and everyone can have access to the data inside of it. Changing a variable’s visibility affects how other contracts can interact with that variable from within our contract, but it doesn’t mean that the variable cannot be publicly accessed. Please keep this in mind and refrain from storing any sensitive information in your [smart contract](https://metana.io/blog/what-is-a-smart-contract-understand-contracts-on-the-blockchain/)s.


![solidity public variablessolidity state variablessolidity time unitssolidity global variablessolidity variables](https://metana.io/wp-content/uploads/2023/10/Downloader-La-HP4TB7ly36-1024x683.jpg)
Constants
---------


The last thing you can apply to storage variables is marking them as **constant** or **immutable**. Constant variables are not really variables because they never change, their value is declared directly and is encoded into the compiled code of the contract. Immutable values are similar, however they must be set when the contract is created using a special function called the “constructor.”




```
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

contract Variables {
    bool public constant THIS_IS_A_CONTRACT = true;
    uint256 public immutable numberOfSnackEatenBeforeDeployment;

    constructor(uint256 _numberOfSnackEatenBeforeDeployment) {
        numberOfSnackEatenBeforeDeployment = _numberOfSnackEatenBeforeDeployment;
    }
}
```



Solidity Global Variables
-------------------------


One more thing we didn’t talk about here is **solidity global variables**. Those variables are very special for solidity and the core functionality of the blockchain, so they deserve a spotlight of their own.


Using Your Variables
--------------------


Variables don’t mean much if you can’t use them, so stay tuned for our next article were we will introduce functions and how to use your variables inside of them!



![](https://metana.io/wp-content/uploads/2023/11/FAQs-cuate-1-1024x1024.png)
1. **What are variables in Solidity?**


Variables in Solidity are used to store and manipulate data within smart contracts. They can hold different types of values, such as integers, strings, addresses, and more.


2. **What are the variables of Solidity language?**


Solidity language supports various variable types, including uint, int, string, address, bool, and more. It also allows for the creation of custom data structures using structs and arrays.


3. **What are the types of state variables in Solidity?**


In Solidity, state variables can be declared as storage variables, which reside permanently on the blockchain, or as memory variables, which are temporary and used for computations.


4. **How do you display variables in Solidity?**


In Solidity, you can display variables using the emit statement inside events or by using the return statement inside functions to return variables as function outputs.


5. **How do you display a variable?**


You can display a variable in Solidity by using it within a function or [event](https://metana.io/blog/what-are-solidity-events/) and emitting or returning its value based on the desired use case.


6. **How do you display variable types?**


Variable types in Solidity are determined during declaration by specifying the appropriate type keyword, such as uint, string, address, etc.


7. **How do you display a variable in a string?**


To display a variable within a string in Solidity, you can use string concatenation with the toString() function or by using placeholder syntax, like string(abi.encodePacked(“Variable: “, variable)).


8. **How do you display two variable data?**


To display or output two variable data in Solidity, you can concatenate them within a string using string concatenation or placeholder syntax.


9. **Which command displays a variable?**


In Solidity, the emit command is commonly used within events to display or emit a variable’s value.


10. **What is a variable command?**


There is no specific “variable command” in Solidity. Variables are declared using appropriate type keywords and can be accessed, modified, and displayed within functions and events based on the desired functionality.






![Solidity Variables- Types and Uses_](https://metana.io/wp-content/uploads/2023/10/Solidity-Variables-Types-and-Uses_.jpg) 





[PrevPreviousHow to Write Solidity Smart Contracts](https://metana.io/blog/solidity-smart-contracts/) 




[Next10 Best Resources to Learn Blockchain DevelopmentNext](https://metana.io/blog/best-resources-to-learn-blockchain-development/) 







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






