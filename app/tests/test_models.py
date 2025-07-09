from django.apps import apps
from django.test import TestCase
from django.utils import timezone

class ModelSmokeTest(TestCase):
    def test_all_models_str(self):
        ignore_models = ['Usuario']  # modelos que você quer pular

        for model in apps.get_models():
            if model.__name__ in ignore_models:
                continue

            fields = {}
            for f in model._meta.fields:
                if f.name == 'id':
                    continue

                try:
                    # Evita ForeignKey para não causar erro
                    if f.get_internal_type() == 'ForeignKey':
                        # Ignorar ou usar None para campos que aceitam nulo
                        if f.null:
                            fields[f.name] = None
                        else:
                            # Se não aceitar null, pula o modelo todo
                            fields = None
                            break
                    else:
                        fields[f.name] = self.get_dummy_value(f)
                except Exception:
                    # Se falhar ao gerar valor, pula o modelo
                    fields = None
                    break

            if fields is None:
                continue

            try:
                obj = model.objects.create(**fields)
                str(obj)
            except Exception as e:
                self.fail(f"{model.__name__} falhou no teste de __str__: {e}")

    def get_dummy_value(self, field):
        if field.blank or field.null:
            return None
        if field.choices:
            return field.choices[0][0]
        if field.get_internal_type() == 'CharField':
            return 'teste'
        if field.get_internal_type() == 'TextField':
            return 'teste'
        if field.get_internal_type() == 'IntegerField':
            return 1
        if field.get_internal_type() == 'DateTimeField':
            return timezone.now()
        if field.get_internal_type() == 'BooleanField':
            return True
        return 'teste'  # fallback
