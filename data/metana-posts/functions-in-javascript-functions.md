



Functions in JavaScript - Metana



















































































 












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





 







Functions in JavaScript
=======================

 



 * [Metana Editorial](https://metana.io/blog/author/editorial/)
* [April 17, 2024](https://metana.io/blog/2024/04/17/)
* [Full-Stack](https://metana.io/blog/category/full-stack/)














Functions are the foundation of well-structured, maintainable, and scalable JavaScript code. They encapsulate a specific task, promoting code reusability and fostering modular programming practices. This article dives into the world of **[JavaScript](https://metana.io/blog/how-javascript-works-all-you-need-to-know/) functions**, exploring their definition, mechanics, various types, and best practices for their effective use.


What Are Functions ?
--------------------


At their core, functions are reusable blocks of code designed to perform a specific operation. They accept optional inputs known as parameters, process them using the function’s logic, and optionally produce an output through a return statement. This input-process-output paradigm makes functions ideal for breaking complex tasks into smaller, manageable units.


Here’s a basic example of a function that calculates the area of a rectangle:



```
function calculateArea(length, width) {
  const area = length * width;
  return area;
}

// Calling the function with arguments
const rectangleArea = calculateArea(5, 10);
console.log(rectangleArea); // Output: 50
```


In this example, calculateArea is the function name. The function takes two parameters, length and width, representing the rectangle’s dimensions. Inside the function body, the area is calculated by multiplying the length and width. Finally, the calculated area is returned using the return statement. When the function is called with specific values for length and width (arguments), it executes the defined logic and returns the result.


Breaking Down JavaScript Functions
----------------------------------


A JavaScript function definition comprises several key elements:


* **Function Keyword (****function****):** This keyword signifies the beginning of a function definition.
* **Function Name:** A unique identifier chosen by the developer to represent the function’s purpose (e.g., calculateArea). Function names follow the same naming conventions as variables, using letters, digits, underscores, and dollar signs.
* **Parameter List (****parameter1, parameter2, …****):** Enclosed within parentheses, this optional list specifies the variables that will act as inputs to the function. These parameters hold the values passed during the function call.
* **Function Body (****{ … }****):** This block of code, enclosed in curly braces, contains the statements that define the function’s logic. These statements determine the actions performed with the received parameters and how the function arrives at its output.
* **Return Statement (****return value;****):** This statement (optional) specifies the value the function sends back after execution. If no return statement is present, the function implicitly returns undefined.


Calling Functions
-----------------


Functions come alive through calling them. To execute a function, we use its name followed by parentheses. These parentheses can optionally contain arguments, which are the actual values passed to the function’s parameters.



```
function greet(name) {
  console.log("Hello, " + name + "!");
}

greet("Alice"); // Output: Hello, Alice!
```


In this example, greet is called with the argument “Alice”, which is assigned to the parameter name inside the function. The function then uses the value of name to construct the greeting message.


Function Arguments vs Parameters
--------------------------------


While often used interchangeably, arguments and parameters have distinct roles:


* **Parameters:** These are placeholders defined within the function’s declaration, specifying the expected inputs. They act as variables local to the function, holding the values passed during the function call.
* **Arguments:** These are the actual values provided when the function is invoked. They are passed within the parentheses during the function call and are assigned to the corresponding parameters within the function body.


Arguments can be missing altogether if the function doesn’t require any input, or there can be more arguments than parameters. In such cases, JavaScript handles these scenarios according to predefined rules.


Function Expressions
--------------------


JavaScript allows defining functions not just through declarations but also using expressions. Function expressions assign a function to a variable, allowing for more dynamic function creation.



```
const calculateVolume = function(length, width, height) {
  return length * width * height;
};

const volume = calculateVolume(5, 10, 2);
console.log(volume); // Output: 100
```


Here, the function is assigned to the variable calculateVolume. This approach offers flexibility when functions need to be created based on certain conditions or passed as arguments to other functions.


Function Scope
--------------


Scope defines the accessibility of variables within your code. Function scope dictates that variables declared inside a function are only accessible within that function and are not visible outside it. This concept is important for preventing naming conflicts and maintaining organized code.


Imagine a function as a self-contained world with its own set of variables. These variables, declared using let or const, are local to the function and cannot be directly accessed from outside. This isolation helps prevent accidental modification of variables from other parts of your code.


Here’s a code example:



```
function calculateArea(length, width) {
  const area = length * width;
  return area;
}

let rectangleLength = 5; // Global variable

const rectangleArea = calculateArea(rectangleLength, 10);
console.log(rectangleArea); // Output: 50

// console.log(area); // This will result in an error because 'area' is not accessible here
```


In this example, the area variable is declared within the calculateArea function. It’s only accessible within the function’s scope and cannot be used outside of it. Even though we have another variable named rectangleLength outside the function, they are completely separate entities due to function scope.


### Key Points to Remember about Function Scope:


![javascript functionsfunctions in javascript](https://metana.io/wp-content/uploads/2024/04/joan-gamell-ZS67i1HLllo-unsplash-1-1024x683.jpg)
* Variables declared with let and const have block scope within a function, meaning their accessibility is limited to the code block where they are declared (introduced in ES6).
* Variables declared with var (though discouraged in modern JavaScript due to potential hoisting issues) have function scope, accessible anywhere within the function.
* Function arguments are also considered local variables, accessible only within the function.


By understanding function scope, you can write cleaner and more predictable JavaScript code. It prevents unintended side effects and promotes modularity by keeping variables local to their functions.


Different Types of Functions in JavaScript
------------------------------------------


JavaScript offers a versatile set of function types, each catering to specific use cases:


* **Regular Functions (Function Declarations):** These are the most common type, defined using the function keyword followed by a name, parameters, and a function body. They are hoisted, meaning their declarations are accessible before their definition in the code.



```
// Regular function
function greet(name) {
  return "Hello, " + name + "!";
}

console.log(greet("Bob"));  // Output: Hello, Bob!
```


* **Function Expressions:** As discussed earlier, these functions are assigned to variables, enabling dynamic function creation. They are not hoisted and are only accessible after their assignment.



```
// Function expression
const greetES6 = function(name) {
  return "Hello, " + name + "!";
};

console.log(greetES6("Alice"));  // Output: Hello, Alice!
```


* **Arrow Functions (ES6):** Introduced in ES6 (ECMAScript 2015), arrow functions provide a concise syntax for defining functions. They use arrow (=>) notation and offer implicit return for single-line expressions.



```
// Arrow function
const greetArrow = (name) => "Hello, " + name + "!";

console.log(greetArrow("Charlie"));  // Output: Hello, Charlie!
```


* **Generator Functions (ES6):** These functions, also introduced in ES6, allow for the creation of iterators. They can pause execution and yield values one at a time using the yield keyword. This is useful for creating infinite sequences or working with large datasets.



```
// Generator function
function* fibonacciSequence() {
  let a = 0, b = 1;
  while (true) {
    yield a;
    const temp = a;
    a = b;
    b = temp + b;
  }
}

const fibonacciGen = fibonacciSequence();

console.log(fibonacciGen.next().value); // Output: 0
console.log(fibonacciGen.next().value); // Output: 1
console.log(fibonacciGen.next().value); // Output: 1
console.log(fibonacciGen.next().value); // Output: 2
// You can continue iterating to get more Fibonacci numbers
```


* **Async/Await Functions (ES7):** Async/await (introduced in ES7 or ECMAScript 2017) further enhance asynchronous programming. Async functions simplify the handling of Promises by using async and await keywords. They make asynchronous code appear more synchronous, improving readability.



```
// Async/Await functions
async function fetchData(url) {
  const response = await fetch(url);
  const data = await response.json();
  return data;
}

async function main() {
  try {
    const userData = await fetchData("https://api.example.com/users/1");
    console.log(userData); // Output: User data object
  } catch (error) {
    console.error(error);
  }
}

main();
```


Function Parameters
-------------------


Function parameters act as channels for communication between the calling code and the function. They provide a way to customize the function’s behavior based on the provided data. Here are some key points about parameters:


* **Optional Parameters:** Functions can have optional parameters that have default values assigned. If no argument is provided during the call, the default value is used.



```
function greet(name = "World") {
  console.log("Hello, " + name + "!");
}

greet(); // Output: Hello, World!
greet("Bob"); // Output: Hello, Bob!
```


* **Rest Parameters (ES6):** Introduced in ES6, the rest parameter (…) allows capturing an indefinite number of arguments into an array. This is useful for functions that can handle a variable number of inputs.



```
function sum(...numbers) {
  let total = 0;
  for (const num of numbers) {
    total += num;
  }
  return total;
}

console.log(sum(1, 2, 3)); // Output: 6
console.log(sum(4, 5, 6, 7)); // Output: 22
```


### Returning Values in Functions


The return statement is used to send data back from a function to the calling code. The returned value can be any valid JavaScript expression, including variables, function calls, or objects. If no return statement is present, the function implicitly returns undefined.



```
function multiply(a, b) {
  return a * b;
}

const result = multiply(5, 3);
console.log(result); // Output: 15
```


In this example, the multiply function returns the product of a and b, which is then stored in the result variable.


### First-Class Functions


A powerful aspect of JavaScript is that functions are first-class objects. This means they can be:


* **Assigned to variables:** As seen with function expressions.
* **Passed as arguments to other functions:** Functions can be arguments to other functions, allowing for higher-order functions that operate on other functions.



```
function greetWithPrefix(prefix, greetFunction) {
  return greetFunction(prefix);
}

function greetMorning(name) {
  return "Good morning, " + name + "!";
}

const morningGreeting = greetWithPrefix("Good morning, ", greetMorning);
console.log(morningGreeting("Alice")); // Output: Good morning, Alice!
```


* **Returned from other functions:** Functions can return other functions, enabling the creation of closures (discussed later).


Function Closures
-----------------


Closures are a fundamental concept in JavaScript that leverage the combination of function scope and first-class functions. A closure is a function that has access to the variable environment of its outer (enclosing) function, even after the outer function has returned. This allows the inner function to “remember” and access variables from the outer function’s scope, even when the outer function is no longer executing.


Here’s an example of closures:



```
function createGreeter(greeting) {
  return function(name) {
    return greeting + ", " + name + "!";
  };
}

const morningGreeter = createGreeter("Good morning");
const eveningGreeter = createGreeter("Good evening");

console.log(morningGreeter("Bob")); // Output: Good morning, Bob!
console.log(eveningGreeter("Alice")); // Output: Good evening, Alice!
```


In this example, the createGreeter function takes a greeting string as input and returns a new function. This inner function has access to the greeting variable even though createGreeter has already finished executing. This is because the inner function forms a closure around the greeting variable, preserving its value for later use.


### Closures offer numerous advantages:


* **Data privacy:** By encapsulating variables within closures, you can protect them from modification by the outer scope, promoting data privacy and preventing unintended side effects.
* **State management:** Closures can be used to create private state within functions, enabling the creation of functions that “remember” their state across multiple calls.
* **Module creation:** Closures play a crucial role in creating modules in JavaScript, which encapsulate functionality and variables, promoting code organization and reusability.


### Recursive Functions


Recursion is a technique where a function calls itself within its body. This allows for the repetitive execution of a task until a base case is reached. Recursion can be powerful for solving problems that involve breaking down a larger problem into smaller, similar subproblems.


Here’s a recursive function to calculate the factorial of a number:



```
function factorial(n) {
  if (n === 0) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

console.log(factorial(5)); // Output: 120
```


In this example, the factorial function calls itself with n – 1 until it reaches the base case of n === 0, where the factorial is 1. Each recursive call multiplies the current n with the result of the previous recursive call, accumulating the final factorial value.


However, it’s essential to be cautious with recursion as excessive recursion can lead to stack overflow errors. Make sure your recursive functions have a well-defined base case to prevent infinite loops.


### Best Practices for Effective Use of Functions


Here are some best practices for writing clean, maintainable, and efficient JavaScript functions:


* **Meaningful Names:** Choose descriptive names for functions that clearly convey their purpose.
* **Modularity:** Break down complex logic into smaller, well-defined functions promoting code reusability and readability.
* **Default Parameters:** Use default parameters to provide sensible fallback values for optional parameters.
* **Documentation:** Document your functions with comments explaining their purpose, parameters, and return values.
* **Error Handling:** Implement proper error handling mechanisms within functions to gracefully handle unexpected inputs or situations.
* **Testing:** Write unit tests for your functions to ensure their correctness and reliability.


By following these practices, you can leverage the power of functions to write well-structured, maintainable, and scalable JavaScript code.


Conclusion
----------


Functions are the building blocks of well-written JavaScript code. They encapsulate logic, promote reusability, and enable modular programming. Understanding different function types, scope rules, closures, and recursion will equip you to tackle complex programming challenges effectively. Embrace functions, follow best practices, and watch your JavaScript code evolve into a masterpiece of clarity and efficiency.



![faq](https://metana.io/wp-content/uploads/2024/01/Questions-cuate-1024x1024.png)
FAQs
----


**What are JavaScript functions?**


* JavaScript functions are blocks of code designed to perform a particular task and can be reused throughout your scripts.


**How do you create a JavaScript function?**


* Create a JavaScript function using the function keyword followed by a name, parentheses, and curly brackets enclosing the code to execute.


**What are the different types of JavaScript functions?**


* There are several types including named functions, anonymous functions, arrow functions, and immediately invoked function expressions (IIFE).


**Why are functions important in JavaScript?**


* Functions are crucial for writing clean, maintainable, and reusable code, allowing for the modularization of tasks.


**How do parameters and arguments work in JavaScript functions?**


* Parameters are named variables in a function’s declaration. When a function is called, it receives values known as arguments that replace these parameters.


**What is the role of JavaScript in web development?**


* JavaScript is essential for creating dynamic and interactive effects on web pages, including responsive forms and live content updates.


**How can I learn JavaScript effectively?**


* Start with basics, practice coding regularly, use online resources, and build projects to apply your knowledge practically.


**What are some best practices for using JavaScript functions?**


* Use clear naming, keep functions focused on a single task, and avoid global variables to maintain clean and efficient code.


**How do arrow functions differ from traditional functions?**


* Arrow functions offer a shorter syntax and do not have their own ‘this’ context, unlike traditional functions.


**What are closures in JavaScript?**


* Closures are a feature where an inner function has access to the outer (enclosing) function’s variables and scope chain even after the outer function has finished executing.






![](https://metana.io/wp-content/uploads/2024/04/Functions-in-JavaScript.jpg) 





[PrevPreviousJavaScript Variables](https://metana.io/blog/javascript-variables/) 




[NextSmart Contract Auditing: Essential Guide for Blockchain SecurityNext](https://metana.io/blog/smart-contract-auditing-essential-guide-for-blockchain-security/) 







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




12 mins ago

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






