#!/usr/bin/env python3
import sys, os, time
import random

lines = []

for line in sys.stdin:
  line_parts = line.rstrip().split(",")
  entity_type = line_parts[1].rstrip()
  if (entity_type == "4aebf73e-95e3-4fd1-95e7-237dcc4a4466"):
    lines.append(line_parts)


for index, line in enumerate(lines):
  if index == 0:
    print("networkCanvasAlterID_1, networkCanvasAlterID_2, prob, count", flush=True)
    continue

  # For every unique combination:
  for index2, line2 in enumerate(lines):
    if index2 <= index:
      continue

    prob = float(random.random()) # randomly assign pairs a probability
    print(f'{line[0].rstrip()}, {line2[0].rstrip()}, {prob}', flush=True)

    break

  break
