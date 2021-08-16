import os
import sys

from django.contrib.staticfiles.management.commands import runserver
from django.conf import settings


class Command(runserver.Command):
    def add_arguments(self, parser):
        super().add_arguments(parser)

        parser.add_argument(
            "--enable-debugger",
            action="store_true",
            dest="enable_debugger",
            help="Enables debugger",
        )

    def run(self, *args, **options):
        if getattr(settings, "DEBUGGER_ENABLE", False) or options["enable_debugger"]:
            if os.environ.get("RUN_MAIN") or os.environ.get("WERKZEUG_RUN_MAIN"):
                import debugpy

                address = getattr(settings, "DEBUGGER_ADDRESS", "0.0.0.0")
                port = getattr(settings, "DEBUGGER_PORT", 5678)

                try:
                    debugpy.listen(address=(address, port))
                    print("Debugger: Listening at {}:{}".format(address, port))
                except (OSError, RuntimeError):
                    print("Debugger: Port {} already in use".format(port))

                if getattr(settings, "DEBUGGER_WAIT_FOR_ATTACH", False):
                    print("Debugger: Waiting for remote debugger to attach")
                    debugpy.wait_for_client()

        super().run(*args, **options)
