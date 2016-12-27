#!/bin/bash
source ENV

letsencrypt-cli register $EMAIL
letsencrypt-cli authorize $DOMAIN -w $WEBROOT_PATH
letsencrypt-cli cert $DOMAIN
