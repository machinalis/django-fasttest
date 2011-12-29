from django.core.management import call_command
from django.db import (transaction, connection, connections, DEFAULT_DB_ALIAS)
from django.test import TransactionTestCase
from django.test.testcases import (disable_transaction_methods,
    restore_transaction_methods)

class TestCase(TransactionTestCase):
    """
    Does basically the same as TransactionTestCase, but surrounds every test
    with a transaction, monkey-patches the real transaction management routines to
    do nothing, and rollsback the test transaction at the end of the test. You have
    to use TransactionTestCase, if you need transaction management inside a test.
    """

    @classmethod
    def setUpClass(cls):
        transaction.enter_transaction_management(using=DEFAULT_DB_ALIAS)
        transaction.managed(True, using=DEFAULT_DB_ALIAS)
        disable_transaction_methods()
        cls.fixtures_loaded = False

    @classmethod
    def tearDownClass(cls):
        restore_transaction_methods()
        transaction.rollback(using=DEFAULT_DB_ALIAS)
        transaction.leave_transaction_management(using=DEFAULT_DB_ALIAS)
        for connection in connections.all():
            connection.close()

    def _fixture_setup(self):
        from django.contrib.sites.models import Site
        Site.objects.clear_cache()

        if hasattr(self, 'fixtures') and not self.fixtures_loaded:
            call_command('loaddata', *self.fixtures, **{
                                                        'verbosity': 0,
                                                        'commit': False,
                                                        'database': DEFAULT_DB_ALIAS
                                                        })
            self.__class__.fixtures_loaded = True
        self.save_point = transaction.savepoint()

    def _fixture_teardown(self):
        transaction.savepoint_rollback(self.save_point)

    def _post_teardown(self):
        self._fixture_teardown()
        self._urlconf_teardown()
        # This is the same method as in TransactionTestCase, WITHOUT the
        # connection closing after every test. That was moved to tearDownClass
