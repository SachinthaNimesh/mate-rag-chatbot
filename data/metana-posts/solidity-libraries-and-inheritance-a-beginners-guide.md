



Solidity Libraries and Inheritance: A Beginner's Guide - Metana




















































































 












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





 







Solidity Libraries and Inheritance: A Beginner’s Guide
======================================================

 



 * [Metana Editorial](https://metana.io/blog/author/editorial/)
* [March 26, 2024](https://metana.io/blog/2024/03/26/)
* [Smart Contracts](https://metana.io/blog/category/smart-contracts/)














Solidity, the programming language powering Ethereum smart contracts, offers robust tools for code reusability. Two key approaches dominate this landscape: inheritance and libraries. While both serve the purpose of reducing code redundancy, they differ significantly in functionality and implementation. Understanding these differences is crucial for crafting efficient and secure [smart contracts](https://metana.io/blog/what-is-a-smart-contract-understand-contracts-on-the-blockchain/).


This article delves into the concepts of inheritance and libraries in Solidity. We’ll explore their characteristics, applications, and best practices to guide you in making informed decisions while building your [smart contracts](https://metana.io/blog/best-practices-for-smart-contract-testing-how-to/).


Inheritance: Building Upon Existing Functionality
-------------------------------------------------


Inheritance allows you to create a new contract (derived contract) that inherits functionalities and state variables from an existing contract (base contract). This establishes an “is-a” relationship. The derived contract can access and potentially override functions and variables defined in the base contract, extending its functionality.


In this example, MyContract inherits from Ownable. This grants MyContract access to the owner variable and the onlyOwner modifier from Ownable. Additionally, MyContract defines its own variable value and a function setValue.



```
contract Ownable {
  address public owner;

  constructor() public {
    owner = msg.sender;
  }

  modifier onlyOwner() {
    require(msg.sender == owner, "Only owner can call this function.");
    _;
  }
}

contract MyContract is Ownable {
  uint public value;

  function setValue(uint _value) public onlyOwner {
    value = _value;
  }
}
```


### Benefits of Inheritance:


* **Reduced Code Duplication:** By inheriting common functionalities, you avoid rewriting the same code in multiple contracts. This simplifies development and maintenance.
* **Enforced Functionality:** Base contracts can define essential functions, ensuring derived contracts inherit necessary functionalities.
* **Code Organization:** Inheritance promotes code organization by grouping related functionalities into base contracts.


### Challenges of Inheritance:


* **Increased Contract Size:** Derived contracts become larger as they inherit code from the base contract. This can lead to higher deployment costs ([gas fees](https://metana.io/blog/what-are-ethereum-gas-fees/)).
* **Tight Coupling:** Changes made to the base contract can potentially affect all derived contracts. Careful planning is required to avoid unintended consequences.
* **Diamond Problem:** In complex inheritance hierarchies, the “diamond problem” can arise where a derived contract inherits the same variable or function from multiple base contracts, leading to ambiguity.


### Libraries: Reusable Utility Functions


Solidity libraries are collections of functions that can be used by other contracts. Unlike inheritance, libraries do not have their own storage and cannot hold state variables. They primarily provide reusable utility functions.



```
library SafeMath {
  function add(uint a, uint b) public pure returns (uint) {
    uint c = a + b;
    require(c >= a, "SafeMath: addition overflow");
    return c;
  }
}

contract MyContract {
  using SafeMath for uint;

  function increment(uint value) public {
    value = value.add(1);
  }
}
```


In this example, the SafeMath library provides a safe add function that prevents overflow errors. The MyContract uses the using statement to import the add function and make it available with a shorter syntax (value.add(1)).


### Benefits of Libraries:


* **Reduced Gas Costs:** Libraries are deployed only once on the blockchain, and their code is reused by referencing contracts. This minimizes gas costs associated with deploying code repeatedly.
* **Modular Code:** Libraries promote modularity by separating utility functions from core contract logic.
* **Improved Security:** Commonly used and well-tested libraries like SafeMath can enhance the security of your contracts by preventing vulnerabilities.


![solidity librariessolidity inheritanceinheritanceinheritance vs libraries](https://metana.io/wp-content/uploads/2024/03/Library-rafiki-1024x1024.png)
### Challenges of Libraries:


* **Limited Functionality:** Libraries cannot hold state or manage storage, limiting their applicability for functionalities requiring persistent data.
* **Increased Reliance on External Code:** Using libraries introduces dependencies on external code. Choosing well-maintained and secure libraries is crucial.


When to Use Inheritance vs. Libraries
-------------------------------------


The choice between inheritance and libraries depends on your specific needs:


### Use Inheritance When:


* **Extends Functionality:** New contract builds upon and modifies existing contract behavior.
* **Enforces Behavior:** Derived contracts inherit essential functions from a base contract.
* **Clear “Is-A” Hierarchy:** Building related contracts with a clear parent-child relationship.


### Use Libraries When:


* **Reusable Functions:** Functions don’t require storage and need reuse across contracts.
* **Minimize Gas Costs:** Frequently used code is deployed once and referenced by multiple contracts.
* **Modular Code:** Separate core contract logic from reusable functions for better maintainability.


**Note:** If you’re familiar with web3.js, a popular library for interacting with Ethereum from JavaScript applications, libraries in Solidity function similarly. They provide reusable functionalities that can be integrated into your smart contracts. However, unlike web3.js libraries that reside outside the blockchain, Solidity libraries are deployed on the blockchain itself.


Best Practices for Inheritance and Libraries
--------------------------------------------


Following best practices ensures you leverage inheritance and libraries effectively while mitigating associated challenges:


### Inheritance:


* **Favor Shallow Inheritance Hierarchies:** Deep inheritance hierarchies can become complex and difficult to maintain. Aim for a maximum of two or three levels of inheritance.
* **Abstract Contracts:** Define abstract contracts as base contracts that cannot be directly instantiated. This ensures derived contracts implement essential functionalities before being deployed.
* **Virtual Functions:** Utilize virtual functions in base contracts for functions that derived contracts can override with customized behavior.
* **Carefully Consider Base Contract Modifications:** Thoroughly test the impact of changes made to base contracts on all derived contracts to avoid unintended consequences.


### Libraries:


* **Choose Well-Tested Libraries:** Opt for well-established and thoroughly tested libraries from reputable sources like [OpenZeppelin](https://www.openzeppelin.com/contracts) to minimize security risks.
* **Understand Library Dependencies:** Be aware of potential dependencies introduced by libraries and ensure compatibility with your project’s requirements.
* **Clearly Document Library Usage:** Document how you’re using libraries within your contracts to improve code clarity and maintainability.


### Advanced Techniques:


* **Multiple Inheritance:** While generally discouraged due to the diamond problem, careful planning and use of abstract contracts can allow for controlled multiple inheritance in specific scenarios.
* **Inheritance with Libraries:** You can combine inheritance and libraries by having a base contract inherit from a library, providing derived contracts with access to both functionalities. However, exercise caution to avoid unnecessary complexity.


Conclusion
----------


Inheritance and libraries are powerful tools in the [Solidity developer](https://metana.io/blog/solidity-developer-job-description/)‘s arsenal. Understanding their strengths and weaknesses allows you to create modular, reusable, and secure smart contracts. By following best practices and carefully considering your project’s needs, you can leverage these techniques to build efficient and robust blockchain applications.



![faq](https://metana.io/wp-content/uploads/2024/01/Questions-cuate-1024x1024.png)
FAQs
----


**What are Solidity libraries?**


* Solidity libraries are reusable pieces of code deployed once and used across multiple contracts, optimizing gas costs and code organization in Ethereum development.


**How does inheritance work in Solidity?**


* Inheritance in Solidity allows contracts to derive properties and functions from one or more parent contracts, promoting code reusability and logical structure in smart contract design.


**What are the benefits of using libraries in Solidity?**


* Libraries in Solidity reduce redundancy, lower gas costs, and improve contract organization, making them a crucial tool for efficient and cost-effective blockchain development.


**Can a Solidity library inherit from another contract or library?**


* Yes, Solidity libraries can inherit from other libraries but not from contracts, which ensures modular, efficient, and reusable code in smart contract ecosystems.


**How do I implement a library in my Solidity contract?**


* Implement a library in Solidity by declaring it with the `library` keyword, deploying it, and then using it in your contract with the `using` keyword for specific data types.


**What is Ethereum programming?**


* Ethereum programming involves developing decentralized applications (dApps) and smart contracts using languages like Solidity, facilitating transactions and agreements without intermediaries.


**How do smart contracts work?**


* Smart contracts are self-executing contracts with the terms of the agreement directly written into lines of code, automatically enforced and executed on the blockchain.


**What is [blockchain development](https://metana.io/blog/why-become-a-blockchain-developer-whats-in-it-for-you/)?**


* Blockchain development involves creating decentralized databases and applications that allow secure, transparent, and tamper-proof transactions and data storage.


**How does code reusability benefit smart contract development?**


* Code reusability enhances smart contract development by saving time, reducing errors, and ensuring consistent behavior across different parts of a blockchain application.


**What is code efficiency in smart contracts?**


* Code efficiency in smart contracts refers to writing optimized, gas-efficient code that minimizes execution costs and enhances performance on the blockchain.






![](https://metana.io/wp-content/uploads/2024/03/Solidity-Libraries-and-Inheritance-A-Beginners-Guide.jpeg) 





[PrevPreviousUpgrading Smart Contracts? Here’s All You Need To Know.](https://metana.io/blog/upgrading-smart-contracts/) 




[NextHow to Connect to Ethereum with Web3.js: Understanding Web3.js LibraryNext](https://metana.io/blog/how-to-connect-to-ethereum-with-web3-js/) 







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




13 mins ago

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






