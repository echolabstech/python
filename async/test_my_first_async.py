import my_first_async
import asyncio
import pytest
from unittest import TestCase
from aiohttp.test_utils import AioHTTPTestCase, unittest_run_loop
from aiohttp import web
import random
from datetime import datetime


class TestMyFirstAsync(AioHTTPTestCase, TestCase):
    tasks = []
    task_completion_times = {}
    success_non_blocking = 'test success: main non-blocking'
    failure_blocking = 'test failure: main is blocking'

    def get_num_pending_tasks(self):
        pending_tasks = 0
        for task in self.tasks:
            if not task.done():
                pending_tasks = pending_tasks + 1
        return pending_tasks


    async def webpage(self, request=None):
        mock_response_delay = random.randint(0, 1)
        await asyncio.sleep(mock_response_delay)
        html = 'foobar'
        return web.Response(text=html)


    async def get_application(self):
        """
        Override the get_app method to return your application.
        """
        app = web.Application()
        app.router.add_get('/', self.webpage)
        return app


    async def listen_requests(self, search_terms):
        tasks = await my_first_async.main(search_terms, url='/')
        await asyncio.sleep(1)
        return tasks


    async def await_pending_tasks(self):
        """
        holds the event loop open to complete running tasks
        """
        num_pending_tasks = self.get_num_pending_tasks()
        await asyncio.sleep(num_pending_tasks)


    async def check_completition_times(self, targets):
        """
        determine if target tasks completed before other tasks
        """
        for target_task in targets:
            target_completed_time = self.task_completion_times[target_task]
            for task in self.tasks:
                task_completed_time = self.task_completion_times[task]
                if target_completed_time < task_completed_time:
                    raise Exception(self.success_non_blocking)
        raise Exception(self.failure_blocking)


    # @pytest.mark.skip(reason='not implemented')
    @unittest_run_loop
    async def test_main_non_blocking(self):
        """
        Main can schedule tasks concurrently without blocking I/O
        """
        tasks = []
        asyncio.set_event_loop(self.loop)
        my_first_async.ClientSession.get = self.client.get
        all_search_terms = ['star wars', 'pale blue dot', 'game of thrones', 'star trek',
                            'Stargate'] * 2

        search_terms = all_search_terms[:10]
        self.tasks = self.tasks + await self.listen_requests(search_terms)

        search_terms = all_search_terms[:1]
        target_tasks = await self.listen_requests(search_terms)
        self.tasks = self.tasks + target_tasks

        def callback(future):
            self.task_completion_times[future] = datetime.now()
        for task in self.tasks:
            task.add_done_callback(callback)

        await self.await_pending_tasks()
        try:
            await self.check_completition_times(target_tasks)
        except Exception as e:
            assert e.__str__()==self.success_non_blocking


    @pytest.mark.skip(reason='not implemented')
    def test_catches_404_page_not_found():
        assert 1 == 2


    @pytest.mark.skip(reason='not implemented')
    def test_catches_400_bad_request():
        assert 1 == 2


    @pytest.mark.skip(reason='not implemented')
    def test_handle_302_redirect():
        assert 1 == 2


    @pytest.mark.skip(reason='not implemented')
    def test_handle_301_moved():
        assert 1 == 2


    @pytest.mark.skip(reason='not implemented')
    def test_log_on_exception():
        assert 1 == 2
