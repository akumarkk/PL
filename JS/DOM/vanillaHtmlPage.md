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