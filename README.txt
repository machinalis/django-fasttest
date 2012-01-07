Django fast TestCase
====================

This is an alternate `TestCase` class to improve test running times (I measured
a 2x improvement on some of my projects).

You can just use it and get a speed improvement for free, as long as your
projects satisfy the follwoing conditions:

 * You use Django 1.3 (It might work with newer versions but I haven't tried)
 * Your tests use postgreSQL as a database backend, 8.0 or newer
 * Your tests usa a single-database setup
 * Your tests don't make operations on the db connection that make some state
   change that is not reverted by a savepoint rollback.

If the last point is false for a few of your tests, you can use the regular
`django.test.TestCase` for that case, and gain the speed improvement in most of
them.

How to use
----------

Change your:

    from django.test import TestCase

to:

    from django_fasttest import TestCase

How does it work
----------------

What makes it faster is that fixture parsing/loading is done once per `TestCase`
instead of once per test. Between tests in a same `TestCase`, the database is
rolled back (using a pgsql savepoint) to the point just after loading the
fixtures.

All the tests within a testcase use the same database connection (the standard
`TestCase` class shuts down the connection between tests), and are run within 
the same transaction. If you use transactions in your code, you'll have the
same limitations as you do currently in Django 1.3

The speed benefits will be more noticeable if you have many test cases that use
large fixtures, and if those tests are grouped in a `TestCase`.

