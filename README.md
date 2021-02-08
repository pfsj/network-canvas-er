# Entity Resolution Sample Scripts

This repository provides some sample scripts and a sample protocol for use with the Entity Resolution feature in Network Canvas Server.

# How entity resolution works

Entity resolution allows you to find pairs of nodes (and egos) across different sessions that represent the same person, place or object.
You can export a single network including these merged nodes, and their resolved properties. This is facilitated by sending a list
of nodes to your script (typically python), which then returns a list of pairs with scores of the probability of matching.

# Writing an entity

1. A `CSV` formatted list of nodes (and attributes) are sent to your entity resolution script via `stdin`.
2. The script can process these nodes any way you choose.
3. The script should write to `stdout` with a list of node pairs and their probability score.

## stdin example

```
id,type,name,age
1,4aebf73e-95e3-4fd1-95e7-237dcc4a4466,Abigail,40
2,4aebf73e-95e3-4fd1-95e7-237dcc4a4466,Bianca,41
3,4aebf73e-95e3-4fd1-95e7-237dcc4a4466,Charlotte,37
4,4aebf73e-95e3-4fd1-95e7-237dcc4a4466,David,23
5,4aebf73e-95e3-4fd1-95e7-237dcc4a4466,Eugene,56
```

## stdout example

```
networkCanvasAlterID_1, networkCanvasAlterID_2, prob
1,2,0.500
2,3,0.900
3,4,0.995
```

# Example scripts

- EntityResolution.py
- Random.py
- Error.py

# Limitations

- egos
