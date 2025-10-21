from notifier.models import Notification

# Create
results = Notification.objects.create(title='Process complete', message='Model loading')
# Read/Retrieve
results = Notification.objects.filter(is_read=False)
# Update
# Multiple one line query commands
results = Notification.objects.get(id=1); results.is_read=True; results.save()
# Chaining queries
results = Notification.objects.filter(id=1).update(is_read=True)
# Delete
results.delete()



Absolutely 👍 — here’s a clear, teaching-ready summary of Django Queries and QuerySets, focused especially on optimisation, written in Markdown so you can drop it into slides or lesson notes.

⸻


# 🧩 Django Queries and QuerySets

Django’s ORM turns database operations into **Pythonic expressions** using QuerySets.  
A QuerySet represents a **collection of database rows** mapped to model instances.

---

## 1. What Is a QuerySet?

A **QuerySet** is a lazy, iterable object created when you query a model.

```python
# Example: Fetch all notifications
notifications = Notification.objects.all()

	•	Lazy Evaluation: No database access occurs until the data is used (e.g., iterated, sliced, or printed).
	•	Composability: You can chain filters, excludes, and ordering before execution.

unread = Notification.objects.filter(is_read=False).order_by("-created_at")


⸻

2. Common QuerySet Methods

Category	Method	Example	Purpose
Filtering	filter()	.filter(is_read=False)	Get subset matching condition
Excluding	exclude()	.exclude(priority="low")	Exclude matching rows
Ordering	order_by()	.order_by("-created_at")	Sort results
Slicing	[:10]	.order_by("-id")[:10]	Limit results (adds LIMIT)
Aggregation	aggregate()	.aggregate(Count("id"))	Run SQL aggregate functions
Annotation	annotate()	.annotate(Count("user"))	Add calculated fields
Bulk Updates	update()	.filter(is_read=False).update(is_read=True)	Update without loading objects
Existence Check	exists()	.filter(...).exists()	Efficient boolean check


⸻

3. Optimisation Techniques

✅ a. Use select_related() for Foreign Keys

Performs a SQL JOIN and loads related objects in a single query.

# Without select_related: one query per user
notifications = Notification.objects.all()

# With select_related: one JOIN query
notifications = Notification.objects.select_related("user")

Best for: ForeignKey and OneToOneField relationships.

⸻

✅ b. Use prefetch_related() for Many-to-Many

Runs two queries, then combines results in Python to avoid N+1 queries.

# Example: Each post has many tags
posts = Post.objects.prefetch_related("tags")

Best for: ManyToManyField or reverse relationships.

⸻

✅ c. Limit Fields Using only() or defer()

Load only the fields you need.

# Only load title and created_at
Notification.objects.only("title", "created_at")

Benefit: Reduces memory use and transfer time.

⸻

✅ d. Use values() or values_list() for Raw Data

Return dictionaries or tuples instead of model objects.

Notification.objects.values("id", "title")

Great for data export or JSON responses where model methods aren’t needed.

⸻

✅ e. Batch Large Queries

Iterate through large datasets efficiently using .iterator() or QuerySet.chunked().

for n in Notification.objects.iterator(chunk_size=2000):
    process(n)

Benefit: Prevents loading all rows into memory at once.

⸻

✅ f. Cache Expensive Queries

Use Django’s caching framework or database query caching to reduce repeated hits.

from django.core.cache import cache

data = cache.get("notifications")
if not data:
    data = list(Notification.objects.filter(is_read=False))
    cache.set("notifications", data, 300)  # cache for 5 minutes


⸻

✅ g. Profile Queries

Use django-debug-toolbar or QuerySet.query to inspect executed SQL.

print(Notification.objects.filter(is_read=False).query)

These tools help detect redundant queries and unoptimised relationships.

⸻

4. Best Practices for Efficient Queries
	1.	Query early, filter often: Push filters into SQL, not Python loops.
	2.	Avoid N+1 problems: Use select_related and prefetch_related.
	3.	Paginate results: Use Django’s Paginator for large lists.
	4.	Minimise ORM calls: Batch updates/deletes instead of looping.
	5.	Index key fields: Add database indexes to frequently filtered columns.
	6.	**Use .exists() instead of .count() for presence checks.
	7.	Avoid all() in templates: Pass filtered, optimised QuerySets.

⸻

✅ Quick Example

# Inefficient: performs multiple queries
notifications = Notification.objects.all()
for n in notifications:
    print(n.user.username)

# Optimised: single JOIN query
notifications = Notification.objects.select_related("user")
for n in notifications:
    print(n.user.username)


⸻

Summary

Concept	Description	Optimisation Tip
QuerySet	Lazy, chainable representation of SQL query	Use filtering and slicing before evaluation
select_related	Joins related tables	Use for foreign keys
prefetch_related	Separate queries with caching	Use for many-to-many
only / defer	Limit loaded fields	Reduces memory
values / values_list	Return raw data	Speeds up API responses
iterator	Batch large queries	Prevents memory overflow


⸻

Author: Jamie Robertson
Topic: Django ORM – QuerySets & Optimisation (Notifier App Context)

---

Would you like me to export this summary as a downloadable `.md` file (`django_querysets_optimisation.md`)?
