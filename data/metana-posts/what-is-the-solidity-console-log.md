



What is the Solidity Console Log? - Metana






















































































 












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





 







What is the Solidity Console Log?
=================================

 



 * [Metana Editorial](https://metana.io/blog/author/editorial/)
* [January 24, 2024](https://metana.io/blog/2024/01/24/)
* [Smart Contracts](https://metana.io/blog/category/smart-contracts/)














Debugging is super important when you make things using Solidity, a language for Ethereum smart contracts. Imagine building a LEGO structure, but once it’s built, you can’t change it easily. That’s why checking for mistakes (debugging) in Solidity is so crucial – you want to get it right the first time!


Hardhat is like a special toolbox for people making stuff on Ethereum. It has lots of helpful tools, and one of its coolest features is helping you find and fix mistakes in your code. Hardhat’s like a detective, making it easier to spot where things might go wrong in your smart contracts.


But Hardhat isn’t the only toolbox out there. There are other cool tools like Foundry, Truffle, and Brownie. Each of these has its own neat tricks for helping you build and fix things in Ethereum.


In this article, we’re going on an adventure to explore how Hardhat and these other tools help you fix mistakes in your [Solidity projects](https://metana.io/blog/solidity-projects-for-beginners-building-a-strong-foundation/). We’ll take a close look at Hardhat’s special features, especially its detective-like console log, and see how it compares with the other tools. By the end, you’ll know all about these awesome tools and how they can help you make really cool and mistake-free projects on Ethereum!


What is Solidity Console Log?
-----------------------------


**The Solidity console log is a tool used for debugging code in Solidity**, the programming language for Ethereum smart contracts. It allows developers to output information to the console, helping them understand and troubleshoot issues in their program.


In Solidity, `console.log()` is a function provided by the Hardhat contract library. It is similar to the `console.log()` function used in other programming languages like JavaScript. By using `console.log()`, developers can print values or messages to the console during the execution of their smart contracts.


**The `console.log()` [function in Solidity](https://metana.io/blog/solidity-functions-types-and-use-cases/) is often used for debugging purposes**. It allows developers to inspect the values of variables, check the flow of execution, and track the behavior of their smart contracts. By logging information to the console, developers can gain insights into the inner workings of their code and identify any potential issues or errors.


While console.log() can be useful for debugging, it is important to note that it is not recommended for production or live usage. In production environments, using events is considered ideal as they are distributed across nodes and provide a more reliable and scalable way to log information.


Basic Usage of Console Log in Solidity
--------------------------------------


Using the console log in Solidity is straightforward once you’ve set up your development environment. Here’s a guide to help you get started with the syntax, basic commands, examples, and best practices.


### Syntax and Basic Commands


* The syntax for using console log in Solidity is similar to JavaScript. You use `console.log()` to output information.
* Basic commands include:
	+ `console.log(<variable>)`: Logs the value of `<variable>`.
	+ `console.log("Message: ", <variable>)`: Logs a string followed by a variable.
* Solidity’s console log can handle various data types including strings, integers, addresses, etc.


### Simple Examples


**Example 1:** 


Logging a String and a Variable



```
pragma solidity ^0.8.0;

import "hardhat/console.sol";

contract MyContract {
    uint256 counter;

    function increment() public {
        counter++;
        console.log("Counter is now", counter);
    }
}

```

This contract increments a counter and logs its value each time `increment` is called.



**Example 2:** 


Logging Multiple Variables



```
pragma solidity ^0.8.0;

import "hardhat/console.sol";

contract Token {
    address public owner;

    constructor(address _owner) {
        owner = _owner;
        console.log("Token deployed by:", owner);
    }
}

```

Here, the contract logs the address of the owner when the Token is deployed.


### Tips on Best Practices for Effective Logging


* **Use Descriptive Messages:** Include clear and descriptive messages along with variable values to make logs more understandable.
* **Avoid Excessive Logging:** Overuse of console logs can clutter your output and make debugging harder. Log only what is necessary.
* **Remove Unnecessary Logs in Production:** Before deploying your contract, ensure that all console logs used for debugging are removed to avoid any confusion.
* **Keep Security in Mind:** Be cautious about logging sensitive information, even in a development environment.
* **Consistent Format:** Adopt a consistent format for logging messages to maintain readability and ease of debugging.


What is Hardhat?
----------------


Hardhat is a comprehensive development environment specifically designed for Ethereum. It serves as an indispensable toolkit for developers engaged in building, testing, and deploying smart contracts – the foundational elements of Ethereum’s blockchain applications.


**Primary Features of Hardhat:**


1. **Smart Contract Compilation**: Hardhat efficiently translates Solidity, Ethereum’s native programming language, into bytecode, the language understood by the Ethereum Virtual Machine (EVM).
2. **Automated Testing Framework**: It offers a robust testing environment, enabling developers to rigorously test their contracts under various conditions, ensuring reliability and robustness.
3. **Ethereum Network Simulation**: Developers can emulate the Ethereum network locally, allowing for a seamless and cost-effective development process without the need to interact with the actual blockchain.
4. **Script Execution**: Hardhat facilitates the execution of custom deployment scripts and tasks, enhancing the efficiency of the development workflow.


**Emphasizing Debugging Capabilities:**


* Hardhat’s standout feature lies in its advanced debugging capabilities. This functionality is critical, given the immutable nature of blockchain, where errors in smart contracts can have irreversible consequences.
* It provides detailed error logs and stack traces, offering clear insights into issues and anomalies within the smart contracts.
* The Hardhat console log, in particular, acts as a sophisticated diagnostic tool, recording the execution flow and state changes in contracts, thereby enabling developers to pinpoint and rectify issues with precision.


How to Print Solidity Console Logs
----------------------------------


To print to Solidity console logs, especially when using Hardhat, you typically follow these steps:


**Install Hardhat Console**:


* Ensure you have the Hardhat console package installed in your project. You can do this by running `npm install @nomiclabs/hardhat-ethers ethers @nomiclabs/hardhat-waffle ethereum-waffle chai @nomiclabs/hardhat-etherscan`.


**Import Console in Your Solidity File**:


* At the top of your Solidity file, import the Hardhat console by adding `import "hardhat/console.sol";`.


**Using console.log in Your Contract**:


* Within your smart contract’s functions, you can use `console.log` to output variable values, messages, or states. For example:



```
function setNumber(uint _num) public {
    console.log("Setting number to", _num);
    number = _num;
}

```

* `console.log` in Hardhat works similarly to JavaScript’s console.log, allowing you to print various data types.


**Compile and Test Your Contract**:


* After adding your console log statements, compile your contract using `npx hardhat compile`.
* Test your contract using Hardhat’s local development network or scripts. The console log output will appear in your terminal where you run the Hardhat test scripts.


**Interpret the Output**:


* The output from `console.log` will help you understand how your [smart contract](https://metana.io/blog/what-is-a-smart-contract-understand-contracts-on-the-blockchain/) is behaving at various stages of its execution.


**Remove console.log for Production**:


* Before deploying your contract to a live network (like Ethereum Mainnet), remember to remove `console.log` statements. They are for debugging purposes and should not be part of the production code.


This approach offers a practical and straightforward way to print information to the console while developing and debugging Solidity smart contracts using Hardhat.


Tips for Using Console Log Effectively
--------------------------------------


To effectively use **Solidity console log**, follow these condensed best practices:


**Strategic Placement**: Insert console log statements at critical code sections to monitor execution flow and contract behavior.


**Clear Messages**: Ensure log messages are descriptive for easy understanding and effective troubleshooting.


**Variable Value Logging**: Log variable values to check their states at various execution points, aiding in identifying unexpected behaviors.


**Use as a Temporary Tool**: Employ console logs primarily during development and testing. They offer immediate insights but should be removed or disabled in production code for the following reasons:


* **Security**: They might inadvertently expose sensitive data.
* **Code Clarity**: Removing logs avoids cluttering the codebase.
* **Performance**: Console logs can slow down contract execution.


**Consider Alternatives When Necessary**: Recognize the limitations of Solidity console logs. For advanced logging needs, large data storage, contract accessibility, or structured logging, explore external databases, Solidity events, or specialized logging frameworks.


Let’s Compare Hardhat to Other Tools,
-------------------------------------


When comparing Hardhat’s logging capabilities with other Ethereum development tools, it’s essential to look at the broader landscape of tools commonly used in blockchain development. Each tool has its unique features and functionalities, and understanding these can help developers choose the right tool for their specific needs. Let’s compare Hardhat with two other prominent Ethereum development tools: Truffle and Remix.


### Hardhat vs. Truffle


* **Logging Features:**
	+ Hardhat: Offers a built-in console.log functionality that allows developers to insert logging statements directly into their smart contracts. This feature makes debugging more straightforward and efficient.
	+ Truffle: Primarily relies on external debugging tools like Truffle Debugger. While effective, it might not be as intuitive as Hardhat’s console.log approach for developers accustomed to traditional logging methods.
* **Advantages of Hardhat:**
	+ More straightforward logging with console.log.
	+ Enhanced debugging experience, especially for developers familiar with JavaScript.
	+ Better integration with Ethers.js and Waffle for testing and interacting with contracts.
* **Advantages of Truffle:**
	+ Truffle Debugger provides a more traditional debugging experience, which might be preferred by some developers.
	+ A longer track record and larger user base, providing a wealth of community support and resources.
* **Limitations of Hardhat:**
	+ Hardhat’s logging might not provide as detailed transaction execution information as Truffle’s debugger in some complex scenarios.


### Hardhat vs. Remix


* **Logging Features:**
	+ Hardhat: Console.log functionality is part of its local development environment, suitable for larger projects and extensive testing.
	+ Remix: An online IDE primarily used for quick prototyping and smaller projects. Its logging capabilities are more basic and integrated into its online console.
* **Advantages of Hardhat:**
	+ More robust and suitable for complex, large-scale projects.
	+ Console.log provides a familiar experience for developers from a JavaScript background.
* **Advantages of Remix:**
	+ Easy to access and use for beginners or for rapid prototyping.
	+ No setup required, as it’s a browser-based IDE.
* **Limitations of Hardhat:**
	+ Requires setup and familiarity with Node.js environment, which might be a hurdle for beginners.


What is an Alternative for Logging Information in Smart Contracts
-----------------------------------------------------------------


Solidity events provide a powerful alternative for logging information in smart contracts. Events allow developers to print information on the blockchain in a structured and searchable manner. They are an integral part of smart contract development, offering several benefits over the console log.


### Benefits of Using Solidity Events:


1. **Searchability and Gas Efficiency:** Solidity events are stored in logs on the blockchain, making them searchable and queryable. This allows developers to retrieve specific transaction data efficiently. Emitting events is also more gas-efficient compared to storing data in public storage variables within the contract.
2. **Testing and Debugging:** Events are invaluable for testing and debugging smart contracts. They enable developers to test for specific variables, track the flow of execution, and verify the behavior of the contract. By emitting events at critical points in the code, developers can gain insights into the contract’s execution and identify any issues or unexpected behavior.
3. **Frontend Interaction:** Solidity events facilitate automated frontend updates. By listening for emitted events, frontend applications can automatically update their user interfaces based on the changes happening in the smart contract. This provides a seamless and real-time user experience.


### Drawbacks of Using Solidity Events:


1. **Limited Data Storage:** Solidity events have a limited storage capacity. They are primarily used for logging important information and events, rather than storing large amounts of data. If extensive data storage is required, alternative methods like using public storage variables or external databases may be more suitable.
2. **Inaccessibility to Smart Contracts:** Solidity events cannot be directly accessed by smart contracts. They are primarily intended for external use, such as querying and referencing transaction data. If the contract itself needs to access the logged information, alternative approaches like storing data in public variables within the contract may be necessary.


***Comparing Solidity Events to the Console Log:***


Solidity events and the console log serve different purposes and have distinct advantages. Here’s a comparison:


1. **Purpose:** Solidity events are primarily used for long-term logging and tracking of important contract events. They offer searchability, gas efficiency, and automated frontend interaction. On the other hand, the console log is a temporary debugging tool used during development and testing phases to gain immediate visibility into code execution.
2. **Data Storage:** Solidity events store data in logs on the blockchain, making it accessible and queryable. In contrast, the console log does not persist data on the blockchain and is primarily used for immediate debugging purposes.
3. **Accessibility:** Solidity events can be accessed externally, allowing other applications to query and reference the logged information. The console log, however, is not directly accessible by other contracts or applications.


![solidity console loghardhat console log](https://metana.io/wp-content/uploads/2024/01/Questions-cuate-1024x1024.png)
FAQs
----


**What is the Solidity console log?**


* The Solidity console log is a tool used to debug Solidity code by logging information to the console. It helps developers understand and troubleshoot issues in their smart contracts.


**How can I use console.log() in Solidity?**


* To use console.log() in Solidity, you need to import the “hardhat/console.sol” library in your contract code. This function allows you to print logging messages and contract variables during contract execution.


**What are the benefits of using the Solidity console log?**


* The Solidity console log provides immediate visibility into the state of your contract during development and testing phases. It helps you log variable values and messages to understand the behavior of your contract.


**Can I use console.log() in production code?**


* It is recommended to remove or disable console.log() statements in production code to optimize performance and ensure security. Leaving console.log() statements can impact performance and potentially expose sensitive information.


**Are there any alternatives to the Solidity console log for logging information in smart contracts?**


* Yes, Solidity events are a powerful alternative for logging information in smart contracts. They provide persistent storage, searchability, and automated frontend interaction.


**What is Solidity?**


* Solidity is a contract-oriented, high-level programming language used for implementing smart contracts on blockchain platforms, primarily Ethereum. It is influenced by C++, Python, and JavaScript and is designed to target the Ethereum Virtual Machine (EVM).


**What are the main components of a Solidity contract?**


* The main components of a Solidity contract include the contract declaration, state variables, functions, modifiers, events, and struct and enum definitions.


**What are Solidity events and how are they related to topics?**


* Solidity events are used to emit information from a contract to the blockchain. They can be indexed to allow for faster filtering. Topics are used to identify events and are part of the event’s data structure.


**What is the Solidity statement to print data?**


* In older versions of Solidity, the logX statement was used to print data. However, it is now deprecated, and events or Solidity libraries enabling the use of console.log() inside contract code are recommended.


**What are some common Solidity interview questions?**


* Common Solidity interview questions cover topics such as the basics of Solidity, smart contract development, blockchain technology, and Ethereum. These questions help assess a candidate’s knowledge and understanding of Solidity and its ecosystem.






![](https://metana.io/wp-content/uploads/2024/01/What-is-the-Solidity-Console-Log.jpg) 





[PrevPreviousWhat is a Tech Lead? All You Need To Know](https://metana.io/blog/what-is-a-tech-lead-all-you-need-to-know/) 




[NextWhat Coding Language Should I Learn? 10 Best Coding LanguagesNext](https://metana.io/blog/what-coding-language-should-i-learn/) 







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






