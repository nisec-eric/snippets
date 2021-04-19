
# HOW TO: Spoof Your MAC Address

How to easily spoof your MAC address on macOS, Linux and Windows.

[![](https://www.funkyspacemonkey.com/wp-content/uploads/2019/10/spoof-mac-address-linux-macos-windows-FSMdotCOM.jpg)](https://www.funkyspacemonkey.com/how-to-spoof-your-mac-address/spoof-mac-address-linux-macos-windows-fsmdotcom)

If you’re looking to keep your online identity anonymous, a step in the right direction would be to change the unique MAC address of your computer every time you connect to a network.

**ALSO READ** [A VPN is NOT a Privacy Tool and It Won’t Make You Anonymous](https://www.funkyspacemonkey.com/a-vpn-is-not-a-privacy-tool-and-it-wont-make-you-anonymous) and [An Easier and Faster Way to Spoof the MAC Address of Your Mac](https://www.funkyspacemonkey.com/an-easier-and-faster-way-to-spoof-the-mac-address-of-your-mac)

This is especially useful if you’re constantly on the move and you connect to networks from different locations like cafes and airports.

**What is a MAC address?**

This should go without saying, but just to clarify this from the get-go: a MAC address has NOTHING to do with macOS.

MAC = media access control. A MAC address of a device is a unique identifier assigned to a network interface controller.

A computer for example usually has two unique MAC addresses. One is for Ethernet and the other for Wifi.

When you try to connect to a Wifi, your laptop will broadcast its MAC address as it searches for a wireless network to connect to.

Manufacturers keep lists of MAC addresses of all the devices they’ve built. So buying a laptop with your own credit card will make it possible to link your purchase to a unique MAC address. Unlikely, but possible.

Also if someone wants to track your MAC address, it would be easy to trace your movements because your laptop reveales its location every time it communicates with a wireless network.

> According to Edward Snowden, the US National Security Agency has a system that tracks the movements of mobile devices in a city by monitoring MAC addresses. To avert this practice, Apple has started using random MAC addresses in iOS devices while scanning for networks. Other vendors followed quickly. MAC address randomization during scanning was added in Android starting from version 6.0, Windows 10, and Linux kernel 3.18\. The actual implementations of the MAC address randomization technique vary largely in different devices. Moreover, various flaws and shortcomings in these implementations may allow an attacker to track a device even if its MAC address is changed, for instance its probe requests’ other elements, or their timing. If random MAC addresses are not used, researchers have confirmed that it is possible to link a real identity to a particular wireless MAC address.
> 
> Using wireless access points in SSID-hidden mode (network cloaking), a mobile wireless device may not only disclose its own MAC address when traveling, but even the MAC addresses associated to SSIDs the device has already connected to, if they are configured to send these as part of probe request packets. Alternative modes to prevent this include configuring access points to be either in beacon-broadcasting mode, or probe-response with SSID mode. In these modes, probe requests may be unnecessary, or sent in broadcast mode without disclosing the identity of previously-known networks.

[More info](https://en.wikipedia.org/wiki/MAC_address#Tracking).

**HOW TO SPOOF YOUR MAC ADDRESS ON macOS**

1\. First let’s see what’s your MAC adress. Open up a terminal shell and type:

`ifconfig en1 | grep ether | awk '{print $2}'`

[![](https://www.funkyspacemonkey.com/wp-content/uploads/2019/10/spoof-MAC-address-macos-1-FSMdotCOM.jpg)](https://www.funkyspacemonkey.com/how-to-spoof-your-mac-address/spoof-mac-address-macos-1-fsmdotcom)

**NOTE**: usually _en1_ is Wifi, _en0_ is ethernet. If unsure, run `ifconfig` in the terminal and check which one is active. ( if you’re connected to WiFi, en0 which is ethernet will say “inactive” and viceversa )

2\. Install [Homebrew](https://www.funkyspacemonkey.com/homebrew-starter-guide-missing-package-manager-macos) ( click on homebrew to learn how to install and use it ). If already installed move on.

3\. Install SpoofMAC via Homebrew. In the terminal type `brew install spoof-mac`

[![](https://www.funkyspacemonkey.com/wp-content/uploads/2019/10/spoof-MAC-address-macos-2-FSMdotCOM.jpg)](https://www.funkyspacemonkey.com/how-to-spoof-your-mac-address/spoof-mac-address-macos-2-fsmdotcom)

4\. Once installed type `spoof-mac --help` to learn how to use it.

[![](https://www.funkyspacemonkey.com/wp-content/uploads/2019/10/spoof-MAC-address-macos-3-FSMdotCOM.jpg)](https://www.funkyspacemonkey.com/how-to-spoof-your-mac-address/spoof-mac-address-macos-3-fsmdotcom)

5\. To randomize your MAC address type `sudo spoof-mac randomize en1` or `sudo spoof-mac randomize wi-fi`.

[![](https://www.funkyspacemonkey.com/wp-content/uploads/2019/10/spoof-MAC-address-macos-4-FSMdotCOM.jpg)](https://www.funkyspacemonkey.com/how-to-spoof-your-mac-address/spoof-mac-address-macos-4-fsmdotcom)

**NOTE**: You won’t get any output. You will know that it worked because you will be disconnected from wifi and will have to reconnect. Also you can run the command from the first step and confirm your MAC address changed.

**NOTE**: if you’re running an older version of macOS ( or OS X, whetever you want to call it ) you might need to replace “wi-fi” with “airport”. so `sudo spoof-mac randomize wi-fi` becomes `sudo spoof-mac randomize airport`

6\. You can also set your MAC adress to something specific. To do this type `sudo spoof-mac set 00:00:00:00:00:00 en1` ( replace 00:00:00:00:00:00 to your desired address )

7\. To reset your MAC address you need to type `spoof-mac reset wi-fi` OR just restart your computer. macOS does not store MAC address changes between restarts.

8\. If you want run SpoofMAC at startup run this in terminal:

Download the startup file for launchd
`curl https://raw.githubusercontent.com/feross/SpoofMAC/master/misc/local.macspoof.plist > local.macspoof.plist`

Customize location of `spoof-mac.py` to match your system
`cat local.macspoof.plist | sed "s|/usr/local/bin/spoof-mac.py|`which spoof-mac.py`|" | tee local.macspoof.plist`

Copy file to the OS X launchd folder
`sudo cp local.macspoof.plist /Library/LaunchDaemons`

Set file permissions
`cd /Library/LaunchDaemons`
`sudo chown root:wheel local.macspoof.plist`
`sudo chmod 0644 local.macspoof.plist`

By default, the above will randomize your MAC address on computer startup. You can change the command that gets run at startup by editing the `local.macspoof.plist` file:

`sudo nano /Library/LaunchDaemons/local.macspoof.plist`

**HOW TO SPOOF YOUR MAC ADDRESS ON Linux**

1\. First, you need to figure out what your wireless or ethernet network is named. To do that, in a terminal shell run `ifconfig` or `ip addr`

**NOTE:** if you’re running `ifconfig` and get “command not found” you need to install “net-tools”.

2\. Install ‘macchanger’. The package should be availble in your distro package manager or you can install it via terminal by typing `sudo pacman -S macchanger` OR `sudo apt-get install macchanger` OR equivalent for your distro.

[![](https://www.funkyspacemonkey.com/wp-content/uploads/2019/10/spoof-MAC-address-linux-3-FSMdotCOM.jpg)](https://www.funkyspacemonkey.com/how-to-spoof-your-mac-address/spoof-mac-address-linux-3-fsmdotcom)

3\. Once installed, run macchanger –help to learn how to use it.

[![](https://www.funkyspacemonkey.com/wp-content/uploads/2019/10/spoof-MAC-address-linux-4-FSMdotCOM.jpg)](https://www.funkyspacemonkey.com/how-to-spoof-your-mac-address/spoof-mac-address-linux-4-fsmdotcom)

4\. To show your current MAC address run `macchanger enp0s3 -s`. To assign a new and random MAC address, run `sudo macchanger enp0s3 -r`.

**NOTE**: change ‘enp0s3’ accordingly to reflect your setup.

[![](https://www.funkyspacemonkey.com/wp-content/uploads/2019/10/spoof-MAC-address-linux-5-FSMdotCOM.jpg)](https://www.funkyspacemonkey.com/how-to-spoof-your-mac-address/spoof-mac-address-linux-5-fsmdotcom)

**NOTE**: if you get the following error `[ERROR] Could not change MAC: interface up or insufficient permissions: Device or resource busy` you will have to take your interface down, change address then take it back up like this:

`sudo ifconfig enp0s3 down && sudo macchanger enp0s3 -r && sudo ifconfig enp0s3 up` ( change ‘enp0s3’ accordingly to reflect your setup )

**NOTE**: on some distros, during macchanger installation you will be prompted with the following screen asking you if you’d like to automatically change your MAC address every time your network interface goes online.

[![](https://www.funkyspacemonkey.com/wp-content/uploads/2019/10/spoof-MAC-address-linux-6-FSMdotCOM.jpg)](https://www.funkyspacemonkey.com/how-to-spoof-your-mac-address/spoof-mac-address-linux-6-fsmdotcom)Chooce <Yes> and you’re set. Otherwise you either need to create a script to run it at startup or a bash alias.  Your MAC address will reset to factory on each reboot.

**HOW TO SPOOF YOUR MAC ADDRESS ON Windows**

Most network cards allow you to set a custom MAC address from the config panes in Device Manager.

1.  Open Device Manager and under “Network adapters” right click on the network interface that you want to modify, and select properties.

[![](https://www.funkyspacemonkey.com/wp-content/uploads/2019/10/spoof-MAC-address-windows-1-FSMdotCOM.jpg)](https://www.funkyspacemonkey.com/how-to-spoof-your-mac-address/spoof-mac-address-windows-1-fsmdotcom)2\. In the properties window, select the “Advanced” tab. In the “Property” list select the “Network Address” entry. Enable the “Value” option and type your new MAC address without separating the characters ( no dashes or colons ). Click “OK” and you’re done.

[![](https://www.funkyspacemonkey.com/wp-content/uploads/2019/10/spoof-MAC-address-windows-2-FSMdotCOM.jpg)](https://www.funkyspacemonkey.com/how-to-spoof-your-mac-address/spoof-mac-address-windows-2-fsmdotcom)

**NOTE**: If you don’t see the “Network Address” entry in the “Property” list, then your network driver does not support this feature.

