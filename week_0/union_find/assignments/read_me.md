Percolation
===================
Given a composite systems comprised of randomly distributed 
insulating and metallic materials: what fraction of the materials 
need to be metallic so that the composite system is an electrical 
conductor? Given a porous landscape with water on the surface 
(or oil below), under what conditions will the water be able to drain 
through to the bottom (or the oil to gush through to the surface)? 
Scientists have defined an abstract process known as percolation to 
model such situations.

The Model
----------
We model a percolation system using an n-by-n grid of sites. Each 
site is either open or blocked. A full site is an open site that can 
be connected to an open site in the top row via a chain of neighboring 
(left, right, up, down) open sites. We say the system percolates if 
there is a full site in the bottom row. In other words, a system percolates 
if we fill all open sites connected to the top row and that process 
fills some open site on the bottom row. (For the insulating/metallic 
materials example, the open sites correspond to metallic materials, 
so that a system that percolates has a metallic path from top to bottom, 
with full sites conducting. For the porous substance example, the open 
sites correspond to empty space through which water might flow, so that 
a system that percolates lets water fill open sites, flowing from top to 
bottom.)

The Problem
-----------
In a famous scientific problem, researchers are interested in the following 
question: if sites are independently set to be open with probability p 
(and therefore blocked with probability 1 − p), what is the probability that 
the system percolates? When p equals 0, the system does not percolate; 
when p equals 1, the system percolates. 

When n is sufficiently large, there is a threshold value p* such that 
when p < p* a random n-by-n grid almost never percolates, and when p > p*, a 
random n-by-n grid almost always percolates. No mathematical solution for 
determining the percolation threshold p* has yet been derived. Your task is 
to write a computer program to estimate p*.

Performance requirements
-------------------------
The constructor must take time proportional to n2; all instance methods must 
take constant time plus a constant number of calls to union() and find().

Analysis
--------
- Measure the total running time of PercolationStats for 
  various values of n and T. How does doubling n affect 
  the total running time? How does doubling T affect the 
  total running time? 
  
- Give a formula (using tilde notation) of the total running 
  time on your computer (in seconds) as a single function of 
  both n and T. 
  
- Using the 64-bit memory-cost model from the lecture, give the 
  total memory usage in bytes (using tilde notation) that a 
  Percolation object uses to model an n-by-n percolation system. 
  Count all memory that is used, including memory for the 
  union–find data structure.

