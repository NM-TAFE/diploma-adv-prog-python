Time: 60–90 minutes
Focus: Algorithm implementation + comparison dunder methods

The target API (what must exist and behave correctly):

**Must exist and be importable**
- Return a sequence of galaxies in the expected order (see brief)
- Sort in place (change the original).
- Return a new, sorted sequence without changing the original

You also need a Galaxy class whose instances can be sorted via comparison dunders (e.g. __lt__, __eq__, etc).

Solution must pass the acceptance tests below.

### Scenario

-	Make Galaxy objects comparable and hashable correctly.
-	Provide one in‑place sorting function and one immutable sorting function.
-	Provide an implementation for sorting galaxies.

### Constraints
-	do not call sorted() or .sort() (except inside the helper methods)
-	Use clear, readable Python and small docstrings.

### Pick your roles
-	Algorithm Lead: chooses algorithms, writes the core loops.
-	Comparator Owner: designs and implements the Galaxy dunder methods.
-	Tester: writes tests first (or alongside), runs them often, keeps definition of done.
-	Coordinator/Writer: keeps time, records decisions, writes the final README.

### Deliverables
1.	galaxy.py — defines Galaxy with comparison dunders (__eq__, __lt__, __le__, __gt__, __ge__, __ne__) and __hash__, plus __repr__/__str__.
2.	sorting.py — implements:
-	my_mutating_sort(items) — in‑place sort
-	my_immutable_sort(items) — returns new sorted sequence 
-	galaxy_sorting_method(galaxies) — returns galaxies in the required order.
3.	tests/test_sorting.py — your unit tests that cover:
-	Ordering of Galaxy objects.
-	In‑place vs immutable behavior.
-	Correctness on small and medium datasets.
4.	README.md — short notes: chosen algorithms, complexity, stability, and who did what.

### Hints 
-	Implement __eq__ and __lt__ first; the rest follow the same field.
-	Keep your immutable function separate: copy the input first, then sort the copy.

### Definition of Done
-	All acceptance tests pass.
-	Team commits show contributions from each member.