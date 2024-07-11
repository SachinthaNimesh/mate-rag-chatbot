



Understanding Solidity Methods: How They Differ from Functions - Metana




















































































 












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





 







Understanding Solidity Methods: How They Differ from Functions
==============================================================

 



 * [Metana Editorial](https://metana.io/blog/author/editorial/)
* [November 28, 2023](https://metana.io/blog/2023/11/28/)
* [Smart Contracts](https://metana.io/blog/category/smart-contracts/)














You probably already know about Solidity, right? It’s a programming language that helps us create smart contracts on the Ethereum network. It’s quite similar to JavaScript, and we use “functions” and “methods” a lot when writing in Solidity.


Of course, you might already know a lot about this, but sometimes, it can be a bit tricky to tell what makes functions and methods different from each other.


So, why don’t we dive a bit deeper into what **Solidity methods** are all about? And, if you need to, you can always brush up on your knowledge about functions with our earlier article [here](https://metana.io/blog/solidity-functions-types-and-use-cases/). Let’s get started!


Understanding Solidity Functions
--------------------------------


A “function” in Solidity is like a little robot. It’s given a job to do, it does that job, and then it gives you the results. This little robot can work anywhere in the program – it doesn’t have to be tied to any specific part.


For example, let’s say we have a function that adds two numbers together. It looks like this:



```
function add(uint a, uint b) public pure returns (uint) {
    return a + b;
}
```

This `add` function takes two numbers (we call these “inputs”), adds them together, and gives us the total (this is the “output”).


![solidity methodssolidity functions](https://metana.io/wp-content/uploads/2023/11/Hand-coding-cuate-1024x1024.png)
What about Solidity Methods?
----------------------------


On the other hand, a “method” in Solidity still does a job like a function, but it’s tied to a specific part of the program. It’s like if our little robot could only work in one room of a house. These methods can interact with other parts of their specific room (in programming, we call this a “contract”).


For example, look at this:



```
contract SimpleContract {
    uint public data;

    function setData(uint x) public {
        data = x;
    }
}
```

Here, `setData`is a method. It’s tied to the contract named `SimpleContract`, and it can interact with this contract’s data.


So, What’s the Difference?
--------------------------


The big difference between functions and methods in Solidity is where they can work:


1. **Instance Association (Place of Work):** Methods are tied to a specific part of the program (a contract). But, functions can work anywhere – they don’t have to be tied to a specific contract.
2. **State Interaction:** Methods can interact with their specific contracts, but functions can’t change parts of a contract.
3. **Visibility:** Methods can be set to be seen by everyone, or only by certain parts of the program. Functions are usually set to be seen by everyone.


So, while functions and methods might seem similar, they play different roles in Solidity. Knowing the difference can help you understand how to use this programming language better!


In Conclusion
-------------


Solidity, the language of Ethereum smart contracts, uses both functions and methods to make things work. Functions are like handy little tools that can work anywhere in the program. On the other hand, methods are tightly tied to specific parts of the program, known as contracts, where they can interact and change things around.


The main differences between functions and methods boil down to where they can work, what they can interact with, and who can see them. Understanding these differences is a big step towards getting better at using Solidity. It’s like knowing how to use every single tool in a toolbox – the more you know, the better you can build!



![Frequently Asked Quesions](https://metana.io/wp-content/uploads/2023/10/FAQs-cuate-1024x1024.png)
1. What is a method in Solidity?


* A method in Solidity is a function defined within a contract and associated with a specific instance of that contract. It can interact with the contract’s state variables.


2. How is a method different from Solidity functions?


* The major difference is that methods are associated with a specific contract instance and can interact with its state variables, while functions are not tied to a specific contract instance.


3. How do I define a method in Solidity?


* Methods are defined within a contract. For example:



```
contract SimpleContract {

    uint public data;

    function setData(uint x) public {

        data = x;

    }

}
```

The `setData` function is a method of the SimpleContract contract.


4. Can methods in Solidity return values?


* Yes, methods in Solidity can return a value using the returns keyword, similar to functions.


5. Can a method in Solidity modify the state of a contract?


* Yes, methods in Solidity can read and modify the state of a contract as they are tied to a specific contract instance.


6. What are visibility specifiers in Solidity methods?


* Visibility specifiers (public, external, internal, private) define where your method can be accessed from.


7. What does the public keyword mean in a Solidity method?


* public is a visibility specifier. A public method can be called from any contract.


8. How can I call a method in Solidity?


* A method can be called within a contract using this.methodName(), or from another contract by using contractInstance.methodName().


9. Can Solidity methods have parameters?


* Yes, similar to **Solidity functions**, methods can take parameters.


10. What does the external keyword mean in a Solidity method?


* external is a visibility specifier. An external method can only be called from other contracts and cannot be called internally, except with this.methodName().






![Understanding-Solidity-Methods-How-They-Differ-from-Functions](https://metana.io/wp-content/uploads/2023/11/Understanding-Solidity-Methods-How-They-Differ-from-Functions.jpg) 





[PrevPreviousUnderstanding Solidity Global Variables: Types and Uses](https://metana.io/blog/solidity-global-variables-types-and-uses/) 




[Next15 Common Web3 Interview Questions and AnswersNext](https://metana.io/blog/web3-interview-questions/) 







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






