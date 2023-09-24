# Object Oriented Programming
 Basics of object oriented programming

 * We will go through the basics following a tutorial on Linkdi Learning

 ## NOTES
 In software engineering, the FURPS model is a framework for categorizing and organizing software requirements. FURPS stands for:

1. **Functionality:** This category focuses on the features and capabilities that the software should provide. It includes requirements related to the primary functions of the software, user interactions, and system behavior. In the context of Object-Oriented Programming (OOP), this often translates into defining classes, methods, and objects that encapsulate the required functionality.

2. **Usability:** Usability requirements pertain to how user-friendly and intuitive the software should be. It encompasses aspects like user interfaces, accessibility, and user experience. In OOP, this may involve designing classes and methods that facilitate a user-friendly interaction with the software.

3. **Reliability:** Reliability requirements address the software's ability to perform consistently and correctly. It includes aspects like error handling, fault tolerance, and system stability. In OOP, this might mean creating classes that handle exceptions gracefully or ensuring that critical functionality is robust and dependable.

4. **Performance:** Performance requirements deal with the software's speed, responsiveness, and efficiency. It covers factors like response times, throughput, and resource utilization. In OOP, optimizing algorithms and data structures within classes can help meet performance goals.

5. **Supportability:** Supportability requirements focus on the software's ease of maintenance, manageability, and extensibility. It includes aspects like documentation, modularity, and adaptability. OOP principles, such as encapsulation and abstraction, can facilitate supportability by isolating changes to specific classes and modules.

To apply Object-Oriented Programming principles to address FURPS requirements, you can:

- **Use Classes:** Design classes that encapsulate related functionality and attributes. This supports the modularity and organization required to meet FURPS objectives.

- **Leverage Inheritance:** Inheritance can help in reusing and extending functionality while maintaining consistency. For example, you can create subclasses that inherit features from a base class and add specialized behavior.

- **Encapsulate Data:** Use encapsulation to hide implementation details and protect data integrity. This aligns with reliability and usability requirements by ensuring that data is handled correctly and safely.

- **Implement Interfaces:** Implementing interfaces and defining clear method signatures can enhance usability and supportability. This allows clients to interact with objects in a standardized way.

- **Optimize Algorithms:** In cases where performance is a concern, design efficient algorithms within your classes. Consider data structures and algorithms that meet performance requirements.

- **Document and Comment:** Proper documentation of classes, methods, and code comments supports supportability. It helps developers understand and maintain the software.

Remember that FURPS requirements can vary greatly depending on the specific project and its context. Your application of Object-Oriented Programming should align with the particular FURPS requirements of your software project to ensure that the resulting software meets its goals effectively and efficiently.




 ## PROJECT
 ### Poker Probability

I want to create a Python simulation of the game of poker to investigate if, over a large number of games, the actual probabilities of getting different poker hand combinations are reflected by the frequency of those combinations occurring in the simulation results. This is a common approach in statistics and probability to empirically verify theoretical probabilities through simulation.

Here are the general steps you can follow to implement this project:

1. **Define the Poker Game Rules:**
   - Define the rules of the poker game you want to simulate. This includes details like the deck of cards, the number of players, and the hand ranking (e.g., royal flush, full house, etc.).

2. **Simulate Poker Games:**
   - Write Python code to simulate a large number of poker games. In each game, shuffle the deck, deal cards to players, and evaluate the poker hands for each player.

3. **Keep Track of Hand Combinations:**
   - Maintain counters or data structures to keep track of the number of times each poker hand combination occurs (e.g., how many times a player gets a royal flush, full house, etc.).

4. **Run a Large Number of Simulations:**
   - Run the simulations for a significant number of games (e.g., tens of thousands or more) to get statistically meaningful results.

5. **Analyze and Compare:**
   - Analyze the simulation results to see if the observed frequencies of each poker hand combination match the theoretical probabilities. You can calculate the empirical probabilities based on your simulation data.

6. **Visualize the Results:**
   - Create charts or visualizations to present your findings. This can help illustrate any discrepancies between theoretical and empirical probabilities.

7. **Refine and Experiment:**
   - You can refine your simulation and experiment with different parameters (e.g., number of players, deck variations) to see how they affect the results.

Here's a simplified example of Python code that simulates a single hand of poker:


