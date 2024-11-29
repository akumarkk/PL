###### mjs modules package

{
  "name": "my-package",
  "version": "1.0.0",
  "type": "module",
  "exports": {
    ".": "./index.mjs",
    "./lib": "./lib/index.mjs"
  }
}

- type field: Set this to module to indicate that your package uses ECMAScript modules.
- exports field: Use this field to define the entry points for your package. You can specify different entry points for different environments or use conditional exports to target specific Node.js versions.

my-package/
  package.json
  index.mjs
  lib/
    index.mjs
    utils.mjs

- import myPackage from "my-package"
This will import the index.mjs file from the root directory.
- import {p} from 'my-package/lib'
This will import the someFunction from the index.mjs file within the lib directory.