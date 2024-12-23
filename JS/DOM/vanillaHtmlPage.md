###### Vanilla Html
Reflow
The process of recalculating the size and position of all elements in the document (or a portion of it). This happens whenever anything on the page changes that might affect the layout, such as:

- Adding or removing elements from the DOM
- Resizing the browser window
- Changing font sizes, margins, or padding
- Applying CSS styles that affect layout (e.g., width, height, display, float)
Most expensive operation: Reflows can be computationally expensive, especially on complex pages with many elements.

Repaint
Definition: The process of redrawing the affected parts of the page to reflect changes in visual appearance that don't affect the layout. This happens when:

- Changing colors, background images, or visibility of elements
- Applying CSS styles that only affect appearance (e.g., color, background-color, opacity)

Impact:
Less expensive than reflow: Repaints generally have a lower performance impact than reflows.

###### Virtual DOM for the rescue
Essentially, the virtual DOM provides a mechanism that allows the actual DOM to compute minimal DOM operations when re-rendering the UI.

It allows you to update a view whenever state changes by creating a full representation of the view and then patching the DOM efficiently to look exactly as you described it.

After React creates the new virtual DOM tree, it compares it to the previous snapshot using a diffing algorithm called reconciliation to figure out what changes are necessary.

After the reconciliation process, React uses a renderer library like ReactDOM, which takes the differ information to update the rendered app. This library ensures that the actual DOM only receives and repaints the updated node or nodes.

```
import React, { useState } from 'react';

// Simplified representation of a DOM node (for illustration purposes)
const createElement = (type, props, ...children) => ({
  type,
  props,
  children,
});

// Example: Create a simple virtual DOM for an unordered list
const initialVirtualDOM = createElement('ul', {}, [
  createElement('li', { key: '1' }, 'Item 1'),
  createElement('li', { key: '2' }, 'Item 2'),
  createElement('li', { key: '3' }, 'Item 3'),
]);

function ReconciliationExample() {
  const [items, setItems] = useState([
    { id: 1, name: 'Item 1' },
    { id: 2, name: 'Item 2' },
    { id: 3, name: 'Item 3' },
  ]);
  const [virtualDOM, setVirtualDOM] = useState(initialVirtualDOM);

  const handleReorder = () => {
    // Simulate reordering by shuffling the array
    const shuffledItems = [...items].sort(() => Math.random() - 0.5);
    setItems(shuffledItems);

    // Update the virtual DOM to reflect the new order
    const newVirtualDOM = createElement('ul', {}, shuffledItems.map((item) => (
      createElement('li', { key: item.id }, item.name)
    )));
    setVirtualDOM(newVirtualDOM);
  };

  // Simplified reconciliation logic (for illustration)
  const reconcile = (oldVirtualDOM, newVirtualDOM) => {
    // ... (Actual reconciliation logic would be more complex) 
    // This simplified version only checks for changes in children 
    if (oldVirtualDOM.type !== newVirtualDOM.type) {
      // Handle major changes (e.g., element type changed)
      return newVirtualDOM; 
    }

    const newChildren = [];
    newVirtualDOM.children.forEach((newChild) => {
      const matchingOldChild = oldVirtualDOM.children.find(
        (oldChild) => oldChild.props.key === newChild.props.key
      );
      if (matchingOldChild) {
        // Update existing child
        newChildren.push(reconcile(matchingOldChild, newChild));
      } else {
        // Add new child
        newChildren.push(newChild);
      }
    });

    return {
      ...newVirtualDOM,
      children: newChildren,
    };
  };

  return (
    <div>
      <h1>Reconciliation Example</h1>
      <button onClick={handleReorder}>Reorder Items</button>
      <ul>
        {virtualDOM.children.map((child) => (
          <li key={child.props.key}>{child.children}</li>
        ))}
      </ul>
    </div>
  );
}

export default ReconciliationExample;
```