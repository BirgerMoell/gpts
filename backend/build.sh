#!/bin/bash

gcloud config set project reinforcedlife
gcloud builds submit --tag gcr.io/reinforcedlife/af_backend
gcloud run deploy mindmuse \
  --image gcr.io/reinforcedlife/af_backend \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated