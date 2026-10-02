# Basic Browser Extensions

It's fun and easy to make little browser extensions. There are two basic ways extensions work: 1) load a script that runs in the background of pages, 2) have a little icon that brings up an interface. These can also be combined.

In both cases, you'll need to create a folder to house your extension containing a `manifest.json` file, which contains info about the extension.

The most minimal manifest file looks like this:

```json
{
  "manifest_version": 3,
  "name": "Example Name",
  "version": "1.0"
}
```

There are many fields you can add to change the way your extension works.

## Background Scripts

To make something that runs a script (also called a "content script") in the background, make a manifest file that looks like this:

```json
{
  "manifest_version": 3,
  "name": "Example Name",
  "description": "Example description",
  "version": "1.0",
  "content_scripts": [
    {
      "matches": ["<all_urls>"],
      "js": ["main.js"],
      "run_at": "document_idle",
      "world": "MAIN"
    }
  ],
  "icons": {
    "500": "logo.png"
  }
}
```

The important fields here are:

`matches`: an array of of urls where the extension should run. This could just be a single url, a list or urls, or the special keyword `<all_urls>` which menas the extension will run on all pages. If you want a specific set of pages, just make a list with a `*` at the end of the url, something like: `["https://google.com/*", "https://nytimes.com/*"]`

`js`: indicates a javascript file that should run. It can also be a list of javascript files.

`css`: a list of css files to load (optional)

`run_at`: when your script should run. Can be `document_idle` (after the page finishes loaded), `document_start` (when the document starts to load), `document_end` (when the document almost finishes loading).

`world`: can be `MAIN` or `ISOLATED`. You want `MAIN` to run the script in the same context as the page being loaded.

`icons`: a list of icon files for your extension.

If for example we want to make an alert appear on every page, and also make the background color of pages red, you could put this in `main.js`:

```javascript
alert("hi!");
document.querySelector("body").style.backgroundColor = "red";
```

## Extensions with Interfaces

If you want your extension to have a little interface popup, add an `action` field to your manifest.

```json
{
  "manifest_version": 3,
  "name": "Popup example",
  "version": "1.0",
  "action": {
    "default_popup": "popup.html"
  }
}
```

This will load `popup.html` when a user clicks your extensions icon in the toolbar.

## Basic HTML Manipulation

You can use javascript to easily manipulate the content or style of a website.

Every element on the page can be represented as a javascript object whose properties can then by modified.

The two basic ways of manipulating elements are `document.querySelector()` and `document.querySelectorAll()`.

`document.querySelector()` takes as an argument the css selector of an element and returns an object. If multiple elements are found, it returns the first one. For example, to grab the body of a page as an object:

```javascript
const el = document.querySelector("body");

// change a css property
el.style.backgroundColor = "red";

// change the text content
el.textContent = "the page is now gone";

// change the html content
el.innerHTML = "<h1>Hi!</h1><p>hiiiii</p>";
```

`document.querySelectorAll` works the same way but returns a list of objects. For example, to get every link on a page:

```javascript
const els = document.querySelectorAll("a");

for (let el of els) {
  el.style.fontSize = "100px";
  el.textContent = "CLICK ME";
}
```

## Service Workers

Some browser extension functionality, like manipulating tabs, can't be called from a content script. Instead you need another javascript file that will run in a seperate process, called a "service worker". Your content script can interact with the service worker.

Some things you can do with a service worker include:

- injecting javascript into pages
- list, create, and remove tabs
- send and intercept network requests
- get, set and remove cookies
