###### Dom
- Node List vs HTML Collection
- document.getElementById()
- document.getElementsByClassName()
- document.getElementsByTagName()doc
- document.querySelector()
- document.querySelectorAll()

###### Browser
- User Interface (UI):Address bar, Back/Forward buttons, Tabs, Bookmarks, Search bar, Status bar, Scroll bar, Zoom
- Browser Engine
    WebKit(safari, initially chrome),
    Blink(Chrome, Edge),
    Gecko(Firefox),
    Trident(IE),
    EdgeHTML(now blink)
    - DOM Handling: Managing the structure of the webpage for JavaScript interaction.   
    - JavaScript Execution: (Often handled by a separate engine within the browser engine)
    - Security: Enforcing security policies.
    - Resource Loading: Fetching images, scripts, stylesheets. 
    - Rendering: (A key part, but not the only one)
    - Navigation: Handling navigation events.

- JS Engine
- Rendering Engine: The rendering engine is a crucial component within the broader browser engine.
- Data storage
- Networking
- Security(Cors, CSP)
- DevTools
- BOM : Browser Object Model
- DOM

Api - JS to access any component of the browser
document - enables the interaction/programming with the webpage in response to the user actions!
#document = root of the DOM
1. Read an element: document.querySelector('<selector>') - returns the first element that matches the selector; selector - id, class, tag, attribute, psuedo class, pseudo element, nth child, nth last child!
    1. document.getElementById('<id>')
    2. document.getElementsByClassName('<class>')
    3. document.getElementsByTagName('<tag>')
    4. document.querySelector('<selector>') - returns the first element that matches the selector
    5. document.querySelectorAll('<selector>') - Nodelist of the matched selectors
2. Create an element: document.createElement('<element>')
3. Append an element: document.appendChild(element)
4. Remove an element: document.removeChild(element)



##### Properties
- innerHTML : returns the inner HTML of the element
- innerText : returns the inner text of the element
- textContent : returns the text content of the element
- outerText