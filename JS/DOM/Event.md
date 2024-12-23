###### Events
Event Capturing

Concept:
Event capturing is one of the two phases of event propagation in the DOM (Document Object Model). In this phase, an event "trickles down" from the outermost element (e.g., document or window) to the target element where the event originated.
This allows ancestor elements to "intercept" an event before it reaches the target element.

How it Works:
- When an event occurs (e.g., a click), the browser starts at the top of the DOM tree.
- It checks each ancestor element in the tree to see if it has an event listener for that specific event.
- If an ancestor has a listener, the event is handled by that ancestor.
- This process continues down the tree until the event reaches the target element.

Enabling Event Capturing:
You can enable event capturing by setting the third argument of the addEventListener() method to true:
```
JavaScript

element.addEventListener('click', function() { 
    // Event handler code
}, true); 
```

Use Cases:
- Intercepting events: You can prevent events from reaching the target element by handling them in an ancestor during the capturing phase.
- Global event handling: You can attach event listeners to higher-level elements (like document) to handle events for a broader range of elements.

Key Points:

- Event capturing is less commonly used than event bubbling.
- Event capturing can improve performance in some cases by preventing unnecessary event handling at the target level.
- It's important to understand how event capturing works to avoid unexpected behavior in your web applications.