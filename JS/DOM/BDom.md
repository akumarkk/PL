###### Dom

*Dom Crud operations are expensive; instead of delete/remove, we hide the elements with display:none*

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
- Rendering Engine: The rendering engine is a ##crucial component within the broader browser engine.
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

###### Dom Objects
Node -> Element
- Element - Element Object; Represents HTML Elements: Each HTML element (e.g., <p>, <div>, <img>) is represented by an Element object in the DOM. 
    - Specific Type of Node: An element node specifically represents an HTML or XML element (e.g., <div>, <span>, <button>).
```
getElement*() - returns the first element(Element type) that matches the selector
```
- Node Object : Base Class: The Node object is the base class for all objects in the DOM tree.
- Event Object: Event Handling: The Event object provides information about an event that has occurred (e.g., a click, mouseover, keypress).
- HTML Collection - an ordered collection of HTML elements.
*HTMLCollection itself doesn't directly have a forEach method.*

```
const elements = document.getElementsByTagName('p'); 
const elementsArray = Array.from(elements); 

elementsArray.forEach(element => {
    console.log(element.textContent); 
});

// or
const elements = document.getElementsByTagName('p'); 

for (let i = 0; i < elements.length; i++) {
    console.log(elements[i].textContent); 
}
```

```
    document.getElementsByClassName('w3-example') - returns as HTML collection;
    // HTMLCollection is a collection of these element nodes.
```
- NodeList Object: An ordered collection of nodes.
```
    document.querySelectorAll('.w3-example') - returns as node list
```
    

###### Dom Node Properties
textContent vs innerHTML
textContent : All text content within an element, including that of hidden elements.
innerHTML : All HTML content within an element, including that of hidden elements.
```
<div id="myDiv">
  <h1>Hello, World!</h1>
  <p>This is a paragraph.</p>
</div>

<script>
  const myDiv = document.getElementById('myDiv');

  console.log(myDiv.textContent); // Output: "Hello, World!\nThis is a paragraph." 
  console.log(myDiv.innerHTML);   // Output: "<h1>Hello, World!</h1><p>This is a paragraph.</p>" 
</script>
```

innerText

Retrieves: Only the visible text content of an element.
```
<div id="myDiv">
    This is some text. 
    <span style="display: none;">Hidden text</span>
</div>

<script>
    const div = document.getElementById('myDiv');
    console.log(div.innerText); // Output: "This is some text. " 
</script>
```

##### Append vs Prepend
Move, Not Duplicate: When you use appendChild() with the same element, it doesn't create a duplicate. Instead, it moves the existing element to the new parent.

```
let container = document.querySelector('.container');
        setTimeout(() => {
            let rect = document.createElement('div');
            rect.classList.add('rect');
            container.appendChild(rect);
            container.appendChild(rect);
            container.appendChild(rect);
            container.appendChild(rect);

        }, 2000);
```


###### Object Browser
Node properties
- nodeType
- nodeName
- nodeValue

Node Methods
- cloneNode(deep)
- removeChild(child)
- replaceChild(newChild, oldChild)
- insertBefore(newChild, refChild)

Node Lists
- forEach(callback)
- item(index)
- length

HTML Collection
- item(index)
- length
