###### Event List
Click Events

- click: Fired when the mouse button is pressed and released on an element.
- dblclick: Fired when the mouse button is pressed and released twice quickly on an element.
- mousedown: Fired when the mouse button is pressed down on an element.
- mouseup: Fired when the mouse button is released after being pressed down.

Hover Events
- mouseover: Fired when the mouse pointer moves onto an element or one of its child elements.
- mouseout: Fired when the mouse pointer moves off of an element, including its child elements.
- mouseenter: Fired when the mouse pointer enters an element.
- mouseleave: Fired when the mouse pointer leaves an element.

Movement Events
- mousemove: Fired repeatedly as the mouse pointer moves over an element.
- wheel: Fired when the mouse wheel is scrolled.

Context Menu Event
- contextmenu: Fired when the right mouse button is clicked.


##### Keyboard Events
- keydown:
Fired when a key is pressed down.
Fires repeatedly if a key is held down.

- keyup:
Fired when a key is released.

- keypress:
Fired when a character key is pressed and released.
Not fired for all keys (e.g., function keys, arrow keys).

Note: *onkeypress deprecated in favor of more robust alternatives like the onkeydown and onkeyup events.*
Ref : https://www.dhiwise.com/post/onkeypress-deprecated-what-developers-need-to-know

Key Event Properties
- key: Returns the character associated with the key pressed (e.g., "a", "Enter").
- code: Returns a unique identifier for the physical key (e.g., "KeyA", "Enter").
- shiftKey: True if the Shift key was held down.
- ctrlKey: True if the Ctrl key was held down.
- altKey: True if the Alt key was held down.
- metaKey: True if the Meta key (usually Windows or Command key) was held down.

##### Element Events
- Each Element could have own events, custom events, default events

- input:
Fires repeatedly as the user types or modifies the input value. Catches every change, making it suitable for real-time feedback (e.g., live search, input validation).

- change:
Fires when the input loses focus and the value has been modified. Useful for actions that should happen after the user has finished interacting with the input (e.g., form submission).

- focus: Fires when the input element receives focus (e.g., when the user clicks on it).
- blur : Fires when the input element loses focus.
- keydown: Fires when a key is pressed down on the - keyboard (can be used for specific key handling).
- keyup: Fires when a key is released.
```
const inputField = document.getElementById('myInput');

inputField.addEventListener('input', (event) => {
  console.log('Input value changed:', event.target.value);
  // Perform actions based on the input value (e.g., live search, input validation)
});

inputField.addEventListener('change', () => {
  console.log('Input value changed and focus lost.');
  // Perform actions after the input is complete (e.g., submit form)
});
```

###### Form Events
- submit: Fired when a form is submitted.
- reset: Fired when a form is reset.

###### Drag and Drop Events
- dragstart: Fired when a draggable element is being dragged.
- drag: Fired repeatedly while a draggable element is being dragged.
- dragend: Fired when a draggable element is released after being dragged.
- dragenter: Fired when a draggable element enters a drop target.
- dragleave: Fired when a draggable element leaves a drop target.
- dragover: Fired when a draggable element is being dragged over a drop target.
- drop: Fired when a draggable element is dropped on a drop target.

###### Window Events
- resize: Fired when the window is resized.
- scroll: Fired when the window is scrolled.