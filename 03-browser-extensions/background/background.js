chrome.tabs.onUpdated.addListener(main);

async function main(tabId, info, tab) {
  if (info.status !== "complete") return;

  // list tabs
  const tabs = await chrome.tabs.query({});
  for (const tab of tabs) {
    console.log(tab.id, tab.windowId, tab.title, tab.url);
  }

  // create a tab
  // this makes a new tab every time a tab finishes loading, so uh, be careful
  // chrome.tabs.create({ url: "https://lav.io" });
}
