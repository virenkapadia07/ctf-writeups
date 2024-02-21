#!/bin/bash

/usr/bin/docker rmi --force rust_maalik:latest

/usr/bin/docker build -t  rust_maalik:latest .

/usr/bin/docker run -p 0.0.0.0:1337:1337 rust_maalik:latest
