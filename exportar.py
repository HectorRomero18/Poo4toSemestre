import os
import django
from django.apps import apps
from django.core import serializers

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proy_clinico.settings')  # Ajusta aquí
django.setup()

all_objects = []

for model in apps.get_models():
    try:
        objs = model.objects.all()
        all_objects.extend(objs)
    except Exception as e:
        print(f"Error exportando modelo {model}: {e}")

data = serializers.serialize('json', all_objects, indent=2)

with open('fixture_completa.json', 'w', encoding='utf-8') as f:
    f.write(data)

print("Fixture compatible con loaddata creado como fixture_completa.json")
