from django.core.management import call_command

with open("datos.json", "w", encoding="utf-8") as f:
    call_command("dumpdata", indent=4, stdout=f)