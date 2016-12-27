## Requirements

- letsencrypt-cli
- python2-selenium
- chromium web browser

### Generating a certificate

```
cp ENV-example ENV
nano ENV
./mount.sh
./generate-cert.sh
```

### Important files that are generated:
- Certificate: cert.pem
- Private key: key.pem

### Updating certificate in cPANEL:
```
sudo docker run -d -p 4444:4444 -v /dev/shm:/dev/shm selenium/standalone-chrome-debug:3.0.1-carbon
source ENV && export $(cut -d= -f1 ENV) && python2 cpanel-import-cert.py
```

