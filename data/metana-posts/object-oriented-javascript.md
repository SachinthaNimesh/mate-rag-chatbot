



Object Oriented JavaScript - Metana


















































































 












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





 







Object Oriented JavaScript
==========================

 



 * [Metana Editorial](https://metana.io/blog/author/editorial/)
* [April 26, 2024](https://metana.io/blog/2024/04/26/)
* [Full-Stack](https://metana.io/blog/category/full-stack/)














JavaScript (JS), the popular language of web development, has a unique relationship with object-oriented programming (OOP). In contrast to class-based languages like Java or C++, JavaScript leverages a prototype-based inheritance model. This article will explain everything about **Object-Oriented JavaScript**, exploring core concepts, practical applications, and best practices.


What is OOP?
------------


**Object-oriented programming** is a model for software development centered around objects. These objects encapsulate data (properties) and the actions they can perform (methods). Imagine a car: its properties include color, model, and horsepower, while its methods include driving, braking, and turning. Objects interact with each other through method calls, fostering modularity and code reusability.


Here’s a breakdown of key OOP concepts relevant to JS:


* **Objects:** Fundamental entities that hold properties and methods. Objects are created using object literals ({}) or constructor functions.
* **Classes (ECMAScript 2015+):** Blueprints that define the properties and methods shared by objects of a particular type. Classes offer a more concise way to write code that achieves the same results as the underlying prototype-based system.
* **Properties:** Data attributes associated with an object. They represent the object’s characteristics.
* **Methods:** Functions attached to objects that define their behavior. Methods operate on the object’s data.
* **Inheritance:** Mechanism for creating new objects (subclasses) that inherit properties and methods from existing objects (superclasses). This promotes code reuse and simplifies complex hierarchies.
* **Encapsulation:** Practice of bundling data and methods together within an object, potentially restricting direct access to internal properties. This promotes data integrity and controlled modification.
* **Polymorphism:** Ability of objects of different classes to respond to the same method call in distinct ways. This allows for flexible and dynamic interactions.


While JavaScript doesn’t strictly adhere to class-based OOP, it achieves similar functionality through prototypes.



![](https://metana.io/wp-content/uploads/2024/04/markus-spiske-jG8nlwLRZTM-unsplash-1.jpg)
**Prototypes**
--------------


In JS, objects are linked together through a prototype chain. Each object has an internal hidden property called `[[Prototype]]` (prototype) that points to another object. This prototype object serves as a blueprint, containing properties and methods that the original object inherits. When a property or method is accessed on an object, JS first searches within the object itself. If not found, it traverses the prototype chain, looking for the property or method in the prototype object and any further prototypes in the chain.


Here’s a simplified example:



```
function Person(name, age) {
  this.name = name;
  this.age = age;
}

Person.prototype.greet = function() {
  console.log("Hello, my name is " + this.name);
};

const person1 = new Person("Alice", 30);
person1.greet(); // Outputs: "Hello, my name is Alice"
```

In this example, `Person` is a constructor function that creates `Person` objects. The `greet` method is defined on the `Person.prototype` object, making it accessible to all `Person` instances like `person1`.


Classes in JavaScript
---------------------


ECMAScript 2015 (ES6) introduced the `class` keyword, providing a more familiar syntax for those accustomed to class-based OOP. While classes in JavaScript offer a convenient way to write code, it’s essential to understand that they ultimately translate to prototype-based inheritance. Under the hood, they still make use of the prototype chain.


Here’s the previous example rewritten using a class:



```
class Person {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }

  greet() {
    console.log("Hello, my name is " + this.name);
  }
}

const person1 = new Person("Alice", 30);
person1.greet(); // Outputs: "Hello, my name is Alice"
```

Both approaches achieve the same result. Classes offer a cleaner syntax for defining object properties and methods, making code more readable and maintainable, especially for developers coming from class-based languages.


Inheritance
-----------


Inheritance allows you to create new object types (subclasses) that inherit properties and methods from existing object types (superclasses). This promotes code reuse and simplifies the creation of object hierarchies.


Here’s how inheritance works in JS:



```
class Person {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }
}

class Employee extends Person {
  constructor(name, age, salary) {
    super(name, age); // Call superclass constructor
    this.salary = salary;
  }
}

// Usage
const employee1 = new Employee("Bob", 30, 50000);
console.log(employee1.name, employee1.age, employee1.salary); // Outputs: "Bob 30 50000"
```

This code snippet demonstrates inheritance in JS. Let’s break it down:


1. **Person Class:** This class defines the basic properties (`name` and `age`) for all `Person` objects.
2. **Employee Class:** This class inherits from the `Person` class using the `extends` keyword. It adds a new property `(salary)` specific to employees.
3. **Employee Constructor:** The `Employee` constructor calls the `super` constructor (`super(name, age))` to initialize the inherited properties from `Person`. Then, it assigns the `salary` property.


Now, you can create `Employee` objects that inherit properties from `Person` (like `name` and `age`) and add their own property `(salary)`.


Encapsulation
-------------


Encapsulation refers to the practice of bundling data (properties) and methods together within an object, potentially restricting direct access to internal properties. Imagine an object in your code as a box. This box holds both the data (like a value) and the instructions for working with that data (like methods). Encapsulation is like putting a lock on that box. You can still access the data and use the instructions, but you can’t directly mess with the inner workings. This promotes data integrity and controlled modification.


JS doesn’t have strict mechanisms for enforcing encapsulation like private properties in other languages. However, there are conventions to achieve a similar effect:


1. **Variable Naming:** Use private member variables by prefixing them with an underscore (\_). This discourages direct modification from outside the object.
2. **Getter and Setter Methods:** Define methods to access and modify private properties. These methods can perform validation or additional logic before retrieving or setting the value.


Here’s an example:



```
class Car {
  constructor(model) {
    this._model = model; // Private property
  }

  get model() {
    return this._model;
  }

  set model(newModel) {
    if (newModel.length < 3) {
      throw new Error("Model name must be at least 3 characters long");
    }
    this._model = newModel;
  }
}

const car1 = new Car("Camaro");
console.log(car1.model); // Outputs: "Camaro"

// Attempting to directly modify _model throws an error
car1._model = "Short"; // throws Error
```

In this example, the `_model` property is private. The `model` getter and setter methods provide controlled access and validation for the model name.


Polymorphism
------------


Polymorphism allows objects of different classes to respond to the same method call in distinct ways. Imagine you’re a spy and you have a special device that lets you disguise yourself. When someone calls out “Show your ID,” you might respond with your agent ID if you’re undercover as a government official, or with your student ID if you’re posing as a college student.


Polymorphism in JS works similarly. It allows objects of different classes to respond to the same method call in different ways, depending on their type. This is like the spy’s device – the same “show ID” call gets a different response based on the object’s disguise (its class). This enables flexible and dynamic interactions.


Here’s a demonstration using function overriding:



```
class Animal {
  makeSound() {
    console.log("Generic animal sound");
  }
}

class Dog extends Animal {
  makeSound() {
    console.log("Woof!");
  }
}

class Cat extends Animal {
  makeSound() {
    console.log("Meow!");
  }
}

const animal1 = new Dog();
const animal2 = new Cat();

animal1.makeSound(); // Outputs: "Woof!"
animal2.makeSound(); // Outputs: "Meow!"
```

In this example, the `makeSound` method is polymorphic. It’s defined in the base `Animal` class, but overridden in the `Dog` and `Cat` subclasses to produce their specific sounds. This demonstrates how polymorphism allows for a single method call to trigger different behaviors based on the object’s type.


Building Real-World Applications
--------------------------------


Object-oriented principles empower you to structure complex applications in JS. Here’s an example of a simple e-commerce application using these concepts:



```
class Product {
  constructor(name, price, quantity) {
    this.name = name;
    this.price = price;
    this.quantity = quantity;
  }

  calculateTotal() {
    return this.price * this.quantity;
  }
}

class Cart {
  constructor(items = []) {
    this.items = items;
  }

  addItem(product) {
    this.items.push(product);
  }

  removeItem(product) {
    const index = this.items.findIndex(item => item === product);
    if (index > -1) {
    this.items.splice(index, 1);
}
}

getTotalCost() {
let total = 0;
for (const item of this.items) {
total += item.calculateTotal();
}
return total;
}
}

const product1 = new Product("T-Shirt", 20, 2);
const product2 = new Product("Jeans", 50, 1);

const cart = new Cart();
cart.addItem(product1);
cart.addItem(product2);

console.log(cart.getTotalCost()); // Outputs: 90 (20 * 2 + 50 * 1)

cart.removeItem(product2);
console.log(cart.getTotalCost()); // Outputs: 40 (20 * 2)
```

This example demonstrates:


* **Product Class:** Represents a product with properties like name, price, and quantity. It includes a calculateTotal method.
* **Cart Class:** Manages a collection of products. It provides methods to add, remove, and calculate the total cost of items in the cart.


This is a simplified example, but it showcases how objects can encapsulate data and functionalities relevant to specific entities in your application.


### Best Practices for Effective OOP in JavaScript


Here are some best practices to keep in mind when using OOP in JavaScript:


* **Favor Composition over Inheritance:** While inheritance can be useful, relying heavily on it can lead to complex hierarchies and tight coupling. Consider using composition, where objects delegate tasks to other objects, to achieve code reusability and maintainability.
* **Use Classes Judiciously (ES6+):** While classes offer cleaner syntax, remember that JS functions as a prototype-based language at its core. Don’t overuse classes if simpler object literals or functions suffice.
* **Focus on Object Responsibility:** Each object should have a clear and well-defined purpose. Avoid creating “god objects” that handle too much logic.
* **Document Your Code:** Use comments to explain the purpose of classes, methods, and properties. This enhances code readability and maintainability for yourself and others.
* **Test Your Code:** Write unit tests to ensure your objects behave as expected. This helps catch bugs early in the development process.


By following these best practices, you can make use of the power of OOP to write cleaner, more maintainable, and scalable JavaScript applications.


Conclusion
----------


Object-Oriented JavaScript offers a powerful approach to structuring complex applications. While it differs from class-based languages, understanding prototypes and effectively applying OOP principles can significantly improve your code organization, reusability, and maintainability. This guide has equipped you with the fundamental concepts, practical applications, and best practices to begin your journey with OOP in JavaScript.


Wanna Learn more about JavaScript? Check our articles on JavaScript 👇


* [How JavaScript Works?](https://metana.io/blog/how-javascript-works-all-you-need-to-know/?swcfpc=1)
* [JavaScript Varialbles](https://metana.io/blog/javascript-variables/?swcfpc=1)
* [JavaScript Operators](https://metana.io/blog/javascript-operators/?swcfpc=1)
* [JavaScript Functions](https://metana.io/blog/functions-in-javascript-functions/?swcfpc=1)
* [JavaScript Arrays](https://metana.io/blog/javascript-arrays/?swcfpc=1)
* [JavaScript Control Structures](https://metana.io/blog/javascript-control-structures/)



![faq](https://metana.io/wp-content/uploads/2024/01/Questions-cuate-1024x1024.png)
FAQs
----


**What is Object Oriented JavaScript**


* Object Oriented JavaScript (OOP) is a programming paradigm that uses objects and classes to create more reusable and modular code.


**How does inheritance work in [JavaScript](https://metana.io/blog/how-javascript-works-all-you-need-to-know/)?**


* In JavaScript, inheritance allows objects to inherit properties and methods from other objects, typically using prototypes or the class syntax introduced in ES6.


**What are the benefits of using OOP in JavaScript?**


* Using OOP in JavaScript enhances code reusability, simplifies debugging, and improves project scalability.


**Can you explain polymorphism in JavaScript?**


* Polymorphism in JavaScript involves using the same interface for different data types. Methods can be overwritten or objects can be handled differently based on their data type or structure.


**What is the role of constructors in JavaScript classes?**


* Constructors in JavaScript classes initialize new objects. They set up properties and bind methods, preparing the object for use.


**What are the core principles of Object Oriented Programming?**


* The core principles include encapsulation, inheritance, and polymorphism, all aimed at creating more efficient and manageable code.


**How can I improve my JavaScript coding skills?**


* Practice consistently, study various JavaScript projects, and participate in coding communities or forums to learn from experienced developers.


**What tools are available for debugging JavaScript?**


* Tools like Chrome DevTools, Firefox Developer Edition, and Visual Studio Code offer powerful debugging features for JavaScript.


**Are there any popular frameworks that support OOP in JavaScript?**


* Frameworks like Angular, React, and Vue.js support OOP practices, though they implement them in different ways based on their architecture.


**What is the future of JavaScript development?**


* The future looks robust with the ongoing evolution of ECMAScript standards, more sophisticated frameworks, and improved support for modern web development techniques.






![](https://metana.io/wp-content/uploads/2024/04/Object-Oriented-JavaScript.jpg) 





[PrevPreviousJavaScript Control Structures](https://metana.io/blog/javascript-control-structures/) 




[NextThe Rise of Layer 2 SolutionsNext](https://metana.io/blog/the-rise-of-layer-2-solutions/) 







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




23 hours ago

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






