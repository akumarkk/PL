###### Fragment
The document.createDocumentFragment() method creates an empty DocumentFragment object.
```
const fragment = document.createDocumentFragment();

li.forEach((l) => {
    fragment.appendChild(l);
});

lu.appendChild(fragment);
```

Key difference: Instead of updating DOM 1000 times, we:

Create a lightweight container (fragment)
- Add all elements to fragment first
- Update DOM just once by appending fragment
- Think of fragment like a temporary shopping cart - you collect all items first, then checkout once, rather than checking out each item separately.