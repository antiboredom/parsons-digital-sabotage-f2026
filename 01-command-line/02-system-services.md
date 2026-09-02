# System Services

A "system service" is a program that runs in the background of your computer without requiring user interaction.

On a mac, these programs are managed by system called `launchd` which reads configuration files from a few different locations on your computer.

`/Library/LaunchDaemons/` contain scripts that run when your computer boots up (even if no user is logged in)

`/Library/LaunchAgents/` run when any user logs in.

`/Users/YOURNAMEHERE/Library/LaunchAgents/` run when _you_ log in.

Each service has a `.plist` file, meaning "property list", a list of key and value pairs formatted in XML.

Here's a basic one that runs a program on bootup, and keeps it running.

```xml

<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>

  <key>Label</key>
  <string>com.yourname.myservice</string>

  <key>KeepAlive</key>
  <true/>

  <key>RunAtLoad</key>
  <true/>

  <key>ProgramArguments</key>
  <array>
    <string>/full/path/to/your/program</string>
    <!-- <string>--optional-arguments</string> -->
    <!-- <string>--more-optional-arguments</string> -->
  </array>

</dict>
</plist>
```

To add a service, create a file like the one above, then move it to `~/Library/LaunchAgents/yourservice.plist`

To enable it:

```bash
launchctl load ~/Library/LaunchAgents/yourservice.plist
```

To disabled it:

```bash
launchctl unload ~/Library/LaunchAgents/yourservice.plist
```

## Timed Intervals

You can also have a program run at a timed interval. Remove

```xml
<key>KeepAlive</key>
<true/>
```

and replace with:

```xml
<key>StartInterval</key>
<integer>5</integer>
```

(where `5` is a time in seconds)

## Specific Times/Dates

Or, if you want your program to run at specific times, you can use `StartCalendarInterval`:

```xml

<key>StartCalendarInterval</key>
<dict>
  <key>Hour</key>
  <integer>3</integer>
  <key>Minute</key>
  <integer>0</integer>
</dict>
```

(this will run at 3am every day)
