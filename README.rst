Project setup
=============

Project setup instructions here.

mkdir -p local
cp core/project/settings/template/settings.dev.py ./local/settings.dev.py
cp cooking_core/project/settings/template/settings.unittests.py ./local/settings.unittests.py


```
make shell

from cooking_core.config.models import Config
Config.objects.create(owner=None, transaction_fee=1)
```
