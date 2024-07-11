



Understanding Solidity Functions: Types and Use Cases - Metana




















































































 












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





 







Understanding Solidity Functions: Types and Use Cases
=====================================================

 



 * [Ali Kanso](https://metana.io/blog/author/aii-kanso/)
* [November 1, 2023](https://metana.io/blog/2023/11/01/)
* [Smart Contracts](https://metana.io/blog/category/smart-contracts/)














Solidity is a high-level programming language specifically designed for developing smart contracts on the Ethereum blockchain. In Solidity, functions are a fundamental building block, allowing developers to define the behavior of a smart contract. Understanding the various **types of functions in Solidity** and the **use cases of** **Solidity functions** is crucial for creating secure and efficient smart contracts.


What is a Solidity Function?
----------------------------


In Solidity, a function is a piece of code that performs a specific task. These functions can be called by other contracts or external applications. Functions define the actions a smart contract can perform, and their proper design is crucial for the contract’s integrity and functionality. Solidity functions can be categorized into several types based on their purpose and visibility.


Functions are almost always associated with state or global variables. If you don’t know how Solidity variables work, make sure to check our [latest article](https://metana.io/blog/solidity-variables-types-and-uses/) about them. And if you’ve come here from the article, then you’re at the right place!


Basic Syntax
------------


Like any other programming language, functions have three key ingredients to them:


1. A set of inputs
2. An execution code
3. An output


![solidity functionssolidity functiontypes of functions in solidity](https://metana.io/wp-content/uploads/2023/10/Binary-code-amico-1024x1024.png)
To define a function in a Solidity contract, you simply have to use the **`function`** keyword followed by the desired function name. After that, you open a set of parentheses that will enclose any input your function will receive. That is proceeded by the function’s modifiers, one of which is the visibility modifier which needs to be specified. For now we will put it as public then we will touch on it later. And last but not least we have the function output.


A function doesn’t always need to have an input or an output, but it almost always has some logic to do.




```
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

contract Functions {
    function funcWithoutInputsNorOutputs() public {
        // ...
    }

    function funcWithInput(uint256 _input) public {
        // ...
    }

    function funcWithOutput() public returns (uint256) {
        // ...
        return 0;
    }

    function funcWithInputAndOutput(uint256 _input) public returns (uint256) {
        // ...
        return 0;
    }
}

```


Inputs & Outputs
----------------


Function inputs are declared just like regular variables, and we can have as many of them as we want.


To declare a basic input (uint256, bool, address…), we simply give the type and name of the input inside the function parentheses, and add a comma to insert another one.


Complex inputs on the other hand (string, array…), have to be additionally prefixed with the `**memory**` or **`calldata`** keywords. These tell the function where the variables will live throughout the life-cycle of the function call.


The difference between **`memory`** and **`calldata`** is that **`calldata`** marks the variable as read only which means it cannot be modified within the function. If you don’t plan on making changes to your variables, its better to prefix them with **`calldata`** as it makes the function call more efficient.




```
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

contract Functions {
    function withBasicInput(uint256 _num, bool _bool, address _account) public {
        // ...
    }

    function withComplexInput(
        uint256[] memory _nums,
        string memory _str
    ) public {
        // ...
    }

    function withUnchangedComplexInput(
        uint256[] calldata _nums,
        string calldata _str
    ) public {
        // ...
    }

    function withEverything(
        address _account,
        uint256[] memory _nums,
        string calldata _str
    ) public {
        // ...
    }
}

```


Function outputs behave in a similar manner, but you can only specify one output at a time.




```
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

contract Functions {
    function withBasicOutput() public returns (uint256) {
        // ...
    }

    function withComplexOutput() public returns (uint256[] memory) {
        // ...
    }

    // This is not a common pattern, but it is possible
    function withUnchangedComplexOutput(
        uint256[] calldata _nums
    ) public returns (uint256[] calldata) {
        // ...
        return _nums;
    }
}

```


Visibility
----------


Similar to variables, functions can have visibility modifiers including **public**, **private**, **internal**, and an additional visibility **external** which is special to them. And like variables, visibility modifiers specify who can access a function, including the contract itself.


* **Public** functions can be accessed by everyone including other functions in the contract.
* **Private** functions can only be accessed by the other functions in the contract.
* **Internal** functions can be accessed by the contract and any contract the inherits it. Its important to note that the inherited contract calls its own version of the function and not the original function itself.
* **External** functions can only be called from outside the contract. This can be achieved by calling the functions programatically, either from other contracts or through tools like [ethers](https://docs.ethers.org/v6/).




```
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

contract Functions {
    function publicFunc() public {
        // ...
    }

    function externalFunc() external {
        // ...
    }

    function internalFunc() internal {
        // ...
    }

    function _privateFunc() private {
        // ...
    }

    function callOtherFuncs() public {
        publicFunc();
        // externalFunc(); // This will error
        internalFunc();
        _privateFunc();
    }
}

contract FunctionsClone is Functions {
    function callOtherFuncsClone() public {
        publicFunc();
        // externalFunc(); // This will error
        internalFunc();
        // _privateFunc(); // This will error
    }
}

```


Types of Functions in Solidity
------------------------------


The last important thing you need to know about functions is their types, which dictate their functionalities. These types of functions in Solidity are **view**, **pure**, and **payable**.


* **View** functions don’t mutate any state variables, but can read them and return their values.
* **Pure** functions don’t mutate neither read the contract variables, and are used to perform calculations. The output of a pure function will always be the same given the same set of inputs.
* **Payable** functions are the ones that can receive money (Ether), and are fundamental to all financial transaction on the Ethereum blockchain.




```
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

contract Functions {
    uint256 private _num;

    function normalFunc(uint256 num_) public {
        _num = num_;
    }

    function viewFunc() public view returns (uint256) {
        return _num;
    }

    function pureFunc(uint256 a, uint256 b) public pure returns (uint256) {
        return a + b;
    }

    function payableFunc() public payable {
        // ...
    }
}

```


A Real World Example for Solidity Functions
-------------------------------------------


Here’s how you would use functions in an actual solidity contract:




```
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

contract Functions {
    uint256 private _num;

    function getNum() public view returns (uint256) {
        return _num;
    }

    function addToNum(uint256 num_) external payable {
        uint256 sum = _sum(_num, num_);
        _num = sum;
    }

    function _sum(uint256 a, uint256 b) private pure returns (uint256) {
        return a + b;
    }
}

```


The “Secret” Functions
----------------------


Similar to global variables, Solidity offers a set of special functions for contracts to work with. We will talk about those in an upcoming “secret” functions article 😉


Hope you got the idea of various types of functions in Solidity and the use cases of Solidity functions!




![](https://metana.io/wp-content/uploads/2023/10/FAQs-cuate-1024x1024.png)

1. **What are the two types of functions in Solidity?**


* The two main types of functions in Solidity are state-changing functions and view functions.


2. **What are private and public functions in Solidity?**


* Private functions can only be called from within the same contract, not from any derived contracts or external entities. Public functions, on the other hand, can be called both internally and externally, including from derived contracts.


3. **What are internal functions in Solidity?**


* Internal functions in Solidity are similar to private functions, but they can also be accessed by contracts that inherit from the contract where the internal function is defined.


4. **What are the different types of calls in Solidity?**


* In Solidity, there are external calls (call, callcode, delegatecall, and staticcall) that call external contracts, and internal calls that call functions within the same contract.


5. **What is a function in Solidity syntax?**


* A function in Solidity is declared using the function keyword, followed by the function name, parameters within parentheses, visibility keywords (like private, public, internal, external), and the return types. Example: function myFunction(uint \_param) public returns(uint) {…}.


6. **What are public functions in Solidity?**


* Public functions in Solidity are the ones that can be called both internally (from within the same contract or an inheriting contract) and externally (from other contracts or transactions).


7. **What is the difference between public and private functions?**


* The key difference between public and private functions lies in their accessibility. Public functions can be called from anywhere, including from outside the contract, while private functions can only be called from inside the contract where they are defined.


8. **Why would one use a public function**


* Public functions are used when we want to allow other contracts or external parties to interact with our contract.


9. **What is the difference between public and private functions?**


* Public functions can be called from anywhere, including from other contracts or from external transactions. Private functions, on the other hand, can only be called from the contract in which they’re declared.


10. **Is the constructor of a contract always public in Solidity?**


* No, from Solidity version 0.7.0 onwards, constructors can’t be marked as public or internal. They’re implicitly internal, meaning a contract can only be created directly, and not by a contract that inherits from it






![](https://metana.io/wp-content/uploads/2023/11/Understanding-Solidity-Functions-Types-and-Use-Cases-2.jpg) 





[PrevPreviousHow to Become a Web3 Developer: Roadmap for Web3 Beginners](https://metana.io/blog/how-to-become-a-web3-developer/) 




[NextUnderstanding Solidity Global Variables: Types and UsesNext](https://metana.io/blog/solidity-global-variables-types-and-uses/) 







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

 






![](https://metana.io/wp-content/uploads/2024/07/ERC-Token-Standards-Your-Simplified-Guide-copy-640x364.jpg)







### [Metana Editorial](https://metana.io/blog/author/editorial/)




24 hours ago

#### [Address Poisoning in Smart Contracts](https://metana.io/blog/address-poisoning-in-smart-contracts/)




Web3 thrives on user empowerment and the ease of sending and receiving cryptocurrency. However, a 


![](https://metana.io/wp-content/uploads/2024/07/ERC-Token-Standards-Your-Simplified-Guide-640x364.jpg)







### [Metana Editorial](https://metana.io/blog/author/editorial/)




2 days ago

#### [ERC Token Standards: Your Simplified Guide](https://metana.io/blog/erc-token-standards-your-simplified-guide/)




The lifeblood of Web3 applications often lies in tokens, and ERC token standards provide a 
 







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






