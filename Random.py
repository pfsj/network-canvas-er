#!/usr/bin/env python3
import sys, os, time
import argparse
import random

parser = argparse.ArgumentParser("Random resolver")
parser.add_argument('--minimumThreshold', type=float, required=False, default=0.999, help='Ignore matches lower than this threshold')
args = parser.parse_args()

lines = []

for line in sys.stdin:
    lines.append(line)

# spoof slow streamed response

count = 0

for index, line in enumerate(lines):
  # time.sleep(0.05)
  if index == 0:
    print("networkCanvasAlterID_1, networkCanvasAlterID_2, prob, count", flush=True)
    continue

  line_parts = line.rstrip().split(",")

  # For every unique combination:
  for index2, line2 in enumerate(lines):
    if index2 <= index:
      continue

    line_parts2 = line2.rstrip().split(",")
    prob = float(random.random()) # randomly assign pairs a probability
    count += 1

    if (args.minimumThreshold and prob > args.minimumThreshold):
      print(f'{line_parts[0].rstrip()}, {line_parts2[0].rstrip()}, {prob}, {count}', flush=True)
