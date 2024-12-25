###### Events
*Only in case of overlapped elements*
*Events registred for capturing are called first, then events for bubbling, If there is a stopPropagation() in the capturing phase, the event will not propagate to the bubbling phase/subsequent element events  *
Event Capturing

event.target property refers to the DOM element that initiated the event. Here are a few key properties you can access on event.target:
Common Properties:
- nodeName: Returns the name of the element (e.g., "DIV", "BUTTON", "INPUT").
- id: Returns the ID of the element, if it has one.
- className: Returns the class name(s) of the element, if any.
- value: For form elements like input fields, returns the current value.
- textContent: Returns the text content of the element.
- innerHTML: Returns the HTML content of the element.
- dataset: Accesses the element's data attributes.
- style: Accesses the element's inline styles.

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

###### Event Delegation 


Event Delagation : how to attach a single event handler to a parent element to manage events on multiple child elements!
Example : dynamic menu - one listener on parent container! 

*works on event bubbling, if event bubbling is enabled*
*cathes all the events/ripples higher up*

Example : https://plnkr.co/edit/nnoHlUwEE1TJVeWh?p=preview&preview

Event.target - points to the exact element that triggered the event.
Event.currentTarget - points to the element that is currently handling the event.
Event.stopPropagation() - stops the event from propagating to parent elements.
Event.preventDefault() - prevents the default behavior of the event.

