



Insecure Randomness in Smart Contracts - Metana






















































































 












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





 







Insecure Randomness in Smart Contracts
======================================

 



 * [Metana Editorial](https://metana.io/blog/author/editorial/)
* [June 25, 2024](https://metana.io/blog/2024/06/25/)
* [Smart Contracts](https://metana.io/blog/category/smart-contracts/), [Solidity](https://metana.io/blog/category/solidity/)














In the dynamic and evolving landscape of Web3, randomness plays a crucial role in ensuring the fairness and unpredictability of various applications. From provably fair gaming to the generation of unique tokens, the integrity of randomness is paramount. However, when this randomness is compromised, it opens the door to a range of vulnerabilities collectively known as **Insecure Randomness Attacks**. Understanding and mitigating these risks is essential for anyone developing smart contracts.


The Source of the Trouble
-------------------------


At the heart of many Web3 applications lies the pseudorandom number generator (PRNG). While PRNGs are designed to produce sequences of numbers that appear random, their output is determined by an initial value known as the seed. The security of these generators hinges on the unpredictability of the seed. If attackers can predict or manipulate the seed, they can predict the PRNG’s output, compromising the randomness and security of the application.


### Why Predictable Seeds Are Dangerous


* **Predictable Seeds:** If the seed value is derived from easily obtainable data, such as timestamps, block hashes, or user addresses, it becomes predictable. Attackers can use this predictability to their advantage, undermining the randomness.
* **Off-chain Bias:** When randomness is generated off-chain (e.g., on a user’s computer), it can be tampered with before being submitted to the blockchain. This allows attackers to manipulate the input to their benefit.


### Example of Predictable Seed in Solidity


Consider a simple example in Solidity where a seed is generated using the current block timestamp:



```
pragma solidity ^0.8.0;

contract PredictableRandom {
    function getRandomNumber() public view returns (uint256) {
        uint256 seed = uint256(keccak256(abi.encodePacked(block.timestamp)));
        return seed;
    }
}

```

In this example, the seed is derived from the current block timestamp, making it predictable. An attacker can easily guess the seed by knowing the block time.


When Lady Luck Frowns
---------------------


The consequences of insecure randomness can be severe and far-reaching. Here are a few scenarios where insecure randomness can wreak havoc:


* **Unfair Games** In provably fair games, the fairness relies on the unpredictability of the outcomes. If attackers can predict the random numbers used in the game, they can unfairly win bets, draining funds from the contract and eroding trust in the platform.
* **RNG-Based Token Exploits** Randomness is often used in token generation to ensure a fair distribution. Predictable randomness allows attackers to manipulate the system, acquiring a disproportionate share of valuable tokens.
* **Reentrancy Vulnerability** Insecure randomness can also exacerbate other vulnerabilities, such as reentrancy attacks. An attacker can exploit predictable randomness to repeatedly exploit the contract within a single transaction.



![insecure randomness in smart contracts](https://metana.io/wp-content/uploads/2024/06/DALL·E-2024-06-25-13.50.32-A-relatable-and-simple-illustration-showing-a-smart-contract-with-a-warning-sign-for-insecure-randomness.-The-image-features-a-person-looking-at-a-com.jpg)
Real-World Incidents
--------------------


History has shown that insecure randomness can lead to devastating exploits. Here are a couple of notable incidents:


### The Etherroll Exploit (2016)


Etherroll, a decentralized dice game, suffered an exploit due to a flaw in its PRNG. Attackers were able to predict the winning numbers, resulting in significant financial losses for the platform.


### The DAO Roulette (2016)


The DAO’s use of an off-chain source of randomness made it vulnerable to manipulation. This contributed to the infamous DAO hack, which led to the loss of millions of dollars worth of Ether.


Securing Your Random Acts
-------------------------


To safeguard your smart contracts from insecure randomness, consider the following best practices:


### Leverage Secure Oracles


Decentralized oracles can provide verifiable randomness on-chain, ensuring that the random numbers used in your contract are truly unpredictable. Oracles like Chainlink VRF (Verifiable Random Function) are designed specifically for this purpose.


### Example of Using Chainlink VRF


Here is an example of how to use Chainlink VRF to generate secure random numbers in a Solidity contract:



```
pragma solidity ^0.8.0;

import "@chainlink/contracts/src/v0.8/VRFConsumerBase.sol";

contract SecureRandom is VRFConsumerBase {
    bytes32 internal keyHash;
    uint256 internal fee;
    uint256 public randomResult;

    constructor(address _vrfCoordinator, address _linkToken, bytes32 _keyHash, uint256 _fee)
        VRFConsumerBase(_vrfCoordinator, _linkToken)
    {
        keyHash = _keyHash;
        fee = _fee;
    }

    function getRandomNumber() public returns (bytes32 requestId) {
        require(LINK.balanceOf(address(this)) >= fee, "Not enough LINK");
        return requestRandomness(keyHash, fee);
    }

    function fulfillRandomness(bytes32 requestId, uint256 randomness) internal override {
        randomResult = randomness;
    }
}

```

In this example, Chainlink VRF is used to generate a secure random number. The random number is provided by a decentralized oracle, ensuring its unpredictability.


### Cryptographically Secure PRNGs


Using cryptographically secure PRNGs with unpredictable seeds is another effective way to ensure the security of your randomness. These PRNGs are designed to withstand attacks and produce truly random outputs.


### Example of Cryptographically Secure PRNG in Solidity


Here’s an example of using a more secure method for generating random numbers in Solidity:



```
pragma solidity ^0.8.0;

contract SecureRandom {
    function getSecureRandomNumber() public view returns (uint256) {
        uint256 seed = uint256(keccak256(abi.encodePacked(block.timestamp, block.difficulty, msg.sender)));
        return seed;
    }
}

```

In this example, the seed is derived from a combination of the current block timestamp, block difficulty, and the caller’s address, making it significantly harder to predict.


### Community Audits


Encouraging community code reviews and audits can help identify potential randomness vulnerabilities. Peer review by experienced developers can uncover flaws that might otherwise go unnoticed.


Conclusion: Insecure Randomness
-------------------------------


Insecure randomness is a critical vulnerability that can compromise the integrity and security of Web3 applications. By understanding the risks and implementing best practices, developers can protect their smart contracts from these attacks. Leveraging secure oracles, using cryptographically secure PRNGs, and encouraging community audits are essential steps in ensuring the security of randomness in your smart contracts.


Understanding and addressing insecure randomness is not just about protecting your code; it’s about safeguarding the trust and fairness that underpin the entire Web3 ecosystem. By taking these precautions, you can help ensure that Lady Luck remains impartial and that your smart contracts remain secure.



![faq](https://metana.io/wp-content/uploads/2024/05/Questions-bro-1.svg)
FAQs:
-----


**What is insecure randomness in smart contracts?**


* Insecure randomness refers to the use of predictable or easily manipulated random number generation in smart contracts, making them vulnerable to exploitation.


**How does insecure randomness affect blockchain security?**


* It can lead to predictable outcomes, allowing attackers to manipulate contract behavior, compromise fairness, and exploit vulnerabilities for financial gain.


**What are common sources of insecure randomness in smart contracts?**


* Common sources include block hashes, timestamps, and other on-chain data that can be influenced or predicted by malicious actors.


**How can insecure randomness be prevented in smart contracts?**


* Utilizing secure randomness techniques such as off-chain randomness, cryptographic functions, and decentralized oracle networks can prevent vulnerabilities.


**Why is secure randomness crucial in decentralized applications?**


* Secure randomness ensures fair and unpredictable outcomes, which are essential for applications like lotteries, gaming, and consensus mechanisms.


**What are some examples of attacks due to insecure randomness?**


* Notable examples include lottery manipulation in early Ethereum contracts and gaming applications where outcomes were predictably influenced.


**How do decentralized oracles enhance randomness security?**


* Decentralized oracles provide unbiased and tamper-proof external data, reducing the risk of predictable or manipulated random number generation.


**What are the best practices for implementing secure randomness in smart contracts?**


* Best practices include using verifiable random functions (VRFs), combining multiple sources of entropy, and regularly updating randomness algorithms.


**How can regular audits help in addressing insecure randomness?**


* Regular audits can identify and correct weaknesses in randomness implementation, ensuring that smart contracts remain secure against manipulation.


**What role do developers play in securing randomness in smart contracts?**


* Developers must implement robust random number generation methods, stay updated with security practices, and conduct thorough testing to ensure contract integrity.






![](https://metana.io/wp-content/uploads/2024/06/Insecure-Randomness-in-Smart-Contracts.jpg) 





[PrevPreviousEthernaut Level 15 Walkthrough: Naught Coin](https://metana.io/blog/ethernaut-level-15-walkthrough-naught-coin/) 




[NextGovernance Attacks in Smart ContractsNext](https://metana.io/blog/governance-attacks-in-smart-contracts/) 







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




8 mins ago

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






