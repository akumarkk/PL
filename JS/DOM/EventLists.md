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