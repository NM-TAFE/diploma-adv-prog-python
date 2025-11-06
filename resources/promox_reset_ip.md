# SET OR RESET IP ADDRESS

Run the following commands to regenerate the machine ID and restart networking:

```bash
sudo rm -rf /etc/machine-id
sudo systemd-machine-id-setup
sudo systemctl restart systemd-networkd
reboot
```

After reboot, verify the IP address:

```bash
ip addr
```
