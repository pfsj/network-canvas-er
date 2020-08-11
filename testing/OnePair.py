#!/usr/bin/env python3
import sys, os, time
import random

lines = []

for line in sys.stdin:
    lines.append(line)

for index, line in enumerate(lines):
  if index == 0:
    print("networkCanvasAlterID_1, networkCanvasAlterID_2, prob, count", flush=True)
    continue

  line_parts = line.rstrip().split(",")

  # For every unique combination:
  for index2, line2 in enumerate(lines):
    if index2 <= index:
      continue

    line_parts2 = line2.rstrip().split(",")
    print(f'{line_parts[0].rstrip()}, {line_parts2[0].rstrip()}, {prob}, {count}', flush=True)

    break

  break
