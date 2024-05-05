#!/bin/bash

sudo docker compose up -d --build
echo "Waiting for db to be ready..."
sleep 10
sudo docker compose exec web ./prepare.sh
echo "Setup OK!"
