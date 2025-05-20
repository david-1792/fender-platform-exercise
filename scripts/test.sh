#!/bin/bash
docker exec --env-file .env fender-backend-1 pytest