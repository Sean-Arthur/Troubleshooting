#!/bin/bash
# Network Diagnostic Script
# Check basic connectivity, DNS resolution and port availability.

echo "=== Network Diagnostic ==="

# 1. Ping test
echo ""
echo "-- Ping test --"
ping -c 3 example.com

# 2. DNS lookup
echo ""
echo "-- DNS lookup --"
nslookup example.com

# 3. Port check (HTTPS)
echo ""
echo "-- Port 443 check --"
nc -vz example.com 443

echo ""
echo "=== Network Diagnostic Complete ==="     