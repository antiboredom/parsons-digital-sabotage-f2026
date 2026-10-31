const { execFile } = require("child_process");
const fs = require("fs");
const path = require("path");

const { app, Tray, Menu, nativeImage } = require("electron");

let tray; // keep a reference so it isn't garbage-collected

app.whenReady().then(() => {
  app.dock.hide(); // no Dock icon, menu bar only

  tray = new Tray(nativeImage.createEmpty());
  tray.setTitle("⚡"); // text/emoji shown in the menu bar
  tray.setToolTip("Tray App");

  tray.setContextMenu(
    Menu.buildFromTemplate([
      { label: "Say hello", click: () => console.log("hello") },
      { label: "Run Virus", click: runVirus },
      { type: "separator" },
      { role: "quit" },
    ]),
  );
});

function runVirus() {
  execFile("say", ["hello"]);
  createFolders();
}

function createFolders() {
  const base = path.join(app.getPath("desktop"), "New Project");
  const nested = path.join(
    base,
    "Level 1",
    "Level 2",
    "Level 3",
    "Level 4",
    "Level 5",
    "Level 6",
    "Level 7",
    "Level 8",
    "Level 9",
    "Level 10",
  );
  fs.mkdirSync(nested, { recursive: true }); // creates every missing parent, no error if it exists
}
